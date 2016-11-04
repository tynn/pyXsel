#  This is the setup script of pyXsel.
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

"""
pyXsel
======
Get the X11 selection value::

    >>> xsel.get(selection=xsel.PRIMARY)
    'str value of the selection or ""'

Predefined selections are ``PRIMARY``, ``SECONDARY`` and ``CLIPBOARD``.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name            ='pyXsel',
    version         ='1.0',
    description     ="Get the X11 selection value",
    long_description=__doc__,
    author          ="Christian Schmitz",
    author_email    ="tynn.dev@gmail.com",
    url             ="https://github.com/tynn/pyXsel",
    license         ='LGPLv3+',
    py_modules      =['xsel'],
    platforms       =['Linux'],
    classifiers     =[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: '
            'GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ])
