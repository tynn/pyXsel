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
"""long_description"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(name='pyXsel',
      version='1.0',
      platforms=['Linux'],
      author="Christian Schmitz",
      author_email="tynn.dev@gmail.com",
      license='LGPLv3+',
      url="https://github.com/tynn/pyXsel",
      description="Get the X11 selection value",
      py_modules=['xsel'],
      long_description=__doc__)
