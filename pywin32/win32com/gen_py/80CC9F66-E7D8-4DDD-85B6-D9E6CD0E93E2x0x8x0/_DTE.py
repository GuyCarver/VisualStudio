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

from win32com.client import DispatchBaseClass
class _DTE(DispatchBaseClass):
	'Root object from which all other objects and collections in environment extensibility are accessed.'
	CLSID = IID('{04A72314-32E9-48E2-9B87-A63603454F3E}')
	coclass_clsid = IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')

	def ExecuteCommand(self, CommandName=defaultNamedNotOptArg, CommandArgs=''):
		"Executes a environment command based on it's name."
		return self._ApplyTypes_(222, 1, (24, 32), ((8, 1), (8, 49)), 'ExecuteCommand', None,CommandName
			, CommandArgs)

	def GetObject(self, Name=defaultNamedNotOptArg):
		'Returns an interface or object that can be accessed at run time by name.'
		ret = self._oleobj_.InvokeTypes(211, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObject', None)
		return ret

	# The method IsOpenFile is actually a property, but must be used as a method to correctly pass the arguments
	def IsOpenFile(self, ViewKind=defaultNamedNotOptArg, FileName=defaultNamedNotOptArg):
		'Returns True if the file is open in the specified view.'
		return self._oleobj_.InvokeTypes(216, LCID, 2, (11, 0), ((8, 1), (8, 1)),ViewKind
			, FileName)

	def LaunchWizard(self, VSZFile=defaultNamedNotOptArg, ContextParams=defaultNamedNotOptArg):
		'Runs a wizard with the user supplied parameters.'
		return self._oleobj_.InvokeTypes(232, LCID, 1, (3, 0), ((8, 1), (24588, 1)),VSZFile
			, ContextParams)

	# Result is of type Window
	def OpenFile(self, ViewKind=defaultNamedNotOptArg, FileName=defaultNamedNotOptArg):
		'Opens a file as though the user invoked a open file command from the UI.'
		ret = self._oleobj_.InvokeTypes(215, LCID, 1, (9, 0), ((8, 1), (8, 1)),ViewKind
			, FileName)
		if ret is not None:
			ret = Dispatch(ret, 'OpenFile', '{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}')
		return ret

	# Result is of type Properties
	# The method Properties is actually a property, but must be used as a method to correctly pass the arguments
	def Properties(self, Category=defaultNamedNotOptArg, Page=defaultNamedNotOptArg):
		'Returns collection object representing all available categories and subcategories of environment-level properties.'
		ret = self._oleobj_.InvokeTypes(212, LCID, 2, (9, 0), ((8, 0), (8, 0)),Category
			, Page)
		if ret is not None:
			ret = Dispatch(ret, 'Properties', '{4CC8CCF5-A926-4646-B17F-B4940CAED472}')
		return ret

	def Quit(self):
		'Closes the environment.'
		return self._oleobj_.InvokeTypes(207, LCID, 1, (24, 0), (),)

	def SatelliteDllPath(self, Path=defaultNamedNotOptArg, Name=defaultNamedNotOptArg):
		'Returns the location of a DLL containing localized resources, if available.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(245, LCID, 1, (8, 0), ((8, 0), (8, 0)),Path
			, Name)

	_prop_map_get_ = {
		# Method 'ActiveDocument' returns object of type 'Document'
		"ActiveDocument": (221, 2, (9, 0), (), "ActiveDocument", '{63EB5C39-CA8F-498E-9A66-6DD4A27AC95B}'),
		"ActiveSolutionProjects": (237, 2, (12, 0), (), "ActiveSolutionProjects", None),
		# Method 'ActiveWindow' returns object of type 'Window'
		"ActiveWindow": (205, 2, (9, 0), (), "ActiveWindow", '{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}'),
		# Method 'AddIns' returns object of type 'AddIns'
		"AddIns": (200, 2, (9, 0), (), "AddIns", '{50590801-D13E-4404-80C2-5CA30A4D0EE8}'),
		# Method 'Application' returns object of type 'DTE'
		"Application": (240, 2, (13, 0), (), "Application", '{3C9CFE1E-389F-4118-9FAD-365385190329}'),
		"CommandBars": (108, 2, (9, 0), (), "CommandBars", None),
		"CommandLineArguments": (214, 2, (8, 0), (), "CommandLineArguments", None),
		# Method 'Commands' returns object of type 'Commands'
		"Commands": (210, 2, (9, 0), (), "Commands", '{E6B96CAC-B8C7-40AE-B705-5C81878C4A9E}'),
		# Method 'ContextAttributes' returns object of type 'ContextAttributes'
		"ContextAttributes": (241, 2, (9, 0), (), "ContextAttributes", '{33C5EBB8-244E-449D-9CEE-FAD70A774E59}'),
		# Method 'DTE' returns object of type 'DTE'
		"DTE": (217, 2, (13, 0), (), "DTE", '{3C9CFE1E-389F-4118-9FAD-365385190329}'),
		# Method 'Debugger' returns object of type 'Debugger'
		"Debugger": (244, 2, (9, 0), (), "Debugger", '{338FB9A0-BAE5-11D2-8AD1-00C04F79E479}'),
		"DisplayMode": (208, 2, (3, 0), (), "DisplayMode", None),
		# Method 'Documents' returns object of type 'Documents'
		"Documents": (220, 2, (9, 0), (), "Documents", '{9E2CF3EA-140F-413E-BD4B-7D46740CD2F4}'),
		"Edition": (246, 2, (8, 0), (), "Edition", None),
		# Method 'Events' returns object of type 'Events'
		"Events": (111, 2, (9, 0), (), "Events", '{134170F8-93B1-42DD-9F89-A2AC7010BA07}'),
		"FileName": (10, 2, (8, 0), (), "FileName", None),
		# Method 'Find' returns object of type 'Find'
		"Find": (229, 2, (9, 0), (), "Find", '{40D4B9B6-739B-4965-8D65-692AEC692266}'),
		"FullName": (226, 2, (8, 0), (), "FullName", None),
		# Method 'Globals' returns object of type 'Globals'
		"Globals": (223, 2, (9, 0), (), "Globals", '{E68A3E0E-B435-4DDE-86B7-F5ADEFC19DF2}'),
		# Method 'ItemOperations' returns object of type 'ItemOperations'
		"ItemOperations": (233, 2, (9, 0), (), "ItemOperations", '{D5DBE57B-C074-4E95-B015-ABEEAA391693}'),
		"LocaleID": (218, 2, (3, 0), (), "LocaleID", None),
		# Method 'Macros' returns object of type 'Macros'
		"Macros": (236, 2, (9, 0), (), "Macros", '{F9F99155-6D4D-49B1-AD63-C78C3E8A5916}'),
		# Method 'MacrosIDE' returns object of type 'DTE'
		"MacrosIDE": (238, 2, (13, 0), (), "MacrosIDE", '{3C9CFE1E-389F-4118-9FAD-365385190329}'),
		# Method 'MainWindow' returns object of type 'Window'
		"MainWindow": (204, 2, (9, 0), (), "MainWindow", '{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}'),
		"Mode": (230, 2, (3, 0), (), "Mode", None),
		"Name": (0, 2, (8, 0), (), "Name", None),
		# Method 'ObjectExtenders' returns object of type 'ObjectExtenders'
		"ObjectExtenders": (228, 2, (9, 0), (), "ObjectExtenders", '{8D0AA9CC-8465-42F3-AD6E-DFDE28CCC75D}'),
		"RegistryRoot": (239, 2, (8, 0), (), "RegistryRoot", None),
		# Method 'SelectedItems' returns object of type 'SelectedItems'
		"SelectedItems": (213, 2, (9, 0), (), "SelectedItems", '{6CAA67CF-43AE-4184-AAAB-0200DDF6B240}'),
		# Method 'Solution' returns object of type 'Solution'
		"Solution": (209, 2, (13, 0), (), "Solution", '{B35CAA8C-77DE-4AB3-8E5A-F038E3FC6056}'),
		# Method 'SourceControl' returns object of type 'SourceControl'
		"SourceControl": (242, 2, (9, 0), (), "SourceControl", '{F1DDC2C2-DF76-4EBB-9DE8-48AD2557062C}'),
		# Method 'StatusBar' returns object of type 'StatusBar'
		"StatusBar": (225, 2, (9, 0), (), "StatusBar", '{C34301A1-3EF1-41D8-932A-FEA4A8A8CE0C}'),
		"SuppressUI": (243, 2, (11, 0), (), "SuppressUI", None),
		# Method 'UndoContext' returns object of type 'UndoContext'
		"UndoContext": (235, 2, (9, 0), (), "UndoContext", '{D8DEC44D-CAF2-4B39-A539-B91AE921BA92}'),
		"UserControl": (227, 2, (11, 0), (), "UserControl", None),
		"Version": (100, 2, (8, 0), (), "Version", None),
		# Method 'WindowConfigurations' returns object of type 'WindowConfigurations'
		"WindowConfigurations": (219, 2, (9, 0), (), "WindowConfigurations", '{E577442A-98E1-46C5-BD2E-D25807EC81CE}'),
		# Method 'Windows' returns object of type 'Windows'
		"Windows": (110, 2, (9, 0), (), "Windows", '{2294311A-B7BC-4789-B365-1C15FF2CD17C}'),
	}
	_prop_map_put_ = {
		"DisplayMode": ((208, LCID, 4, 0),()),
		"SuppressUI": ((243, LCID, 4, 0),()),
		"UserControl": ((227, LCID, 4, 0),()),
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

win32com.client.CLSIDToClass.RegisterCLSID( "{04A72314-32E9-48E2-9B87-A63603454F3E}", _DTE )
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

_DTE_vtables_dispatch_ = 1
_DTE_vtables_ = [
	(( 'Name' , 'lpbstrReturn' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'lpbstrReturn' , ), 10, (10, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 64 , )),
	(( 'Version' , 'lpbstrReturn' , ), 100, (100, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'CommandBars' , 'ppcbs' , ), 108, (108, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Windows' , 'ppwnsVBWindows' , ), 110, (110, (), [ (16393, 10, None, "IID('{2294311A-B7BC-4789-B365-1C15FF2CD17C}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Events' , 'ppevtEvents' , ), 111, (111, (), [ (16393, 10, None, "IID('{134170F8-93B1-42DD-9F89-A2AC7010BA07}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AddIns' , 'lpppAddIns' , ), 200, (200, (), [ (16393, 10, None, "IID('{50590801-D13E-4404-80C2-5CA30A4D0EE8}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'MainWindow' , 'ppWin' , ), 204, (204, (), [ (16393, 10, None, "IID('{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ActiveWindow' , 'ppwinActive' , ), 205, (205, (), [ (16393, 10, None, "IID('{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Quit' , ), 207, (207, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'DisplayMode' , 'lpDispMode' , ), 208, (208, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DisplayMode' , 'lpDispMode' , ), 208, (208, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Solution' , 'ppSolution' , ), 209, (209, (), [ (16397, 10, None, "IID('{B35CAA8C-77DE-4AB3-8E5A-F038E3FC6056}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Commands' , 'ppCommands' , ), 210, (210, (), [ (16393, 10, None, "IID('{E6B96CAC-B8C7-40AE-B705-5C81878C4A9E}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GetObject' , 'Name' , 'ppObject' , ), 211, (211, (), [ (8, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Properties' , 'Category' , 'Page' , 'ppObject' , ), 212, (212, (), [ 
			 (8, 0, None, None) , (8, 0, None, None) , (16393, 10, None, "IID('{4CC8CCF5-A926-4646-B17F-B4940CAED472}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SelectedItems' , 'ppSelectedItems' , ), 213, (213, (), [ (16393, 10, None, "IID('{6CAA67CF-43AE-4184-AAAB-0200DDF6B240}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CommandLineArguments' , 'lpbstrReturn' , ), 214, (214, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'OpenFile' , 'ViewKind' , 'FileName' , 'ppWin' , ), 215, (215, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
	(( 'IsOpenFile' , 'ViewKind' , 'FileName' , 'lpfReturn' , ), 216, (216, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 64 , )),
	(( 'DTE' , 'lppaReturn' , ), 217, (217, (), [ (16397, 10, None, "IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'LocaleID' , 'lpReturn' , ), 218, (218, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'WindowConfigurations' , 'WindowConfigurationsObject' , ), 219, (219, (), [ (16393, 10, None, "IID('{E577442A-98E1-46C5-BD2E-D25807EC81CE}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Documents' , 'ppDocuments' , ), 220, (220, (), [ (16393, 10, None, "IID('{9E2CF3EA-140F-413E-BD4B-7D46740CD2F4}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ActiveDocument' , 'ppDocument' , ), 221, (221, (), [ (16393, 10, None, "IID('{63EB5C39-CA8F-498E-9A66-6DD4A27AC95B}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteCommand' , 'CommandName' , 'CommandArgs' , ), 222, (222, (), [ (8, 1, None, None) , 
			 (8, 49, "''", None) , ], 1 , 1 , 4 , 0 , 256 , (3, 32, None, None) , 0 , )),
	(( 'Globals' , 'ppGlobals' , ), 223, (223, (), [ (16393, 10, None, "IID('{E68A3E0E-B435-4DDE-86B7-F5ADEFC19DF2}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'StatusBar' , 'ppStatusBar' , ), 225, (225, (), [ (16393, 10, None, "IID('{C34301A1-3EF1-41D8-932A-FEA4A8A8CE0C}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'FullName' , 'lpbstrReturn' , ), 226, (226, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UserControl' , 'UserControl' , ), 227, (227, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UserControl' , 'UserControl' , ), 227, (227, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ObjectExtenders' , 'ppObjectExtenders' , ), 228, (228, (), [ (16393, 10, None, "IID('{8D0AA9CC-8465-42F3-AD6E-DFDE28CCC75D}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Find' , 'ppFind' , ), 229, (229, (), [ (16393, 10, None, "IID('{40D4B9B6-739B-4965-8D65-692AEC692266}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Mode' , 'pVal' , ), 230, (230, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'LaunchWizard' , 'VSZFile' , 'ContextParams' , 'pResult' , ), 232, (232, (), [ 
			 (8, 1, None, None) , (24588, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ItemOperations' , 'ppItemOperations' , ), 233, (233, (), [ (16393, 10, None, "IID('{D5DBE57B-C074-4E95-B015-ABEEAA391693}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UndoContext' , 'ppUndoContext' , ), 235, (235, (), [ (16393, 10, None, "IID('{D8DEC44D-CAF2-4B39-A539-B91AE921BA92}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Macros' , 'ppMacros' , ), 236, (236, (), [ (16393, 10, None, "IID('{F9F99155-6D4D-49B1-AD63-C78C3E8A5916}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ActiveSolutionProjects' , 'pProjects' , ), 237, (237, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'MacrosIDE' , 'pDTE' , ), 238, (238, (), [ (16397, 10, None, "IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'RegistryRoot' , 'pVal' , ), 239, (239, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'pVal' , ), 240, (240, (), [ (16397, 10, None, "IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 64 , )),
	(( 'ContextAttributes' , 'ppVal' , ), 241, (241, (), [ (16393, 10, None, "IID('{33C5EBB8-244E-449D-9CEE-FAD70A774E59}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'SourceControl' , 'ppVal' , ), 242, (242, (), [ (16393, 10, None, "IID('{F1DDC2C2-DF76-4EBB-9DE8-48AD2557062C}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'SuppressUI' , 'pVal' , ), 243, (243, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'SuppressUI' , 'pVal' , ), 243, (243, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Debugger' , 'ppDebugger' , ), 244, (244, (), [ (16393, 10, None, "IID('{338FB9A0-BAE5-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'SatelliteDllPath' , 'Path' , 'Name' , 'pFullPath' , ), 245, (245, (), [ 
			 (8, 0, None, None) , (8, 0, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Edition' , 'ProductEdition' , ), 246, (246, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{04A72314-32E9-48E2-9B87-A63603454F3E}", _DTE )
