# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)]
# From type library '{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}'
# On Thu Jun  6 08:30:30 2013
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
class Breakpoints(DispatchBaseClass):
	'A collection of Breakpoint objects.'
	CLSID = IID('{25968106-BAFB-11D2-8AD1-00C04F79E479}')
	coclass_clsid = None

	# Result is of type Breakpoints
	def Add(self, Function='', File='', Line=1, Column=1
			, Condition='', ConditionType=1, Language='', Data='', DataCount=1
			, Address='', HitCount=0, HitCountType=1):
		'Creates and enables a new breakpoint.  If no parameters are given, the new breakpoint dialog is displayed.'
		return self._ApplyTypes_(4, 1, (9, 32), ((8, 49), (8, 49), (3, 49), (3, 49), (8, 49), (3, 49), (8, 49), (8, 49), (3, 49), (8, 49), (3, 49), (3, 49)), 'Add', '{25968106-BAFB-11D2-8AD1-00C04F79E479}',Function
			, File, Line, Column, Condition, ConditionType
			, Language, Data, DataCount, Address, HitCount
			, HitCountType)

	# Result is of type Breakpoint
	def Item(self, index=defaultNamedNotOptArg):
		'Returns an indexed member of a collection.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{11C5114C-BB00-11D2-8AD1-00C04F79E479}')
		return ret

	_prop_map_get_ = {
		"Count": (3, 2, (3, 0), (), "Count", None),
		# Method 'DTE' returns object of type 'DTE'
		"DTE": (1, 2, (13, 0), (), "DTE", '{3C9CFE1E-389F-4118-9FAD-365385190329}'),
		# Method 'Parent' returns object of type 'Debugger'
		"Parent": (2, 2, (9, 0), (), "Parent", '{338FB9A0-BAE5-11D2-8AD1-00C04F79E479}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Returns an indexed member of a collection.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{11C5114C-BB00-11D2-8AD1-00C04F79E479}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,1,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{11C5114C-BB00-11D2-8AD1-00C04F79E479}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(3, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

win32com.client.CLSIDToClass.RegisterCLSID( "{25968106-BAFB-11D2-8AD1-00C04F79E479}", Breakpoints )
# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)]
# From type library '{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}'
# On Thu Jun  6 08:30:30 2013
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

Breakpoints_vtables_dispatch_ = 1
Breakpoints_vtables_ = [
	(( 'Item' , 'index' , 'Breakpoint' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{11C5114C-BB00-11D2-8AD1-00C04F79E479}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'Enumerator' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 1 , )),
	(( 'DTE' , 'DTEObject' , ), 1, (1, (), [ (16397, 10, None, "IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'Debugger' , ), 2, (2, (), [ (16393, 10, None, "IID('{338FB9A0-BAE5-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Count' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Function' , 'File' , 'Line' , 'Column' , 
			 'Condition' , 'ConditionType' , 'Language' , 'Data' , 'DataCount' , 
			 'Address' , 'HitCount' , 'HitCountType' , 'Breakpoints' , ), 4, (4, (), [ 
			 (8, 49, "''", None) , (8, 49, "''", None) , (3, 49, '1', None) , (3, 49, '1', None) , (8, 49, "''", None) , 
			 (3, 49, '1', None) , (8, 49, "''", None) , (8, 49, "''", None) , (3, 49, '1', None) , (8, 49, "''", None) , 
			 (3, 49, '0', None) , (3, 49, '1', None) , (16393, 10, None, "IID('{25968106-BAFB-11D2-8AD1-00C04F79E479}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 32, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{25968106-BAFB-11D2-8AD1-00C04F79E479}", Breakpoints )
