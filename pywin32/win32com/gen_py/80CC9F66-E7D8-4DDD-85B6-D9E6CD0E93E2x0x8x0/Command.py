# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)]
# From type library '{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}'
# On Thu Jun  6 08:47:12 2013
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
class Command(DispatchBaseClass):
	'Represents a command in the environment.'
	CLSID = IID('{5FE10FB0-91A1-4E55-BAAA-ECCAE5CCEB94}')
	coclass_clsid = None

	def AddControl(self, Owner=defaultNamedNotOptArg, Position=1):
		'Creates a persistent command bar control for this command.'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((9, 1), (3, 49)),Owner
			, Position)
		if ret is not None:
			ret = Dispatch(ret, 'AddControl', None)
		return ret

	def Delete(self):
		'Removes a named command that was created with Commands.AddNamedCommand.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Bindings": (9, 2, (12, 0), (), "Bindings", None),
		# Method 'Collection' returns object of type 'Commands'
		"Collection": (2, 2, (9, 0), (), "Collection", '{E6B96CAC-B8C7-40AE-B705-5C81878C4A9E}'),
		# Method 'DTE' returns object of type 'DTE'
		"DTE": (3, 2, (13, 0), (), "DTE", '{3C9CFE1E-389F-4118-9FAD-365385190329}'),
		"Guid": (4, 2, (8, 0), (), "Guid", None),
		"ID": (5, 2, (3, 0), (), "ID", None),
		"IsAvailable": (6, 2, (11, 0), (), "IsAvailable", None),
		"LocalizedName": (1, 2, (8, 0), (), "LocalizedName", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
		"Bindings": ((9, LCID, 4, 0),()),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{5FE10FB0-91A1-4E55-BAAA-ECCAE5CCEB94}", Command )
# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)]
# From type library '{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}'
# On Thu Jun  6 08:47:12 2013
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

Command_vtables_dispatch_ = 1
Command_vtables_ = [
	(( 'Name' , 'lpbstr' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Collection' , 'lppcReturn' , ), 2, (2, (), [ (16393, 10, None, "IID('{E6B96CAC-B8C7-40AE-B705-5C81878C4A9E}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DTE' , 'lppaReturn' , ), 3, (3, (), [ (16397, 10, None, "IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Guid' , 'lpbstr' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ID' , 'lReturn' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsAvailable' , 'pAvail' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AddControl' , 'Owner' , 'Position' , 'pCommandBarControl' , ), 7, (7, (), [ 
			 (9, 1, None, None) , (3, 49, '1', None) , (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Bindings' , 'pVar' , ), 9, (9, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Bindings' , 'pVar' , ), 9, (9, (), [ (12, 0, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'LocalizedName' , 'lpbstr' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{5FE10FB0-91A1-4E55-BAAA-ECCAE5CCEB94}", Command )
