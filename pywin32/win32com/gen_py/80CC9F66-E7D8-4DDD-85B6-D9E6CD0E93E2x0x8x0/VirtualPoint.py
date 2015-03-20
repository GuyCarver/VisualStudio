# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)]
# From type library '{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}'
# On Thu Aug 29 05:58:28 2013
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
class VirtualPoint(DispatchBaseClass):
	'A TextPoint that may represent a location in virtual space (beyond the end of a line).'
	CLSID = IID('{42320454-626C-4DD0-9ECB-357C4F1966D8}')
	coclass_clsid = None

	# Result is of type CodeElement
	# The method CodeElement is actually a property, but must be used as a method to correctly pass the arguments
	def CodeElement(self, Scope=defaultNamedNotOptArg):
		"Returns the code element at the TextPoint's location."
		ret = self._oleobj_.InvokeTypes(51, LCID, 2, (9, 0), ((3, 1),),Scope
			)
		if ret is not None:
			ret = Dispatch(ret, 'CodeElement', '{0CFBC2B6-0D4E-11D3-8997-00C04F688DDE}')
		return ret

	# Result is of type EditPoint
	def CreateEditPoint(self):
		'Creates an EditPoint object at the current location and returns it.'
		ret = self._oleobj_.InvokeTypes(34, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateEditPoint', '{C1FFE800-028B-4475-A907-14F51F19BB7D}')
		return ret

	def EqualTo(self, Point=defaultNamedNotOptArg):
		'Returns whether the called object is equal to the given object.'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (11, 0), ((9, 1),),Point
			)

	def GreaterThan(self, Point=defaultNamedNotOptArg):
		'Returns whether the called object is greater than the given object.'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (11, 0), ((9, 1),),Point
			)

	def LessThan(self, Point=defaultNamedNotOptArg):
		'Returns whether the called object is less than the given object.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (11, 0), ((9, 1),),Point
			)

	def TryToShow(self, How=0, PointOrCount=defaultNamedOptArg):
		"Tries to make the TextPoint's location visible to the user."
		return self._oleobj_.InvokeTypes(50, LCID, 1, (11, 0), ((3, 49), (12, 17)),How
			, PointOrCount)

	_prop_map_get_ = {
		"AbsoluteCharOffset": (13, 2, (3, 0), (), "AbsoluteCharOffset", None),
		"AtEndOfDocument": (21, 2, (11, 0), (), "AtEndOfDocument", None),
		"AtEndOfLine": (23, 2, (11, 0), (), "AtEndOfLine", None),
		"AtStartOfDocument": (22, 2, (11, 0), (), "AtStartOfDocument", None),
		"AtStartOfLine": (24, 2, (11, 0), (), "AtStartOfLine", None),
		# Method 'DTE' returns object of type 'DTE'
		"DTE": (1, 2, (13, 0), (), "DTE", '{3C9CFE1E-389F-4118-9FAD-365385190329}'),
		"DisplayColumn": (14, 2, (3, 0), (), "DisplayColumn", None),
		"Line": (11, 2, (3, 0), (), "Line", None),
		"LineCharOffset": (12, 2, (3, 0), (), "LineCharOffset", None),
		"LineLength": (25, 2, (3, 0), (), "LineLength", None),
		# Method 'Parent' returns object of type 'TextDocument'
		"Parent": (2, 2, (9, 0), (), "Parent", '{CB218890-1382-472B-9118-782700C88115}'),
		"VirtualCharOffset": (101, 2, (3, 0), (), "VirtualCharOffset", None),
		"VirtualDisplayColumn": (102, 2, (3, 0), (), "VirtualDisplayColumn", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{42320454-626C-4DD0-9ECB-357C4F1966D8}", VirtualPoint )
# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)]
# From type library '{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}'
# On Thu Aug 29 05:58:28 2013
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

VirtualPoint_vtables_dispatch_ = 1
VirtualPoint_vtables_ = [
	(( 'VirtualCharOffset' , 'pOffset' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'VirtualDisplayColumn' , 'lppaReturn' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{42320454-626C-4DD0-9ECB-357C4F1966D8}", VirtualPoint )
