#  This is the xsel module of pyXsel.
#
#  Copyright (c) 2015 Christian Schmitz <tynn.dev@gmail.com>
#
#  pyXsel is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  pyXsel is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with pyXsel.  If not, see <http://www.gnu.org/licenses/>.
"""Get X11 selection value"""
from ctypes.util import find_library
from ctypes import c_char_p, c_int, c_long, c_ulong, c_void_p, \
                   byref, cdll, Structure, Union

__all__ = ['get', 'PRIMARY', 'SECONDARY', 'CLIPBOARD']

X11 = cdll.LoadLibrary(find_library('X11') or 'libX11.so')
Xmu = cdll.LoadLibrary(find_library('Xmu') or 'libXmu.so')

class XSelectionEvent(Structure):
    """X11 XSelectionEvent struct"""
    _fields_ = [('type', c_int),
                ('serial', c_ulong),
                ('send_event', c_int),
                ('display', c_void_p),
                ('requestor', c_ulong),
                ('selection', c_ulong),
                ('target', c_ulong),
                ('property', c_ulong),
                ('time', c_ulong)]

class XEvent(Union):
    """X11 XEvent union"""
    _fields_ = [('type', c_int),
                ('xselection', XSelectionEvent),
                ('pad', c_long*24)]

PRIMARY, SECONDARY = 1, 2
CLIPBOARD = c_void_p.in_dll(Xmu, '_XA_CLIPBOARD')
_XA_UTF8_STRING = c_void_p.in_dll(Xmu, '_XA_UTF8_STRING')

def get(selection=PRIMARY):
    """Get the value of a selection of X11"""
    display = X11.XOpenDisplay(None)
    if not display:
        raise RuntimeError("XOpenDisplay did not succeed")

    try:
        window = X11.XDefaultRootWindow(display)
        window = X11.XCreateSimpleWindow(display, window, 0, 0, 1, 1, 0, 0, 0)

        if isinstance(selection, c_void_p):
            selection = Xmu.XmuInternAtom(display, selection)
        prop = X11.XInternAtom(display, 'pyXsel', False)

        refs = (byref(c_ulong()), byref(c_int()), byref(c_ulong()))
        buf, buf_len = c_char_p(), c_ulong()

        targets = [(Xmu.XmuInternAtom(display, _XA_UTF8_STRING), 'utf8'),
                   (31, 'latin1')]
        event = XEvent()
        for target, enc in targets:
            X11.XConvertSelection(display, selection, target, prop, window, 0)

            event.type = 0
            while event.type != 31:
                X11.XNextEvent(display, byref(event))

            if event.xselection.property != 0:
                X11.XGetWindowProperty(display, window, prop, 0, 0, False,
                                       0, refs[0], refs[1], refs[2],
                                       byref(buf_len), byref(buf))
                X11.XFree(buf)

                X11.XGetWindowProperty(display, window, prop, 0, buf_len, True,
                                       0, refs[0], refs[1], refs[2],
                                       byref(buf_len), byref(buf))
                value = buf.value.decode(enc)
                X11.XFree(buf)

                if isinstance(value, str):
                    return value
                try:
                    return value.encode()
                except UnicodeEncodeError:
                    import sys
                    return value.encode(sys.getfilesystemencoding())

        return ""
    finally:
        X11.XCloseDisplay(display)

if __name__ == '__main__':
    print(get())
