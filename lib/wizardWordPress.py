#!/usr/bin/env python
"""
wizardWordPress.py

Copyright 2013 Daniel Maldonado

This file is part of WPHardening project.

WPHardening is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

WPHardening is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with WPHardening.  If not, see <http://www.gnu.org/licenses/>.

"""

import os


class wizardWordPress:
    def __init__(self):
        self.directory = None

    def setDirectory(self):
        directorio = raw_input("Ingresa el Path: ")
        if os.path.exists(os.path.abspath(directorio)):
            self.directory = directorio

    def getDirectory(self):
        return self.directory
