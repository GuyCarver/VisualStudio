# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:06:53) [MSC v.1600 64 bit (AMD64)]
# From type library '{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}'
# On Wed Jun  5 20:58:12 2013
'Microsoft Development Environment 8.0 (Version 7.0 Object Model)'
makepy_version = '0.5.01'
python_version = 0x30302f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}')
MajorVersion = 8
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import CoClassBaseClass
import sys
__import__('win32com.gen_py.80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2x0x8x0._DTE')
_DTE = sys.modules['win32com.gen_py.80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2x0x8x0._DTE']._DTE
class DTE(CoClassBaseClass): # A CoClass
	# Root object from which all other objects and collections in environment extensibility are accessed.
	CLSID = IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_DTE,
	]
	default_interface = _DTE

win32com.client.CLSIDToClass.RegisterCLSID( "{3C9CFE1E-389F-4118-9FAD-365385190329}", DTE )
