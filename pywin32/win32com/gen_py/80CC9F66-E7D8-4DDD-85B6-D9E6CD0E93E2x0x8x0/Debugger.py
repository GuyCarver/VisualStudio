# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)]
# From type library '{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}'
# On Thu Jun  6 08:27:57 2013
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
class Debugger(DispatchBaseClass):
	'Used to manipulate the general state of the debugger.'
	CLSID = IID('{338FB9A0-BAE5-11D2-8AD1-00C04F79E479}')
	coclass_clsid = None

	def Break(self, WaitForBreakMode=True):
		'Breaks the execution of all programs currently being debugged.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((11, 49),),WaitForBreakMode
			)

	def DetachAll(self):
		'Detaches from all attached programs.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), (),)

	def ExecuteStatement(self, Statement=defaultNamedNotOptArg, Timeout=-1, TreatAsExpression=False):
		'Executes a statement.  If the TreatAsExpression flag is true, then the string is interpreted as an expression.  Output is sent to the Command Window.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((8, 1), (3, 49), (11, 49)),Statement
			, Timeout, TreatAsExpression)

	# Result is of type Expression
	def GetExpression(self, ExpressionText=defaultNamedNotOptArg, UseAutoExpandRules=False, Timeout=-1):
		'Evaluates an expression based on the current stack frame.  If the expression is parsable, but could not be evaluated, an object is returned but will not contain a valid value.'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), ((8, 1), (11, 49), (3, 49)),ExpressionText
			, UseAutoExpandRules, Timeout)
		if ret is not None:
			ret = Dispatch(ret, 'GetExpression', '{27ADC812-BB07-11D2-8AD1-00C04F79E479}')
		return ret

	def Go(self, WaitForBreakOrEnd=True):
		'Starts executing the program from the current statement, or launches the active project.'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((11, 49),),WaitForBreakOrEnd
			)

	def RunToCursor(self, WaitForBreakOrEnd=True):
		'Executes the program to the current position of the source file cursor.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((11, 49),),WaitForBreakOrEnd
			)

	def SetNextStatement(self):
		'Sets the next instruction to be executed according to the current source file cursor position.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	def StepInto(self, WaitForBreakOrEnd=True):
		'Steps over the next statement unless it is a function call.  If so, will step to the beginning of the called function.'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((11, 49),),WaitForBreakOrEnd
			)

	def StepOut(self, WaitForBreakOrEnd=True):
		'Steps out of the current function.'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((11, 49),),WaitForBreakOrEnd
			)

	def StepOver(self, WaitForBreakOrEnd=True):
		'Steps over the next statement regardless of whether or not it is function call.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((11, 49),),WaitForBreakOrEnd
			)

	def Stop(self, WaitForDesignMode=True):
		'Stops debugging, terminating or detaching from all programs being debugged.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((11, 49),),WaitForDesignMode
			)

	def TerminateAll(self):
		'Terminates all attached programs.'
		return self._oleobj_.InvokeTypes(300, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'AllBreakpointsLastHit' returns object of type 'Breakpoints'
		"AllBreakpointsLastHit": (111, 2, (9, 0), (), "AllBreakpointsLastHit", '{25968106-BAFB-11D2-8AD1-00C04F79E479}'),
		# Method 'BreakpointLastHit' returns object of type 'Breakpoint'
		"BreakpointLastHit": (110, 2, (9, 0), (), "BreakpointLastHit", '{11C5114C-BB00-11D2-8AD1-00C04F79E479}'),
		# Method 'Breakpoints' returns object of type 'Breakpoints'
		"Breakpoints": (100, 2, (9, 0), (), "Breakpoints", '{25968106-BAFB-11D2-8AD1-00C04F79E479}'),
		"CurrentMode": (102, 2, (3, 0), (), "CurrentMode", None),
		# Method 'CurrentProcess' returns object of type 'Process'
		"CurrentProcess": (103, 2, (9, 0), (), "CurrentProcess", '{5C5A0070-F396-4E37-A82A-1B767E272DF9}'),
		# Method 'CurrentProgram' returns object of type 'Program'
		"CurrentProgram": (104, 2, (9, 0), (), "CurrentProgram", '{6A38D87C-BBA0-11D2-8AD1-00C04F79E479}'),
		# Method 'CurrentStackFrame' returns object of type 'StackFrame'
		"CurrentStackFrame": (106, 2, (9, 0), (), "CurrentStackFrame", '{1342D0D8-BBA3-11D2-8AD1-00C04F79E479}'),
		# Method 'CurrentThread' returns object of type 'Thread'
		"CurrentThread": (105, 2, (9, 0), (), "CurrentThread", '{9407F466-BBA1-11D2-8AD1-00C04F79E479}'),
		# Method 'DTE' returns object of type 'DTE'
		"DTE": (200, 2, (13, 0), (), "DTE", '{3C9CFE1E-389F-4118-9FAD-365385190329}'),
		# Method 'DebuggedProcesses' returns object of type 'Processes'
		"DebuggedProcesses": (112, 2, (9, 0), (), "DebuggedProcesses", '{9F379969-5EAC-4A54-B2BC-6946CFFB56EF}'),
		"HexDisplayMode": (107, 2, (11, 0), (), "HexDisplayMode", None),
		"HexInputMode": (108, 2, (11, 0), (), "HexInputMode", None),
		# Method 'Languages' returns object of type 'Languages'
		"Languages": (101, 2, (9, 0), (), "Languages", '{A4F4246C-C131-11D2-8AD1-00C04F79E479}'),
		"LastBreakReason": (109, 2, (3, 0), (), "LastBreakReason", None),
		# Method 'LocalProcesses' returns object of type 'Processes'
		"LocalProcesses": (113, 2, (9, 0), (), "LocalProcesses", '{9F379969-5EAC-4A54-B2BC-6946CFFB56EF}'),
		# Method 'Parent' returns object of type 'DTE'
		"Parent": (201, 2, (13, 0), (), "Parent", '{3C9CFE1E-389F-4118-9FAD-365385190329}'),
	}
	_prop_map_put_ = {
		"CurrentProcess": ((103, LCID, 4, 0),()),
		"CurrentProgram": ((104, LCID, 4, 0),()),
		"CurrentStackFrame": ((106, LCID, 4, 0),()),
		"CurrentThread": ((105, LCID, 4, 0),()),
		"HexDisplayMode": ((107, LCID, 4, 0),()),
		"HexInputMode": ((108, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

win32com.client.CLSIDToClass.RegisterCLSID( "{338FB9A0-BAE5-11D2-8AD1-00C04F79E479}", Debugger )
# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)]
# From type library '{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}'
# On Thu Jun  6 08:27:57 2013
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

Debugger_vtables_dispatch_ = 1
Debugger_vtables_ = [
	(( 'GetExpression' , 'ExpressionText' , 'UseAutoExpandRules' , 'Timeout' , 'Expression' , 
			 ), 1, (1, (), [ (8, 1, None, None) , (11, 49, 'False', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{27ADC812-BB07-11D2-8AD1-00C04F79E479}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DetachAll' , ), 2, (2, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'StepInto' , 'WaitForBreakOrEnd' , ), 3, (3, (), [ (11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StepOver' , 'WaitForBreakOrEnd' , ), 4, (4, (), [ (11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StepOut' , 'WaitForBreakOrEnd' , ), 5, (5, (), [ (11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Go' , 'WaitForBreakOrEnd' , ), 6, (6, (), [ (11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Break' , 'WaitForBreakMode' , ), 7, (7, (), [ (11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Stop' , 'WaitForDesignMode' , ), 8, (8, (), [ (11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SetNextStatement' , ), 9, (9, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RunToCursor' , 'WaitForBreakOrEnd' , ), 10, (10, (), [ (11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ExecuteStatement' , 'Statement' , 'Timeout' , 'TreatAsExpression' , ), 11, (11, (), [ 
			 (8, 1, None, None) , (3, 49, '-1', None) , (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Breakpoints' , 'Breakpoints' , ), 100, (100, (), [ (16393, 10, None, "IID('{25968106-BAFB-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Languages' , 'Languages' , ), 101, (101, (), [ (16393, 10, None, "IID('{A4F4246C-C131-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CurrentMode' , 'Mode' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CurrentProcess' , 'Process' , ), 103, (103, (), [ (16393, 10, None, "IID('{5C5A0070-F396-4E37-A82A-1B767E272DF9}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CurrentProcess' , 'Process' , ), 103, (103, (), [ (9, 1, None, "IID('{5C5A0070-F396-4E37-A82A-1B767E272DF9}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CurrentProgram' , 'Program' , ), 104, (104, (), [ (16393, 10, None, "IID('{6A38D87C-BBA0-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CurrentProgram' , 'Program' , ), 104, (104, (), [ (9, 1, None, "IID('{6A38D87C-BBA0-11D2-8AD1-00C04F79E479}')") , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CurrentThread' , 'Thread' , ), 105, (105, (), [ (16393, 10, None, "IID('{9407F466-BBA1-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CurrentThread' , 'Thread' , ), 105, (105, (), [ (9, 1, None, "IID('{9407F466-BBA1-11D2-8AD1-00C04F79E479}')") , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CurrentStackFrame' , 'StackFrame' , ), 106, (106, (), [ (16393, 10, None, "IID('{1342D0D8-BBA3-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CurrentStackFrame' , 'StackFrame' , ), 106, (106, (), [ (9, 1, None, "IID('{1342D0D8-BBA3-11D2-8AD1-00C04F79E479}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'HexDisplayMode' , 'HexModeOn' , ), 107, (107, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'HexDisplayMode' , 'HexModeOn' , ), 107, (107, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'HexInputMode' , 'HexModeOn' , ), 108, (108, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'HexInputMode' , 'HexModeOn' , ), 108, (108, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'LastBreakReason' , 'Reason' , ), 109, (109, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'BreakpointLastHit' , 'Breakpoint' , ), 110, (110, (), [ (16393, 10, None, "IID('{11C5114C-BB00-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'AllBreakpointsLastHit' , 'Breakpoints' , ), 111, (111, (), [ (16393, 10, None, "IID('{25968106-BAFB-11D2-8AD1-00C04F79E479}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'DebuggedProcesses' , 'Processes' , ), 112, (112, (), [ (16393, 10, None, "IID('{9F379969-5EAC-4A54-B2BC-6946CFFB56EF}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'LocalProcesses' , 'Processes' , ), 113, (113, (), [ (16393, 10, None, "IID('{9F379969-5EAC-4A54-B2BC-6946CFFB56EF}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'DTE' , 'DTE' , ), 200, (200, (), [ (16397, 10, None, "IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'DTE' , ), 201, (201, (), [ (16397, 10, None, "IID('{3C9CFE1E-389F-4118-9FAD-365385190329}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'TerminateAll' , ), 300, (300, (), [ ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
]

win32com.client.CLSIDToClass.RegisterCLSID( "{338FB9A0-BAE5-11D2-8AD1-00C04F79E479}", Debugger )
