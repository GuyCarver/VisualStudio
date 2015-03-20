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
class Document(DispatchBaseClass):
	'A Document open for editing.'
	CLSID = IID('{63EB5C39-CA8F-498E-9A66-6DD4A27AC95B}')
	coclass_clsid = None

	def Activate(self):
		'Moves the focus to the current item.'
		return self._oleobj_.InvokeTypes(121, LCID, 1, (24, 0), (),)

	def ClearBookmarks(self):
		'Clears all bookmarks in the document.'
		return self._oleobj_.InvokeTypes(122, LCID, 1, (24, 0), (),)

	def Close(self, Save=3):
		'Closes the document, and optionally saves.'
		return self._oleobj_.InvokeTypes(123, LCID, 1, (24, 0), ((3, 49),),Save
			)

	# The method Extender is actually a property, but must be used as a method to correctly pass the arguments
	def Extender(self, ExtenderName=defaultNamedNotOptArg):
		'Get an Extender for this object under the specified category.'
		ret = self._oleobj_.InvokeTypes(133, LCID, 2, (9, 0), ((8, 1),),ExtenderName
			)
		if ret is not None:
			ret = Dispatch(ret, 'Extender', None)
		return ret

	def MarkText(self, Pattern=defaultNamedNotOptArg, Flags=0):
		'Creates unnamed bookmarks where the specified pattern is found.'
		return self._oleobj_.InvokeTypes(124, LCID, 1, (11, 0), ((8, 1), (3, 49)),Pattern
			, Flags)

	# Result is of type Window
	def NewWindow(self):
		'Creates a new window to view the document.'
		ret = self._oleobj_.InvokeTypes(125, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'NewWindow', '{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}')
		return ret

	def Object(self, ModelKind=''):
		'Returns an interface or object that can be accessed at run time by name.'
		return self._ApplyTypes_(132, 1, (9, 32), ((8, 49),), 'Object', None,ModelKind
			)

	def PrintOut(self):
		'Sends the object to the printer.'
		return self._oleobj_.InvokeTypes(126, LCID, 1, (24, 0), (),)

	def Redo(self):
		'Redo the action last performed by the user on this object.'
		return self._oleobj_.InvokeTypes(127, LCID, 1, (11, 0), (),)

	def ReplaceText(self, FindText=defaultNamedNotOptArg, ReplaceText=defaultNamedNotOptArg, Flags=0):
		'Replaces a pattern of text with new text in a document.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (11, 0), ((8, 1), (8, 1), (3, 49)),FindText
			, ReplaceText, Flags)

	def Save(self, FileName=''):
		'Saves the object to storage.'
		return self._ApplyTypes_(129, 1, (3, 32), ((8, 49),), 'Save', None,FileName
			)

	def Undo(self):
		'Undo the action last performed by the user on this object.'
		return self._oleobj_.InvokeTypes(128, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		# Method 'ActiveWindow' returns object of type 'Window'
		"ActiveWindow": (102, 2, (9, 0), (), "ActiveWindow", '{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}'),
		# Method 'Collection' returns object of type 'Documents'
		"Collection": (101, 2, (9, 0), (), "Collection", '{9E2CF3EA-140F-413E-BD4B-7D46740CD2F4}'),
		# Method 'DTE' returns object of type 'DTE'
		"DTE": (100, 2, (13, 0), (), "DTE", '{3C9CFE1E-389F-4118-9FAD-365385190329}'),
		"ExtenderCATID": (135, 2, (8, 0), (), "ExtenderCATID", None),
		"ExtenderNames": (134, 2, (12, 0), (), "ExtenderNames", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"IndentSize": (142, 2, (3, 0), (), "IndentSize", None),
		"Kind": (141, 2, (8, 0), (), "Kind", None),
		"Language": (144, 2, (8, 0), (), "Language", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
		"Path": (105, 2, (8, 0), (), "Path", None),
		# Method 'ProjectItem' returns object of type 'ProjectItem'
		"ProjectItem": (110, 2, (9, 0), (), "ProjectItem", '{0B48100A-473E-433C-AB8F-66B9739AB620}'),
		"ReadOnly": (106, 2, (11, 0), (), "ReadOnly", None),
		"Saved": (107, 2, (11, 0), (), "Saved", None),
		"Selection": (131, 2, (9, 0), (), "Selection", None),
		"TabSize": (147, 2, (3, 0), (), "TabSize", None),
		"Type": (149, 2, (8, 0), (), "Type", None),
		# Method 'Windows' returns object of type 'Windows'
		"Windows": (109, 2, (9, 0), (), "Windows", '{2294311A-B7BC-4789-B365-1C15FF2CD17C}'),
	}
	_prop_map_put_ = {
		"Language": ((144, LCID, 4, 0),()),
		"ReadOnly": ((106, LCID, 4, 0),()),
		"Saved": ((107, LCID, 4, 0),()),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{63EB5C39-CA8F-498E-9A66-6DD4A27AC95B}", Document )
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

Document_vtables_dispatch_ = 1
Document_vtables_ = [
	(( 'DTE' , 'lppaReturn' , ), 100, (100, (), [ (16397, 10, None, "IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Kind' , 'pKind' , ), 141, (141, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Collection' , 'DocumentsObject' , ), 101, (101, (), [ (16393, 10, None, "IID('{9E2CF3EA-140F-413E-BD4B-7D46740CD2F4}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ActiveWindow' , 'pWindow' , ), 102, (102, (), [ (16393, 10, None, "IID('{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FullName' , 'pRetval' , ), 103, (103, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pRetval' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Path' , 'pRetval' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ReadOnly' , 'pRetval' , ), 106, (106, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Saved' , 'pRetval' , ), 107, (107, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Saved' , 'pRetval' , ), 107, (107, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Windows' , 'pWindows' , ), 109, (109, (), [ (16393, 10, None, "IID('{2294311A-B7BC-4789-B365-1C15FF2CD17C}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ProjectItem' , 'pRetval' , ), 110, (110, (), [ (16393, 10, None, "IID('{0B48100A-473E-433C-AB8F-66B9739AB620}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 121, (121, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Close' , 'Save' , ), 123, (123, (), [ (3, 49, '3', None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NewWindow' , 'pWindow' , ), 125, (125, (), [ (16393, 10, None, "IID('{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Redo' , 'pbRetVal' , ), 127, (127, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Undo' , 'pbRetVal' , ), 128, (128, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Save' , 'FileName' , 'pStatus' , ), 129, (129, (), [ (8, 49, "''", None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 32, None, None) , 0 , )),
	(( 'Selection' , 'SelectionObject' , ), 131, (131, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Object' , 'ModelKind' , 'DataModelObject' , ), 132, (132, (), [ (8, 49, "''", None) , 
			 (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 32, None, None) , 0 , )),
	(( 'Extender' , 'ExtenderName' , 'Extender' , ), 133, (133, (), [ (8, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 1024 , )),
	(( 'ExtenderNames' , 'ExtenderNames' , ), 134, (134, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 1024 , )),
	(( 'ExtenderCATID' , 'pRetval' , ), 135, (135, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 1024 , )),
	(( 'PrintOut' , ), 126, (126, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
	(( 'IndentSize' , 'pSize' , ), 142, (142, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( 'Language' , 'pLanguage' , ), 144, (144, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 64 , )),
	(( 'Language' , 'pLanguage' , ), 144, (144, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 64 , )),
	(( 'ReadOnly' , 'pRetval' , ), 106, (106, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 64 , )),
	(( 'TabSize' , 'pSize' , ), 147, (147, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( 'ClearBookmarks' , ), 122, (122, (), [ ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( 'MarkText' , 'Pattern' , 'Flags' , 'pbRetVal' , ), 124, (124, (), [ 
			 (8, 1, None, None) , (3, 49, '0', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'ReplaceText' , 'FindText' , 'ReplaceText' , 'Flags' , 'pbRetVal' , 
			 ), 21, (21, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 64 , )),
	(( 'Type' , 'pType' , ), 149, (149, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 64 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{63EB5C39-CA8F-498E-9A66-6DD4A27AC95B}", Document )
