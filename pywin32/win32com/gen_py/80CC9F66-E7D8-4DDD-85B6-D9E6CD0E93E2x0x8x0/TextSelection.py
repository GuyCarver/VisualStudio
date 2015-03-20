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
class TextSelection(DispatchBaseClass):
	'Object representing the selection or caret in a text view.'
	CLSID = IID('{1FA0E135-399A-4D2C-A4FE-D21E2480F921}')
	coclass_clsid = None

	def Backspace(self, Count=1):
		'Deletes a specified number of characters to the left of the active point. The default is 1 character.'
		return self._oleobj_.InvokeTypes(80, LCID, 1, (24, 0), ((3, 49),),Count
			)

	def Cancel(self):
		'Collapses the selection to the active point.'
		return self._oleobj_.InvokeTypes(81, LCID, 1, (24, 0), (),)

	def ChangeCase(self, How=defaultNamedNotOptArg):
		'Changes the case of the selected text.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((3, 1),),How
			)

	def CharLeft(self, Extend=False, Count=1):
		'Moves the object the specified number of characters to the left. The default is 1 character.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((11, 49), (3, 49)),Extend
			, Count)

	def CharRight(self, Extend=False, Count=1):
		'Moves the object the specified number of characters to the right. The default is 1 character.'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((11, 49), (3, 49)),Extend
			, Count)

	def ClearBookmark(self):
		'Clears any unnamed bookmarks on the current line.'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), (),)

	def Collapse(self):
		'Collapses the selection to the active point.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	def Copy(self):
		'Copies the selection to the clipboard.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Copies the selection to the clipboard and deletes it.'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), (),)

	def Delete(self, Count=1):
		'Deletes the selection.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((3, 49),),Count
			)

	def DeleteLeft(self, Count=1):
		'Deletes a specified number of characters to the left of the active point. The default is 1 character.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), ((3, 49),),Count
			)

	def DeleteWhitespace(self, Direction=0):
		'Deletes white space horizontally or vertically around the current location.'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), ((3, 49),),Direction
			)

	def DestructiveInsert(self, Text=defaultNamedNotOptArg):
		'Inserts text, overwriting the existing text.'
		return self._oleobj_.InvokeTypes(57, LCID, 1, (24, 0), ((8, 1),),Text
			)

	def EndOfDocument(self, Extend=False):
		'Moves the object to the end of the document.'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), ((11, 49),),Extend
			)

	def EndOfLine(self, Extend=False):
		'Moves the object to the end of the current line.'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), ((11, 49),),Extend
			)

	def FindPattern(self, Pattern=defaultNamedNotOptArg, vsFindOptionsValue=0, Tags=0):
		'Searches for the given pattern from the active point to the end of the document.'
		return self._ApplyTypes_(30, 1, (11, 0), ((8, 1), (3, 49), (16393, 51)), 'FindPattern', None,Pattern
			, vsFindOptionsValue, Tags)

	def FindText(self, Pattern=defaultNamedNotOptArg, vsFindOptionsValue=0):
		'Searches for the given pattern from the active point to the end of the document.'
		return self._oleobj_.InvokeTypes(70, LCID, 1, (11, 0), ((8, 1), (3, 49)),Pattern
			, vsFindOptionsValue)

	def GotoLine(self, Line=defaultNamedNotOptArg, Select=False):
		'Moves to the beginning of the indicated line and selects the line if requested.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), ((3, 1), (11, 49)),Line
			, Select)

	def Indent(self, Count=1):
		'Indents the lines of the selection by the number of indentation levels given. The default is 1 indentation level.'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((3, 49),),Count
			)

	def Insert(self, Text=defaultNamedNotOptArg, vsInsertFlagsCollapseToEndValue=1):
		'Inserts the given string at the current location.'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (24, 0), ((8, 1), (3, 49)),Text
			, vsInsertFlagsCollapseToEndValue)

	def InsertFromFile(self, File=defaultNamedNotOptArg):
		'Inserts the contents of the specified file at the current location.'
		return self._oleobj_.InvokeTypes(61, LCID, 1, (24, 0), ((8, 1),),File
			)

	def LineDown(self, Extend=False, Count=1):
		'Moves the object down by the specified number of lines. The default is 1 line.'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (24, 0), ((11, 49), (3, 49)),Extend
			, Count)

	def LineUp(self, Extend=False, Count=1):
		'Moves the object up by the specified number of lines. The default is 1 line.'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (24, 0), ((11, 49), (3, 49)),Extend
			, Count)

	def MoveTo(self, Line=defaultNamedNotOptArg, Column=defaultNamedNotOptArg, Extend=False):
		'Moves the active point to the indicated display column.'
		return self._oleobj_.InvokeTypes(82, LCID, 1, (24, 0), ((3, 1), (3, 1), (11, 49)),Line
			, Column, Extend)

	def MoveToAbsoluteOffset(self, Offset=defaultNamedNotOptArg, Extend=False):
		'Moves the active point to the given 1-based absolute character offset.'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), ((3, 1), (11, 49)),Offset
			, Extend)

	def MoveToDisplayColumn(self, Line=defaultNamedNotOptArg, Column=defaultNamedNotOptArg, Extend=False):
		'Moves the active point to the indicated display column.'
		return self._oleobj_.InvokeTypes(58, LCID, 1, (24, 0), ((3, 1), (3, 1), (11, 49)),Line
			, Column, Extend)

	def MoveToLineAndOffset(self, Line=defaultNamedNotOptArg, Offset=defaultNamedNotOptArg, Extend=False):
		'Moves the active point to the given position.'
		return self._oleobj_.InvokeTypes(39, LCID, 1, (24, 0), ((3, 1), (3, 1), (11, 49)),Line
			, Offset, Extend)

	def MoveToPoint(self, Point=defaultNamedNotOptArg, Extend=False):
		'Moves the active point to the given position.'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), ((9, 1), (11, 49)),Point
			, Extend)

	def NewLine(self, Count=1):
		'Inserts a line break at the active point.'
		return self._oleobj_.InvokeTypes(41, LCID, 1, (24, 0), ((3, 49),),Count
			)

	def NextBookmark(self):
		'Moves to the location of the next bookmark in the document.'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (11, 0), (),)

	def OutlineSection(self):
		'Creates an outlining section based on the current selection.'
		return self._oleobj_.InvokeTypes(72, LCID, 1, (24, 0), (),)

	def PadToColumn(self, Column=defaultNamedNotOptArg):
		'Fills the current line with white space to the given column.'
		return self._oleobj_.InvokeTypes(45, LCID, 1, (24, 0), ((3, 1),),Column
			)

	def PageDown(self, Extend=False, Count=1):
		'Moves the active point a specified number of pages down in the document, scrolling the view.'
		return self._oleobj_.InvokeTypes(60, LCID, 1, (24, 0), ((11, 49), (3, 49)),Extend
			, Count)

	def PageUp(self, Extend=False, Count=1):
		'Moves the active point a specified number of pages up in the document, scrolling the view.'
		return self._oleobj_.InvokeTypes(59, LCID, 1, (24, 0), ((11, 49), (3, 49)),Extend
			, Count)

	def Paste(self):
		'Inserts the clipboard contents at the current location.'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def PreviousBookmark(self):
		'Moves to the location of the previous bookmark in the document.'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (11, 0), (),)

	def ReplacePattern(self, Pattern=defaultNamedNotOptArg, Replace=defaultNamedNotOptArg, vsFindOptionsValue=0, Tags=0):
		'Searches for the given pattern in the selection and replaces it with new text.'
		return self._ApplyTypes_(31, 1, (11, 0), ((8, 1), (8, 1), (3, 49), (16393, 51)), 'ReplacePattern', None,Pattern
			, Replace, vsFindOptionsValue, Tags)

	def ReplaceText(self, Pattern=defaultNamedNotOptArg, Replace=defaultNamedNotOptArg, vsFindOptionsValue=0):
		'Searches for the given pattern in the selection and replaces it with new text.'
		return self._oleobj_.InvokeTypes(71, LCID, 1, (11, 0), ((8, 1), (8, 1), (3, 49)),Pattern
			, Replace, vsFindOptionsValue)

	def SelectAll(self):
		'Selects the document.'
		return self._oleobj_.InvokeTypes(47, LCID, 1, (24, 0), (),)

	def SelectLine(self):
		'Selects the line containing the active point.'
		return self._oleobj_.InvokeTypes(48, LCID, 1, (24, 0), (),)

	def SetBookmark(self):
		'Sets an unnamed bookmark on the current line.'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (24, 0), (),)

	def SmartFormat(self):
		'Formats the indicated span of text based on the current language.'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (24, 0), (),)

	def StartOfDocument(self, Extend=False):
		'Moves the object to the beginning of the document.'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), ((11, 49),),Extend
			)

	def StartOfLine(self, Where=0, Extend=False):
		'Moves the object to the beginning of the current line.'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (24, 0), ((3, 49), (11, 49)),Where
			, Extend)

	def SwapAnchor(self):
		'Exchanges the positions of the active point and the anchor point.'
		return self._oleobj_.InvokeTypes(49, LCID, 1, (24, 0), (),)

	def Tabify(self):
		"Converts spaces to tabs in the selection according to the user's tab settings."
		return self._oleobj_.InvokeTypes(50, LCID, 1, (24, 0), (),)

	def Unindent(self, Count=1):
		'Removes indents from the selected lines by the number of indentation levels given. The default is 1 indentation level.'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (24, 0), ((3, 49),),Count
			)

	def Untabify(self):
		"Converts tabs to spaces in the selection according to the user's tab settings."
		return self._oleobj_.InvokeTypes(51, LCID, 1, (24, 0), (),)

	def WordLeft(self, Extend=False, Count=1):
		'Moves the object the specified number of words to the left. The default is 1 word.'
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), ((11, 49), (3, 49)),Extend
			, Count)

	def WordRight(self, Extend=False, Count=1):
		'Moves the object the specified number of words to the right. The default is 1 word.'
		return self._oleobj_.InvokeTypes(53, LCID, 1, (24, 0), ((11, 49), (3, 49)),Extend
			, Count)

	_prop_map_get_ = {
		# Method 'ActivePoint' returns object of type 'VirtualPoint'
		"ActivePoint": (4, 2, (9, 0), (), "ActivePoint", '{42320454-626C-4DD0-9ECB-357C4F1966D8}'),
		"AnchorColumn": (5, 2, (3, 0), (), "AnchorColumn", None),
		# Method 'AnchorPoint' returns object of type 'VirtualPoint'
		"AnchorPoint": (3, 2, (9, 0), (), "AnchorPoint", '{42320454-626C-4DD0-9ECB-357C4F1966D8}'),
		"BottomLine": (6, 2, (3, 0), (), "BottomLine", None),
		# Method 'BottomPoint' returns object of type 'VirtualPoint'
		"BottomPoint": (7, 2, (9, 0), (), "BottomPoint", '{42320454-626C-4DD0-9ECB-357C4F1966D8}'),
		"CurrentColumn": (8, 2, (3, 0), (), "CurrentColumn", None),
		"CurrentLine": (9, 2, (3, 0), (), "CurrentLine", None),
		# Method 'DTE' returns object of type 'DTE'
		"DTE": (1, 2, (13, 0), (), "DTE", '{3C9CFE1E-389F-4118-9FAD-365385190329}'),
		"IsActiveEndGreater": (11, 2, (11, 0), (), "IsActiveEndGreater", None),
		"IsEmpty": (10, 2, (11, 0), (), "IsEmpty", None),
		"Mode": (55, 2, (3, 0), (), "Mode", None),
		# Method 'Parent' returns object of type 'TextDocument'
		"Parent": (2, 2, (9, 0), (), "Parent", '{CB218890-1382-472B-9118-782700C88115}'),
		"Text": (0, 2, (8, 0), (), "Text", None),
		# Method 'TextPane' returns object of type 'TextPane'
		"TextPane": (54, 2, (9, 0), (), "TextPane", '{0A3BF283-05F8-4669-9BCB-A84B6423349A}'),
		# Method 'TextRanges' returns object of type 'TextRanges'
		"TextRanges": (56, 2, (9, 0), (), "TextRanges", '{B6422E9C-9EFD-4F87-BDDC-C7FD8F2FD303}'),
		"TopLine": (13, 2, (3, 0), (), "TopLine", None),
		# Method 'TopPoint' returns object of type 'VirtualPoint'
		"TopPoint": (14, 2, (9, 0), (), "TopPoint", '{42320454-626C-4DD0-9ECB-357C4F1966D8}'),
	}
	_prop_map_put_ = {
		"Mode": ((55, LCID, 4, 0),()),
		"Text": ((0, LCID, 4, 0),()),
	}
	# Default property for this class is 'Text'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "Text", None))
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

win32com.client.CLSIDToClass.RegisterCLSID( "{1FA0E135-399A-4D2C-A4FE-D21E2480F921}", TextSelection )
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

TextSelection_vtables_dispatch_ = 1
TextSelection_vtables_ = [
	(( 'DTE' , 'ppDTE' , ), 1, (1, (), [ (16397, 10, None, "IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'ppParent' , ), 2, (2, (), [ (16393, 10, None, "IID('{CB218890-1382-472B-9118-782700C88115}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AnchorPoint' , 'ppPoint' , ), 3, (3, (), [ (16393, 10, None, "IID('{42320454-626C-4DD0-9ECB-357C4F1966D8}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ActivePoint' , 'ppPoint' , ), 4, (4, (), [ (16393, 10, None, "IID('{42320454-626C-4DD0-9ECB-357C4F1966D8}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'AnchorColumn' , 'pColumn' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 64 , )),
	(( 'BottomLine' , 'pLine' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 64 , )),
	(( 'BottomPoint' , 'ppPoint' , ), 7, (7, (), [ (16393, 10, None, "IID('{42320454-626C-4DD0-9ECB-357C4F1966D8}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'CurrentColumn' , 'pColumn' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 64 , )),
	(( 'CurrentLine' , 'pLine' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 64 , )),
	(( 'IsEmpty' , 'pfEmpty' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'IsActiveEndGreater' , 'pfGreater' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'pText' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'pText' , ), 0, (0, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TopLine' , 'pLine' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
	(( 'TopPoint' , 'ppPoint' , ), 14, (14, (), [ (16393, 10, None, "IID('{42320454-626C-4DD0-9ECB-357C4F1966D8}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ChangeCase' , 'How' , ), 15, (15, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CharLeft' , 'Extend' , 'Count' , ), 16, (16, (), [ (11, 49, 'False', None) , 
			 (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CharRight' , 'Extend' , 'Count' , ), 17, (17, (), [ (11, 49, 'False', None) , 
			 (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ClearBookmark' , ), 18, (18, (), [ ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Collapse' , ), 19, (19, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'OutlineSection' , ), 72, (72, (), [ ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , ), 20, (20, (), [ ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Cut' , ), 21, (21, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Paste' , ), 22, (22, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'Count' , ), 23, (23, (), [ (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DeleteLeft' , 'Count' , ), 24, (24, (), [ (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'DeleteWhitespace' , 'Direction' , ), 25, (25, (), [ (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'EndOfLine' , 'Extend' , ), 26, (26, (), [ (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'StartOfLine' , 'Where' , 'Extend' , ), 27, (27, (), [ (3, 49, '0', None) , 
			 (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'EndOfDocument' , 'Extend' , ), 28, (28, (), [ (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'StartOfDocument' , 'Extend' , ), 29, (29, (), [ (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'FindPattern' , 'Pattern' , 'vsFindOptionsValue' , 'Tags' , 'pfFound' , 
			 ), 30, (30, (), [ (8, 1, None, None) , (3, 49, '0', None) , (16393, 51, '0', "IID('{B6422E9C-9EFD-4F87-BDDC-C7FD8F2FD303}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ReplacePattern' , 'Pattern' , 'Replace' , 'vsFindOptionsValue' , 'Tags' , 
			 'pfFound' , ), 31, (31, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , 
			 (16393, 51, '0', "IID('{B6422E9C-9EFD-4F87-BDDC-C7FD8F2FD303}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'FindText' , 'Pattern' , 'vsFindOptionsValue' , 'pfFound' , ), 70, (70, (), [ 
			 (8, 1, None, None) , (3, 49, '0', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ReplaceText' , 'Pattern' , 'Replace' , 'vsFindOptionsValue' , 'pfFound' , 
			 ), 71, (71, (), [ (8, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 64 , )),
	(( 'GotoLine' , 'Line' , 'Select' , ), 32, (32, (), [ (3, 1, None, None) , 
			 (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Indent' , 'Count' , ), 33, (33, (), [ (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Unindent' , 'Count' , ), 34, (34, (), [ (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Insert' , 'Text' , 'vsInsertFlagsCollapseToEndValue' , ), 35, (35, (), [ (8, 1, None, None) , 
			 (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'InsertFromFile' , 'File' , ), 61, (61, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'LineDown' , 'Extend' , 'Count' , ), 36, (36, (), [ (11, 49, 'False', None) , 
			 (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'LineUp' , 'Extend' , 'Count' , ), 37, (37, (), [ (11, 49, 'False', None) , 
			 (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'MoveToPoint' , 'Point' , 'Extend' , ), 38, (38, (), [ (9, 1, None, "IID('{7F59E94E-4939-40D2-9F7F-B7651C25905D}')") , 
			 (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'MoveToLineAndOffset' , 'Line' , 'Offset' , 'Extend' , ), 39, (39, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'MoveToAbsoluteOffset' , 'Offset' , 'Extend' , ), 40, (40, (), [ (3, 1, None, None) , 
			 (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'NewLine' , 'Count' , ), 41, (41, (), [ (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'SetBookmark' , ), 42, (42, (), [ ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'NextBookmark' , 'pbFound' , ), 43, (43, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'PreviousBookmark' , 'pbFound' , ), 44, (44, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'PadToColumn' , 'Column' , ), 45, (45, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'SmartFormat' , ), 46, (46, (), [ ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'SelectAll' , ), 47, (47, (), [ ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'SelectLine' , ), 48, (48, (), [ ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'SwapAnchor' , ), 49, (49, (), [ ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Tabify' , ), 50, (50, (), [ ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Untabify' , ), 51, (51, (), [ ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'WordLeft' , 'Extend' , 'Count' , ), 52, (52, (), [ (11, 49, 'False', None) , 
			 (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'WordRight' , 'Extend' , 'Count' , ), 53, (53, (), [ (11, 49, 'False', None) , 
			 (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'TextPane' , 'ppPane' , ), 54, (54, (), [ (16393, 10, None, "IID('{0A3BF283-05F8-4669-9BCB-A84B6423349A}')") , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'Mode' , 'pMode' , ), 55, (55, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Mode' , 'pMode' , ), 55, (55, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'TextRanges' , 'ppRanges' , ), 56, (56, (), [ (16393, 10, None, "IID('{B6422E9C-9EFD-4F87-BDDC-C7FD8F2FD303}')") , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Backspace' , 'Count' , ), 80, (80, (), [ (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 552 , (3, 0, None, None) , 64 , )),
	(( 'Cancel' , ), 81, (81, (), [ ], 1 , 1 , 4 , 0 , 560 , (3, 0, None, None) , 64 , )),
	(( 'DestructiveInsert' , 'Text' , ), 57, (57, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'MoveTo' , 'Line' , 'Column' , 'Extend' , ), 82, (82, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 64 , )),
	(( 'MoveToDisplayColumn' , 'Line' , 'Column' , 'Extend' , ), 58, (58, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'PageUp' , 'Extend' , 'Count' , ), 59, (59, (), [ (11, 49, 'False', None) , 
			 (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'PageDown' , 'Extend' , 'Count' , ), 60, (60, (), [ (11, 49, 'False', None) , 
			 (3, 49, '1', None) , ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{1FA0E135-399A-4D2C-A4FE-D21E2480F921}", TextSelection )
