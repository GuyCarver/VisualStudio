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
class TextDocument(DispatchBaseClass):
	'Object representing an open text-based document such as a file of code.'
	CLSID = IID('{CB218890-1382-472B-9118-782700C88115}')
	coclass_clsid = None

	def ClearBookmarks(self):
		'Clears all bookmarks in the document.'
		return self._oleobj_.InvokeTypes(122, LCID, 1, (24, 0), (),)

	# Result is of type EditPoint
	def CreateEditPoint(self, TextPoint=0):
		'Creates an EditPoint object at the specified location and returns it. The default location is the beginning of the document.'
		ret = self._oleobj_.InvokeTypes(131, LCID, 1, (9, 0), ((9, 49),),TextPoint
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateEditPoint', '{C1FFE800-028B-4475-A907-14F51F19BB7D}')
		return ret

	def MarkText(self, Pattern=defaultNamedNotOptArg, vsFindOptionsValue=0):
		'Creates unnamed bookmarks where the specified pattern is found.'
		return self._oleobj_.InvokeTypes(124, LCID, 1, (11, 0), ((8, 1), (3, 49)),Pattern
			, vsFindOptionsValue)

	def PrintOut(self):
		'Sends the object to the printer.'
		return self._oleobj_.InvokeTypes(134, LCID, 1, (24, 0), (),)

	def ReplacePattern(self, Pattern=defaultNamedNotOptArg, Replace=defaultNamedNotOptArg, vsFindOptionsValue=0, Tags=0):
		'Replaces a pattern of text with new text in a document.'
		return self._ApplyTypes_(128, 1, (11, 0), ((8, 1), (8, 1), (3, 49), (16393, 51)), 'ReplacePattern', None,Pattern
			, Replace, vsFindOptionsValue, Tags)

	def ReplaceText(self, FindText=defaultNamedNotOptArg, ReplaceText=defaultNamedNotOptArg, vsFindOptionsValue=0):
		'Replaces a pattern of text with new text in a document.'
		return self._oleobj_.InvokeTypes(144, LCID, 1, (11, 0), ((8, 1), (8, 1), (3, 49)),FindText
			, ReplaceText, vsFindOptionsValue)

	_prop_map_get_ = {
		# Method 'DTE' returns object of type 'DTE'
		"DTE": (150, 2, (13, 0), (), "DTE", '{3C9CFE1E-389F-4118-9FAD-365385190329}'),
		# Method 'EndPoint' returns object of type 'TextPoint'
		"EndPoint": (133, 2, (9, 0), (), "EndPoint", '{7F59E94E-4939-40D2-9F7F-B7651C25905D}'),
		"IndentSize": (135, 2, (3, 0), (), "IndentSize", None),
		"Language": (137, 2, (8, 0), (), "Language", None),
		# Method 'Parent' returns object of type 'Document'
		"Parent": (151, 2, (9, 0), (), "Parent", '{63EB5C39-CA8F-498E-9A66-6DD4A27AC95B}'),
		# Method 'Selection' returns object of type 'TextSelection'
		"Selection": (1, 2, (9, 0), (), "Selection", '{1FA0E135-399A-4D2C-A4FE-D21E2480F921}'),
		# Method 'StartPoint' returns object of type 'TextPoint'
		"StartPoint": (132, 2, (9, 0), (), "StartPoint", '{7F59E94E-4939-40D2-9F7F-B7651C25905D}'),
		"TabSize": (140, 2, (3, 0), (), "TabSize", None),
		"Type": (145, 2, (8, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Language": ((137, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{CB218890-1382-472B-9118-782700C88115}", TextDocument )
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

TextDocument_vtables_dispatch_ = 1
TextDocument_vtables_ = [
	(( 'DTE' , 'ppDTE' , ), 150, (150, (), [ (16397, 10, None, "IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'ppParent' , ), 151, (151, (), [ (16393, 10, None, "IID('{63EB5C39-CA8F-498E-9A66-6DD4A27AC95B}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Selection' , 'ppSel' , ), 1, (1, (), [ (16393, 10, None, "IID('{1FA0E135-399A-4D2C-A4FE-D21E2480F921}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ClearBookmarks' , ), 122, (122, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'MarkText' , 'Pattern' , 'vsFindOptionsValue' , 'pbRetVal' , ), 124, (124, (), [ 
			 (8, 1, None, None) , (3, 49, '0', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ReplacePattern' , 'Pattern' , 'Replace' , 'vsFindOptionsValue' , 'Tags' , 
			 'pbRetVal' , ), 128, (128, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , 
			 (16393, 51, '0', "IID('{B6422E9C-9EFD-4F87-BDDC-C7FD8F2FD303}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'CreateEditPoint' , 'TextPoint' , 'lppaReturn' , ), 131, (131, (), [ (9, 49, '0', "IID('{7F59E94E-4939-40D2-9F7F-B7651C25905D}')") , 
			 (16393, 10, None, "IID('{C1FFE800-028B-4475-A907-14F51F19BB7D}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'StartPoint' , 'pStartPoint' , ), 132, (132, (), [ (16393, 10, None, "IID('{7F59E94E-4939-40D2-9F7F-B7651C25905D}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'EndPoint' , 'pEndPoint' , ), 133, (133, (), [ (16393, 10, None, "IID('{7F59E94E-4939-40D2-9F7F-B7651C25905D}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Language' , 'pLanguage' , ), 137, (137, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 64 , )),
	(( 'Language' , 'pLanguage' , ), 137, (137, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 64 , )),
	(( 'Type' , 'pType' , ), 145, (145, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( 'IndentSize' , 'pSize' , ), 135, (135, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( 'TabSize' , 'pSize' , ), 140, (140, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
	(( 'ReplaceText' , 'FindText' , 'ReplaceText' , 'vsFindOptionsValue' , 'pbRetVal' , 
			 ), 144, (144, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 64 , )),
	(( 'PrintOut' , ), 134, (134, (), [ ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 64 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{CB218890-1382-472B-9118-782700C88115}", TextDocument )
