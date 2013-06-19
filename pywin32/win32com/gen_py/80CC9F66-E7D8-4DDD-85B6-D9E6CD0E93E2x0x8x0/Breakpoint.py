# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)]
# From type library '{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}'
# On Thu Jun  6 22:16:48 2013
'Microsoft Development Environment 8.0 (Version 7.0 Object Model)'
makepy_version = '0.5.01'
python_version = 0x30300f0

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

from win32com.client import DispatchBaseClass
class Breakpoint(DispatchBaseClass):
	'Used to manipulate a breakpoint.'
	CLSID = IID('{11C5114C-BB00-11D2-8AD1-00C04F79E479}')
	coclass_clsid = None

	def Delete(self):
		'Deletes this breakpoint.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

	def ResetHitCount(self):
		'Resets the hit count for this breakpoint back to 0'
		return self._oleobj_.InvokeTypes(300, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Children' returns object of type 'Breakpoints'
		"Children": (203, 2, (9, 0), (), "Children", '{25968106-BAFB-11D2-8AD1-00C04F79E479}'),
		# Method 'Collection' returns object of type 'Breakpoints'
		"Collection": (202, 2, (9, 0), (), "Collection", '{25968106-BAFB-11D2-8AD1-00C04F79E479}'),
		"Condition": (109, 2, (8, 0), (), "Condition", None),
		"ConditionType": (108, 2, (3, 0), (), "ConditionType", None),
		"CurrentHits": (115, 2, (3, 0), (), "CurrentHits", None),
		# Method 'DTE' returns object of type 'DTE'
		"DTE": (200, 2, (13, 0), (), "DTE", '{3C9CFE1E-389F-4118-9FAD-365385190329}'),
		"Enabled": (113, 2, (11, 0), (), "Enabled", None),
		"File": (105, 2, (8, 0), (), "File", None),
		"FileColumn": (107, 2, (3, 0), (), "FileColumn", None),
		"FileLine": (106, 2, (3, 0), (), "FileLine", None),
		"FunctionColumnOffset": (104, 2, (3, 0), (), "FunctionColumnOffset", None),
		"FunctionLineOffset": (103, 2, (3, 0), (), "FunctionLineOffset", None),
		"FunctionName": (102, 2, (8, 0), (), "FunctionName", None),
		"HitCountTarget": (112, 2, (3, 0), (), "HitCountTarget", None),
		"HitCountType": (111, 2, (3, 0), (), "HitCountType", None),
		"Language": (110, 2, (8, 0), (), "Language", None),
		"LocationType": (101, 2, (3, 0), (), "LocationType", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'Parent' returns object of type 'Breakpoint'
		"Parent": (201, 2, (9, 0), (), "Parent", '{11C5114C-BB00-11D2-8AD1-00C04F79E479}'),
		# Method 'Program' returns object of type 'Program'
		"Program": (116, 2, (9, 0), (), "Program", '{6A38D87C-BBA0-11D2-8AD1-00C04F79E479}'),
		"Tag": (114, 2, (8, 0), (), "Tag", None),
		"Type": (100, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Enabled": ((113, LCID, 4, 0),()),
		"Name": ((0, LCID, 4, 0),()),
		"Tag": ((114, LCID, 4, 0),()),
	}
	# Default property for this class is 'Name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{11C5114C-BB00-11D2-8AD1-00C04F79E479}", Breakpoint )
# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)]
# From type library '{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}'
# On Thu Jun  6 22:16:48 2013
'Microsoft Development Environment 8.0 (Version 7.0 Object Model)'
makepy_version = '0.5.01'
python_version = 0x30300f0

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

Breakpoint_vtables_dispatch_ = 1
Breakpoint_vtables_ = [
	(( 'Delete' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'Type' , ), 100, (100, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 0, (0, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'LocationType' , 'LocationType' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FunctionName' , 'FunctionName' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'FunctionLineOffset' , 'Offset' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'FunctionColumnOffset' , 'Offset' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'File' , 'File' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'FileLine' , 'Line' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FileColumn' , 'Column' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ConditionType' , 'ConditionType' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Condition' , 'Condition' , ), 109, (109, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Language' , 'Language' , ), 110, (110, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'HitCountType' , 'HitCountType' , ), 111, (111, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'HitCountTarget' , 'HitCountTarget' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Enabled' , 'Enabled' , ), 113, (113, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Enabled' , 'Enabled' , ), 113, (113, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Tag' , 'Tag' , ), 114, (114, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Tag' , 'Tag' , ), 114, (114, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CurrentHits' , 'CurHitCount' , ), 115, (115, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Program' , 'Program' , ), 116, (116, (), [ (16393, 10, None, "IID('{6A38D87C-BBA0-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'DTE' , 'DTE' , ), 200, (200, (), [ (16397, 10, None, "IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Breakpoint' , ), 201, (201, (), [ (16393, 10, None, "IID('{11C5114C-BB00-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Collection' , 'Breakpoints' , ), 202, (202, (), [ (16393, 10, None, "IID('{25968106-BAFB-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Children' , 'Breakpoints' , ), 203, (203, (), [ (16393, 10, None, "IID('{25968106-BAFB-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ResetHitCount' , ), 300, (300, (), [ ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{11C5114C-BB00-11D2-8AD1-00C04F79E479}", Breakpoint )
