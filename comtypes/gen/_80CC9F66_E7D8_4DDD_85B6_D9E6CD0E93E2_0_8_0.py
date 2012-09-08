# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\Common Files\\Microsoft Shared\\MSEnv\\dte80a.olb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from comtypes import BSTR
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import CoClass
from comtypes.automation import VARIANT
STRING = c_char_p
from comtypes.automation import IDispatch
from comtypes.automation import VARIANT
from comtypes import IUnknown
from ctypes.wintypes import VARIANT_BOOL
from comtypes.automation import _midlSAFEARRAY
from comtypes import DISPMETHOD, DISPPROPERTY, helpstring
WSTRING = c_wchar_p
from comtypes.typeinfo import ULONG_PTR
LONG_PTR = c_int


class _EnvironmentKeyboard(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{9C722678-490D-408F-98AE-B6B9A68AA45D}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_EnvironmentKeyboard._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Sets/returns the current keyboard mapping via an ASCII file showing the keyboard mapping.'), 'propput'], HRESULT, 'Scheme',
              ( ['in'], BSTR, 'pbstr' )),
    COMMETHOD([dispid(1), helpstring(u'Sets/returns the current keyboard mapping via an ASCII file showing the keyboard mapping.'), 'propget'], HRESULT, 'Scheme',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstr' )),
]
################################################################
## code template for _EnvironmentKeyboard implementation
##class _EnvironmentKeyboard_Impl(object):
##    def _get(self):
##        u'Sets/returns the current keyboard mapping via an ASCII file showing the keyboard mapping.'
##        #return pbstr
##    def _set(self, pbstr):
##        u'Sets/returns the current keyboard mapping via an ASCII file showing the keyboard mapping.'
##    Scheme = property(_get, _set, doc = _set.__doc__)
##

class UIHierarchy(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{72A2A2EF-C209-408C-A377-76871774ADB7}')
    _idlflags_ = ['dual', 'oleautomation']
class DTE(CoClass):
    u'Root object from which all other objects and collections in environment extensibility are accessed.'
    _reg_clsid_ = GUID('{3C9CFE1E-389F-4118-9FAD-365385190329}')
    _idlflags_ = ['appobject']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _DTE(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Root object from which all other objects and collections in environment extensibility are accessed.'
    _iid_ = GUID('{04A72314-32E9-48E2-9B87-A63603454F3E}')
    _idlflags_ = ['dual', 'oleautomation']
DTE._com_interfaces_ = [_DTE]

class Window(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Represents window(s) in the development environment.'
    _iid_ = GUID('{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}')
    _idlflags_ = ['dual', 'oleautomation']
class UIHierarchyItems(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing collection of UIHierarchyItem objects.'
    _iid_ = GUID('{DB8406B0-A916-449C-A277-BB04028F4394}')
    _idlflags_ = ['dual', 'oleautomation']
class UIHierarchyItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing a node in a UI Hierarchy window (e.g. Solution Explorer).'
    _iid_ = GUID('{FBD0D024-09CD-4D9F-9E2B-CACD628426A5}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsUISelectionType'
vsUISelectionTypeSelect = 1
vsUISelectionTypeToggle = 2
vsUISelectionTypeExtend = 3
vsUISelectionTypeSetCaret = 4
vsUISelectionType = c_int # enum
UIHierarchy._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'ppWin' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the collection representing children of the item.'), 'propget'], HRESULT, 'UIHierarchyItems',
              ( ['retval', 'out'], POINTER(POINTER(UIHierarchyItems)), 'ppUIHierarchyItems' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the collection comprised of the selected items.'), 'propget'], HRESULT, 'SelectedItems',
              ( ['retval', 'out'], POINTER(VARIANT), 'pvarSel' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the item specified.')], HRESULT, 'GetItem',
              ( ['in'], BSTR, 'Names' ),
              ( ['retval', 'out'], POINTER(POINTER(UIHierarchyItem)), 'ppUIHierarchyItem' )),
    COMMETHOD([dispid(6), helpstring(u'Moves the selection up as specified.')], HRESULT, 'SelectUp',
              ( ['in'], vsUISelectionType, 'How' ),
              ( ['in'], c_int, 'Count' )),
    COMMETHOD([dispid(7), helpstring(u'Moves the selection down as specified.')], HRESULT, 'SelectDown',
              ( ['in'], vsUISelectionType, 'How' ),
              ( ['in'], c_int, 'Count' )),
    COMMETHOD([dispid(0)], HRESULT, 'DoDefaultAction'),
]
################################################################
## code template for UIHierarchy implementation
##class UIHierarchy_Impl(object):
##    def SelectDown(self, How, Count):
##        u'Moves the selection down as specified.'
##        #return 
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppWin
##
##    def DoDefaultAction(self):
##        '-no docstring-'
##        #return 
##
##    @property
##    def SelectedItems(self):
##        u'Returns the collection comprised of the selected items.'
##        #return pvarSel
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    def SelectUp(self, How, Count):
##        u'Moves the selection up as specified.'
##        #return 
##
##    @property
##    def UIHierarchyItems(self):
##        u'Returns the collection representing children of the item.'
##        #return ppUIHierarchyItems
##
##    def GetItem(self, Names):
##        u'Returns the item specified.'
##        #return ppUIHierarchyItem
##


# values for enumeration 'vsTaskListColumn'
vsTaskListColumnPriority = 1
vsTaskListColumnGlyph = 2
vsTaskListColumnCheck = 4
vsTaskListColumnDescription = 8
vsTaskListColumnFile = 16
vsTaskListColumnLine = 32
vsTaskListColumn = c_int # enum
vsCATIDSolutionBrowseObject = u'{A2392464-7C22-11d3-BDCA-00C04F688E50}' # Constant STRING
class IExtensibleObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{86C31347-5B52-4715-B454-A6E5FCAB975D}')
    _idlflags_ = ['hidden', 'restricted']
class IExtensibleObjectSite(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{EB5BE8A7-E593-4DE6-A923-C2AFECB96336}')
    _idlflags_ = ['hidden', 'restricted']
IExtensibleObject._methods_ = [
    COMMETHOD([], HRESULT, 'GetAutomationObject',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], POINTER(IExtensibleObjectSite), 'pParent' ),
              ( ['out'], POINTER(POINTER(IDispatch)), 'ppDisp' )),
]
################################################################
## code template for IExtensibleObject implementation
##class IExtensibleObject_Impl(object):
##    def GetAutomationObject(self, Name, pParent):
##        '-no docstring-'
##        #return ppDisp
##


# values for enumeration 'vsFindOptions'
vsFindOptionsNone = 0
vsFindOptionsMatchWholeWord = 2
vsFindOptionsMatchCase = 4
vsFindOptionsRegularExpression = 8
vsFindOptionsBackwards = 128
vsFindOptionsFromStart = 256
vsFindOptionsMatchInHiddenText = 512
vsFindOptionsWildcards = 1024
vsFindOptionsSearchSubfolders = 4096
vsFindOptionsKeepModifiedDocumentsOpen = 8192
vsFindOptions = c_int # enum

# values for enumeration 'vsWindowState'
vsWindowStateNormal = 0
vsWindowStateMinimize = 1
vsWindowStateMaximize = 2
vsWindowState = c_int # enum
vsTaskCategoryBuildCompile = u'BuildCompile' # Constant STRING
vsWindowKindFindSymbolResults = u'{68487888-204A-11D3-87EB-00C04F7971A5}' # Constant STRING
vsWindowKindFindReplace = u'{CF2DDC32-8CAD-11D2-9302-005345000000}' # Constant STRING
vsWindowKindResourceView = u'{2D7728C2-DE0A-45b5-99AA-89B609DFDE73}' # Constant STRING
class Commands(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Represents commands in the environment.'
    _iid_ = GUID('{E6B96CAC-B8C7-40AE-B705-5C81878C4A9E}')
    _idlflags_ = ['dual', 'oleautomation']
class Command(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Represents a command in the environment.'
    _iid_ = GUID('{5FE10FB0-91A1-4E55-BAAA-ECCAE5CCEB94}')
    _idlflags_ = ['dual', 'oleautomation']
class AddIn(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides information about an add-in to other Add-in objects.'
    _iid_ = GUID('{53A87FA1-CE93-48BF-958B-C6DA793C5028}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsCommandBarType'
vsCommandBarTypePopup = 10
vsCommandBarTypeToolbar = 23
vsCommandBarTypeMenu = 24
vsCommandBarType = c_int # enum
Commands._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(3), helpstring(u'Adds the command, as represented by the GUID and ID, to the Commands object.'), 'hidden'], HRESULT, 'Add',
              ( ['in'], BSTR, 'Guid' ),
              ( ['in'], c_int, 'ID' ),
              ( ['in'], POINTER(VARIANT), 'Control' )),
    COMMETHOD([dispid(4), helpstring(u'Invokes a command.')], HRESULT, 'Raise',
              ( ['in'], BSTR, 'Guid' ),
              ( ['in'], c_int, 'ID' ),
              ( ['in', 'out'], POINTER(VARIANT), 'CustomIn' ),
              ( ['in', 'out'], POINTER(VARIANT), 'CustomOut' )),
    COMMETHOD([dispid(5), helpstring(u"Returns command's GUID and ID in group associated with the CommandBarControl.")], HRESULT, 'CommandInfo',
              ( ['in'], POINTER(IDispatch), 'CommandBarControl' ),
              ( ['out'], POINTER(BSTR), 'Guid' ),
              ( ['out'], POINTER(c_int), 'ID' )),
    COMMETHOD([dispid(10), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'lplReturn' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['in', 'optional'], c_int, 'ID', -1 ),
              ( ['retval', 'out'], POINTER(POINTER(Command)), 'lppcReturn' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(11), helpstring(u'Creates a command that persists and is available the next time started.')], HRESULT, 'AddNamedCommand',
              ( ['in'], POINTER(AddIn), 'AddInInstance' ),
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'ButtonText' ),
              ( ['in'], BSTR, 'Tooltip' ),
              ( ['in'], VARIANT_BOOL, 'MSOButton' ),
              ( ['in', 'optional'], c_int, 'Bitmap', 0 ),
              ( ['in', 'optional'], POINTER(_midlSAFEARRAY(VARIANT)), 'ContextUIGUIDs' ),
              ( ['in', 'optional'], c_int, 'vsCommandDisabledFlagsValue', 16 ),
              ( ['retval', 'out'], POINTER(POINTER(Command)), 'pVal' )),
    COMMETHOD([dispid(12), helpstring(u'Creates a command bar that persists and is available the next time started.')], HRESULT, 'AddCommandBar',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], vsCommandBarType, 'Type' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'CommandBarParent' ),
              ( ['in', 'optional'], c_int, 'Position', 1 ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'pVal' )),
    COMMETHOD([dispid(13), helpstring(u'Removes a command bar that was created with Commands.AddCommandBar.')], HRESULT, 'RemoveCommandBar',
              ( ['in'], POINTER(IDispatch), 'CommandBar' )),
]
################################################################
## code template for Commands implementation
##class Commands_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return lplReturn
##
##    def AddNamedCommand(self, AddInInstance, Name, ButtonText, Tooltip, MSOButton, Bitmap, ContextUIGUIDs, vsCommandDisabledFlagsValue):
##        u'Creates a command that persists and is available the next time started.'
##        #return pVal
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    def Raise(self, Guid, ID):
##        u'Invokes a command.'
##        #return CustomIn, CustomOut
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppaReturn
##
##    def AddCommandBar(self, Name, Type, CommandBarParent, Position):
##        u'Creates a command bar that persists and is available the next time started.'
##        #return pVal
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def CommandInfo(self, CommandBarControl):
##        u"Returns command's GUID and ID in group associated with the CommandBarControl."
##        #return Guid, ID
##
##    def Item(self, index, ID):
##        u'Returns an indexed member of a collection.'
##        #return lppcReturn
##
##    def Add(self, Guid, ID, Control):
##        u'Adds the command, as represented by the GUID and ID, to the Commands object.'
##        #return 
##
##    def RemoveCommandBar(self, CommandBar):
##        u'Removes a command bar that was created with Commands.AddCommandBar.'
##        #return 
##

class _MiscSlnFilesEventsRoot(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{7658B944-F37B-11D2-AACF-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_MiscSlnFilesEventsRoot._methods_ = [
    COMMETHOD([dispid(1), 'propget'], HRESULT, 'SolutionItemsEvents',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppeNew' )),
    COMMETHOD([dispid(2), 'propget'], HRESULT, 'MiscFilesEvents',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppeNew' )),
]
################################################################
## code template for _MiscSlnFilesEventsRoot implementation
##class _MiscSlnFilesEventsRoot_Impl(object):
##    @property
##    def MiscFilesEvents(self):
##        '-no docstring-'
##        #return ppeNew
##
##    @property
##    def SolutionItemsEvents(self):
##        '-no docstring-'
##        #return ppeNew
##

vsWindowKindObjectBrowser = u'{269A02DC-6AF8-11D3-BDC4-00C04F688E50}' # Constant STRING
vsTaskCategoryComment = u'Comment' # Constant STRING
vsTaskCategoryShortcut = u'Shortcut' # Constant STRING
class ToolBoxTabs(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Collection of all pages on the tool box.'
    _iid_ = GUID('{CF177B52-4F2F-42A0-8DA3-CE78679A0D2D}')
    _idlflags_ = ['dual', 'oleautomation']
class ToolBoxTab(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An individual tab on the tool box.'
    _iid_ = GUID('{CE2DEF9E-3387-4BF2-967B-A1F7F70DF325}')
    _idlflags_ = ['dual', 'oleautomation']
class ToolBox(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing the tool box window.'
    _iid_ = GUID('{56FCD5AF-7F17-4C5C-AA8D-AE2BB2DDBF38}')
    _idlflags_ = ['dual', 'oleautomation']
ToolBoxTabs._methods_ = [
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( [], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ToolBoxTab)), 'pItem' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(ToolBox)), 'pParent' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([dispid(4), helpstring(u'Adds a tab to the tool box.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(ToolBoxTab)), 'pToolBoxTabs' )),
]
################################################################
## code template for ToolBoxTabs implementation
##class ToolBoxTabs_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return pParent
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return pItem
##
##    def Add(self, Name):
##        u'Adds a tab to the tool box.'
##        #return pToolBoxTabs
##

vsTaskCategoryUser = u'User' # Constant STRING
vsTaskCategoryMisc = u'Misc' # Constant STRING
vsTaskCategoryHTML = u'HTML' # Constant STRING
vsext_wk_WatchWindow = u'{90243340-BD7A-11D0-93EF-00A0C90F2734}' # Constant STRING
vsDocumentKindText = u'{8E7B96A8-E33D-11D0-A6D5-00C04FB67F6A}' # Constant STRING
class CodeTypeRef(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object defining the type of a construct in a source file.'
    _iid_ = GUID('{0CFBC2BC-0D4E-11D3-8997-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsCMTypeRef'
vsCMTypeRefOther = 0
vsCMTypeRefCodeType = 1
vsCMTypeRefArray = 2
vsCMTypeRefVoid = 3
vsCMTypeRefPointer = 4
vsCMTypeRefString = 5
vsCMTypeRefObject = 6
vsCMTypeRefByte = 7
vsCMTypeRefChar = 8
vsCMTypeRefShort = 9
vsCMTypeRefInt = 10
vsCMTypeRefLong = 11
vsCMTypeRefFloat = 12
vsCMTypeRefDouble = 13
vsCMTypeRefDecimal = 14
vsCMTypeRefBool = 15
vsCMTypeRefVariant = 16
vsCMTypeRef = c_int # enum
class CodeType(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object defining a class construct in a source file.'
    _iid_ = GUID('{0CFBC2B7-0D4E-11D3-8997-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation']
CodeTypeRef._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ParentObject' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the base type of the item.'), 'propget'], HRESULT, 'TypeKind',
              ( ['retval', 'out'], POINTER(vsCMTypeRef), 'pType' )),
    COMMETHOD([dispid(4), helpstring(u'Sets/Returns information describing what kind of object this item is.'), 'nonbrowsable', 'propget'], HRESULT, 'CodeType',
              ( ['retval', 'out'], POINTER(POINTER(CodeType)), 'ppCodeType' )),
    COMMETHOD([dispid(4), helpstring(u'Sets/Returns information describing what kind of object this item is.'), 'nonbrowsable', 'propput'], HRESULT, 'CodeType',
              ( [], POINTER(CodeType), 'ppCodeType' )),
    COMMETHOD([dispid(5), helpstring(u'Sets/Returns an object representing the programmatic type.'), 'nonbrowsable', 'propget'], HRESULT, 'ElementType',
              ( ['retval', 'out'], POINTER(POINTER(CodeTypeRef)), 'ppCodeTypeRef' )),
    COMMETHOD([dispid(5), helpstring(u'Sets/Returns an object representing the programmatic type.'), 'nonbrowsable', 'propput'], HRESULT, 'ElementType',
              ( [], POINTER(CodeTypeRef), 'ppCodeTypeRef' )),
    COMMETHOD([dispid(6), helpstring(u'Returns a string to use for displaying the object.'), 'propget'], HRESULT, 'AsString',
              ( ['retval', 'out'], POINTER(BSTR), 'pAsString' )),
    COMMETHOD([dispid(7), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'AsFullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pAsFullName' )),
    COMMETHOD([dispid(8), helpstring(u'If this item is an array, sets/returns the number of dimensions in this array.'), 'propget'], HRESULT, 'Rank',
              ( ['retval', 'out'], POINTER(c_int), 'pRank' )),
    COMMETHOD([dispid(8), helpstring(u'If this item is an array, sets/returns the number of dimensions in this array.'), 'propput'], HRESULT, 'Rank',
              ( [], c_int, 'pRank' )),
    COMMETHOD([dispid(9), helpstring(u'Creates an array of specified type, and inserts it into the code in the correct location.')], HRESULT, 'CreateArrayType',
              ( ['optional'], c_int, 'Rank', 1 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeTypeRef)), 'ppTypeRef' )),
]
################################################################
## code template for CodeTypeRef implementation
##class CodeTypeRef_Impl(object):
##    def _get(self):
##        u'Sets/Returns an object representing the programmatic type.'
##        #return ppCodeTypeRef
##    def _set(self, ppCodeTypeRef):
##        u'Sets/Returns an object representing the programmatic type.'
##    ElementType = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ParentObject
##
##    @property
##    def TypeKind(self):
##        u'Returns the base type of the item.'
##        #return pType
##
##    @property
##    def AsFullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pAsFullName
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def CreateArrayType(self, Rank):
##        u'Creates an array of specified type, and inserts it into the code in the correct location.'
##        #return ppTypeRef
##
##    def _get(self):
##        u'If this item is an array, sets/returns the number of dimensions in this array.'
##        #return pRank
##    def _set(self, pRank):
##        u'If this item is an array, sets/returns the number of dimensions in this array.'
##    Rank = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Sets/Returns information describing what kind of object this item is.'
##        #return ppCodeType
##    def _set(self, ppCodeType):
##        u'Sets/Returns information describing what kind of object this item is.'
##    CodeType = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def AsString(self):
##        u'Returns a string to use for displaying the object.'
##        #return pAsString
##

vsDocumentKindResource = u'{00000000-0000-0000-0000-000000000000}' # Constant STRING
vsDocumentKindBinary = u'{25834150-CD7E-11D0-92DF-00A0C9138C45}' # Constant STRING
vsViewKindPrimary = u'{00000000-0000-0000-0000-000000000000}' # Constant STRING
vsViewKindAny = u'{FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF}' # Constant STRING
vsViewKindDebugging = u'{7651A700-06E5-11D1-8EBD-00A0C90F26EA}' # Constant STRING
class CodeEnum(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing an enumeration in source code.'
    _iid_ = GUID('{B1F42512-91CD-4D3A-8B25-A317D8032B24}')
    _idlflags_ = ['dual', 'oleautomation']
class CodeElements(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of objects defining code constructs in a source file.'
    _iid_ = GUID('{0CFBC2B5-0D4E-11D3-8997-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation']
class ProjectItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Generic object representing items contained in project/current instance of development environment.'
    _iid_ = GUID('{0B48100A-473E-433C-AB8F-66B9739AB620}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsCMElement'
vsCMElementOther = 0
vsCMElementClass = 1
vsCMElementFunction = 2
vsCMElementVariable = 3
vsCMElementProperty = 4
vsCMElementNamespace = 5
vsCMElementParameter = 6
vsCMElementAttribute = 7
vsCMElementInterface = 8
vsCMElementDelegate = 9
vsCMElementEnum = 10
vsCMElementStruct = 11
vsCMElementUnion = 12
vsCMElementLocalDeclStmt = 13
vsCMElementFunctionInvokeStmt = 14
vsCMElementPropertySetStmt = 15
vsCMElementAssignmentStmt = 16
vsCMElementInheritsStmt = 17
vsCMElementImplementsStmt = 18
vsCMElementOptionStmt = 19
vsCMElementVBAttributeStmt = 20
vsCMElementVBAttributeGroup = 21
vsCMElementEventsDeclaration = 22
vsCMElementUDTDecl = 23
vsCMElementDeclareDecl = 24
vsCMElementDefineStmt = 25
vsCMElementTypeDef = 26
vsCMElementIncludeStmt = 27
vsCMElementUsingStmt = 28
vsCMElementMacro = 29
vsCMElementMap = 30
vsCMElementIDLImport = 31
vsCMElementIDLImportLib = 32
vsCMElementIDLCoClass = 33
vsCMElementIDLLibrary = 34
vsCMElementImportStmt = 35
vsCMElementMapEntry = 36
vsCMElementVCBase = 37
vsCMElementEvent = 38
vsCMElementModule = 39
vsCMElement = c_int # enum

# values for enumeration 'vsCMInfoLocation'
vsCMInfoLocationProject = 1
vsCMInfoLocationExternal = 2
vsCMInfoLocationNone = 4
vsCMInfoLocationVirtual = 8
vsCMInfoLocation = c_int # enum
class TextPoint(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing a fixed (but tracking) point within a text document.'
    _iid_ = GUID('{7F59E94E-4939-40D2-9F7F-B7651C25905D}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsCMPart'
vsCMPartName = 1
vsCMPartAttributes = 2
vsCMPartHeader = 4
vsCMPartWhole = 8
vsCMPartBody = 16
vsCMPartNavigate = 32
vsCMPartAttributesWithDelimiter = 68
vsCMPartBodyWithDelimiter = 80
vsCMPartHeaderWithAttributes = 6
vsCMPartWholeWithAttributes = 10
vsCMPart = c_int # enum
class CodeNamespace(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object defining a namespace construct in a source file.'
    _iid_ = GUID('{0CFBC2B8-0D4E-11D3-8997-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsCMAccess'
vsCMAccessPublic = 1
vsCMAccessPrivate = 2
vsCMAccessProject = 4
vsCMAccessProtected = 8
vsCMAccessDefault = 32
vsCMAccessAssemblyOrFamily = 64
vsCMAccessWithEvents = 128
vsCMAccessProjectOrProtected = 12
vsCMAccess = c_int # enum
class CodeElement(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object defining a code construct in a source file.'
    _iid_ = GUID('{0CFBC2B6-0D4E-11D3-8997-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation']
class CodeAttribute(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u"An object defining an item's attribute."
    _iid_ = GUID('{0CFBC2BE-0D4E-11D3-8997-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation']
class CodeVariable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object defining a variable construct in a source file.'
    _iid_ = GUID('{0CFBC2BA-0D4E-11D3-8997-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation']
CodeEnum._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ParentObject' )),
    COMMETHOD([dispid(32), helpstring(u'Returns an object defining the parent namespace.'), 'nonbrowsable', 'propget'], HRESULT, 'Namespace',
              ( ['retval', 'out'], POINTER(POINTER(CodeNamespace)), 'ppCodeNamespace' )),
    COMMETHOD([dispid(33), helpstring(u'Returns a collection of classes this item derives from.'), 'nonbrowsable', 'propget'], HRESULT, 'Bases',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(34), helpstring(u'Returns a collection of items contained by this element.'), 'nonbrowsable', 'propget'], HRESULT, 'Members',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(35), helpstring(u'Defines the access attributes of this item.'), 'propput'], HRESULT, 'Access',
              ( [], vsCMAccess, 'pAccess' )),
    COMMETHOD([dispid(35), helpstring(u'Defines the access attributes of this item.'), 'propget'], HRESULT, 'Access',
              ( ['retval', 'out'], POINTER(vsCMAccess), 'pAccess' )),
    COMMETHOD([dispid(36), helpstring(u'Returns a collection of items containing attributes.'), 'nonbrowsable', 'propget'], HRESULT, 'Attributes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(37), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propget'], HRESULT, 'DocComment',
              ( ['retval', 'out'], POINTER(BSTR), 'pDocComment' )),
    COMMETHOD([dispid(37), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propput'], HRESULT, 'DocComment',
              ( [], BSTR, 'pDocComment' )),
    COMMETHOD([dispid(38), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Comment',
              ( ['retval', 'out'], POINTER(BSTR), 'pComment' )),
    COMMETHOD([dispid(38), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propput'], HRESULT, 'Comment',
              ( [], BSTR, 'pComment' )),
    COMMETHOD([dispid(39), helpstring(u'Adds an item to the list of inherited objects.')], HRESULT, 'AddBase',
              ( [], VARIANT, 'Base' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeElement)), 'ppOut' )),
    COMMETHOD([dispid(40), helpstring(u'Creates a new attribute code construct and inserts the code in the correct location.')], HRESULT, 'AddAttribute',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeAttribute)), 'ppCodeAttribute' )),
    COMMETHOD([dispid(41), helpstring(u'Removes an object from the list of bases.')], HRESULT, 'RemoveBase',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(42), helpstring(u'Removes a member code construct.')], HRESULT, 'RemoveMember',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(43), helpstring(u'Returns a Boolean telling if an object has another object as a base.'), 'propget'], HRESULT, 'IsDerivedFrom',
              ( [], BSTR, 'FullName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(44), helpstring(u'Returns a collection of objects derived from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'DerivedTypes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(61), helpstring(u'Creates a new member code construct and inserts the code in the correct location.')], HRESULT, 'AddMember',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeVariable)), 'ppCodeElements' )),
]
################################################################
## code template for CodeEnum implementation
##class CodeEnum_Impl(object):
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def Namespace(self):
##        u'Returns an object defining the parent namespace.'
##        #return ppCodeNamespace
##
##    def AddBase(self, Base, Position):
##        u'Adds an item to the list of inherited objects.'
##        #return ppOut
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    def _get(self):
##        u'Defines the access attributes of this item.'
##        #return pAccess
##    def _set(self, pAccess):
##        u'Defines the access attributes of this item.'
##    Access = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Bases(self):
##        u'Returns a collection of classes this item derives from.'
##        #return ppCodeElements
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##
##    def AddMember(self, Name, Value, Position):
##        u'Creates a new member code construct and inserts the code in the correct location.'
##        #return ppCodeElements
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ParentObject
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    def AddAttribute(self, Name, Value, Position):
##        u'Creates a new attribute code construct and inserts the code in the correct location.'
##        #return ppCodeAttribute
##
##    def RemoveMember(self, Element):
##        u'Removes a member code construct.'
##        #return 
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def Members(self):
##        u'Returns a collection of items contained by this element.'
##        #return ppCodeElements
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def _get(self):
##        u'Returns the document comment on the current code model element.'
##        #return pDocComment
##    def _set(self, pDocComment):
##        u'Returns the document comment on the current code model element.'
##    DocComment = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveBase(self, Element):
##        u'Removes an object from the list of bases.'
##        #return 
##
##    @property
##    def Attributes(self):
##        u'Returns a collection of items containing attributes.'
##        #return ppCodeElements
##
##    def _get(self):
##        u'Sets/Returns an object defining the comment for this object.'
##        #return pComment
##    def _set(self, pComment):
##        u'Sets/Returns an object defining the comment for this object.'
##    Comment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsDerivedFrom(self, FullName):
##        u'Returns a Boolean telling if an object has another object as a base.'
##        #return pVal
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    @property
##    def DerivedTypes(self):
##        u'Returns a collection of objects derived from this object.'
##        #return ppCodeElements
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##

vsViewKindCode = u'{7651A701-06E5-11D1-8EBD-00A0C90F26EA}' # Constant STRING
vsViewKindDesigner = u'{7651A702-06E5-11D1-8EBD-00A0C90F26EA}' # Constant STRING
vsViewKindTextView = u'{7651A703-06E5-11D1-8EBD-00A0C90F26EA}' # Constant STRING
vsWindowKindTaskList = u'{4A9B7E51-AA16-11D0-A8C5-00A0C921A4D2}' # Constant STRING
vsWindowKindToolbox = u'{B1E99781-AB81-11D0-B683-00AA00A3EE26}' # Constant STRING
vsWindowKindCallStack = u'{0504FF91-9D61-11D0-A794-00A0C9110051}' # Constant STRING
Command._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstr' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(Commands)), 'lppcReturn' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(4), helpstring(u'The command group GUID used to represent the command.'), 'propget'], HRESULT, 'Guid',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstr' )),
    COMMETHOD([dispid(5), helpstring(u'The ID within a command group GUID used to represent the command.'), 'propget'], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(c_int), 'lReturn' )),
    COMMETHOD([dispid(6), helpstring(u'Returns a value specifying if the command is enabled in the current context.'), 'propget'], HRESULT, 'IsAvailable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pAvail' )),
    COMMETHOD([dispid(7), helpstring(u'Creates a persistent command bar control for this command.')], HRESULT, 'AddControl',
              ( ['in'], POINTER(IDispatch), 'Owner' ),
              ( ['in', 'optional'], c_int, 'Position', 1 ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'pCommandBarControl' )),
    COMMETHOD([dispid(8), helpstring(u'Removes a named command that was created with Commands.AddNamedCommand.')], HRESULT, 'Delete'),
    COMMETHOD([dispid(9), helpstring(u'Gets/Sets the list of key strokes to invoke the command.'), 'propget'], HRESULT, 'Bindings',
              ( ['retval', 'out'], POINTER(VARIANT), 'pVar' )),
    COMMETHOD([dispid(9), helpstring(u'Gets/Sets the list of key strokes to invoke the command.'), 'propput'], HRESULT, 'Bindings',
              ( [], VARIANT, 'pVar' )),
    COMMETHOD([dispid(1), 'propget'], HRESULT, 'LocalizedName',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstr' )),
]
################################################################
## code template for Command implementation
##class Command_Impl(object):
##    @property
##    def Name(self):
##        u'Returns the name of the object.'
##        #return lpbstr
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    @property
##    def LocalizedName(self):
##        '-no docstring-'
##        #return lpbstr
##
##    def _get(self):
##        u'Gets/Sets the list of key strokes to invoke the command.'
##        #return pVar
##    def _set(self, pVar):
##        u'Gets/Sets the list of key strokes to invoke the command.'
##    Bindings = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return lppcReturn
##
##    def AddControl(self, Owner, Position):
##        u'Creates a persistent command bar control for this command.'
##        #return pCommandBarControl
##
##    @property
##    def IsAvailable(self):
##        u'Returns a value specifying if the command is enabled in the current context.'
##        #return pAvail
##
##    @property
##    def Guid(self):
##        u'The command group GUID used to represent the command.'
##        #return lpbstr
##
##    @property
##    def ID(self):
##        u'The ID within a command group GUID used to represent the command.'
##        #return lReturn
##
##    def Delete(self):
##        u'Removes a named command that was created with Commands.AddNamedCommand.'
##        #return 
##

vsWindowKindAutoLocals = u'{F2E84780-2AF1-11D1-A7FA-00A0C9110051}' # Constant STRING
vsWindowKindWatch = u'{90243340-BD7A-11D0-93EF-00A0C90F2734}' # Constant STRING
vsWindowKindProperties = u'{EEFA5220-E298-11D0-8F78-00A0C9110057}' # Constant STRING
vsWindowKindSolutionExplorer = u'{3AE79031-E1BC-11D0-8F78-00A0C9110057}' # Constant STRING
vsContextMacroRecordingToolbar = u'{85A70471-270A-11D2-88F9-0060083196C6}' # Constant STRING
vsWindowKindOutput = u'{34E76E81-EE4A-11D0-AE2E-00A0C90FFFC3}' # Constant STRING
vsWindowKindMacroExplorer = u'{07CD18B4-3BA1-11D2-890A-0060083196C6}' # Constant STRING
class TextSelection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing the selection or caret in a text view.'
    _iid_ = GUID('{1FA0E135-399A-4D2C-A4FE-D21E2480F921}')
    _idlflags_ = ['dual', 'oleautomation']
class TextDocument(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing an open text-based document such as a file of code.'
    _iid_ = GUID('{CB218890-1382-472B-9118-782700C88115}')
    _idlflags_ = ['dual', 'oleautomation']
class VirtualPoint(TextPoint):
    _case_insensitive_ = True
    u'A TextPoint that may represent a location in virtual space (beyond the end of a line).'
    _iid_ = GUID('{42320454-626C-4DD0-9ECB-357C4F1966D8}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsCaseOptions'
vsCaseOptionsLowercase = 1
vsCaseOptionsUppercase = 2
vsCaseOptionsCapitalize = 3
vsCaseOptions = c_int # enum

# values for enumeration 'vsWhitespaceOptions'
vsWhitespaceOptionsHorizontal = 0
vsWhitespaceOptionsVertical = 1
vsWhitespaceOptions = c_int # enum

# values for enumeration 'vsStartOfLineOptions'
vsStartOfLineOptionsFirstColumn = 0
vsStartOfLineOptionsFirstText = 1
vsStartOfLineOptions = c_int # enum
class TextRanges(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of TextRange objects.'
    _iid_ = GUID('{B6422E9C-9EFD-4F87-BDDC-C7FD8F2FD303}')
    _idlflags_ = ['dual', 'oleautomation']
class TextPane(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing a view on a text document.'
    _iid_ = GUID('{0A3BF283-05F8-4669-9BCB-A84B6423349A}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsSelectionMode'
vsSelectionModeStream = 0
vsSelectionModeBox = 1
vsSelectionMode = c_int # enum
TextSelection._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(TextDocument)), 'ppParent' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the origin point of the selection.'), 'propget'], HRESULT, 'AnchorPoint',
              ( ['retval', 'out'], POINTER(POINTER(VirtualPoint)), 'ppPoint' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the current endpoint of the selection.'), 'propget'], HRESULT, 'ActivePoint',
              ( ['retval', 'out'], POINTER(POINTER(VirtualPoint)), 'ppPoint' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the 1-based column index of the anchor point.'), 'hidden', 'propget'], HRESULT, 'AnchorColumn',
              ( ['retval', 'out'], POINTER(c_int), 'pColumn' )),
    COMMETHOD([dispid(6), helpstring(u'Returns the 1-based line index of the bottom point.'), 'hidden', 'propget'], HRESULT, 'BottomLine',
              ( ['retval', 'out'], POINTER(c_int), 'pLine' )),
    COMMETHOD([dispid(7), helpstring(u'Returns the bottom end of the selection.'), 'propget'], HRESULT, 'BottomPoint',
              ( ['retval', 'out'], POINTER(POINTER(VirtualPoint)), 'ppPoint' )),
    COMMETHOD([dispid(8), helpstring(u'Returns the 1-based column index of the active point.'), 'hidden', 'propget'], HRESULT, 'CurrentColumn',
              ( ['retval', 'out'], POINTER(c_int), 'pColumn' )),
    COMMETHOD([dispid(9), helpstring(u'Returns the 1-based line index of the active point.'), 'hidden', 'propget'], HRESULT, 'CurrentLine',
              ( ['retval', 'out'], POINTER(c_int), 'pLine' )),
    COMMETHOD([dispid(10), helpstring(u'Indicates whether the anchor point is equal to the active point.'), 'propget'], HRESULT, 'IsEmpty',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfEmpty' )),
    COMMETHOD([dispid(11), helpstring(u'Indicates whether the active point is equal to the bottom point.'), 'propget'], HRESULT, 'IsActiveEndGreater',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfGreater' )),
    COMMETHOD([dispid(0), helpstring(u'Returns the selected text.'), 'propget'], HRESULT, 'Text',
              ( ['retval', 'out'], POINTER(BSTR), 'pText' )),
    COMMETHOD([dispid(0), helpstring(u'Returns the selected text.'), 'propput'], HRESULT, 'Text',
              ( ['in'], BSTR, 'pText' )),
    COMMETHOD([dispid(13), helpstring(u'Returns the 1-based line index of the top point.'), 'hidden', 'propget'], HRESULT, 'TopLine',
              ( ['retval', 'out'], POINTER(c_int), 'pLine' )),
    COMMETHOD([dispid(14), helpstring(u'Returns the top end of the selection.'), 'propget'], HRESULT, 'TopPoint',
              ( ['retval', 'out'], POINTER(POINTER(VirtualPoint)), 'ppPoint' )),
    COMMETHOD([dispid(15), helpstring(u'Changes the case of the selected text.')], HRESULT, 'ChangeCase',
              ( ['in'], vsCaseOptions, 'How' )),
    COMMETHOD([dispid(16), helpstring(u'Moves the object the specified number of characters to the left. The default is 1 character.')], HRESULT, 'CharLeft',
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False ),
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(17), helpstring(u'Moves the object the specified number of characters to the right. The default is 1 character.')], HRESULT, 'CharRight',
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False ),
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(18), helpstring(u'Clears any unnamed bookmarks on the current line.')], HRESULT, 'ClearBookmark'),
    COMMETHOD([dispid(19), helpstring(u'Collapses the selection to the active point.')], HRESULT, 'Collapse'),
    COMMETHOD([dispid(72), helpstring(u'Creates an outlining section based on the current selection.')], HRESULT, 'OutlineSection'),
    COMMETHOD([dispid(20), helpstring(u'Copies the selection to the clipboard.')], HRESULT, 'Copy'),
    COMMETHOD([dispid(21), helpstring(u'Copies the selection to the clipboard and deletes it.')], HRESULT, 'Cut'),
    COMMETHOD([dispid(22), helpstring(u'Inserts the clipboard contents at the current location.')], HRESULT, 'Paste'),
    COMMETHOD([dispid(23), helpstring(u'Deletes the selection.')], HRESULT, 'Delete',
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(24), helpstring(u'Deletes a specified number of characters to the left of the active point. The default is 1 character.')], HRESULT, 'DeleteLeft',
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(25), helpstring(u'Deletes white space horizontally or vertically around the current location.')], HRESULT, 'DeleteWhitespace',
              ( ['in', 'optional'], vsWhitespaceOptions, 'Direction', 0 )),
    COMMETHOD([dispid(26), helpstring(u'Moves the object to the end of the current line.')], HRESULT, 'EndOfLine',
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False )),
    COMMETHOD([dispid(27), helpstring(u'Moves the object to the beginning of the current line.')], HRESULT, 'StartOfLine',
              ( ['in', 'optional'], vsStartOfLineOptions, 'Where', 0 ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False )),
    COMMETHOD([dispid(28), helpstring(u'Moves the object to the end of the document.')], HRESULT, 'EndOfDocument',
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False )),
    COMMETHOD([dispid(29), helpstring(u'Moves the object to the beginning of the document.')], HRESULT, 'StartOfDocument',
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False )),
    COMMETHOD([dispid(30), helpstring(u'Searches for the given pattern from the active point to the end of the document.')], HRESULT, 'FindPattern',
              ( ['in'], BSTR, 'Pattern' ),
              ( ['in', 'optional'], c_int, 'vsFindOptionsValue', 0 ),
              ( ['in', 'out', 'optional'], POINTER(POINTER(TextRanges)), 'Tags', 0 ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfFound' )),
    COMMETHOD([dispid(31), helpstring(u'Searches for the given pattern in the selection and replaces it with new text.')], HRESULT, 'ReplacePattern',
              ( ['in'], BSTR, 'Pattern' ),
              ( ['in'], BSTR, 'Replace' ),
              ( ['in', 'optional'], c_int, 'vsFindOptionsValue', 0 ),
              ( ['in', 'out', 'optional'], POINTER(POINTER(TextRanges)), 'Tags', 0 ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfFound' )),
    COMMETHOD([dispid(70), helpstring(u'Searches for the given pattern from the active point to the end of the document.')], HRESULT, 'FindText',
              ( ['in'], BSTR, 'Pattern' ),
              ( ['in', 'optional'], c_int, 'vsFindOptionsValue', 0 ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfFound' )),
    COMMETHOD([dispid(71), helpstring(u'Searches for the given pattern in the selection and replaces it with new text.'), 'hidden'], HRESULT, 'ReplaceText',
              ( ['in'], BSTR, 'Pattern' ),
              ( ['in'], BSTR, 'Replace' ),
              ( ['in', 'optional'], c_int, 'vsFindOptionsValue', 0 ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfFound' )),
    COMMETHOD([dispid(32), helpstring(u'Moves to the beginning of the indicated line and selects the line if requested.')], HRESULT, 'GotoLine',
              ( ['in'], c_int, 'Line' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Select', False )),
    COMMETHOD([dispid(33), helpstring(u'Indents the lines of the selection by the number of indentation levels given. The default is 1 indentation level.')], HRESULT, 'Indent',
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(34), helpstring(u'Removes indents from the selected lines by the number of indentation levels given. The default is 1 indentation level.')], HRESULT, 'Unindent',
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(35), helpstring(u'Inserts the given string at the current location.')], HRESULT, 'Insert',
              ( ['in'], BSTR, 'Text' ),
              ( ['in', 'optional'], c_int, 'vsInsertFlagsCollapseToEndValue', 1 )),
    COMMETHOD([dispid(61), helpstring(u'Inserts the contents of the specified file at the current location.')], HRESULT, 'InsertFromFile',
              ( ['in'], BSTR, 'File' )),
    COMMETHOD([dispid(36), helpstring(u'Moves the object down by the specified number of lines. The default is 1 line.')], HRESULT, 'LineDown',
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False ),
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(37), helpstring(u'Moves the object up by the specified number of lines. The default is 1 line.')], HRESULT, 'LineUp',
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False ),
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(38), helpstring(u'Moves the active point to the given position.')], HRESULT, 'MoveToPoint',
              ( ['in'], POINTER(TextPoint), 'Point' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False )),
    COMMETHOD([dispid(39), helpstring(u'Moves the active point to the given position.')], HRESULT, 'MoveToLineAndOffset',
              ( ['in'], c_int, 'Line' ),
              ( ['in'], c_int, 'Offset' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False )),
    COMMETHOD([dispid(40), helpstring(u'Moves the active point to the given 1-based absolute character offset.')], HRESULT, 'MoveToAbsoluteOffset',
              ( ['in'], c_int, 'Offset' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False )),
    COMMETHOD([dispid(41), helpstring(u'Inserts a line break at the active point.')], HRESULT, 'NewLine',
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(42), helpstring(u'Sets an unnamed bookmark on the current line.')], HRESULT, 'SetBookmark'),
    COMMETHOD([dispid(43), helpstring(u'Moves to the location of the next bookmark in the document.')], HRESULT, 'NextBookmark',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbFound' )),
    COMMETHOD([dispid(44), helpstring(u'Moves to the location of the previous bookmark in the document.')], HRESULT, 'PreviousBookmark',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbFound' )),
    COMMETHOD([dispid(45), helpstring(u'Fills the current line with white space to the given column.')], HRESULT, 'PadToColumn',
              ( ['in'], c_int, 'Column' )),
    COMMETHOD([dispid(46), helpstring(u'Formats the indicated span of text based on the current language.')], HRESULT, 'SmartFormat'),
    COMMETHOD([dispid(47), helpstring(u'Selects the document.')], HRESULT, 'SelectAll'),
    COMMETHOD([dispid(48), helpstring(u'Selects the line containing the active point.')], HRESULT, 'SelectLine'),
    COMMETHOD([dispid(49), helpstring(u'Exchanges the positions of the active point and the anchor point.')], HRESULT, 'SwapAnchor'),
    COMMETHOD([dispid(50), helpstring(u"Converts spaces to tabs in the selection according to the user's tab settings.")], HRESULT, 'Tabify'),
    COMMETHOD([dispid(51), helpstring(u"Converts tabs to spaces in the selection according to the user's tab settings.")], HRESULT, 'Untabify'),
    COMMETHOD([dispid(52), helpstring(u'Moves the object the specified number of words to the left. The default is 1 word.')], HRESULT, 'WordLeft',
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False ),
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(53), helpstring(u'Moves the object the specified number of words to the right. The default is 1 word.')], HRESULT, 'WordRight',
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False ),
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(54), helpstring(u'Returns the text pane that contains the selection.'), 'propget'], HRESULT, 'TextPane',
              ( ['retval', 'out'], POINTER(POINTER(TextPane)), 'ppPane' )),
    COMMETHOD([dispid(55), helpstring(u'Sets/returns value determining whether dragging the mouse selects in stream mode or block mode.'), 'propget'], HRESULT, 'Mode',
              ( ['retval', 'out'], POINTER(vsSelectionMode), 'pMode' )),
    COMMETHOD([dispid(55), helpstring(u'Sets/returns value determining whether dragging the mouse selects in stream mode or block mode.'), 'propput'], HRESULT, 'Mode',
              ( ['in'], vsSelectionMode, 'pMode' )),
    COMMETHOD([dispid(56), helpstring(u'Returns a TextRanges collection with one TextRange object for each line or partial line in the selection.'), 'propget'], HRESULT, 'TextRanges',
              ( ['retval', 'out'], POINTER(POINTER(TextRanges)), 'ppRanges' )),
    COMMETHOD([dispid(80), helpstring(u'Deletes a specified number of characters to the left of the active point. The default is 1 character.'), 'hidden'], HRESULT, 'Backspace',
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(81), helpstring(u'Collapses the selection to the active point.'), 'hidden'], HRESULT, 'Cancel'),
    COMMETHOD([dispid(57), helpstring(u'Inserts text, overwriting the existing text.')], HRESULT, 'DestructiveInsert',
              ( ['in'], BSTR, 'Text' )),
    COMMETHOD([dispid(82), helpstring(u'Moves the active point to the indicated display column.'), 'hidden'], HRESULT, 'MoveTo',
              ( ['in'], c_int, 'Line' ),
              ( ['in'], c_int, 'Column' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False )),
    COMMETHOD([dispid(58), helpstring(u'Moves the active point to the indicated display column.')], HRESULT, 'MoveToDisplayColumn',
              ( ['in'], c_int, 'Line' ),
              ( ['in'], c_int, 'Column' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False )),
    COMMETHOD([dispid(59), helpstring(u'Moves the active point a specified number of pages up in the document, scrolling the view.')], HRESULT, 'PageUp',
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False ),
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(60), helpstring(u'Moves the active point a specified number of pages down in the document, scrolling the view.')], HRESULT, 'PageDown',
              ( ['in', 'optional'], VARIANT_BOOL, 'Extend', False ),
              ( ['in', 'optional'], c_int, 'Count', 1 )),
]
################################################################
## code template for TextSelection implementation
##class TextSelection_Impl(object):
##    def Cut(self):
##        u'Copies the selection to the clipboard and deletes it.'
##        #return 
##
##    @property
##    def AnchorPoint(self):
##        u'Returns the origin point of the selection.'
##        #return ppPoint
##
##    def EndOfDocument(self, Extend):
##        u'Moves the object to the end of the document.'
##        #return 
##
##    @property
##    def TopPoint(self):
##        u'Returns the top end of the selection.'
##        #return ppPoint
##
##    def StartOfDocument(self, Extend):
##        u'Moves the object to the beginning of the document.'
##        #return 
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    def SetBookmark(self):
##        u'Sets an unnamed bookmark on the current line.'
##        #return 
##
##    def PadToColumn(self, Column):
##        u'Fills the current line with white space to the given column.'
##        #return 
##
##    def WordLeft(self, Extend, Count):
##        u'Moves the object the specified number of words to the left. The default is 1 word.'
##        #return 
##
##    def Backspace(self, Count):
##        u'Deletes a specified number of characters to the left of the active point. The default is 1 character.'
##        #return 
##
##    def DestructiveInsert(self, Text):
##        u'Inserts text, overwriting the existing text.'
##        #return 
##
##    def FindPattern(self, Pattern, vsFindOptionsValue):
##        u'Searches for the given pattern from the active point to the end of the document.'
##        #return Tags, pfFound
##
##    def CharRight(self, Extend, Count):
##        u'Moves the object the specified number of characters to the right. The default is 1 character.'
##        #return 
##
##    @property
##    def TopLine(self):
##        u'Returns the 1-based line index of the top point.'
##        #return pLine
##
##    def SelectAll(self):
##        u'Selects the document.'
##        #return 
##
##    def MoveTo(self, Line, Column, Extend):
##        u'Moves the active point to the indicated display column.'
##        #return 
##
##    def NextBookmark(self):
##        u'Moves to the location of the next bookmark in the document.'
##        #return pbFound
##
##    @property
##    def AnchorColumn(self):
##        u'Returns the 1-based column index of the anchor point.'
##        #return pColumn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppParent
##
##    def PreviousBookmark(self):
##        u'Moves to the location of the previous bookmark in the document.'
##        #return pbFound
##
##    def NewLine(self, Count):
##        u'Inserts a line break at the active point.'
##        #return 
##
##    def DeleteLeft(self, Count):
##        u'Deletes a specified number of characters to the left of the active point. The default is 1 character.'
##        #return 
##
##    @property
##    def ActivePoint(self):
##        u'Returns the current endpoint of the selection.'
##        #return ppPoint
##
##    def GotoLine(self, Line, Select):
##        u'Moves to the beginning of the indicated line and selects the line if requested.'
##        #return 
##
##    def FindText(self, Pattern, vsFindOptionsValue):
##        u'Searches for the given pattern from the active point to the end of the document.'
##        #return pfFound
##
##    def MoveToPoint(self, Point, Extend):
##        u'Moves the active point to the given position.'
##        #return 
##
##    def ReplaceText(self, Pattern, Replace, vsFindOptionsValue):
##        u'Searches for the given pattern in the selection and replaces it with new text.'
##        #return pfFound
##
##    def WordRight(self, Extend, Count):
##        u'Moves the object the specified number of words to the right. The default is 1 word.'
##        #return 
##
##    @property
##    def BottomPoint(self):
##        u'Returns the bottom end of the selection.'
##        #return ppPoint
##
##    def Untabify(self):
##        u"Converts tabs to spaces in the selection according to the user's tab settings."
##        #return 
##
##    def CharLeft(self, Extend, Count):
##        u'Moves the object the specified number of characters to the left. The default is 1 character.'
##        #return 
##
##    def ReplacePattern(self, Pattern, Replace, vsFindOptionsValue):
##        u'Searches for the given pattern in the selection and replaces it with new text.'
##        #return Tags, pfFound
##
##    def PageUp(self, Extend, Count):
##        u'Moves the active point a specified number of pages up in the document, scrolling the view.'
##        #return 
##
##    def Copy(self):
##        u'Copies the selection to the clipboard.'
##        #return 
##
##    def Paste(self):
##        u'Inserts the clipboard contents at the current location.'
##        #return 
##
##    def Delete(self, Count):
##        u'Deletes the selection.'
##        #return 
##
##    def PageDown(self, Extend, Count):
##        u'Moves the active point a specified number of pages down in the document, scrolling the view.'
##        #return 
##
##    def Insert(self, Text, vsInsertFlagsCollapseToEndValue):
##        u'Inserts the given string at the current location.'
##        #return 
##
##    def Unindent(self, Count):
##        u'Removes indents from the selected lines by the number of indentation levels given. The default is 1 indentation level.'
##        #return 
##
##    def Indent(self, Count):
##        u'Indents the lines of the selection by the number of indentation levels given. The default is 1 indentation level.'
##        #return 
##
##    @property
##    def TextRanges(self):
##        u'Returns a TextRanges collection with one TextRange object for each line or partial line in the selection.'
##        #return ppRanges
##
##    @property
##    def CurrentLine(self):
##        u'Returns the 1-based line index of the active point.'
##        #return pLine
##
##    @property
##    def BottomLine(self):
##        u'Returns the 1-based line index of the bottom point.'
##        #return pLine
##
##    @property
##    def IsActiveEndGreater(self):
##        u'Indicates whether the active point is equal to the bottom point.'
##        #return pfGreater
##
##    def SelectLine(self):
##        u'Selects the line containing the active point.'
##        #return 
##
##    def MoveToLineAndOffset(self, Line, Offset, Extend):
##        u'Moves the active point to the given position.'
##        #return 
##
##    @property
##    def IsEmpty(self):
##        u'Indicates whether the anchor point is equal to the active point.'
##        #return pfEmpty
##
##    def _get(self):
##        u'Sets/returns value determining whether dragging the mouse selects in stream mode or block mode.'
##        #return pMode
##    def _set(self, pMode):
##        u'Sets/returns value determining whether dragging the mouse selects in stream mode or block mode.'
##    Mode = property(_get, _set, doc = _set.__doc__)
##
##    def ChangeCase(self, How):
##        u'Changes the case of the selected text.'
##        #return 
##
##    def OutlineSection(self):
##        u'Creates an outlining section based on the current selection.'
##        #return 
##
##    def Collapse(self):
##        u'Collapses the selection to the active point.'
##        #return 
##
##    @property
##    def CurrentColumn(self):
##        u'Returns the 1-based column index of the active point.'
##        #return pColumn
##
##    def LineUp(self, Extend, Count):
##        u'Moves the object up by the specified number of lines. The default is 1 line.'
##        #return 
##
##    def SwapAnchor(self):
##        u'Exchanges the positions of the active point and the anchor point.'
##        #return 
##
##    def MoveToAbsoluteOffset(self, Offset, Extend):
##        u'Moves the active point to the given 1-based absolute character offset.'
##        #return 
##
##    def SmartFormat(self):
##        u'Formats the indicated span of text based on the current language.'
##        #return 
##
##    def _get(self):
##        u'Returns the selected text.'
##        #return pText
##    def _set(self, pText):
##        u'Returns the selected text.'
##    Text = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def TextPane(self):
##        u'Returns the text pane that contains the selection.'
##        #return ppPane
##
##    def StartOfLine(self, Where, Extend):
##        u'Moves the object to the beginning of the current line.'
##        #return 
##
##    def Tabify(self):
##        u"Converts spaces to tabs in the selection according to the user's tab settings."
##        #return 
##
##    def LineDown(self, Extend, Count):
##        u'Moves the object down by the specified number of lines. The default is 1 line.'
##        #return 
##
##    def ClearBookmark(self):
##        u'Clears any unnamed bookmarks on the current line.'
##        #return 
##
##    def Cancel(self):
##        u'Collapses the selection to the active point.'
##        #return 
##
##    def MoveToDisplayColumn(self, Line, Column, Extend):
##        u'Moves the active point to the indicated display column.'
##        #return 
##
##    def InsertFromFile(self, File):
##        u'Inserts the contents of the specified file at the current location.'
##        #return 
##
##    def DeleteWhitespace(self, Direction):
##        u'Deletes white space horizontally or vertically around the current location.'
##        #return 
##
##    def EndOfLine(self, Extend):
##        u'Moves the object to the end of the current line.'
##        #return 
##

vsWindowKindDynamicHelp = u'{66DBA47C-61DF-11D2-AA79-00C04F990343}' # Constant STRING
vsWindowKindClassView = u'{C9C0AE26-AA77-11D2-B3F0-0000F87570EE}' # Constant STRING
vsWindowKindDocumentOutline = u'{25F7E850-FFA1-11D0-B63F-00A0C922E851}' # Constant STRING
vsWindowKindServerExplorer = u'{74946827-37A0-11D2-A273-00C04F8EF4FF}' # Constant STRING
vsWindowKindCommandWindow = u'{28836128-FC2C-11D2-A433-00C04F72D18A}' # Constant STRING
vsWindowKindFindSymbol = u'{53024D34-0EF5-11D3-87E0-00C04F7971A5}' # Constant STRING

# values for enumeration 'DsGoToLineOptions'
dsLastLine = -1
DsGoToLineOptions = c_int # enum

# values for enumeration 'DsMovementOptions'
dsMove = 0
dsExtend = 1
DsMovementOptions = c_int # enum
class _FindEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides events for Find operations.'
    _iid_ = GUID('{C5331ACD-C5D5-11D2-8598-006097C68E81}')
    _idlflags_ = ['oleautomation']
_FindEvents._methods_ = [
]
################################################################
## code template for _FindEvents implementation
##class _FindEvents_Impl(object):

class SolutionBuild(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object used to build, clean, deploy, etc. the currently active SolutionConfiguration.'
    _iid_ = GUID('{A3C1C40C-9218-4D4C-9DAA-075F64F6922C}')
    _idlflags_ = ['dual', 'oleautomation']
class Solution(CoClass):
    u'Collection of all projects in the environment; contains many properties of the solution.'
    _reg_clsid_ = GUID('{B35CAA8C-77DE-4AB3-8E5A-F038E3FC6056}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _Solution(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Collection of all projects in the environment; contains many properties of the solution.'
    _iid_ = GUID('{26F6CC4B-7A48-4E4D-8AF5-9E960232E05F}')
    _idlflags_ = ['dual', 'oleautomation']
Solution._com_interfaces_ = [_Solution]

class SolutionConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u"Object defining a set of which projects and it's configuration should be built."
    _iid_ = GUID('{60AAAD75-CB8D-4C62-9959-24D6A6A50DE7}')
    _idlflags_ = ['dual', 'oleautomation']
class BuildDependencies(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Collection of projects that must be built before the owning project can be built.'
    _iid_ = GUID('{EAD260EB-1E5B-450A-B628-4CFADA11B4A1}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsBuildState'
vsBuildStateNotStarted = 1
vsBuildStateInProgress = 2
vsBuildStateDone = 3
vsBuildState = c_int # enum
class SolutionConfigurations(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Collection of defined SolutionConfiguration objects.'
    _iid_ = GUID('{23E78ED7-C9E1-462D-8BC6-366003486ED9}')
    _idlflags_ = ['dual', 'oleautomation']
SolutionBuild._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Solution)), 'ppSolution' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the currently active SolutionConfiguration object.'), 'propget'], HRESULT, 'ActiveConfiguration',
              ( ['retval', 'out'], POINTER(POINTER(SolutionConfiguration)), 'ppSolutionConfiguration' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the object used for setting inter-project dependencies.'), 'propget'], HRESULT, 'BuildDependencies',
              ( ['retval', 'out'], POINTER(POINTER(BuildDependencies)), 'ppBuildDependencies' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the current state (building, no builds started, build completed) of the build engine.'), 'propget'], HRESULT, 'BuildState',
              ( ['retval', 'out'], POINTER(vsBuildState), 'pvsBuildState' )),
    COMMETHOD([dispid(6), helpstring(u'Returns the results of the last build.'), 'propget'], HRESULT, 'LastBuildInfo',
              ( ['retval', 'out'], POINTER(c_int), 'pBuiltSuccessfully' )),
    COMMETHOD([dispid(7), helpstring(u'Sets/Returns the list of startup projects.'), 'propput'], HRESULT, 'StartupProjects',
              ( ['in'], VARIANT, 'pProject' )),
    COMMETHOD([dispid(7), helpstring(u'Sets/Returns the list of startup projects.'), 'propget'], HRESULT, 'StartupProjects',
              ( ['retval', 'out'], POINTER(VARIANT), 'pProject' )),
    COMMETHOD([dispid(8), helpstring(u'Build the currently active SolutionConfiguration.')], HRESULT, 'Build',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForBuildToFinish', False )),
    COMMETHOD([dispid(9), helpstring(u'Starts debugging the currently active SolutionConfiguration.')], HRESULT, 'Debug'),
    COMMETHOD([dispid(10), helpstring(u'Deploys the currently active SolutionConfiguration.')], HRESULT, 'Deploy',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForDeployToFinish', False )),
    COMMETHOD([dispid(11), helpstring(u'Removes all files built from the currently active SolutionConfiguration.')], HRESULT, 'Clean',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForCleanToFinish', False )),
    COMMETHOD([dispid(12), helpstring(u'Sets all StartupProjects in the running state.')], HRESULT, 'Run'),
    COMMETHOD([dispid(13), helpstring(u'Returns the collection of SolutionConfigurations for the open solution.'), 'propget'], HRESULT, 'SolutionConfigurations',
              ( ['retval', 'out'], POINTER(POINTER(SolutionConfigurations)), 'ppSolutionConfigurations' )),
    COMMETHOD([dispid(14), helpstring(u'Builds a particular project within a specified Solution Configuration.')], HRESULT, 'BuildProject',
              ( [], BSTR, 'SolutionConfiguration' ),
              ( [], BSTR, 'ProjectUniqueName' ),
              ( ['optional'], VARIANT_BOOL, 'WaitForBuildToFinish', False )),
]
################################################################
## code template for SolutionBuild implementation
##class SolutionBuild_Impl(object):
##    def Run(self):
##        u'Sets all StartupProjects in the running state.'
##        #return 
##
##    def _get(self):
##        u'Sets/Returns the list of startup projects.'
##        #return pProject
##    def _set(self, pProject):
##        u'Sets/Returns the list of startup projects.'
##    StartupProjects = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppSolution
##
##    def Deploy(self, WaitForDeployToFinish):
##        u'Deploys the currently active SolutionConfiguration.'
##        #return 
##
##    @property
##    def SolutionConfigurations(self):
##        u'Returns the collection of SolutionConfigurations for the open solution.'
##        #return ppSolutionConfigurations
##
##    def BuildProject(self, SolutionConfiguration, ProjectUniqueName, WaitForBuildToFinish):
##        u'Builds a particular project within a specified Solution Configuration.'
##        #return 
##
##    @property
##    def BuildState(self):
##        u'Returns the current state (building, no builds started, build completed) of the build engine.'
##        #return pvsBuildState
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    def Build(self, WaitForBuildToFinish):
##        u'Build the currently active SolutionConfiguration.'
##        #return 
##
##    def Clean(self, WaitForCleanToFinish):
##        u'Removes all files built from the currently active SolutionConfiguration.'
##        #return 
##
##    def Debug(self):
##        u'Starts debugging the currently active SolutionConfiguration.'
##        #return 
##
##    @property
##    def LastBuildInfo(self):
##        u'Returns the results of the last build.'
##        #return pBuiltSuccessfully
##
##    @property
##    def ActiveConfiguration(self):
##        u'Returns the currently active SolutionConfiguration object.'
##        #return ppSolutionConfiguration
##
##    @property
##    def BuildDependencies(self):
##        u'Returns the object used for setting inter-project dependencies.'
##        #return ppBuildDependencies
##

class _DocumentEventsRoot(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{DC5437F4-F114-11D2-AACF-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
class Document(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A Document open for editing.'
    _iid_ = GUID('{63EB5C39-CA8F-498E-9A66-6DD4A27AC95B}')
    _idlflags_ = ['dual', 'oleautomation']
_DocumentEventsRoot._methods_ = [
    COMMETHOD([dispid(1), 'hidden', 'propget'], HRESULT, 'DocumentEvents',
              ( ['in'], POINTER(Document), 'WindowFilter' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppDisp' )),
]
################################################################
## code template for _DocumentEventsRoot implementation
##class _DocumentEventsRoot_Impl(object):
##    @property
##    def DocumentEvents(self, WindowFilter):
##        '-no docstring-'
##        #return ppDisp
##

class CommandBarEvents(CoClass):
    u'The CommandBarEvents object triggers an event when a control on the command bar is clicked.'
    _reg_clsid_ = GUID('{BFD4B2B2-9EEC-4DB8-ABA0-AC316F4C7328}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _CommandBarControlEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The CommandBarEvents object triggers an event when a control on the command bar is clicked.'
    _iid_ = GUID('{9E66FE98-A1C6-421D-8C0C-6DA4E652E770}')
    _idlflags_ = ['oleautomation']
class _dispCommandBarControlEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The CommandBarEvents object triggers an event when a control on the command bar is clicked.'
    _iid_ = GUID('{987FB893-F96D-11D0-BBBB-00A0C90F2744}')
    _idlflags_ = []
    _methods_ = []
CommandBarEvents._com_interfaces_ = [_CommandBarControlEvents]
CommandBarEvents._outgoing_interfaces_ = [_dispCommandBarControlEvents]

class FileCodeModel(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object allowing access to programmatic constructs in a source file.'
    _iid_ = GUID('{ED1A3F99-4477-11D3-89BF-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation']
class CodeClass(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing a class in source code.'
    _iid_ = GUID('{B1F42514-91CD-4D3A-8B25-A317D8032B24}')
    _idlflags_ = ['dual', 'oleautomation']
class CodeInterface(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing an interface in source code.'
    _iid_ = GUID('{B1F42510-91CD-4D3A-8B25-A317D8032B24}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsCMFunction'
vsCMFunctionOther = 0
vsCMFunctionConstructor = 1
vsCMFunctionPropertyGet = 2
vsCMFunctionPropertyLet = 4
vsCMFunctionPropertySet = 8
vsCMFunctionPutRef = 16
vsCMFunctionPropertyAssign = 32
vsCMFunctionSub = 64
vsCMFunctionFunction = 128
vsCMFunctionTopLevel = 256
vsCMFunctionDestructor = 512
vsCMFunctionOperator = 1024
vsCMFunctionVirtual = 2048
vsCMFunctionPure = 4096
vsCMFunctionConstant = 8192
vsCMFunctionShared = 16384
vsCMFunctionInline = 32768
vsCMFunctionComMethod = 65536
vsCMFunction = c_int # enum
class CodeFunction(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object defining a function construct in a source file.'
    _iid_ = GUID('{0CFBC2B9-0D4E-11D3-8997-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation']
class CodeStruct(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing a structure in source code.'
    _iid_ = GUID('{B1F42511-91CD-4D3A-8B25-A317D8032B24}')
    _idlflags_ = ['dual', 'oleautomation']
class CodeDelegate(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing a delegate in source code.'
    _iid_ = GUID('{B1F42513-91CD-4D3A-8B25-A317D8032B24}')
    _idlflags_ = ['dual', 'oleautomation']
FileCodeModel._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(3), helpstring(u'Programming language used to author the code.'), 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(4), helpstring(u'Returns a collection of code elements.'), 'propget'], HRESULT, 'CodeElements',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(5), helpstring(u'Returns a code element at a specific location in a source file.')], HRESULT, 'CodeElementFromPoint',
              ( [], POINTER(TextPoint), 'Point' ),
              ( [], vsCMElement, 'Scope' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeElement)), 'ppCodeElement' )),
    COMMETHOD([dispid(7), helpstring(u'Creates a new namespace code construct and inserts the code in the correct location.')], HRESULT, 'AddNamespace',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeNamespace)), 'ppCodeNamespace' )),
    COMMETHOD([dispid(8), helpstring(u'Creates a new class code construct and inserts the code in the correct location.')], HRESULT, 'AddClass',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], VARIANT, 'ImplementedInterfaces' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeClass)), 'ppCodeClass' )),
    COMMETHOD([dispid(9), helpstring(u'Creates a new interface code construct and inserts the code in the correct location.')], HRESULT, 'AddInterface',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeInterface)), 'ppCodeInterface' )),
    COMMETHOD([dispid(10), helpstring(u'Creates a new function code construct and inserts the code in the correct location.')], HRESULT, 'AddFunction',
              ( [], BSTR, 'Name' ),
              ( [], vsCMFunction, 'Kind' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeFunction)), 'ppCodeFunction' )),
    COMMETHOD([dispid(11), helpstring(u'Creates a new variable code construct and inserts the code in the correct location.')], HRESULT, 'AddVariable',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeVariable)), 'ppCodeVariable' )),
    COMMETHOD([dispid(12), helpstring(u'Creates a new attribute code construct and inserts the code in the correct location.')], HRESULT, 'AddAttribute',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeAttribute)), 'ppCodeAttribute' )),
    COMMETHOD([dispid(13), helpstring(u'Creates a new structure code construct and inserts the code in the correct location.')], HRESULT, 'AddStruct',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], VARIANT, 'ImplementedInterfaces' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeStruct)), 'ppCodeStruct' )),
    COMMETHOD([dispid(14), helpstring(u'Creates a new enumeration code construct and inserts the code in the correct location.')], HRESULT, 'AddEnum',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeEnum)), 'ppCodeEnum' )),
    COMMETHOD([dispid(15), helpstring(u'Creates a new delegate code construct and inserts the code in the correct location.')], HRESULT, 'AddDelegate',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeDelegate)), 'ppCodeDelegate' )),
    COMMETHOD([dispid(16), helpstring(u'Removes a code element from the source file.')], HRESULT, 'Remove',
              ( [], VARIANT, 'Element' )),
]
################################################################
## code template for FileCodeModel implementation
##class FileCodeModel_Impl(object):
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return pProjItem
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    def AddStruct(self, Name, Position, Bases, ImplementedInterfaces, Access):
##        u'Creates a new structure code construct and inserts the code in the correct location.'
##        #return ppCodeStruct
##
##    def Remove(self, Element):
##        u'Removes a code element from the source file.'
##        #return 
##
##    def AddFunction(self, Name, Kind, Type, Position, Access):
##        u'Creates a new function code construct and inserts the code in the correct location.'
##        #return ppCodeFunction
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def AddAttribute(self, Name, Value, Position):
##        u'Creates a new attribute code construct and inserts the code in the correct location.'
##        #return ppCodeAttribute
##
##    def AddVariable(self, Name, Type, Position, Access):
##        u'Creates a new variable code construct and inserts the code in the correct location.'
##        #return ppCodeVariable
##
##    def AddNamespace(self, Name, Position):
##        u'Creates a new namespace code construct and inserts the code in the correct location.'
##        #return ppCodeNamespace
##
##    def AddDelegate(self, Name, Type, Position, Access):
##        u'Creates a new delegate code construct and inserts the code in the correct location.'
##        #return ppCodeDelegate
##
##    @property
##    def CodeElements(self):
##        u'Returns a collection of code elements.'
##        #return ppCodeElements
##
##    def AddEnum(self, Name, Position, Bases, Access):
##        u'Creates a new enumeration code construct and inserts the code in the correct location.'
##        #return ppCodeEnum
##
##    def AddInterface(self, Name, Position, Bases, Access):
##        u'Creates a new interface code construct and inserts the code in the correct location.'
##        #return ppCodeInterface
##
##    def AddClass(self, Name, Position, Bases, ImplementedInterfaces, Access):
##        u'Creates a new class code construct and inserts the code in the correct location.'
##        #return ppCodeClass
##
##    def CodeElementFromPoint(self, Point, Scope):
##        u'Returns a code element at a specific location in a source file.'
##        #return ppCodeElement
##

CodeAttribute._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppParent' )),
    COMMETHOD([dispid(32), helpstring(u'Sets/Returns the data for this object.'), 'propget'], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(BSTR), 'pValue' )),
    COMMETHOD([dispid(32), helpstring(u'Sets/Returns the data for this object.'), 'propput'], HRESULT, 'Value',
              ( [], BSTR, 'pValue' )),
    COMMETHOD([dispid(33), helpstring(u'Removes an object from a collection.')], HRESULT, 'Delete'),
]
################################################################
## code template for CodeAttribute implementation
##class CodeAttribute_Impl(object):
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    def _get(self):
##        u'Sets/Returns the data for this object.'
##        #return pValue
##    def _set(self, pValue):
##        u'Sets/Returns the data for this object.'
##    Value = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppParent
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##
##    def Delete(self):
##        u'Removes an object from a collection.'
##        #return 
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##


# values for enumeration 'vsBuildKind'
vsBuildKindSolution = 0
vsBuildKindProject = 1
vsBuildKindProjectItem = 2
vsBuildKind = c_int # enum
class _OutputWindowEventsRoot(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{AA6F4085-33B6-4629-B9EA-692101007CC2}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_OutputWindowEventsRoot._methods_ = [
    COMMETHOD([dispid(1), 'hidden', 'propget'], HRESULT, 'OutputWindowEvents',
              ( ['in'], BSTR, 'PaneFilter' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppDisp' )),
]
################################################################
## code template for _OutputWindowEventsRoot implementation
##class _OutputWindowEventsRoot_Impl(object):
##    @property
##    def OutputWindowEvents(self, PaneFilter):
##        '-no docstring-'
##        #return ppDisp
##

class CodeProperty(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object defining a property construct in a source file.'
    _iid_ = GUID('{0CFBC2BB-0D4E-11D3-8997-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation']
CodeInterface._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ParentObject' )),
    COMMETHOD([dispid(32), helpstring(u'Returns an object defining the parent namespace.'), 'nonbrowsable', 'propget'], HRESULT, 'Namespace',
              ( ['retval', 'out'], POINTER(POINTER(CodeNamespace)), 'ppCodeNamespace' )),
    COMMETHOD([dispid(33), helpstring(u'Returns a collection of classes this item derives from.'), 'nonbrowsable', 'propget'], HRESULT, 'Bases',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(34), helpstring(u'Returns a collection of items contained by this element.'), 'nonbrowsable', 'propget'], HRESULT, 'Members',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(35), helpstring(u'Defines the access attributes of this item.'), 'propput'], HRESULT, 'Access',
              ( [], vsCMAccess, 'pAccess' )),
    COMMETHOD([dispid(35), helpstring(u'Defines the access attributes of this item.'), 'propget'], HRESULT, 'Access',
              ( ['retval', 'out'], POINTER(vsCMAccess), 'pAccess' )),
    COMMETHOD([dispid(36), helpstring(u'Returns a collection of items containing attributes.'), 'nonbrowsable', 'propget'], HRESULT, 'Attributes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(37), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propget'], HRESULT, 'DocComment',
              ( ['retval', 'out'], POINTER(BSTR), 'pDocComment' )),
    COMMETHOD([dispid(37), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propput'], HRESULT, 'DocComment',
              ( [], BSTR, 'pDocComment' )),
    COMMETHOD([dispid(38), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Comment',
              ( ['retval', 'out'], POINTER(BSTR), 'pComment' )),
    COMMETHOD([dispid(38), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propput'], HRESULT, 'Comment',
              ( [], BSTR, 'pComment' )),
    COMMETHOD([dispid(39), helpstring(u'Adds an item to the list of inherited objects.')], HRESULT, 'AddBase',
              ( [], VARIANT, 'Base' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeElement)), 'ppOut' )),
    COMMETHOD([dispid(40), helpstring(u'Creates a new attribute code construct and inserts the code in the correct location.')], HRESULT, 'AddAttribute',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeAttribute)), 'ppCodeAttribute' )),
    COMMETHOD([dispid(41), helpstring(u'Removes an object from the list of bases.')], HRESULT, 'RemoveBase',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(42), helpstring(u'Removes a member code construct.')], HRESULT, 'RemoveMember',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(43), helpstring(u'Returns a Boolean telling if an object has another object as a base.'), 'propget'], HRESULT, 'IsDerivedFrom',
              ( [], BSTR, 'FullName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(44), helpstring(u'Returns a collection of objects derived from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'DerivedTypes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(61), helpstring(u'Creates a new function code construct and inserts the code in the correct location.')], HRESULT, 'AddFunction',
              ( [], BSTR, 'Name' ),
              ( [], vsCMFunction, 'Kind' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeFunction)), 'ppCodeFunction' )),
    COMMETHOD([dispid(62), helpstring(u'Creates a new property code construct and inserts the code in the correct location.')], HRESULT, 'AddProperty',
              ( [], BSTR, 'GetterName' ),
              ( [], BSTR, 'PutterName' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['optional'], VARIANT, 'Location' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeProperty)), 'ppCodeProperty' )),
]
################################################################
## code template for CodeInterface implementation
##class CodeInterface_Impl(object):
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    def AddProperty(self, GetterName, PutterName, Type, Position, Access, Location):
##        u'Creates a new property code construct and inserts the code in the correct location.'
##        #return ppCodeProperty
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def Namespace(self):
##        u'Returns an object defining the parent namespace.'
##        #return ppCodeNamespace
##
##    def AddBase(self, Base, Position):
##        u'Adds an item to the list of inherited objects.'
##        #return ppOut
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    def _get(self):
##        u'Defines the access attributes of this item.'
##        #return pAccess
##    def _set(self, pAccess):
##        u'Defines the access attributes of this item.'
##    Access = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Bases(self):
##        u'Returns a collection of classes this item derives from.'
##        #return ppCodeElements
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ParentObject
##
##    def AddFunction(self, Name, Kind, Type, Position, Access):
##        u'Creates a new function code construct and inserts the code in the correct location.'
##        #return ppCodeFunction
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    def AddAttribute(self, Name, Value, Position):
##        u'Creates a new attribute code construct and inserts the code in the correct location.'
##        #return ppCodeAttribute
##
##    def RemoveMember(self, Element):
##        u'Removes a member code construct.'
##        #return 
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def Members(self):
##        u'Returns a collection of items contained by this element.'
##        #return ppCodeElements
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def _get(self):
##        u'Returns the document comment on the current code model element.'
##        #return pDocComment
##    def _set(self, pDocComment):
##        u'Returns the document comment on the current code model element.'
##    DocComment = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveBase(self, Element):
##        u'Removes an object from the list of bases.'
##        #return 
##
##    @property
##    def Attributes(self):
##        u'Returns a collection of items containing attributes.'
##        #return ppCodeElements
##
##    def _get(self):
##        u'Sets/Returns an object defining the comment for this object.'
##        #return pComment
##    def _set(self, pComment):
##        u'Sets/Returns an object defining the comment for this object.'
##    Comment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsDerivedFrom(self, FullName):
##        u'Returns a Boolean telling if an object has another object as a base.'
##        #return pVal
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    @property
##    def DerivedTypes(self):
##        u'Returns a collection of objects derived from this object.'
##        #return ppCodeElements
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##


# values for enumeration 'vsFindResult'
vsFindResultNotFound = 0
vsFindResultFound = 1
vsFindResultReplaceAndNotFound = 2
vsFindResultReplaceAndFound = 3
vsFindResultReplaced = 4
vsFindResultPending = 5
vsFindResultError = 6
vsFindResult = c_int # enum
class ToolBoxItems(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Collection of all items on a tool box page.'
    _iid_ = GUID('{395C7DFB-F158-431C-8F43-DDA83B4EF54E}')
    _idlflags_ = ['dual', 'oleautomation']
ToolBoxTab._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( ['in'], BSTR, 'pName' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(ToolBoxTabs)), 'pToolBoxTabs' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(4), helpstring(u'Moves the focus to the specified window.')], HRESULT, 'Activate'),
    COMMETHOD([dispid(5), helpstring(u'Removes an object from a collection.')], HRESULT, 'Delete'),
    COMMETHOD([dispid(6), helpstring(u'Returns the collection of items on this tab.'), 'propget'], HRESULT, 'ToolBoxItems',
              ( ['retval', 'out'], POINTER(POINTER(ToolBoxItems)), 'pToolBoxItems' )),
    COMMETHOD([dispid(8), helpstring(u'Gets/Sets the view to list mode.'), 'propget'], HRESULT, 'ListView',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pListView' )),
    COMMETHOD([dispid(8), helpstring(u'Gets/Sets the view to list mode.'), 'propput'], HRESULT, 'ListView',
              ( ['in'], VARIANT_BOOL, 'pListView' )),
]
################################################################
## code template for ToolBoxTab implementation
##class ToolBoxTab_Impl(object):
##    def Activate(self):
##        u'Moves the focus to the specified window.'
##        #return 
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pName
##    def _set(self, pName):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets the view to list mode.'
##        #return pListView
##    def _set(self, pListView):
##        u'Gets/Sets the view to list mode.'
##    ListView = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return pToolBoxTabs
##
##    def Delete(self):
##        u'Removes an object from a collection.'
##        #return 
##
##    @property
##    def ToolBoxItems(self):
##        u'Returns the collection of items on this tab.'
##        #return pToolBoxItems
##

class IVsTextEditFonts(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{F39AB913-E6C9-4546-A265-1E43F8DE924C}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden', 'restricted']

# values for enumeration 'vsFontCharSet'
vsFontCharSetANSI = 0
vsFontCharSetDefault = 1
vsFontCharSetSymbol = 2
vsFontCharSetShiftJIS = 128
vsFontCharSetHangeul = 129
vsFontCharSetGB2312 = 134
vsFontCharSetChineseBig5 = 136
vsFontCharSetOEM = 255
vsFontCharSetJohab = 130
vsFontCharSetHebrew = 177
vsFontCharSetArabic = 178
vsFontCharSetGreek = 161
vsFontCharSetTurkish = 162
vsFontCharSetVietnamese = 163
vsFontCharSetThai = 222
vsFontCharSetEastEurope = 238
vsFontCharSetRussian = 204
vsFontCharSetMac = 77
vsFontCharSetBaltic = 186
vsFontCharSet = c_int # enum
IVsTextEditFonts._methods_ = [
    COMMETHOD([dispid(1), 'propput'], HRESULT, 'FontFamily',
              ( ['in'], BSTR, 'pbstrFontFamily' )),
    COMMETHOD([dispid(1), 'propget'], HRESULT, 'FontFamily',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrFontFamily' )),
    COMMETHOD([dispid(2), 'propput'], HRESULT, 'FontCharacterSet',
              ( ['in'], vsFontCharSet, 'pbstrCharacterSet' )),
    COMMETHOD([dispid(2), 'propget'], HRESULT, 'FontCharacterSet',
              ( ['retval', 'out'], POINTER(vsFontCharSet), 'pbstrCharacterSet' )),
    COMMETHOD([dispid(3), 'propput'], HRESULT, 'FontSize',
              ( ['in'], c_short, 'piFontSize' )),
    COMMETHOD([dispid(3), 'propget'], HRESULT, 'FontSize',
              ( ['retval', 'out'], POINTER(c_short), 'piFontSize' )),
]
################################################################
## code template for IVsTextEditFonts implementation
##class IVsTextEditFonts_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return pbstrCharacterSet
##    def _set(self, pbstrCharacterSet):
##        '-no docstring-'
##    FontCharacterSet = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pbstrFontFamily
##    def _set(self, pbstrFontFamily):
##        '-no docstring-'
##    FontFamily = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return piFontSize
##    def _set(self, piFontSize):
##        '-no docstring-'
##    FontSize = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'vsTextChanged'
vsTextChangedMultiLine = 1
vsTextChangedSave = 2
vsTextChangedCaretMoved = 4
vsTextChangedReplaceAll = 8
vsTextChangedNewline = 16
vsTextChangedFindStarting = 32
vsTextChanged = c_int # enum

# values for enumeration '_vsIndentStyle'
vsIndentStyleNone = 0
vsIndentStyleDefault = 1
vsIndentStyleSmart = 2
_vsIndentStyle = c_int # enum
UIHierarchyItems._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppDispatch' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(UIHierarchyItem)), 'ppUIHierarchyItem' )),
    COMMETHOD([dispid(5), helpstring(u'Sets/Returns the expand state of the collection of UIHierarchyItem objects.'), 'propget'], HRESULT, 'Expanded',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfExpanded' )),
    COMMETHOD([dispid(5), helpstring(u'Sets/Returns the expand state of the collection of UIHierarchyItem objects.'), 'propput'], HRESULT, 'Expanded',
              ( ['in'], VARIANT_BOOL, 'pfExpanded' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppUnknown' )),
]
################################################################
## code template for UIHierarchyItems implementation
##class UIHierarchyItems_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return ppUnknown
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppDispatch
##
##    def _get(self):
##        u'Sets/Returns the expand state of the collection of UIHierarchyItem objects.'
##        #return pfExpanded
##    def _set(self, pfExpanded):
##        u'Sets/Returns the expand state of the collection of UIHierarchyItem objects.'
##    Expanded = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return ppUIHierarchyItem
##

class _TextEditorEventsRoot(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{B3C38885-B288-44A8-B290-34FE63BF3C76}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_TextEditorEventsRoot._methods_ = [
    COMMETHOD([dispid(1), 'hidden', 'propget'], HRESULT, 'TextEditorEvents',
              ( ['in'], POINTER(TextDocument), 'TextDocumentFilter' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppDisp' )),
]
################################################################
## code template for _TextEditorEventsRoot implementation
##class _TextEditorEventsRoot_Impl(object):
##    @property
##    def TextEditorEvents(self, TextDocumentFilter):
##        '-no docstring-'
##        #return ppDisp
##


# values for enumeration 'DsStartOfLineOptions'
dsFirstColumn = 0
dsFirstText = 1
DsStartOfLineOptions = c_int # enum

# values for enumeration 'DsCaseOptions'
dsLowercase = 1
dsUppercase = 2
dsCapitalize = 3
DsCaseOptions = c_int # enum
class ContextAttributes(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{33C5EBB8-244E-449D-9CEE-FAD70A774E59}')
    _idlflags_ = ['dual', 'oleautomation']
class ContextAttribute(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{1A6E2CB3-B897-42EB-96BE-FF0FDB65DB2F}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsContextAttributeType'
vsContextAttributeFilter = 1
vsContextAttributeLookup = 2
vsContextAttributeLookupF1 = 3
vsContextAttributeType = c_int # enum

# values for enumeration 'vsContextAttributes'
vsContextAttributesGlobal = 1
vsContextAttributesWindow = 2
vsContextAttributesHighPriority = 3
vsContextAttributes = c_int # enum
ContextAttributes._methods_ = [
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(0), helpstring(u'Get a ContextAttribute by index from the attribute collection.')], HRESULT, 'Item',
              ( [], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ContextAttribute)), 'ppVal' )),
    COMMETHOD([dispid(1), helpstring(u'Get the DTE object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Get the parent object for this attribute collection (DTE or Window).'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'lppaReturn' )),
    COMMETHOD([dispid(3), helpstring(u'Get the number of attribute names in this collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([dispid(4), helpstring(u'Add an attribute name/value pair to this collection.')], HRESULT, 'Add',
              ( [], BSTR, 'AttributeName' ),
              ( [], BSTR, 'AttributeValue' ),
              ( [], vsContextAttributeType, 'Type' ),
              ( ['retval', 'out'], POINTER(POINTER(ContextAttribute)), 'ppVal' )),
    COMMETHOD([dispid(5), helpstring(u'Get the type of this collection (Global, Window, High Priority).'), 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(vsContextAttributes), 'Type' )),
    COMMETHOD([dispid(6), helpstring(u'Get the High Priority attribute collection.  There is only one instance of this attribute collection.  It is only available from Global attribute collection.'), 'propget'], HRESULT, 'HighPriorityAttributes',
              ( ['retval', 'out'], POINTER(POINTER(ContextAttributes)), 'ppVal' )),
    COMMETHOD([dispid(7), helpstring(u'Refresh the contents of this attribute collection.')], HRESULT, 'Refresh'),
]
################################################################
## code template for ContextAttributes implementation
##class ContextAttributes_Impl(object):
##    @property
##    def Count(self):
##        u'Get the number of attribute names in this collection.'
##        #return Count
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Get the parent object for this attribute collection (DTE or Window).'
##        #return lppaReturn
##
##    @property
##    def HighPriorityAttributes(self):
##        u'Get the High Priority attribute collection.  There is only one instance of this attribute collection.  It is only available from Global attribute collection.'
##        #return ppVal
##
##    @property
##    def DTE(self):
##        u'Get the DTE object.'
##        #return lppaReturn
##
##    def Item(self, index):
##        u'Get a ContextAttribute by index from the attribute collection.'
##        #return ppVal
##
##    def Add(self, AttributeName, AttributeValue, Type):
##        u'Add an attribute name/value pair to this collection.'
##        #return ppVal
##
##    def Refresh(self):
##        u'Refresh the contents of this attribute collection.'
##        #return 
##
##    @property
##    def Type(self):
##        u'Get the type of this collection (Global, Window, High Priority).'
##        #return Type
##

class HTMLWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{F6576203-FBCE-477E-A66B-EDA237BB68A7}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsHTMLTabs'
vsHTMLTabsSource = 0
vsHTMLTabsDesign = 1
vsHTMLTabs = c_int # enum
HTMLWindow._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'ppParent' )),
    COMMETHOD([dispid(4), helpstring(u'The currently selected tab of the HTML editor: Design or HTML.'), 'propget'], HRESULT, 'CurrentTab',
              ( ['retval', 'out'], POINTER(vsHTMLTabs), 'pTab' )),
    COMMETHOD([dispid(4), helpstring(u'The currently selected tab of the HTML editor: Design or HTML.'), 'propput'], HRESULT, 'CurrentTab',
              ( ['in'], vsHTMLTabs, 'pTab' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the automation object for the current tab (e.g., a TextSelection for the HTML tab).'), 'propget'], HRESULT, 'CurrentTabObject',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppObj' )),
]
################################################################
## code template for HTMLWindow implementation
##class HTMLWindow_Impl(object):
##    @property
##    def CurrentTabObject(self):
##        u'Returns the automation object for the current tab (e.g., a TextSelection for the HTML tab).'
##        #return ppObj
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppParent
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    def _get(self):
##        u'The currently selected tab of the HTML editor: Design or HTML.'
##        #return pTab
##    def _set(self, pTab):
##        u'The currently selected tab of the HTML editor: Design or HTML.'
##    CurrentTab = property(_get, _set, doc = _set.__doc__)
##

SolutionConfigurations._methods_ = [
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(SolutionConfiguration)), 'ppOut' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(SolutionBuild)), 'ppBuild' )),
    COMMETHOD([dispid(3), helpstring(u'Copies an existing SolutionConfiguration object, and returns the new SolutionConfiguration.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'NewName' ),
              ( ['in'], BSTR, 'ExistingName' ),
              ( ['in'], VARIANT_BOOL, 'Propagate' ),
              ( ['retval', 'out'], POINTER(POINTER(SolutionConfiguration)), 'ppSolutionConfiguration' )),
    COMMETHOD([dispid(4), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
]
################################################################
## code template for SolutionConfigurations implementation
##class SolutionConfigurations_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppBuild
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return ppOut
##
##    def Add(self, NewName, ExistingName, Propagate):
##        u'Copies an existing SolutionConfiguration object, and returns the new SolutionConfiguration.'
##        #return ppSolutionConfiguration
##

class TextEditorEvents(CoClass):
    u'Events fired when the text of a document is changed.'
    _reg_clsid_ = GUID('{ADF22C37-0069-4ADF-B12D-D8D47C38FE79}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _TextEditorEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{23B7A868-6C89-436A-94FA-25D755456A77}')
    _idlflags_ = ['oleautomation']
class _dispTextEditorEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{2699DD44-C507-4DA3-AA34-314A6C21DFE2}')
    _idlflags_ = []
    _methods_ = []
TextEditorEvents._com_interfaces_ = [_TextEditorEvents]
TextEditorEvents._outgoing_interfaces_ = [_dispTextEditorEvents]


# values for enumeration 'dsSaveStatus'
dsSaveCancelled = 2
dsSaveSucceeded = 1
dsSaveStatus = c_int # enum
vsIndentStyle = _vsIndentStyle
class ProjectItems(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Generic object representing items contained in project/current instance of development environment.'
    _iid_ = GUID('{8E2F1269-185E-43C7-8899-950AD2769CCF}')
    _idlflags_ = ['dual', 'oleautomation']
class Project(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Generic object used to represent projects.'
    _iid_ = GUID('{866311E6-C887-4143-9833-645F5B93F6F1}')
    _idlflags_ = ['dual', 'oleautomation']
ProjectItems._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'lppcReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'lppptReturn' )),
    COMMETHOD([dispid(10), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'lplReturn' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(201), helpstring(u'Returns a GUID String indicating the kind or type of the object.'), 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrFileName' )),
    COMMETHOD([dispid(202), helpstring(u'Adds a ProjectItem object from a file installed in project directory structure.')], HRESULT, 'AddFromFile',
              ( ['in'], BSTR, 'FileName' ),
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'lppcReturn' )),
    COMMETHOD([dispid(203), helpstring(u'Copies indicated file to ProjectItems directory; adds file as member of ProjectItems collection.')], HRESULT, 'AddFromTemplate',
              ( ['in'], BSTR, 'FileName' ),
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'lppcReturn' )),
    COMMETHOD([dispid(204), helpstring(u'Adds ProjectItem objects/sets ProjectItems properties/returns ProjectItem object representing FileName argument.')], HRESULT, 'AddFromDirectory',
              ( ['in'], BSTR, 'Directory' ),
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'lppcReturn' )),
    COMMETHOD([dispid(205), helpstring(u'Returns the project that hosts this ProjectItems object.'), 'propget'], HRESULT, 'ContainingProject',
              ( ['retval', 'out'], POINTER(POINTER(Project)), 'ppProject' )),
    COMMETHOD([dispid(206), helpstring(u'Creates a new ProjectItems object, and a folder within the project user interface.')], HRESULT, 'AddFolder',
              ( [], BSTR, 'Name' ),
              ( ['optional'], BSTR, 'Kind', u'{6BB5F8EF-4483-11D3-8BCF-00C04F8EC28C}' ),
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjectItem' )),
    COMMETHOD([dispid(207), helpstring(u'Copies a source file, and adds it to the project.')], HRESULT, 'AddFromFileCopy',
              ( [], BSTR, 'FilePath' ),
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjectItem' )),
]
################################################################
## code template for ProjectItems implementation
##class ProjectItems_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return lplReturn
##
##    def AddFromTemplate(self, FileName, Name):
##        u'Copies indicated file to ProjectItems directory; adds file as member of ProjectItems collection.'
##        #return lppcReturn
##
##    @property
##    def Kind(self):
##        u'Returns a GUID String indicating the kind or type of the object.'
##        #return lpbstrFileName
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppptReturn
##
##    def AddFromFileCopy(self, FilePath):
##        u'Copies a source file, and adds it to the project.'
##        #return pProjectItem
##
##    def AddFromDirectory(self, Directory):
##        u'Adds ProjectItem objects/sets ProjectItems properties/returns ProjectItem object representing FileName argument.'
##        #return lppcReturn
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def AddFromFile(self, FileName):
##        u'Adds a ProjectItem object from a file installed in project directory structure.'
##        #return lppcReturn
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return lppcReturn
##
##    def AddFolder(self, Name, Kind):
##        u'Creates a new ProjectItems object, and a folder within the project user interface.'
##        #return pProjectItem
##
##    @property
##    def ContainingProject(self):
##        u'Returns the project that hosts this ProjectItems object.'
##        #return ppProject
##

class _dispTaskListEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The TaskListEvents object triggers events about the Task List.'
    _iid_ = GUID('{1125C423-49BD-11D2-8823-00C04FB6C6FF}')
    _idlflags_ = []
    _methods_ = []
class TaskItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An individual item within the task list.'
    _iid_ = GUID('{58E4D419-6B8C-4C63-92DE-70161CD95890}')
    _idlflags_ = ['dual', 'oleautomation']
_dispTaskListEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Occurs when a new task is added to the Task List.')], None, 'TaskAdded',
               ( ['in'], POINTER(TaskItem), 'TaskItem' )),
    DISPMETHOD([dispid(2), helpstring(u'Occurs when a task is removed from the Task List.')], None, 'TaskRemoved',
               ( ['in'], POINTER(TaskItem), 'TaskItem' )),
    DISPMETHOD([dispid(3), helpstring(u'Occurs when a task is changed.')], None, 'TaskModified',
               ( ['in'], POINTER(TaskItem), 'TaskItem' ),
               ( ['in'], vsTaskListColumn, 'ColumnModified' )),
    DISPMETHOD([dispid(4), helpstring(u'Occurs when the user wishes to go to the source of the task item.')], None, 'TaskNavigated',
               ( ['in'], POINTER(TaskItem), 'TaskItem' ),
               ( ['in', 'out'], POINTER(VARIANT_BOOL), 'NavigateHandled' )),
]
class _WindowEventsRoot(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{17D12026-BA99-403E-A359-71FD1E5A72CD}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_WindowEventsRoot._methods_ = [
    COMMETHOD([dispid(1), 'hidden', 'propget'], HRESULT, 'WindowEvents',
              ( ['in'], POINTER(Window), 'WindowFilter' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppDisp' )),
]
################################################################
## code template for _WindowEventsRoot implementation
##class _WindowEventsRoot_Impl(object):
##    @property
##    def WindowEvents(self, WindowFilter):
##        '-no docstring-'
##        #return ppDisp
##

class TaskItems(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Collection of all items in the Task List.'
    _iid_ = GUID('{4B51103D-513C-4773-B56A-354D0928FD04}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsTaskPriority'
vsTaskPriorityLow = 1
vsTaskPriorityMedium = 2
vsTaskPriorityHigh = 3
vsTaskPriority = c_int # enum
TaskItem._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(TaskItems)), 'pTaskItems' )),
    COMMETHOD([dispid(3), helpstring(u'Returns which group of tasks this item belongs to.'), 'propget'], HRESULT, 'Category',
              ( ['retval', 'out'], POINTER(BSTR), 'pCategory' )),
    COMMETHOD([dispid(4), helpstring(u'Returns which subgroup of tasks this item belongs to.'), 'propget'], HRESULT, 'SubCategory',
              ( ['retval', 'out'], POINTER(BSTR), 'pSubCategory' )),
    COMMETHOD([dispid(5), helpstring(u'Gets/Sets the priority of the task item.'), 'propget'], HRESULT, 'Priority',
              ( ['retval', 'out'], POINTER(vsTaskPriority), 'pPriority' )),
    COMMETHOD([dispid(5), helpstring(u'Gets/Sets the priority of the task item.'), 'propput'], HRESULT, 'Priority',
              ( ['in'], vsTaskPriority, 'pPriority' )),
    COMMETHOD([dispid(6), helpstring(u'Gets/Sets the description of the task item.'), 'propget'], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'pDescription' )),
    COMMETHOD([dispid(6), helpstring(u'Gets/Sets the description of the task item.'), 'propput'], HRESULT, 'Description',
              ( ['in'], BSTR, 'pDescription' )),
    COMMETHOD([dispid(7), helpstring(u'Gets/Sets the line the task item refers to.'), 'propget'], HRESULT, 'FileName',
              ( ['retval', 'out'], POINTER(BSTR), 'pFileName' )),
    COMMETHOD([dispid(7), helpstring(u'Gets/Sets the line the task item refers to.'), 'propput'], HRESULT, 'FileName',
              ( ['in'], BSTR, 'pFileName' )),
    COMMETHOD([dispid(8), helpstring(u'Determines if a item within a task can be modified.'), 'propget'], HRESULT, 'IsSettable',
              ( ['in'], vsTaskListColumn, 'Column' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pSettable' )),
    COMMETHOD([dispid(9), helpstring(u'Gets/Sets the line the task item refers to.'), 'propget'], HRESULT, 'Line',
              ( ['retval', 'out'], POINTER(c_int), 'pLine' )),
    COMMETHOD([dispid(9), helpstring(u'Gets/Sets the line the task item refers to.'), 'propput'], HRESULT, 'Line',
              ( ['in'], c_int, 'pLine' )),
    COMMETHOD([dispid(10), helpstring(u'Returns if the task item is currently displayed.'), 'propget'], HRESULT, 'Displayed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pDisplayed' )),
    COMMETHOD([dispid(11), helpstring(u'Gets/Sets the checked state of the task item.'), 'propget'], HRESULT, 'Checked',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pChecked' )),
    COMMETHOD([dispid(11), helpstring(u'Gets/Sets the checked state of the task item.'), 'propput'], HRESULT, 'Checked',
              ( ['in'], VARIANT_BOOL, 'pChecked' )),
    COMMETHOD([dispid(12), helpstring(u'Displays the document the task item refers to.')], HRESULT, 'Navigate'),
    COMMETHOD([dispid(13), helpstring(u'Removes an object from a collection.')], HRESULT, 'Delete'),
    COMMETHOD([dispid(14), helpstring(u'Causes this item to become active in the user interface.')], HRESULT, 'Select'),
]
################################################################
## code template for TaskItem implementation
##class TaskItem_Impl(object):
##    @property
##    def Category(self):
##        u'Returns which group of tasks this item belongs to.'
##        #return pCategory
##
##    def _get(self):
##        u'Gets/Sets the checked state of the task item.'
##        #return pChecked
##    def _set(self, pChecked):
##        u'Gets/Sets the checked state of the task item.'
##    Checked = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets the description of the task item.'
##        #return pDescription
##    def _set(self, pDescription):
##        u'Gets/Sets the description of the task item.'
##    Description = property(_get, _set, doc = _set.__doc__)
##
##    def Navigate(self):
##        u'Displays the document the task item refers to.'
##        #return 
##
##    @property
##    def Displayed(self):
##        u'Returns if the task item is currently displayed.'
##        #return pDisplayed
##
##    def Select(self):
##        u'Causes this item to become active in the user interface.'
##        #return 
##
##    @property
##    def Collection(self):
##        u'Returns the parent object.'
##        #return pTaskItems
##
##    def _get(self):
##        u'Gets/Sets the line the task item refers to.'
##        #return pFileName
##    def _set(self, pFileName):
##        u'Gets/Sets the line the task item refers to.'
##    FileName = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets the priority of the task item.'
##        #return pPriority
##    def _set(self, pPriority):
##        u'Gets/Sets the priority of the task item.'
##    Priority = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    def _get(self):
##        u'Gets/Sets the line the task item refers to.'
##        #return pLine
##    def _set(self, pLine):
##        u'Gets/Sets the line the task item refers to.'
##    Line = property(_get, _set, doc = _set.__doc__)
##
##    def Delete(self):
##        u'Removes an object from a collection.'
##        #return 
##
##    @property
##    def IsSettable(self, Column):
##        u'Determines if a item within a task can be modified.'
##        #return pSettable
##
##    @property
##    def SubCategory(self):
##        u'Returns which subgroup of tasks this item belongs to.'
##        #return pSubCategory
##

class LinkedWindows(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Returns the collection of all linked windows contained in a linked window frame.'
    _iid_ = GUID('{F00EF34A-A654-4C1B-897A-585D5BCBB35A}')
    _idlflags_ = ['dual', 'oleautomation']
LinkedWindows._methods_ = [
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'ppptReturn' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'lppcReturn' )),
    COMMETHOD([dispid(201), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'lplReturn' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(202), helpstring(u'Removes a Window object from the LinkedWindows collection.')], HRESULT, 'Remove',
              ( ['in'], POINTER(Window), 'Window' )),
    COMMETHOD([dispid(203), helpstring(u'Adds a window to the collection of currently linked windows.')], HRESULT, 'Add',
              ( ['in'], POINTER(Window), 'Window' )),
    COMMETHOD([dispid(301), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
]
################################################################
## code template for LinkedWindows implementation
##class LinkedWindows_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return lplReturn
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppptReturn
##
##    def Remove(self, Window):
##        u'Removes a Window object from the LinkedWindows collection.'
##        #return 
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return lppcReturn
##
##    def Add(self, Window):
##        u'Adds a window to the collection of currently linked windows.'
##        #return 
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##

_TextEditorEvents._methods_ = [
]
################################################################
## code template for _TextEditorEvents implementation
##class _TextEditorEvents_Impl(object):

class ToolBoxItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An individual item on a tool box tab.'
    _iid_ = GUID('{46538D1B-4D81-4002-8BB4-DBDB65BABB23}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsToolBoxItemFormat'
vsToolBoxItemFormatText = 1
vsToolBoxItemFormatHTML = 2
vsToolBoxItemFormatGUID = 4
vsToolBoxItemFormatDotNETComponent = 8
vsToolBoxItemFormat = c_int # enum
ToolBoxItems._methods_ = [
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( [], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ToolBoxItem)), 'pItem' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(ToolBoxTab)), 'pParent' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([dispid(4), helpstring(u'Adds an item to the tool box.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], VARIANT, 'Data' ),
              ( ['in', 'optional'], vsToolBoxItemFormat, 'Format', 1 ),
              ( ['retval', 'out'], POINTER(POINTER(ToolBoxItem)), 'pToolBoxItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the currently active item in the collection.'), 'propget'], HRESULT, 'SelectedItem',
              ( ['retval', 'out'], POINTER(POINTER(ToolBoxItem)), 'pToolBoxItem' )),
]
################################################################
## code template for ToolBoxItems implementation
##class ToolBoxItems_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return pParent
##
##    @property
##    def SelectedItem(self):
##        u'Returns the currently active item in the collection.'
##        #return pToolBoxItem
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return pItem
##
##    def Add(self, Name, Data, Format):
##        u'Adds an item to the tool box.'
##        #return pToolBoxItem
##

class _WindowEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The WindowEvents object triggers events about Windows.'
    _iid_ = GUID('{0D3A23A8-67BB-11D2-97C1-00C04FB6C6FF}')
    _idlflags_ = ['oleautomation']
_WindowEvents._methods_ = [
]
################################################################
## code template for _WindowEvents implementation
##class _WindowEvents_Impl(object):

ContextAttribute._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Get the name of this attribute.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(1), helpstring(u'Get the DTE object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Get the parent attribute collection for this attribute.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(ContextAttributes)), 'ppCollection' )),
    COMMETHOD([dispid(3), helpstring(u'Get the collection of values for this attribute.'), 'propget'], HRESULT, 'Values',
              ( ['retval', 'out'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Remove this attribute from its parent collection.')], HRESULT, 'Remove'),
]
################################################################
## code template for ContextAttribute implementation
##class ContextAttribute_Impl(object):
##    def Remove(self):
##        u'Remove this attribute from its parent collection.'
##        #return 
##
##    @property
##    def Collection(self):
##        u'Get the parent attribute collection for this attribute.'
##        #return ppCollection
##
##    @property
##    def Values(self):
##        u'Get the collection of values for this attribute.'
##        #return pVal
##
##    @property
##    def Name(self):
##        u'Get the name of this attribute.'
##        #return pName
##
##    @property
##    def DTE(self):
##        u'Get the DTE object.'
##        #return lppaReturn
##

class TaskList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The object representing the Task List.'
    _iid_ = GUID('{4E4F0569-E16A-4DA1-92DE-10882A4DDD8C}')
    _idlflags_ = ['dual', 'oleautomation']
TaskItems._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(TaskList)), 'pTaskList' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(TaskItem)), 'pTaskItem' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([dispid(4), helpstring(u'Creates a task item and adds it to the task list.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'Category' ),
              ( ['in'], BSTR, 'SubCategory' ),
              ( ['in'], BSTR, 'Description' ),
              ( ['in', 'optional'], vsTaskPriority, 'Priority', 2 ),
              ( ['in', 'optional'], VARIANT, 'Icon' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Checkable', False ),
              ( ['in', 'optional'], BSTR, 'File', u'' ),
              ( ['in', 'optional'], c_int, 'Line', -1 ),
              ( ['in', 'optional'], VARIANT_BOOL, 'CanUserDelete', True ),
              ( ['in', 'optional'], VARIANT_BOOL, 'FlushItem', True ),
              ( ['retval', 'out'], POINTER(POINTER(TaskItem)), 'pTaskItem' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(6), helpstring(u'Force display all task items not yet added to the task list.')], HRESULT, 'ForceItemsToTaskList'),
]
################################################################
## code template for TaskItems implementation
##class TaskItems_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return pTaskList
##
##    def ForceItemsToTaskList(self):
##        u'Force display all task items not yet added to the task list.'
##        #return 
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return pTaskItem
##
##    def Add(self, Category, SubCategory, Description, Priority, Icon, Checkable, File, Line, CanUserDelete, FlushItem):
##        u'Creates a task item and adds it to the task list.'
##        #return pTaskItem
##

class _TaskListEventsRoot(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{6BC8C372-C6F0-4BE6-B255-827AC190BF71}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_TaskListEventsRoot._methods_ = [
    COMMETHOD([dispid(1), 'propget'], HRESULT, 'TaskListEvents',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppDisp' )),
]
################################################################
## code template for _TaskListEventsRoot implementation
##class _TaskListEventsRoot_Impl(object):
##    @property
##    def TaskListEvents(self):
##        '-no docstring-'
##        #return ppDisp
##


# values for enumeration 'vsStatusAnimation'
vsStatusAnimationGeneral = 0
vsStatusAnimationPrint = 1
vsStatusAnimationSave = 2
vsStatusAnimationDeploy = 3
vsStatusAnimationSync = 4
vsStatusAnimationBuild = 5
vsStatusAnimationFind = 6
vsStatusAnimation = c_int # enum
class IDTToolsOptionsPage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'This interface is implemented by tools options page writers to construct a tools options page.'
    _iid_ = GUID('{BDCAF240-2692-4713-902A-B110B1D0F100}')
    _idlflags_ = ['dual', 'oleautomation']
IDTToolsOptionsPage._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Called just after the tools options page is created for the first time.')], HRESULT, 'OnAfterCreated',
              ( ['in'], POINTER(DTE), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Called to return an object that holds the properties for the page.')], HRESULT, 'GetProperties',
              ( ['in', 'out'], POINTER(POINTER(IDispatch)), 'PropertiesObject' )),
    COMMETHOD([dispid(3), helpstring(u'Called if the user presses the OK button on the Tools Options dialog.')], HRESULT, 'OnOK'),
    COMMETHOD([dispid(4), helpstring(u'Called if the user presses the Cancel button on the Tools Options dialog.')], HRESULT, 'OnCancel'),
    COMMETHOD([dispid(5), helpstring(u'Called if the user presses the Help button on the Tools Options dialog.')], HRESULT, 'OnHelp'),
]
################################################################
## code template for IDTToolsOptionsPage implementation
##class IDTToolsOptionsPage_Impl(object):
##    def OnCancel(self):
##        u'Called if the user presses the Cancel button on the Tools Options dialog.'
##        #return 
##
##    def OnHelp(self):
##        u'Called if the user presses the Help button on the Tools Options dialog.'
##        #return 
##
##    def OnOK(self):
##        u'Called if the user presses the OK button on the Tools Options dialog.'
##        #return 
##
##    def GetProperties(self):
##        u'Called to return an object that holds the properties for the page.'
##        #return PropertiesObject
##
##    def OnAfterCreated(self, DTEObject):
##        u'Called just after the tools options page is created for the first time.'
##        #return 
##

class SolutionContexts(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Collection of SolutionContext objects within a SolutionConfiguration object.'
    _iid_ = GUID('{0685B546-FB84-4917-AB98-98D40F892D61}')
    _idlflags_ = ['dual', 'oleautomation']
class SolutionContext(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u"Object defining a project's configuration within a SolutionConfiguration object."
    _iid_ = GUID('{FC6A1A82-9C8A-47BB-A046-6E965DF5A99B}')
    _idlflags_ = ['dual', 'oleautomation']
SolutionContexts._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(SolutionConfiguration)), 'ppSolutionConfiguration' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(SolutionContext)), 'ppOut' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
]
################################################################
## code template for SolutionContexts implementation
##class SolutionContexts_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return ppOut
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppSolutionConfiguration
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##


# values for enumeration 'vsPaneShowHow'
vsPaneShowCentered = 0
vsPaneShowTop = 1
vsPaneShowAsIs = 2
vsPaneShowHow = c_int # enum
class EditPoint(TextPoint):
    _case_insensitive_ = True
    u'Object representing a movable point in a text document.'
    _iid_ = GUID('{C1FFE800-028B-4475-A907-14F51F19BB7D}')
    _idlflags_ = ['dual', 'oleautomation']
TextPoint._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(TextDocument)), 'lppaReturn' )),
    COMMETHOD([dispid(11), helpstring(u'Returns the 1-based index of the current line.'), 'propget'], HRESULT, 'Line',
              ( ['retval', 'out'], POINTER(c_int), 'lppaReturn' )),
    COMMETHOD([dispid(12), helpstring(u'Returns the 1-based index of the current column.'), 'propget'], HRESULT, 'LineCharOffset',
              ( ['retval', 'out'], POINTER(c_int), 'lppaReturn' )),
    COMMETHOD([dispid(13), helpstring(u'Returns the 1-based character index of the current position from the beginning of the document.'), 'propget'], HRESULT, 'AbsoluteCharOffset',
              ( ['retval', 'out'], POINTER(c_int), 'lppaReturn' )),
    COMMETHOD([dispid(14), helpstring(u'Returns the display column of the current position.'), 'propget'], HRESULT, 'DisplayColumn',
              ( ['retval', 'out'], POINTER(c_int), 'lppaReturn' )),
    COMMETHOD([dispid(21), helpstring(u'Returns whether the current position is at the end of the document.'), 'propget'], HRESULT, 'AtEndOfDocument',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lppaReturn' )),
    COMMETHOD([dispid(22), helpstring(u'Returns whether the current position is at the beginning of the document.'), 'propget'], HRESULT, 'AtStartOfDocument',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lppaReturn' )),
    COMMETHOD([dispid(23), helpstring(u'Returns whether the current position is at the end of the line.'), 'propget'], HRESULT, 'AtEndOfLine',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lppaReturn' )),
    COMMETHOD([dispid(24), helpstring(u'Returns whether the current position is at the beginning of the line.'), 'propget'], HRESULT, 'AtStartOfLine',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lppaReturn' )),
    COMMETHOD([dispid(25), helpstring(u'Returns the number of characters in the current line.'), 'propget'], HRESULT, 'LineLength',
              ( ['retval', 'out'], POINTER(c_int), 'lppaReturn' )),
    COMMETHOD([dispid(31), helpstring(u'Returns whether the called object is equal to the given object.')], HRESULT, 'EqualTo',
              ( ['in'], POINTER(TextPoint), 'Point' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lppaReturn' )),
    COMMETHOD([dispid(32), helpstring(u'Returns whether the called object is less than the given object.')], HRESULT, 'LessThan',
              ( ['in'], POINTER(TextPoint), 'Point' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lppaReturn' )),
    COMMETHOD([dispid(33), helpstring(u'Returns whether the called object is greater than the given object.')], HRESULT, 'GreaterThan',
              ( ['in'], POINTER(TextPoint), 'Point' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lppaReturn' )),
    COMMETHOD([dispid(50), helpstring(u"Tries to make the TextPoint's location visible to the user.")], HRESULT, 'TryToShow',
              ( ['in', 'optional'], vsPaneShowHow, 'How', 0 ),
              ( ['in', 'optional'], VARIANT, 'PointOrCount' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbResult' )),
    COMMETHOD([dispid(51), helpstring(u"Returns the code element at the TextPoint's location."), 'propget'], HRESULT, 'CodeElement',
              ( ['in'], vsCMElement, 'Scope' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeElement)), 'ppResult' )),
    COMMETHOD([dispid(34), helpstring(u'Creates an EditPoint object at the current location and returns it.')], HRESULT, 'CreateEditPoint',
              ( ['retval', 'out'], POINTER(POINTER(EditPoint)), 'lppaReturn' )),
]
################################################################
## code template for TextPoint implementation
##class TextPoint_Impl(object):
##    @property
##    def LineLength(self):
##        u'Returns the number of characters in the current line.'
##        #return lppaReturn
##
##    @property
##    def DisplayColumn(self):
##        u'Returns the display column of the current position.'
##        #return lppaReturn
##
##    def TryToShow(self, How, PointOrCount):
##        u"Tries to make the TextPoint's location visible to the user."
##        #return pbResult
##
##    @property
##    def AbsoluteCharOffset(self):
##        u'Returns the 1-based character index of the current position from the beginning of the document.'
##        #return lppaReturn
##
##    @property
##    def CodeElement(self, Scope):
##        u"Returns the code element at the TextPoint's location."
##        #return ppResult
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppaReturn
##
##    def EqualTo(self, Point):
##        u'Returns whether the called object is equal to the given object.'
##        #return lppaReturn
##
##    @property
##    def AtStartOfLine(self):
##        u'Returns whether the current position is at the beginning of the line.'
##        #return lppaReturn
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def CreateEditPoint(self):
##        u'Creates an EditPoint object at the current location and returns it.'
##        #return lppaReturn
##
##    @property
##    def AtEndOfLine(self):
##        u'Returns whether the current position is at the end of the line.'
##        #return lppaReturn
##
##    def LessThan(self, Point):
##        u'Returns whether the called object is less than the given object.'
##        #return lppaReturn
##
##    def GreaterThan(self, Point):
##        u'Returns whether the called object is greater than the given object.'
##        #return lppaReturn
##
##    @property
##    def AtEndOfDocument(self):
##        u'Returns whether the current position is at the end of the document.'
##        #return lppaReturn
##
##    @property
##    def AtStartOfDocument(self):
##        u'Returns whether the current position is at the beginning of the document.'
##        #return lppaReturn
##
##    @property
##    def Line(self):
##        u'Returns the 1-based index of the current line.'
##        #return lppaReturn
##
##    @property
##    def LineCharOffset(self):
##        u'Returns the 1-based index of the current column.'
##        #return lppaReturn
##

_dispTextEditorEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Occurs when changes in a buffer are committed.')], None, 'LineChanged',
               ( ['in'], POINTER(TextPoint), 'StartPoint' ),
               ( [], POINTER(TextPoint), 'EndPoint' ),
               ( [], c_int, 'Hint' )),
]

# values for enumeration 'VSEXECRESULT'
RESULT_Success = -1
RESULT_Failure = 0
RESULT_Cancel = 1
VSEXECRESULT = c_int # enum

# values for enumeration 'vsext_FontCharSet'
vsext_fontcs_ANSI = 0
vsext_fontcs_DEFAULT = 1
vsext_fontcs_SYMBOL = 2
vsext_fontcs_SHIFTJIS = 128
vsext_fontcs_HANGEUL = 129
vsext_fontcs_GB2312 = 134
vsext_fontcs_CHINESEBIG5 = 136
vsext_fontcs_OEM = 255
vsext_fontcs_JOHAB = 130
vsext_fontcs_HEBREW = 177
vsext_fontcs_ARABIC = 178
vsext_fontcs_GREEK = 161
vsext_fontcs_TURKISH = 162
vsext_fontcs_VIETNAMESE = 163
vsext_fontcs_THAI = 222
vsext_fontcs_EASTEUROPE = 238
vsext_fontcs_RUSSIAN = 204
vsext_fontcs_MAC = 77
vsext_fontcs_BALTIC = 186
vsext_FontCharSet = c_int # enum
SolutionContext._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(SolutionContexts)), 'ppSolutionContexts' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the name of the Project this context will build.'), 'propget'], HRESULT, 'ProjectName',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(4), helpstring(u"Sets/Returns the Project's configuration that will be built."), 'propget'], HRESULT, 'ConfigurationName',
              ( ['retval', 'out'], POINTER(BSTR), 'pConfigurationName' )),
    COMMETHOD([dispid(4), helpstring(u"Sets/Returns the Project's configuration that will be built."), 'propput'], HRESULT, 'ConfigurationName',
              ( ['in'], BSTR, 'pConfigurationName' )),
    COMMETHOD([dispid(5), helpstring(u"Returns the Project's platform that will be built."), 'propget'], HRESULT, 'PlatformName',
              ( ['retval', 'out'], POINTER(BSTR), 'pPlatformName' )),
    COMMETHOD([dispid(6), helpstring(u'Sets/Returns if when the owning SolutionConfiguration is built, if this SolutionContext will also build.'), 'propget'], HRESULT, 'ShouldBuild',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pPlatformName' )),
    COMMETHOD([dispid(6), helpstring(u'Sets/Returns if when the owning SolutionConfiguration is built, if this SolutionContext will also build.'), 'propput'], HRESULT, 'ShouldBuild',
              ( ['in'], VARIANT_BOOL, 'pPlatformName' )),
    COMMETHOD([dispid(7), helpstring(u'Sets/Returns if when the owning SolutionConfiguration is deployed, if this SolutionContext will also deploy.'), 'propget'], HRESULT, 'ShouldDeploy',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pPlatformName' )),
    COMMETHOD([dispid(7), helpstring(u'Sets/Returns if when the owning SolutionConfiguration is deployed, if this SolutionContext will also deploy.'), 'propput'], HRESULT, 'ShouldDeploy',
              ( ['in'], VARIANT_BOOL, 'pPlatformName' )),
]
################################################################
## code template for SolutionContext implementation
##class SolutionContext_Impl(object):
##    def _get(self):
##        u'Sets/Returns if when the owning SolutionConfiguration is deployed, if this SolutionContext will also deploy.'
##        #return pPlatformName
##    def _set(self, pPlatformName):
##        u'Sets/Returns if when the owning SolutionConfiguration is deployed, if this SolutionContext will also deploy.'
##    ShouldDeploy = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ProjectName(self):
##        u'Returns the name of the Project this context will build.'
##        #return pName
##
##    @property
##    def Collection(self):
##        u'Returns the parent object.'
##        #return ppSolutionContexts
##
##    def _get(self):
##        u'Sets/Returns if when the owning SolutionConfiguration is built, if this SolutionContext will also build.'
##        #return pPlatformName
##    def _set(self, pPlatformName):
##        u'Sets/Returns if when the owning SolutionConfiguration is built, if this SolutionContext will also build.'
##    ShouldBuild = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"Sets/Returns the Project's configuration that will be built."
##        #return pConfigurationName
##    def _set(self, pConfigurationName):
##        u"Sets/Returns the Project's configuration that will be built."
##    ConfigurationName = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    @property
##    def PlatformName(self):
##        u"Returns the Project's platform that will be built."
##        #return pPlatformName
##

TextDocument._methods_ = [
    COMMETHOD([dispid(150), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(151), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Document)), 'ppParent' )),
    COMMETHOD([dispid(1), helpstring(u'Returns an object representing the selection on this object.'), 'propget'], HRESULT, 'Selection',
              ( ['retval', 'out'], POINTER(POINTER(TextSelection)), 'ppSel' )),
    COMMETHOD([dispid(122), helpstring(u'Clears all bookmarks in the document.')], HRESULT, 'ClearBookmarks'),
    COMMETHOD([dispid(124), helpstring(u'Creates unnamed bookmarks where the specified pattern is found.')], HRESULT, 'MarkText',
              ( ['in'], BSTR, 'Pattern' ),
              ( ['in', 'optional'], c_int, 'vsFindOptionsValue', 0 ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbRetVal' )),
    COMMETHOD([dispid(128), helpstring(u'Replaces a pattern of text with new text in a document.')], HRESULT, 'ReplacePattern',
              ( ['in'], BSTR, 'Pattern' ),
              ( ['in'], BSTR, 'Replace' ),
              ( ['in', 'optional'], c_int, 'vsFindOptionsValue', 0 ),
              ( ['in', 'out', 'optional'], POINTER(POINTER(TextRanges)), 'Tags', 0 ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbRetVal' )),
    COMMETHOD([dispid(131), helpstring(u'Creates an EditPoint object at the specified location and returns it. The default location is the beginning of the document.')], HRESULT, 'CreateEditPoint',
              ( ['in', 'optional'], POINTER(TextPoint), 'TextPoint', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(EditPoint)), 'lppaReturn' )),
    COMMETHOD([dispid(132), helpstring(u"Returns a TextPoint object representing the beginning of the object's text."), 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'pStartPoint' )),
    COMMETHOD([dispid(133), helpstring(u"Returns a TextPoint object representing the end of the object's text."), 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'pEndPoint' )),
    COMMETHOD([dispid(137), helpstring(u"Returns the name of the document's language."), 'hidden', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(137), helpstring(u"Returns the name of the document's language."), 'hidden', 'propput'], HRESULT, 'Language',
              ( ['in'], BSTR, 'pLanguage' )),
    COMMETHOD([dispid(145), helpstring(u'Returns an enumerated string indicating the object type.'), 'hidden', 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(BSTR), 'pType' )),
    COMMETHOD([dispid(135), helpstring(u'Sets/returns a Long value indicating the width of an indent level in spaces.'), 'hidden', 'propget'], HRESULT, 'IndentSize',
              ( ['retval', 'out'], POINTER(c_int), 'pSize' )),
    COMMETHOD([dispid(140), helpstring(u'Sets/returns value determining tab size in the editor.'), 'hidden', 'propget'], HRESULT, 'TabSize',
              ( ['retval', 'out'], POINTER(c_int), 'pSize' )),
    COMMETHOD([dispid(144), helpstring(u'Replaces a pattern of text with new text in a document.'), 'hidden'], HRESULT, 'ReplaceText',
              ( ['in'], BSTR, 'FindText' ),
              ( ['in'], BSTR, 'ReplaceText' ),
              ( ['in', 'optional'], c_int, 'vsFindOptionsValue', 0 ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbRetVal' )),
    COMMETHOD([dispid(134), helpstring(u'Sends the object to the printer.'), 'hidden'], HRESULT, 'PrintOut'),
]
################################################################
## code template for TextDocument implementation
##class TextDocument_Impl(object):
##    @property
##    def Selection(self):
##        u'Returns an object representing the selection on this object.'
##        #return ppSel
##
##    def _get(self):
##        u"Returns the name of the document's language."
##        #return pLanguage
##    def _set(self, pLanguage):
##        u"Returns the name of the document's language."
##    Language = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppParent
##
##    @property
##    def IndentSize(self):
##        u'Sets/returns a Long value indicating the width of an indent level in spaces.'
##        #return pSize
##
##    @property
##    def Type(self):
##        u'Returns an enumerated string indicating the object type.'
##        #return pType
##
##    def PrintOut(self):
##        u'Sends the object to the printer.'
##        #return 
##
##    def ClearBookmarks(self):
##        u'Clears all bookmarks in the document.'
##        #return 
##
##    def CreateEditPoint(self, TextPoint):
##        u'Creates an EditPoint object at the specified location and returns it. The default location is the beginning of the document.'
##        #return lppaReturn
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    def ReplaceText(self, FindText, ReplaceText, vsFindOptionsValue):
##        u'Replaces a pattern of text with new text in a document.'
##        #return pbRetVal
##
##    @property
##    def EndPoint(self):
##        u"Returns a TextPoint object representing the end of the object's text."
##        #return pEndPoint
##
##    @property
##    def TabSize(self):
##        u'Sets/returns value determining tab size in the editor.'
##        #return pSize
##
##    def ReplacePattern(self, Pattern, Replace, vsFindOptionsValue):
##        u'Replaces a pattern of text with new text in a document.'
##        #return Tags, pbRetVal
##
##    @property
##    def StartPoint(self):
##        u"Returns a TextPoint object representing the beginning of the object's text."
##        #return pStartPoint
##
##    def MarkText(self, Pattern, vsFindOptionsValue):
##        u'Creates unnamed bookmarks where the specified pattern is found.'
##        #return pbRetVal
##

class Projects(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Generic object used to represent projects.'
    _iid_ = GUID('{E3EC0ADD-31B3-461F-8303-8A5E6931257A}')
    _idlflags_ = ['dual', 'oleautomation']
class Properties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Generic object representing property of another object/containing all currently available Property objects.'
    _iid_ = GUID('{4CC8CCF5-A926-4646-B17F-B4940CAED472}')
    _idlflags_ = ['dual', 'oleautomation']
class ConfigurationManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object containing Configuration and Platform objects.'
    _iid_ = GUID('{9043FDA1-345B-4364-900F-BC8598EB8E4F}')
    _idlflags_ = ['dual', 'oleautomation']
class Globals(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object used for storing temporary or persistent data.'
    _iid_ = GUID('{E68A3E0E-B435-4DDE-86B7-F5ADEFC19DF2}')
    _idlflags_ = ['dual', 'oleautomation']
class CodeModel(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object allowing access to programmatic constructs in a source file.'
    _iid_ = GUID('{0CFBC2B4-0D4E-11D3-8997-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation']
Project._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the project.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrName' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the project.'), 'propput'], HRESULT, 'Name',
              ( ['in'], BSTR, 'lpbstrName' )),
    COMMETHOD([dispid(109), helpstring(u'Returns full pathname indicating the location of the project file.'), 'hidden', 'propget'], HRESULT, 'FileName',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
    COMMETHOD([dispid(110), helpstring(u'Returns value indicating whether object was changed since the last time it was saved.'), 'hidden', 'propget'], HRESULT, 'IsDirty',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lpfReturn' )),
    COMMETHOD([dispid(110), helpstring(u'Returns value indicating whether object was changed since the last time it was saved.'), 'hidden', 'propput'], HRESULT, 'IsDirty',
              ( ['in'], VARIANT_BOOL, 'lpfReturn' )),
    COMMETHOD([dispid(123), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(Projects)), 'lppaReturn' )),
    COMMETHOD([dispid(127), helpstring(u'Saves the project.')], HRESULT, 'SaveAs',
              ( ['in'], BSTR, 'NewFileName' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(201), helpstring(u'Returns a GUID String indicating the kind or type of the object.'), 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrFileName' )),
    COMMETHOD([dispid(202), helpstring(u'Returns a ProjectItems collection for the object.'), 'propget'], HRESULT, 'ProjectItems',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItems)), 'lppcReturn' )),
    COMMETHOD([dispid(203), helpstring(u'Returns the Properties collection.'), 'propget'], HRESULT, 'Properties',
              ( ['retval', 'out'], POINTER(POINTER(Properties)), 'ppObject' )),
    COMMETHOD([dispid(204), helpstring(u'Returns name of project as relative pathname from directory containing solution file leading to project file.'), 'propget'], HRESULT, 'UniqueName',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrFileName' )),
    COMMETHOD([dispid(205), helpstring(u'Returns an interface or object that can be accessed at run time by name.'), 'propget'], HRESULT, 'Object',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ProjectModel' )),
    COMMETHOD([dispid(206), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(207), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(208), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(209), helpstring(u'Returns full pathname indicating the location of the project file.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
    COMMETHOD([dispid(210), helpstring(u'Returns value indicating whether object was changed since the last time it was saved.'), 'propget'], HRESULT, 'Saved',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lpfReturn' )),
    COMMETHOD([dispid(210), helpstring(u'Returns value indicating whether object was changed since the last time it was saved.'), 'propput'], HRESULT, 'Saved',
              ( ['in'], VARIANT_BOOL, 'lpfReturn' )),
    COMMETHOD([dispid(213), helpstring(u'Returns the ConfigurationManager object for this item.'), 'propget'], HRESULT, 'ConfigurationManager',
              ( ['retval', 'out'], POINTER(POINTER(ConfigurationManager)), 'ppConfigurationManager' )),
    COMMETHOD([dispid(214), helpstring(u'Returns the Globals object for storing persistent data.'), 'propget'], HRESULT, 'Globals',
              ( ['retval', 'out'], POINTER(POINTER(Globals)), 'ppGlobals' )),
    COMMETHOD([dispid(215), helpstring(u"Causes the project to persist it's self to storage.")], HRESULT, 'Save',
              ( ['optional'], BSTR, 'FileName', u'' )),
    COMMETHOD([dispid(216), helpstring(u'Returns the ProjectItem object for the nested project in the host project.'), 'propget'], HRESULT, 'ParentProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'ppParentProjectItem' )),
    COMMETHOD([dispid(217), helpstring(u'Returns the CodeModel, if available, for this project.'), 'propget'], HRESULT, 'CodeModel',
              ( ['retval', 'out'], POINTER(POINTER(CodeModel)), 'ppCodeModel' )),
    COMMETHOD([dispid(218), helpstring(u'Removes the project from storage.')], HRESULT, 'Delete'),
]
################################################################
## code template for Project implementation
##class Project_Impl(object):
##    @property
##    def ConfigurationManager(self):
##        u'Returns the ConfigurationManager object for this item.'
##        #return ppConfigurationManager
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def FileName(self):
##        u'Returns full pathname indicating the location of the project file.'
##        #return lpbstrReturn
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def Save(self, FileName):
##        u"Causes the project to persist it's self to storage."
##        #return 
##
##    @property
##    def ParentProjectItem(self):
##        u'Returns the ProjectItem object for the nested project in the host project.'
##        #return ppParentProjectItem
##
##    @property
##    def Object(self):
##        u'Returns an interface or object that can be accessed at run time by name.'
##        #return ProjectModel
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return lppaReturn
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    @property
##    def Properties(self):
##        u'Returns the Properties collection.'
##        #return ppObject
##
##    @property
##    def Kind(self):
##        u'Returns a GUID String indicating the kind or type of the object.'
##        #return lpbstrFileName
##
##    def _get(self):
##        u'Sets/returns the name of the project.'
##        #return lpbstrName
##    def _set(self, lpbstrName):
##        u'Sets/returns the name of the project.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ProjectItems(self):
##        u'Returns a ProjectItems collection for the object.'
##        #return lppcReturn
##
##    @property
##    def CodeModel(self):
##        u'Returns the CodeModel, if available, for this project.'
##        #return ppCodeModel
##
##    def Delete(self):
##        u'Removes the project from storage.'
##        #return 
##
##    def SaveAs(self, NewFileName):
##        u'Saves the project.'
##        #return 
##
##    def _get(self):
##        u'Returns value indicating whether object was changed since the last time it was saved.'
##        #return lpfReturn
##    def _set(self, lpfReturn):
##        u'Returns value indicating whether object was changed since the last time it was saved.'
##    IsDirty = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Globals(self):
##        u'Returns the Globals object for storing persistent data.'
##        #return ppGlobals
##
##    @property
##    def UniqueName(self):
##        u'Returns name of project as relative pathname from directory containing solution file leading to project file.'
##        #return lpbstrFileName
##
##    @property
##    def FullName(self):
##        u'Returns full pathname indicating the location of the project file.'
##        #return lpbstrReturn
##
##    def _get(self):
##        u'Returns value indicating whether object was changed since the last time it was saved.'
##        #return lpfReturn
##    def _set(self, lpfReturn):
##        u'Returns value indicating whether object was changed since the last time it was saved.'
##    Saved = property(_get, _set, doc = _set.__doc__)
##

class _DebuggerEventsRoot(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{D4BB39FB-0F0E-11D3-B880-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_DebuggerEventsRoot._methods_ = [
    COMMETHOD([dispid(1), 'hidden', 'propget'], HRESULT, 'DebuggerEvents',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'disp' )),
]
################################################################
## code template for _DebuggerEventsRoot implementation
##class _DebuggerEventsRoot_Impl(object):
##    @property
##    def DebuggerEvents(self):
##        '-no docstring-'
##        #return disp
##

ToolBoxItem._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(ToolBoxItems)), 'pToolBoxItems' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(3), helpstring(u'Removes an object from a collection.')], HRESULT, 'Delete'),
    COMMETHOD([dispid(4), helpstring(u'Causes this item to become active in the user interface.')], HRESULT, 'Select'),
]
################################################################
## code template for ToolBoxItem implementation
##class ToolBoxItem_Impl(object):
##    def Select(self):
##        u'Causes this item to become active in the user interface.'
##        #return 
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return Name
##    def _set(self, Name):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return pToolBoxItems
##
##    def Delete(self):
##        u'Removes an object from a collection.'
##        #return 
##

class Configuration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Defines a configuration, or build settings, within a platform.'
    _iid_ = GUID('{90813589-FE21-4AA4-A2E5-053FD274E980}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsConfigurationType'
vsConfigurationTypeProject = 1
vsConfigurationTypeProjectItem = 2
vsConfigurationType = c_int # enum
class OutputGroups(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Collection of OutputGroup objects.'
    _iid_ = GUID('{F9FA748E-E302-44CF-891B-E263189D585E}')
    _idlflags_ = ['dual', 'oleautomation']
Configuration._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(ConfigurationManager)), 'ppConfigurationManager' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the name of this configuration.'), 'propget'], HRESULT, 'ConfigurationName',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the name of the platform supported by this assignment.'), 'propget'], HRESULT, 'PlatformName',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object type.'), 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(vsConfigurationType), 'pType' )),
    COMMETHOD([dispid(6), helpstring(u'Returns the owning object for this Configuration.'), 'propget'], HRESULT, 'Owner',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppOwner' )),
    COMMETHOD([dispid(7), helpstring(u'Returns the Properties collection.'), 'propget'], HRESULT, 'Properties',
              ( ['retval', 'out'], POINTER(POINTER(Properties)), 'ppProperties' )),
    COMMETHOD([dispid(8), helpstring(u'Returns if the configuration can be built.'), 'propget'], HRESULT, 'IsBuildable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pBuildable' )),
    COMMETHOD([dispid(9), helpstring(u'Returns if a Configuration can be set into run mode.'), 'propget'], HRESULT, 'IsRunable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pRunable' )),
    COMMETHOD([dispid(10), helpstring(u'Returns if the configuration can be debugged.'), 'propget'], HRESULT, 'IsDeployable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pDeployable' )),
    COMMETHOD([dispid(11), helpstring(u'Returns an interface or object that can be accessed at run time by name.'), 'propget'], HRESULT, 'Object',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppDisp' )),
    COMMETHOD([dispid(12), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(13), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns an object for discovering the files built by this configuration.'), 'propget'], HRESULT, 'OutputGroups',
              ( ['retval', 'out'], POINTER(POINTER(OutputGroups)), 'ppOutputGroups' )),
]
################################################################
## code template for Configuration implementation
##class Configuration_Impl(object):
##    @property
##    def IsDeployable(self):
##        u'Returns if the configuration can be debugged.'
##        #return pDeployable
##
##    @property
##    def Object(self):
##        u'Returns an interface or object that can be accessed at run time by name.'
##        #return ppDisp
##
##    @property
##    def PlatformName(self):
##        u'Returns the name of the platform supported by this assignment.'
##        #return pName
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def IsBuildable(self):
##        u'Returns if the configuration can be built.'
##        #return pBuildable
##
##    @property
##    def OutputGroups(self):
##        u'Returns an object for discovering the files built by this configuration.'
##        #return ppOutputGroups
##
##    @property
##    def Collection(self):
##        u'Returns the parent object.'
##        #return ppConfigurationManager
##
##    @property
##    def ConfigurationName(self):
##        u'Returns the name of this configuration.'
##        #return pName
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    @property
##    def IsRunable(self):
##        u'Returns if a Configuration can be set into run mode.'
##        #return pRunable
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    @property
##    def Owner(self):
##        u'Returns the owning object for this Configuration.'
##        #return ppOwner
##
##    @property
##    def Type(self):
##        u'Returns an enumeration indicating the object type.'
##        #return pType
##
##    @property
##    def Properties(self):
##        u'Returns the Properties collection.'
##        #return ppProperties
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##


# values for enumeration 'vsFindPatternSyntax'
vsFindPatternSyntaxLiteral = 0
vsFindPatternSyntaxRegExpr = 1
vsFindPatternSyntaxWildcards = 2
vsFindPatternSyntax = c_int # enum
CodeClass._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ParentObject' )),
    COMMETHOD([dispid(32), helpstring(u'Returns an object defining the parent namespace.'), 'nonbrowsable', 'propget'], HRESULT, 'Namespace',
              ( ['retval', 'out'], POINTER(POINTER(CodeNamespace)), 'ppCodeNamespace' )),
    COMMETHOD([dispid(33), helpstring(u'Returns a collection of classes this item derives from.'), 'nonbrowsable', 'propget'], HRESULT, 'Bases',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(34), helpstring(u'Returns a collection of items contained by this element.'), 'nonbrowsable', 'propget'], HRESULT, 'Members',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(35), helpstring(u'Defines the access attributes of this item.'), 'propput'], HRESULT, 'Access',
              ( [], vsCMAccess, 'pAccess' )),
    COMMETHOD([dispid(35), helpstring(u'Defines the access attributes of this item.'), 'propget'], HRESULT, 'Access',
              ( ['retval', 'out'], POINTER(vsCMAccess), 'pAccess' )),
    COMMETHOD([dispid(36), helpstring(u'Returns a collection of items containing attributes.'), 'nonbrowsable', 'propget'], HRESULT, 'Attributes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(37), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propget'], HRESULT, 'DocComment',
              ( ['retval', 'out'], POINTER(BSTR), 'pDocComment' )),
    COMMETHOD([dispid(37), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propput'], HRESULT, 'DocComment',
              ( [], BSTR, 'pDocComment' )),
    COMMETHOD([dispid(38), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Comment',
              ( ['retval', 'out'], POINTER(BSTR), 'pComment' )),
    COMMETHOD([dispid(38), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propput'], HRESULT, 'Comment',
              ( [], BSTR, 'pComment' )),
    COMMETHOD([dispid(39), helpstring(u'Adds an item to the list of inherited objects.')], HRESULT, 'AddBase',
              ( [], VARIANT, 'Base' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeElement)), 'ppOut' )),
    COMMETHOD([dispid(40), helpstring(u'Creates a new attribute code construct and inserts the code in the correct location.')], HRESULT, 'AddAttribute',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeAttribute)), 'ppCodeAttribute' )),
    COMMETHOD([dispid(41), helpstring(u'Removes an object from the list of bases.')], HRESULT, 'RemoveBase',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(42), helpstring(u'Removes a member code construct.')], HRESULT, 'RemoveMember',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(43), helpstring(u'Returns a Boolean telling if an object has another object as a base.'), 'propget'], HRESULT, 'IsDerivedFrom',
              ( [], BSTR, 'FullName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(44), helpstring(u'Returns a collection of objects derived from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'DerivedTypes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(61), helpstring(u'Returns a collection of interfaces implemented by this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ImplementedInterfaces',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(62), helpstring(u'Sets/Returns if the item is declared abstract or not.'), 'propget'], HRESULT, 'IsAbstract',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsAbstract' )),
    COMMETHOD([dispid(62), helpstring(u'Sets/Returns if the item is declared abstract or not.'), 'propput'], HRESULT, 'IsAbstract',
              ( [], VARIANT_BOOL, 'pIsAbstract' )),
    COMMETHOD([dispid(63), helpstring(u'Adds an interface to the list of inherited objects.')], HRESULT, 'AddImplementedInterface',
              ( [], VARIANT, 'Base' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeInterface)), 'ppCodeInterface' )),
    COMMETHOD([dispid(64), helpstring(u'Creates a new function code construct and inserts the code in the correct location.')], HRESULT, 'AddFunction',
              ( [], BSTR, 'Name' ),
              ( [], vsCMFunction, 'Kind' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['optional'], VARIANT, 'Location' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeFunction)), 'ppCodeFunction' )),
    COMMETHOD([dispid(65), helpstring(u'Creates a new variable code construct and inserts the code in the correct location.')], HRESULT, 'AddVariable',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['optional'], VARIANT, 'Location' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeVariable)), 'ppCodeVariable' )),
    COMMETHOD([dispid(66), helpstring(u'Creates a new property code construct and inserts the code in the correct location.')], HRESULT, 'AddProperty',
              ( [], BSTR, 'GetterName' ),
              ( [], BSTR, 'PutterName' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['optional'], VARIANT, 'Location' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeProperty)), 'ppCodeProperty' )),
    COMMETHOD([dispid(67), helpstring(u'Creates a new class code construct and inserts the code in the correct location.')], HRESULT, 'AddClass',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], VARIANT, 'ImplementedInterfaces' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeClass)), 'ppCodeClass' )),
    COMMETHOD([dispid(68), helpstring(u'Creates a new structure code construct and inserts the code in the correct location.')], HRESULT, 'AddStruct',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], VARIANT, 'ImplementedInterfaces' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeStruct)), 'ppCodeStruct' )),
    COMMETHOD([dispid(69), helpstring(u'Creates a new enumeration code construct and inserts the code in the correct location.')], HRESULT, 'AddEnum',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeEnum)), 'ppCodeEnum' )),
    COMMETHOD([dispid(70), helpstring(u'Creates a new delegate code construct and inserts the code in the correct location.')], HRESULT, 'AddDelegate',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeDelegate)), 'ppCodeDelegate' )),
    COMMETHOD([dispid(71), helpstring(u'Removes an interface from the list of implemented interfaces.')], HRESULT, 'RemoveInterface',
              ( [], VARIANT, 'Element' )),
]
################################################################
## code template for CodeClass implementation
##class CodeClass_Impl(object):
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    def AddProperty(self, GetterName, PutterName, Type, Position, Access, Location):
##        u'Creates a new property code construct and inserts the code in the correct location.'
##        #return ppCodeProperty
##
##    def AddStruct(self, Name, Position, Bases, ImplementedInterfaces, Access):
##        u'Creates a new structure code construct and inserts the code in the correct location.'
##        #return ppCodeStruct
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def Namespace(self):
##        u'Returns an object defining the parent namespace.'
##        #return ppCodeNamespace
##
##    def AddBase(self, Base, Position):
##        u'Adds an item to the list of inherited objects.'
##        #return ppOut
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    def _get(self):
##        u'Defines the access attributes of this item.'
##        #return pAccess
##    def _set(self, pAccess):
##        u'Defines the access attributes of this item.'
##    Access = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Bases(self):
##        u'Returns a collection of classes this item derives from.'
##        #return ppCodeElements
##
##    def AddEnum(self, Name, Position, Bases, Access):
##        u'Creates a new enumeration code construct and inserts the code in the correct location.'
##        #return ppCodeEnum
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##
##    def _get(self):
##        u'Sets/Returns if the item is declared abstract or not.'
##        #return pIsAbstract
##    def _set(self, pIsAbstract):
##        u'Sets/Returns if the item is declared abstract or not.'
##    IsAbstract = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def ImplementedInterfaces(self):
##        u'Returns a collection of interfaces implemented by this object.'
##        #return ppCodeElements
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ParentObject
##
##    def AddImplementedInterface(self, Base, Position):
##        u'Adds an interface to the list of inherited objects.'
##        #return ppCodeInterface
##
##    def AddFunction(self, Name, Kind, Type, Position, Access, Location):
##        u'Creates a new function code construct and inserts the code in the correct location.'
##        #return ppCodeFunction
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    def AddAttribute(self, Name, Value, Position):
##        u'Creates a new attribute code construct and inserts the code in the correct location.'
##        #return ppCodeAttribute
##
##    def RemoveMember(self, Element):
##        u'Removes a member code construct.'
##        #return 
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def Members(self):
##        u'Returns a collection of items contained by this element.'
##        #return ppCodeElements
##
##    def AddDelegate(self, Name, Type, Position, Access):
##        u'Creates a new delegate code construct and inserts the code in the correct location.'
##        #return ppCodeDelegate
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def _get(self):
##        u'Returns the document comment on the current code model element.'
##        #return pDocComment
##    def _set(self, pDocComment):
##        u'Returns the document comment on the current code model element.'
##    DocComment = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveInterface(self, Element):
##        u'Removes an interface from the list of implemented interfaces.'
##        #return 
##
##    def RemoveBase(self, Element):
##        u'Removes an object from the list of bases.'
##        #return 
##
##    @property
##    def Attributes(self):
##        u'Returns a collection of items containing attributes.'
##        #return ppCodeElements
##
##    def AddClass(self, Name, Position, Bases, ImplementedInterfaces, Access):
##        u'Creates a new class code construct and inserts the code in the correct location.'
##        #return ppCodeClass
##
##    def _get(self):
##        u'Sets/Returns an object defining the comment for this object.'
##        #return pComment
##    def _set(self, pComment):
##        u'Sets/Returns an object defining the comment for this object.'
##    Comment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsDerivedFrom(self, FullName):
##        u'Returns a Boolean telling if an object has another object as a base.'
##        #return pVal
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    def AddVariable(self, Name, Type, Position, Access, Location):
##        u'Creates a new variable code construct and inserts the code in the correct location.'
##        #return ppCodeVariable
##
##    @property
##    def DerivedTypes(self):
##        u'Returns a collection of objects derived from this object.'
##        #return ppCodeElements
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##

vs_exec_Result = VSEXECRESULT
class IVsGlobalsCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{E2CC506A-588B-4F65-A1F0-2244C060ABCB}')
    _idlflags_ = ['hidden', 'restricted']
IVsGlobalsCallback._methods_ = [
    COMMETHOD([], HRESULT, 'WriteVariablesToData',
              ( ['in'], WSTRING, 'pVariableName' ),
              ( ['in'], POINTER(VARIANT), 'varData' )),
    COMMETHOD([], HRESULT, 'ReadData',
              ( ['in'], POINTER(Globals), 'pGlobals' )),
    COMMETHOD([], HRESULT, 'ClearVariables'),
    COMMETHOD([], HRESULT, 'VariableChanged'),
    COMMETHOD([], HRESULT, 'CanModifySource'),
    COMMETHOD([], HRESULT, 'GetParent',
              ( [], POINTER(POINTER(IDispatch)), 'ppOut' )),
]
################################################################
## code template for IVsGlobalsCallback implementation
##class IVsGlobalsCallback_Impl(object):
##    def ClearVariables(self):
##        '-no docstring-'
##        #return 
##
##    def GetParent(self, ppOut):
##        '-no docstring-'
##        #return 
##
##    def WriteVariablesToData(self, pVariableName, varData):
##        '-no docstring-'
##        #return 
##
##    def ReadData(self, pGlobals):
##        '-no docstring-'
##        #return 
##
##    def CanModifySource(self):
##        '-no docstring-'
##        #return 
##
##    def VariableChanged(self):
##        '-no docstring-'
##        #return 
##

class Configurations(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of Configuration objects.'
    _iid_ = GUID('{B6B4C8D6-4D27-43B9-B45C-52BD16B6BA38}')
    _idlflags_ = ['dual', 'oleautomation']
ConfigurationManager._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppParent' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['optional'], BSTR, 'Platform', u'' ),
              ( ['retval', 'out'], POINTER(POINTER(Configuration)), 'ppOut' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([dispid(4), helpstring(u"Returns a collection of items representing a build configuration and it's platforms.")], HRESULT, 'ConfigurationRow',
              ( [], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(Configurations)), 'ppOut' )),
    COMMETHOD([dispid(5), helpstring(u"Creates an item representing a build configuration and it's platforms.")], HRESULT, 'AddConfigurationRow',
              ( [], BSTR, 'NewName' ),
              ( [], BSTR, 'ExistingName' ),
              ( ['in'], VARIANT_BOOL, 'Propagate' ),
              ( ['retval', 'out'], POINTER(POINTER(Configurations)), 'ppOut' )),
    COMMETHOD([dispid(6), helpstring(u"Deletes an item representing a build configuration and it's platforms.")], HRESULT, 'DeleteConfigurationRow',
              ( [], BSTR, 'Name' )),
    COMMETHOD([dispid(7), helpstring(u'Returns an array of names of configurations.'), 'propget'], HRESULT, 'ConfigurationRowNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'pNames' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of ConfigurationAssignment object for the specified platform.')], HRESULT, 'Platform',
              ( [], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(Configurations)), 'ppOut' )),
    COMMETHOD([dispid(9), helpstring(u'Creates a new platform based off an existing platform.')], HRESULT, 'AddPlatform',
              ( [], BSTR, 'NewName' ),
              ( [], BSTR, 'ExistingName' ),
              ( ['in'], VARIANT_BOOL, 'Propagate' ),
              ( ['retval', 'out'], POINTER(POINTER(Configurations)), 'ppOut' )),
    COMMETHOD([dispid(10), helpstring(u'Removes a unneeded platform.')], HRESULT, 'DeletePlatform',
              ( [], BSTR, 'Name' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a list of all available platforms.'), 'propget'], HRESULT, 'PlatformNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'pNames' )),
    COMMETHOD([dispid(12), helpstring(u'Returns a list of all platforms currently available for this particular project.'), 'propget'], HRESULT, 'SupportedPlatforms',
              ( ['retval', 'out'], POINTER(VARIANT), 'pPlatforms' )),
    COMMETHOD([dispid(13), helpstring(u'Returns the currently active configuration.'), 'propget'], HRESULT, 'ActiveConfiguration',
              ( ['retval', 'out'], POINTER(POINTER(Configuration)), 'ppOut' )),
]
################################################################
## code template for ConfigurationManager implementation
##class ConfigurationManager_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    @property
##    def ActiveConfiguration(self):
##        u'Returns the currently active configuration.'
##        #return ppOut
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    def DeleteConfigurationRow(self, Name):
##        u"Deletes an item representing a build configuration and it's platforms."
##        #return 
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppParent
##
##    def Platform(self, Name):
##        u'Returns a collection of ConfigurationAssignment object for the specified platform.'
##        #return ppOut
##
##    def AddConfigurationRow(self, NewName, ExistingName, Propagate):
##        u"Creates an item representing a build configuration and it's platforms."
##        #return ppOut
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    def AddPlatform(self, NewName, ExistingName, Propagate):
##        u'Creates a new platform based off an existing platform.'
##        #return ppOut
##
##    def Item(self, index, Platform):
##        u'Returns an indexed member of a collection.'
##        #return ppOut
##
##    def DeletePlatform(self, Name):
##        u'Removes a unneeded platform.'
##        #return 
##
##    @property
##    def PlatformNames(self):
##        u'Returns a list of all available platforms.'
##        #return pNames
##
##    @property
##    def SupportedPlatforms(self):
##        u'Returns a list of all platforms currently available for this particular project.'
##        #return pPlatforms
##
##    def ConfigurationRow(self, Name):
##        u"Returns a collection of items representing a build configuration and it's platforms."
##        #return ppOut
##
##    @property
##    def ConfigurationRowNames(self):
##        u'Returns an array of names of configurations.'
##        #return pNames
##

ToolBox._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'pParent' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the currently active item in the collection.'), 'propget'], HRESULT, 'ActiveTab',
              ( ['retval', 'out'], POINTER(POINTER(ToolBoxTab)), 'pToolBoxTab' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the collection of Tabs on the tool box.'), 'propget'], HRESULT, 'ToolBoxTabs',
              ( ['retval', 'out'], POINTER(POINTER(ToolBoxTabs)), 'pToolBoxTabs' )),
]
################################################################
## code template for ToolBox implementation
##class ToolBox_Impl(object):
##    @property
##    def ToolBoxTabs(self):
##        u'Returns the collection of Tabs on the tool box.'
##        #return pToolBoxTabs
##
##    @property
##    def ActiveTab(self):
##        u'Returns the currently active item in the collection.'
##        #return pToolBoxTab
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return pParent
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##

class IVsTextEditGeneral(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{2E1BFD1C-5B26-4ACA-B97B-ED9D261BA3E7}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
IVsTextEditGeneral._methods_ = [
    COMMETHOD([dispid(1), 'propput'], HRESULT, 'SelectionMargin',
              ( ['in'], VARIANT_BOOL, 'pfSelectionMargin' )),
    COMMETHOD([dispid(1), 'propget'], HRESULT, 'SelectionMargin',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfSelectionMargin' )),
    COMMETHOD([dispid(2), 'propput'], HRESULT, 'GoToAnchorAfterEscape',
              ( ['in'], VARIANT_BOOL, 'pfGoToAnchorAfterEscape' )),
    COMMETHOD([dispid(2), 'propget'], HRESULT, 'GoToAnchorAfterEscape',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfGoToAnchorAfterEscape' )),
    COMMETHOD([dispid(3), 'propput'], HRESULT, 'DragNDropTextEditing',
              ( ['in'], VARIANT_BOOL, 'pfDragNDropTextEditing' )),
    COMMETHOD([dispid(3), 'propget'], HRESULT, 'DragNDropTextEditing',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfDragNDropTextEditing' )),
    COMMETHOD([dispid(4), 'propput'], HRESULT, 'UndoCaretActions',
              ( ['in'], VARIANT_BOOL, 'pfUndoCaretActions' )),
    COMMETHOD([dispid(4), 'propget'], HRESULT, 'UndoCaretActions',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfUndoCaretActions' )),
    COMMETHOD([dispid(5), 'propput'], HRESULT, 'MarginIndicatorBar',
              ( ['in'], VARIANT_BOOL, 'pfMarginIndicatorBar' )),
    COMMETHOD([dispid(5), 'propget'], HRESULT, 'MarginIndicatorBar',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfMarginIndicatorBar' )),
    COMMETHOD([dispid(6), 'propput'], HRESULT, 'HorizontalScrollBar',
              ( ['in'], VARIANT_BOOL, 'pfHorizontalScrollBar' )),
    COMMETHOD([dispid(6), 'propget'], HRESULT, 'HorizontalScrollBar',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfHorizontalScrollBar' )),
    COMMETHOD([dispid(7), 'propput'], HRESULT, 'VerticalScrollBar',
              ( ['in'], VARIANT_BOOL, 'pfVerticalScrollBar' )),
    COMMETHOD([dispid(7), 'propget'], HRESULT, 'VerticalScrollBar',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfVerticalScrollBar' )),
    COMMETHOD([dispid(8), 'propput'], HRESULT, 'AutoDelimiterHighlighting',
              ( ['in'], VARIANT_BOOL, 'pfHighlighting' )),
    COMMETHOD([dispid(8), 'propget'], HRESULT, 'AutoDelimiterHighlighting',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfHighlighting' )),
]
################################################################
## code template for IVsTextEditGeneral implementation
##class IVsTextEditGeneral_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return pfHighlighting
##    def _set(self, pfHighlighting):
##        '-no docstring-'
##    AutoDelimiterHighlighting = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfMarginIndicatorBar
##    def _set(self, pfMarginIndicatorBar):
##        '-no docstring-'
##    MarginIndicatorBar = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfUndoCaretActions
##    def _set(self, pfUndoCaretActions):
##        '-no docstring-'
##    UndoCaretActions = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfDragNDropTextEditing
##    def _set(self, pfDragNDropTextEditing):
##        '-no docstring-'
##    DragNDropTextEditing = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfGoToAnchorAfterEscape
##    def _set(self, pfGoToAnchorAfterEscape):
##        '-no docstring-'
##    GoToAnchorAfterEscape = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfVerticalScrollBar
##    def _set(self, pfVerticalScrollBar):
##        '-no docstring-'
##    VerticalScrollBar = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfSelectionMargin
##    def _set(self, pfSelectionMargin):
##        '-no docstring-'
##    SelectionMargin = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfHorizontalScrollBar
##    def _set(self, pfHorizontalScrollBar):
##        '-no docstring-'
##    HorizontalScrollBar = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'vsCMPrototype'
vsCMPrototypeFullname = 1
vsCMPrototypeNoName = 2
vsCMPrototypeClassName = 4
vsCMPrototypeParamTypes = 8
vsCMPrototypeParamNames = 16
vsCMPrototypeParamDefaultValues = 32
vsCMPrototypeUniqueSignature = 64
vsCMPrototypeType = 128
vsCMPrototypeInitExpression = 256
vsCMPrototype = c_int # enum

# values for enumeration 'vsext_DisplayMode'
vsext_dm_SDI = 0
vsext_dm_MDI = 1
vsext_DisplayMode = c_int # enum

# values for enumeration 'vsFindResultsLocation'
vsFindResultsNone = 0
vsFindResults1 = 1
vsFindResults2 = 2
vsFindResultsLocation = c_int # enum
vsCMLanguageVC = u'{B5E9BD32-6D3E-4B5D-925E-8A43B79820B4}' # Constant STRING
vsCMLanguageVB = u'{B5E9BD33-6D3E-4B5D-925E-8A43B79820B4}' # Constant STRING
vsCMLanguageCSharp = u'{B5E9BD34-6D3E-4B5D-925E-8A43B79820B4}' # Constant STRING
vsCMLanguageIDL = u'{B5E9BD35-6D3E-4B5D-925E-8A43B79820B4}' # Constant STRING
TaskList._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'lppReturn' )),
    COMMETHOD([dispid(3), 'propget'], HRESULT, 'DefaultCommentToken',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrToken' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the TaskListItems Collection.'), 'propget'], HRESULT, 'TaskItems',
              ( ['retval', 'out'], POINTER(POINTER(TaskItems)), 'pTaskItems' )),
    COMMETHOD([dispid(6), helpstring(u'Returns the currently active item in the collection.'), 'propget'], HRESULT, 'SelectedItems',
              ( ['retval', 'out'], POINTER(VARIANT), 'Selections' )),
]
################################################################
## code template for TaskList implementation
##class TaskList_Impl(object):
##    @property
##    def SelectedItems(self):
##        u'Returns the currently active item in the collection.'
##        #return Selections
##
##    @property
##    def DefaultCommentToken(self):
##        '-no docstring-'
##        #return pbstrToken
##
##    @property
##    def TaskItems(self):
##        u'Returns the TaskListItems Collection.'
##        #return pTaskItems
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppReturn
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppReturn
##

vsCMLanguageMC = u'{B5E9BD36-6D3E-4B5D-925E-8A43B79820B4}' # Constant STRING
class _DocumentEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{DC5437F5-F114-11D2-AACF-00C04F688DDE}')
    _idlflags_ = ['oleautomation']
_DocumentEvents._methods_ = [
]
################################################################
## code template for _DocumentEvents implementation
##class _DocumentEvents_Impl(object):

class _EnvironmentDocuments(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{76ED1C48-ED86-4E9E-ACF8-A40E765DAF25}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_EnvironmentDocuments._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'If a document window is saved, allows re-using that window when a new document is opened.'), 'propput'], HRESULT, 'ReuseSavedActiveDocWindow',
              ( [], VARIANT_BOOL, 'pReuse' )),
    COMMETHOD([dispid(1), helpstring(u'If a document window is saved, allows re-using that window when a new document is opened.'), 'propget'], HRESULT, 'ReuseSavedActiveDocWindow',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pReuse' )),
    COMMETHOD([dispid(2), helpstring(u'Sets/ returns value controlling whether IDE automatically reloads open files if it detects that they have changed on disk outside the IDE.'), 'propput'], HRESULT, 'DetectFileChangesOutsideIDE',
              ( ['in'], VARIANT_BOOL, 'pfAutoRead' )),
    COMMETHOD([dispid(2), helpstring(u'Sets/ returns value controlling whether IDE automatically reloads open files if it detects that they have changed on disk outside the IDE.'), 'propget'], HRESULT, 'DetectFileChangesOutsideIDE',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfAutoRead' )),
    COMMETHOD([dispid(3), 'propput'], HRESULT, 'AutoloadExternalChanges',
              ( ['in'], VARIANT_BOOL, 'pfAutoload' )),
    COMMETHOD([dispid(3), 'propget'], HRESULT, 'AutoloadExternalChanges',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfAutoload' )),
    COMMETHOD([dispid(4), 'propput'], HRESULT, 'InitializeOpenFileFromCurrentDocument',
              ( ['in'], VARIANT_BOOL, 'pfInit' )),
    COMMETHOD([dispid(4), 'propget'], HRESULT, 'InitializeOpenFileFromCurrentDocument',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfInit' )),
    COMMETHOD([dispid(5), helpstring(u'Sets/returns value indicating number of files stored in Miscellaneous Files Project.'), 'propput'], HRESULT, 'MiscFilesProjectSavesLastNItems',
              ( ['in'], c_int, 'plCount' )),
    COMMETHOD([dispid(5), helpstring(u'Sets/returns value indicating number of files stored in Miscellaneous Files Project.'), 'propget'], HRESULT, 'MiscFilesProjectSavesLastNItems',
              ( ['retval', 'out'], POINTER(c_int), 'plCount' )),
    COMMETHOD([dispid(6), helpstring(u'Gets/Sets if a message box should be stopped from displaying while doing a search/replace.'), 'propget'], HRESULT, 'FindReplaceShowMessageBoxes',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShow' )),
    COMMETHOD([dispid(6), helpstring(u'Gets/Sets if a message box should be stopped from displaying while doing a search/replace.'), 'propput'], HRESULT, 'FindReplaceShowMessageBoxes',
              ( [], VARIANT_BOOL, 'pShow' )),
    COMMETHOD([dispid(7), helpstring(u'Gets/Sets if a search/replace operation should be seeded from text selected in the editor.'), 'propget'], HRESULT, 'FindReplaceInitializeFromEditor',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShow' )),
    COMMETHOD([dispid(7), helpstring(u'Gets/Sets if a search/replace operation should be seeded from text selected in the editor.'), 'propput'], HRESULT, 'FindReplaceInitializeFromEditor',
              ( [], VARIANT_BOOL, 'pShow' )),
]
################################################################
## code template for _EnvironmentDocuments implementation
##class _EnvironmentDocuments_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return pfAutoload
##    def _set(self, pfAutoload):
##        '-no docstring-'
##    AutoloadExternalChanges = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Sets/ returns value controlling whether IDE automatically reloads open files if it detects that they have changed on disk outside the IDE.'
##        #return pfAutoRead
##    def _set(self, pfAutoRead):
##        u'Sets/ returns value controlling whether IDE automatically reloads open files if it detects that they have changed on disk outside the IDE.'
##    DetectFileChangesOutsideIDE = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets if a message box should be stopped from displaying while doing a search/replace.'
##        #return pShow
##    def _set(self, pShow):
##        u'Gets/Sets if a message box should be stopped from displaying while doing a search/replace.'
##    FindReplaceShowMessageBoxes = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'If a document window is saved, allows re-using that window when a new document is opened.'
##        #return pReuse
##    def _set(self, pReuse):
##        u'If a document window is saved, allows re-using that window when a new document is opened.'
##    ReuseSavedActiveDocWindow = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Sets/returns value indicating number of files stored in Miscellaneous Files Project.'
##        #return plCount
##    def _set(self, plCount):
##        u'Sets/returns value indicating number of files stored in Miscellaneous Files Project.'
##    MiscFilesProjectSavesLastNItems = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets if a search/replace operation should be seeded from text selected in the editor.'
##        #return pShow
##    def _set(self, pShow):
##        u'Gets/Sets if a search/replace operation should be seeded from text selected in the editor.'
##    FindReplaceInitializeFromEditor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfInit
##    def _set(self, pfInit):
##        '-no docstring-'
##    InitializeOpenFileFromCurrentDocument = property(_get, _set, doc = _set.__doc__)
##

CodeElement._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
]
################################################################
## code template for CodeElement implementation
##class CodeElement_Impl(object):
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##


# values for enumeration 'vsCommandDisabledFlags'
vsCommandDisabledFlagsEnabled = 0
vsCommandDisabledFlagsGrey = 16
vsCommandDisabledFlagsHidden = 32
vsCommandDisabledFlags = c_int # enum
class _DebuggerEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Events supported by the Debugger.'
    _iid_ = GUID('{D4EAE958-0FBA-11D3-B880-00C04F79E479}')
    _idlflags_ = ['oleautomation']
_DebuggerEvents._methods_ = [
]
################################################################
## code template for _DebuggerEvents implementation
##class _DebuggerEvents_Impl(object):


# values for enumeration 'wizardResult'
wizardResultSuccess = -1
wizardResultFailure = 0
wizardResultCancel = 1
wizardResultBackOut = 2
wizardResult = c_int # enum
class IDTWizard(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'This interface is implemented by wizard writers to construct a wizard.'
    _iid_ = GUID('{E914BBE1-03A4-11D1-BBCD-00A0C90F2744}')
    _idlflags_ = ['dual', 'oleautomation']
IDTWizard._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Called when a wizard is executed. Implemented by a wizard writer.')], HRESULT, 'Execute',
              ( ['in'], POINTER(IDispatch), 'Application' ),
              ( ['in'], c_int, 'hwndOwner' ),
              ( ['in'], POINTER(_midlSAFEARRAY(VARIANT)), 'ContextParams' ),
              ( ['in'], POINTER(_midlSAFEARRAY(VARIANT)), 'CustomParams' ),
              ( ['in', 'out'], POINTER(wizardResult), 'retval' )),
]
################################################################
## code template for IDTWizard implementation
##class IDTWizard_Impl(object):
##    def Execute(self, Application, hwndOwner, ContextParams, CustomParams):
##        u'Called when a wizard is executed. Implemented by a wizard writer.'
##        #return retval
##

class ItemOperations(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object for performing common file actions.'
    _iid_ = GUID('{D5DBE57B-C074-4E95-B015-ABEEAA391693}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsNavigateOptions'
vsNavigateOptionsDefault = 0
vsNavigateOptionsNewWindow = 1
vsNavigateOptions = c_int # enum

# values for enumeration 'vsPromptResult'
vsPromptResultYes = 1
vsPromptResultNo = 2
vsPromptResultCancelled = 3
vsPromptResult = c_int # enum
ItemOperations._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(3), helpstring(u'Opens a file as though the user invoked a open file command from the UI.')], HRESULT, 'OpenFile',
              ( ['in'], BSTR, 'FileName' ),
              ( ['in', 'optional'], BSTR, 'ViewKind', u'{00000000-0000-0000-0000-000000000000}' ),
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'Window' )),
    COMMETHOD([dispid(4), helpstring(u'Creates a file as though the user invoked a new file command from the UI.')], HRESULT, 'NewFile',
              ( ['in', 'optional'], BSTR, 'Item', u'General\text File' ),
              ( ['in', 'optional'], BSTR, 'Name', u'' ),
              ( ['in', 'optional'], BSTR, 'ViewKind', u'{00000000-0000-0000-0000-000000000000}' ),
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'Window' )),
    COMMETHOD([dispid(5), helpstring(u'Returns True if the file is open in the specified view.')], HRESULT, 'IsFileOpen',
              ( ['in'], BSTR, 'FileName' ),
              ( ['in', 'optional'], BSTR, 'ViewKind', u'{FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF}' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfRetval' )),
    COMMETHOD([dispid(6), helpstring(u'Adds an existing item to the current project.')], HRESULT, 'AddExistingItem',
              ( ['in'], BSTR, 'FileName' ),
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'ProjectItem' )),
    COMMETHOD([dispid(7), helpstring(u'Adds a new item to the current project.')], HRESULT, 'AddNewItem',
              ( ['in', 'optional'], BSTR, 'Item', u'General\text File' ),
              ( ['in', 'optional'], BSTR, 'Name', u'' ),
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'ProjectItem' )),
    COMMETHOD([dispid(8), helpstring(u'Navigates to the given URL.')], HRESULT, 'Navigate',
              ( ['in', 'optional'], BSTR, 'URL', u'' ),
              ( ['in', 'optional'], vsNavigateOptions, 'Options', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'Window' )),
    COMMETHOD([dispid(9), helpstring(u'Displays all unsaved files, and allows the user to optionally save specific files.'), 'propget'], HRESULT, 'PromptToSave',
              ( ['retval', 'out'], POINTER(vsPromptResult), 'Saved' )),
]
################################################################
## code template for ItemOperations implementation
##class ItemOperations_Impl(object):
##    def AddExistingItem(self, FileName):
##        u'Adds an existing item to the current project.'
##        #return ProjectItem
##
##    def OpenFile(self, FileName, ViewKind):
##        u'Opens a file as though the user invoked a open file command from the UI.'
##        #return Window
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppaReturn
##
##    def Navigate(self, URL, Options):
##        u'Navigates to the given URL.'
##        #return Window
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def IsFileOpen(self, FileName, ViewKind):
##        u'Returns True if the file is open in the specified view.'
##        #return pfRetval
##
##    @property
##    def PromptToSave(self):
##        u'Displays all unsaved files, and allows the user to optionally save specific files.'
##        #return Saved
##
##    def AddNewItem(self, Item, Name):
##        u'Adds a new item to the current project.'
##        #return ProjectItem
##
##    def NewFile(self, Item, Name, ViewKind):
##        u'Creates a file as though the user invoked a new file command from the UI.'
##        #return Window
##


# values for enumeration 'vsInitializeMode'
vsInitializeModeStartup = 0
vsInitializeModeReset = 1
vsInitializeMode = c_int # enum

# values for enumeration 'vsStartUp'
vsStartUpShowHomePage = 0
vsStartUpLoadLastSolution = 1
vsStartUpOpenProjectDialog = 2
vsStartUpNewProjectDialog = 3
vsStartUpEmptyEnvironment = 4
vsStartUp = c_int # enum
class IVsExtensibility(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{3C536122-57B1-46DE-AB34-ACC524140093}')
    _idlflags_ = ['hidden', 'restricted']
class ISupportVSProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{6659ED14-2AB6-47F3-A890-00C8ABA43B84}')
    _idlflags_ = ['oleautomation', 'hidden']
class TextBuffer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides access to the code associated with a project item.'
    _iid_ = GUID('{F47DC7E7-84B6-474F-BB91-631640AA0560}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
IVsExtensibility._methods_ = [
    COMMETHOD([], HRESULT, 'get_Properties',
              ( ['in'], POINTER(ISupportVSProperties), 'pParent' ),
              ( ['in'], POINTER(IDispatch), 'pdispPropObj' ),
              ( ['out'], POINTER(POINTER(Properties)), 'ppProperties' )),
    COMMETHOD([], HRESULT, 'RunWizardFile',
              ( ['in'], BSTR, 'bstrWizFilename' ),
              ( ['in'], c_int, 'hwndOwner' ),
              ( ['in'], POINTER(_midlSAFEARRAY(VARIANT)), 'vContextParams' ),
              ( ['retval', 'out'], POINTER(wizardResult), 'pResult' )),
    COMMETHOD([], HRESULT, 'Get_TextBuffer',
              ( ['in'], POINTER(IUnknown), 'pVsTextStream' ),
              ( ['in'], POINTER(IExtensibleObjectSite), 'pParent' ),
              ( ['retval', 'out'], POINTER(POINTER(TextBuffer)), 'ppTextBuffer' )),
    COMMETHOD([], HRESULT, 'EnterAutomationFunction'),
    COMMETHOD([], HRESULT, 'ExitAutomationFunction'),
    COMMETHOD([], HRESULT, 'IsInAutomationFunction',
              ( ['retval', 'out'], POINTER(c_int), 'pfInAutoFunc' )),
    COMMETHOD([], HRESULT, 'GetUserControl',
              ( ['out'], POINTER(VARIANT_BOOL), 'fUserControl' )),
    COMMETHOD([], HRESULT, 'SetUserControl',
              ( ['in'], VARIANT_BOOL, 'fUserControl' )),
    COMMETHOD([], HRESULT, 'SetUserControlUnlatched',
              ( ['in'], VARIANT_BOOL, 'fUserControl' )),
    COMMETHOD([], HRESULT, 'LockServer',
              ( ['in'], VARIANT_BOOL, '__MIDL__IVsExtensibility0000' )),
    COMMETHOD([], HRESULT, 'GetLockCount',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([], HRESULT, 'TestForShutdown',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'fShutdown' )),
    COMMETHOD([], HRESULT, 'GetGlobalsObject',
              ( ['in'], VARIANT, 'ExtractFrom' ),
              ( ['retval', 'out'], POINTER(POINTER(Globals)), 'ppGlobals' )),
    COMMETHOD([], HRESULT, 'GetConfigMgr',
              ( ['in'], POINTER(IUnknown), 'pIVsProject' ),
              ( [], ULONG_PTR, 'itemid' ),
              ( ['retval', 'out'], POINTER(POINTER(ConfigurationManager)), 'ppCfgMgr' )),
    COMMETHOD([], HRESULT, 'FireMacroReset'),
    COMMETHOD([], HRESULT, 'GetDocumentFromDocCookie',
              ( [], LONG_PTR, 'lDocCookie' ),
              ( ['retval', 'out'], POINTER(POINTER(Document)), 'ppDoc' )),
    COMMETHOD([], HRESULT, 'IsMethodDisabled',
              ( [], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pGUID' ),
              ( [], c_int, 'dispid' )),
    COMMETHOD([], HRESULT, 'SetSuppressUI',
              ( [], VARIANT_BOOL, 'In' )),
    COMMETHOD([], HRESULT, 'GetSuppressUI',
              ( [], POINTER(VARIANT_BOOL), 'pOut' )),
]
################################################################
## code template for IVsExtensibility implementation
##class IVsExtensibility_Impl(object):
##    def LockServer(self, __MIDL__IVsExtensibility0000):
##        '-no docstring-'
##        #return 
##
##    def Get_TextBuffer(self, pVsTextStream, pParent):
##        '-no docstring-'
##        #return ppTextBuffer
##
##    def IsMethodDisabled(self, pGUID, dispid):
##        '-no docstring-'
##        #return 
##
##    def TestForShutdown(self):
##        '-no docstring-'
##        #return fShutdown
##
##    def SetSuppressUI(self, In):
##        '-no docstring-'
##        #return 
##
##    def GetLockCount(self):
##        '-no docstring-'
##        #return pCount
##
##    def GetGlobalsObject(self, ExtractFrom):
##        '-no docstring-'
##        #return ppGlobals
##
##    def IsInAutomationFunction(self):
##        '-no docstring-'
##        #return pfInAutoFunc
##
##    def GetConfigMgr(self, pIVsProject, itemid):
##        '-no docstring-'
##        #return ppCfgMgr
##
##    def SetUserControl(self, fUserControl):
##        '-no docstring-'
##        #return 
##
##    def ExitAutomationFunction(self):
##        '-no docstring-'
##        #return 
##
##    def get_Properties(self, pParent, pdispPropObj):
##        '-no docstring-'
##        #return ppProperties
##
##    def EnterAutomationFunction(self):
##        '-no docstring-'
##        #return 
##
##    def RunWizardFile(self, bstrWizFilename, hwndOwner, vContextParams):
##        '-no docstring-'
##        #return pResult
##
##    def GetSuppressUI(self, pOut):
##        '-no docstring-'
##        #return 
##
##    def FireMacroReset(self):
##        '-no docstring-'
##        #return 
##
##    def SetUserControlUnlatched(self, fUserControl):
##        '-no docstring-'
##        #return 
##
##    def GetUserControl(self):
##        '-no docstring-'
##        #return fUserControl
##
##    def GetDocumentFromDocCookie(self, lDocCookie):
##        '-no docstring-'
##        #return ppDoc
##

class DTEEvents(CoClass):
    u'The DTEEvents object triggers events about the state of the environment.'
    _reg_clsid_ = GUID('{C6304BAB-6765-4C63-9017-4940AEB6F207}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _DTEEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The DTEEvents object triggers events about the state of the environment.'
    _iid_ = GUID('{FA1BB6D7-CA83-11D2-AAB2-00C04F688DDE}')
    _idlflags_ = ['oleautomation']
class _dispDTEEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The DTEEvents object triggers events about the state of the environment.'
    _iid_ = GUID('{B50C9708-C909-4B87-A03D-AF6CC4BFB422}')
    _idlflags_ = []
    _methods_ = []
DTEEvents._com_interfaces_ = [_DTEEvents]
DTEEvents._outgoing_interfaces_ = [_dispDTEEvents]

CodeVariable._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ParentObject' )),
    COMMETHOD([dispid(33), helpstring(u'Sets/Returns an object defining the initialization code for an element.'), 'propget'], HRESULT, 'InitExpression',
              ( ['retval', 'out'], POINTER(VARIANT), 'pExpr' )),
    COMMETHOD([dispid(33), helpstring(u'Sets/Returns an object defining the initialization code for an element.'), 'propput'], HRESULT, 'InitExpression',
              ( [], VARIANT, 'pExpr' )),
    COMMETHOD([dispid(34), helpstring(u'Returns a string holding the stub definition of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Prototype',
              ( ['in', 'optional'], c_int, 'Flags', 0 ),
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(35), helpstring(u'Sets/Returns an object representing the programmatic type.'), 'nonbrowsable', 'propput'], HRESULT, 'Type',
              ( [], POINTER(CodeTypeRef), 'pCodeTypeRef' )),
    COMMETHOD([dispid(35), helpstring(u'Sets/Returns an object representing the programmatic type.'), 'nonbrowsable', 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(POINTER(CodeTypeRef)), 'pCodeTypeRef' )),
    COMMETHOD([dispid(36), helpstring(u'Defines the access attributes of this item.'), 'propput'], HRESULT, 'Access',
              ( [], vsCMAccess, 'Access' )),
    COMMETHOD([dispid(36), helpstring(u'Defines the access attributes of this item.'), 'propget'], HRESULT, 'Access',
              ( ['retval', 'out'], POINTER(vsCMAccess), 'Access' )),
    COMMETHOD([dispid(37), helpstring(u'Describes if this item is a constant or not.'), 'propget'], HRESULT, 'IsConstant',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsConstant' )),
    COMMETHOD([dispid(37), helpstring(u'Describes if this item is a constant or not.'), 'propput'], HRESULT, 'IsConstant',
              ( [], VARIANT_BOOL, 'pIsConstant' )),
    COMMETHOD([dispid(38), helpstring(u'Returns a collection of items containing attributes.'), 'nonbrowsable', 'propget'], HRESULT, 'Attributes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppMembers' )),
    COMMETHOD([dispid(39), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propget'], HRESULT, 'DocComment',
              ( ['retval', 'out'], POINTER(BSTR), 'pDocComment' )),
    COMMETHOD([dispid(39), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propput'], HRESULT, 'DocComment',
              ( [], BSTR, 'pDocComment' )),
    COMMETHOD([dispid(40), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Comment',
              ( ['retval', 'out'], POINTER(BSTR), 'pComment' )),
    COMMETHOD([dispid(40), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propput'], HRESULT, 'Comment',
              ( [], BSTR, 'pComment' )),
    COMMETHOD([dispid(41), helpstring(u'Creates a new attribute code construct and inserts the code in the correct location.')], HRESULT, 'AddAttribute',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeAttribute)), 'ppCodeAttribute' )),
    COMMETHOD([dispid(42), helpstring(u'Sets/Returns if the item is common to all instances of this object type, or to this object specifically.'), 'propget'], HRESULT, 'IsShared',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pShared' )),
    COMMETHOD([dispid(42), helpstring(u'Sets/Returns if the item is common to all instances of this object type, or to this object specifically.'), 'propput'], HRESULT, 'IsShared',
              ( [], VARIANT_BOOL, 'pShared' )),
]
################################################################
## code template for CodeVariable implementation
##class CodeVariable_Impl(object):
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    def _get(self):
##        u'Defines the access attributes of this item.'
##        #return Access
##    def _set(self, Access):
##        u'Defines the access attributes of this item.'
##    Access = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Describes if this item is a constant or not.'
##        #return pIsConstant
##    def _set(self, pIsConstant):
##        u'Describes if this item is a constant or not.'
##    IsConstant = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    @property
##    def Prototype(self, Flags):
##        u'Returns a string holding the stub definition of this object.'
##        #return pVal
##
##    def _get(self):
##        u'Sets/Returns an object representing the programmatic type.'
##        #return pCodeTypeRef
##    def _set(self, pCodeTypeRef):
##        u'Sets/Returns an object representing the programmatic type.'
##    Type = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ParentObject
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    def AddAttribute(self, Name, Value, Position):
##        u'Creates a new attribute code construct and inserts the code in the correct location.'
##        #return ppCodeAttribute
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def _get(self):
##        u'Returns the document comment on the current code model element.'
##        #return pDocComment
##    def _set(self, pDocComment):
##        u'Returns the document comment on the current code model element.'
##    DocComment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Attributes(self):
##        u'Returns a collection of items containing attributes.'
##        #return ppMembers
##
##    def _get(self):
##        u'Sets/Returns if the item is common to all instances of this object type, or to this object specifically.'
##        #return pShared
##    def _set(self, pShared):
##        u'Sets/Returns if the item is common to all instances of this object type, or to this object specifically.'
##    IsShared = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Sets/Returns an object defining the comment for this object.'
##        #return pComment
##    def _set(self, pComment):
##        u'Sets/Returns an object defining the comment for this object.'
##    Comment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##
##    def _get(self):
##        u'Sets/Returns an object defining the initialization code for an element.'
##        #return pExpr
##    def _set(self, pExpr):
##        u'Sets/Returns an object defining the initialization code for an element.'
##    InitExpression = property(_get, _set, doc = _set.__doc__)
##

class DocumentEvents(CoClass):
    _reg_clsid_ = GUID('{DC5437F7-F114-11D2-AACF-00C04F688DDE}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _dispDocumentEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{DC5437F6-F114-11D2-AACF-00C04F688DDE}')
    _idlflags_ = []
    _methods_ = []
DocumentEvents._com_interfaces_ = [_DocumentEvents]
DocumentEvents._outgoing_interfaces_ = [_dispDocumentEvents]


# values for enumeration 'vsDisplay'
vsDisplayMDI = 1
vsDisplayMDITabs = 2
vsDisplay = c_int # enum

# values for enumeration 'vsIDEMode'
vsIDEModeDesign = 1
vsIDEModeDebug = 2
vsIDEMode = c_int # enum

# values for enumeration 'dbgExecutionAction'
dbgExecutionActionDefault = 1
dbgExecutionActionGo = 2
dbgExecutionActionStopDebugging = 3
dbgExecutionActionStepInto = 4
dbgExecutionActionStepOut = 5
dbgExecutionActionStepOver = 6
dbgExecutionActionRunToCursor = 7
dbgExecutionAction = c_int # enum
class Documents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Collection of Documents open for editing.'
    _iid_ = GUID('{9E2CF3EA-140F-413E-BD4B-7D46740CD2F4}')
    _idlflags_ = ['dual', 'oleautomation']
class Windows(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Represents window(s) in the development environment.'
    _iid_ = GUID('{2294311A-B7BC-4789-B365-1C15FF2CD17C}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsSaveChanges'
vsSaveChangesYes = 1
vsSaveChangesNo = 2
vsSaveChangesPrompt = 3
vsSaveChanges = c_int # enum

# values for enumeration 'vsSaveStatus'
vsSaveCancelled = 2
vsSaveSucceeded = 1
vsSaveStatus = c_int # enum
Document._methods_ = [
    COMMETHOD([dispid(100), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(141), helpstring(u'Returns a GUID String indicating the kind or type of the object.'), 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(BSTR), 'pKind' )),
    COMMETHOD([dispid(101), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(Documents)), 'DocumentsObject' )),
    COMMETHOD([dispid(102), helpstring(u'Returns the current active window.'), 'propget'], HRESULT, 'ActiveWindow',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'pWindow' )),
    COMMETHOD([dispid(103), helpstring(u'Returns the full file path to the item.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(0), helpstring(u'Returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(105), helpstring(u'Returns the Path (without filename) to the file in storage.'), 'propget'], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(106), helpstring(u'Returns a value specifying if the item in storage is read only or not.'), 'propget'], HRESULT, 'ReadOnly',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pRetval' )),
    COMMETHOD([dispid(107), helpstring(u'Returns value indicating whether object was changed since the last time it was saved.'), 'propget'], HRESULT, 'Saved',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pRetval' )),
    COMMETHOD([dispid(107), helpstring(u'Returns value indicating whether object was changed since the last time it was saved.'), 'propput'], HRESULT, 'Saved',
              ( ['in'], VARIANT_BOOL, 'pRetval' )),
    COMMETHOD([dispid(109), helpstring(u'Returns the Windows that display the document.'), 'propget'], HRESULT, 'Windows',
              ( ['retval', 'out'], POINTER(POINTER(Windows)), 'pWindows' )),
    COMMETHOD([dispid(110), helpstring(u'Returns the ProjectItem object.'), 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pRetval' )),
    COMMETHOD([dispid(121), helpstring(u'Moves the focus to the current item.')], HRESULT, 'Activate'),
    COMMETHOD([dispid(123), helpstring(u'Closes the document, and optionally saves.')], HRESULT, 'Close',
              ( ['in', 'optional'], vsSaveChanges, 'Save', 3 )),
    COMMETHOD([dispid(125), helpstring(u'Creates a new window to view the document.')], HRESULT, 'NewWindow',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'pWindow' )),
    COMMETHOD([dispid(127), helpstring(u'Redo the action last performed by the user on this object.')], HRESULT, 'Redo',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbRetVal' )),
    COMMETHOD([dispid(128), helpstring(u'Undo the action last performed by the user on this object.')], HRESULT, 'Undo',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbRetVal' )),
    COMMETHOD([dispid(129), helpstring(u'Saves the object to storage.')], HRESULT, 'Save',
              ( ['in', 'optional'], BSTR, 'FileName', u'' ),
              ( ['retval', 'out'], POINTER(vsSaveStatus), 'pStatus' )),
    COMMETHOD([dispid(131), helpstring(u'Returns an object representing the selection on this object.'), 'propget'], HRESULT, 'Selection',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'SelectionObject' )),
    COMMETHOD([dispid(132), helpstring(u'Returns an interface or object that can be accessed at run time by name.')], HRESULT, 'Object',
              ( ['in', 'optional'], BSTR, 'ModelKind', u'' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'DataModelObject' )),
    COMMETHOD([dispid(133), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(134), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(135), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(126), helpstring(u'Sends the object to the printer.'), 'hidden'], HRESULT, 'PrintOut'),
    COMMETHOD([dispid(142), helpstring(u'Sets/returns a Long value indicating the width of an indent level in spaces.'), 'hidden', 'propget'], HRESULT, 'IndentSize',
              ( ['retval', 'out'], POINTER(c_int), 'pSize' )),
    COMMETHOD([dispid(144), helpstring(u"Returns the name of the document's language."), 'hidden', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(144), helpstring(u"Returns the name of the document's language."), 'hidden', 'propput'], HRESULT, 'Language',
              ( ['in'], BSTR, 'pLanguage' )),
    COMMETHOD([dispid(106), helpstring(u'Returns a value specifying if the item in storage is read only or not.'), 'hidden', 'propput'], HRESULT, 'ReadOnly',
              ( ['in'], VARIANT_BOOL, 'pRetval' )),
    COMMETHOD([dispid(147), helpstring(u'Sets/returns value determining tab size in the editor.'), 'hidden', 'propget'], HRESULT, 'TabSize',
              ( ['retval', 'out'], POINTER(c_int), 'pSize' )),
    COMMETHOD([dispid(122), helpstring(u'Clears all bookmarks in the document.'), 'hidden'], HRESULT, 'ClearBookmarks'),
    COMMETHOD([dispid(124), helpstring(u'Creates unnamed bookmarks where the specified pattern is found.'), 'hidden'], HRESULT, 'MarkText',
              ( ['in'], BSTR, 'Pattern' ),
              ( ['in', 'optional'], c_int, 'Flags', 0 ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbRetVal' )),
    COMMETHOD([dispid(21), helpstring(u'Replaces a pattern of text with new text in a document.'), 'hidden'], HRESULT, 'ReplaceText',
              ( ['in'], BSTR, 'FindText' ),
              ( ['in'], BSTR, 'ReplaceText' ),
              ( ['in', 'optional'], c_int, 'Flags', 0 ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbRetVal' )),
    COMMETHOD([dispid(149), helpstring(u'Returns an enumerated string indicating the object type.'), 'hidden', 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(BSTR), 'pType' )),
]
################################################################
## code template for Document implementation
##class Document_Impl(object):
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    @property
##    def Collection(self):
##        u'Returns the parent object.'
##        #return DocumentsObject
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pRetval
##
##    def Save(self, FileName):
##        u'Saves the object to storage.'
##        #return pStatus
##
##    @property
##    def Type(self):
##        u'Returns an enumerated string indicating the object type.'
##        #return pType
##
##    def Object(self, ModelKind):
##        u'Returns an interface or object that can be accessed at run time by name.'
##        #return DataModelObject
##
##    def Undo(self):
##        u'Undo the action last performed by the user on this object.'
##        #return pbRetVal
##
##    def NewWindow(self):
##        u'Creates a new window to view the document.'
##        #return pWindow
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def Path(self):
##        u'Returns the Path (without filename) to the file in storage.'
##        #return pRetval
##
##    @property
##    def Kind(self):
##        u'Returns a GUID String indicating the kind or type of the object.'
##        #return pKind
##
##    @property
##    def Name(self):
##        u'Returns the name of the object.'
##        #return pRetval
##
##    def _get(self):
##        u"Returns the name of the document's language."
##        #return pLanguage
##    def _set(self, pLanguage):
##        u"Returns the name of the document's language."
##    Language = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IndentSize(self):
##        u'Sets/returns a Long value indicating the width of an indent level in spaces.'
##        #return pSize
##
##    @property
##    def Windows(self):
##        u'Returns the Windows that display the document.'
##        #return pWindows
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def PrintOut(self):
##        u'Sends the object to the printer.'
##        #return 
##
##    def ClearBookmarks(self):
##        u'Clears all bookmarks in the document.'
##        #return 
##
##    @property
##    def Selection(self):
##        u'Returns an object representing the selection on this object.'
##        #return SelectionObject
##
##    @property
##    def ActiveWindow(self):
##        u'Returns the current active window.'
##        #return pWindow
##
##    def Activate(self):
##        u'Moves the focus to the current item.'
##        #return 
##
##    def _get(self):
##        u'Returns value indicating whether object was changed since the last time it was saved.'
##        #return pRetval
##    def _set(self, pRetval):
##        u'Returns value indicating whether object was changed since the last time it was saved.'
##    Saved = property(_get, _set, doc = _set.__doc__)
##
##    def ReplaceText(self, FindText, ReplaceText, Flags):
##        u'Replaces a pattern of text with new text in a document.'
##        #return pbRetVal
##
##    def _get(self):
##        u'Returns a value specifying if the item in storage is read only or not.'
##        #return pRetval
##    def _set(self, pRetval):
##        u'Returns a value specifying if the item in storage is read only or not.'
##    ReadOnly = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def TabSize(self):
##        u'Sets/returns value determining tab size in the editor.'
##        #return pSize
##
##    def Close(self, Save):
##        u'Closes the document, and optionally saves.'
##        #return 
##
##    @property
##    def FullName(self):
##        u'Returns the full file path to the item.'
##        #return pRetval
##
##    def Redo(self):
##        u'Redo the action last performed by the user on this object.'
##        #return pbRetVal
##
##    def MarkText(self, Pattern, Flags):
##        u'Creates unnamed bookmarks where the specified pattern is found.'
##        #return pbRetVal
##

class SourceControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A Document open for editing.'
    _iid_ = GUID('{F1DDC2C2-DF76-4EBB-9DE8-48AD2557062C}')
    _idlflags_ = ['dual', 'oleautomation']
SourceControl._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTEObject' )),
    COMMETHOD([dispid(3), helpstring(u'Returns if an items is under source code control.')], HRESULT, 'IsItemUnderSCC',
              ( ['in'], BSTR, 'ItemName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfControlled' )),
    COMMETHOD([dispid(4), helpstring(u'Returns if an item is checked out of source code control for editing.')], HRESULT, 'IsItemCheckedOut',
              ( ['in'], BSTR, 'ItemName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfCheckedOut' )),
    COMMETHOD([dispid(5), helpstring(u'Checks out an item from source code control for editing.')], HRESULT, 'CheckOutItem',
              ( ['in'], BSTR, 'ItemName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfCheckedOut' )),
    COMMETHOD([dispid(6), helpstring(u'Checks out an item from source code control for editing.')], HRESULT, 'CheckOutItems',
              ( ['in'], POINTER(_midlSAFEARRAY(VARIANT)), 'ItemNames' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfCheckedOut' )),
    COMMETHOD([dispid(7)], HRESULT, 'ExcludeItem',
              ( ['in'], BSTR, 'ProjectFile' ),
              ( ['in'], BSTR, 'ItemName' )),
    COMMETHOD([dispid(8)], HRESULT, 'ExcludeItems',
              ( ['in'], BSTR, 'ProjectFile' ),
              ( ['in'], POINTER(_midlSAFEARRAY(VARIANT)), 'ItemNames' )),
]
################################################################
## code template for SourceControl implementation
##class SourceControl_Impl(object):
##    def ExcludeItem(self, ProjectFile, ItemName):
##        '-no docstring-'
##        #return 
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppDTEObject
##
##    def CheckOutItem(self, ItemName):
##        u'Checks out an item from source code control for editing.'
##        #return pfCheckedOut
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTEObject
##
##    def IsItemUnderSCC(self, ItemName):
##        u'Returns if an items is under source code control.'
##        #return pfControlled
##
##    def IsItemCheckedOut(self, ItemName):
##        u'Returns if an item is checked out of source code control for editing.'
##        #return pfCheckedOut
##
##    def CheckOutItems(self, ItemNames):
##        u'Checks out an item from source code control for editing.'
##        #return pfCheckedOut
##
##    def ExcludeItems(self, ProjectFile, ItemNames):
##        '-no docstring-'
##        #return 
##

class _EnvironmentWebBrowser(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{A3286B03-5AC6-44F0-8CC3-EBED7F1124E5}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']

# values for enumeration 'vsBrowserViewSource'
vsBrowserViewSourceSource = 1
vsBrowserViewSourceDesign = 2
vsBrowserViewSourceExternal = 3
vsBrowserViewSource = c_int # enum
_EnvironmentWebBrowser._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Use the default home page when the browser is opened, or use a custom home page.'), 'propput'], HRESULT, 'UseDefaultHomePage',
              ( [], VARIANT_BOOL, 'pUseDefault' )),
    COMMETHOD([dispid(1), helpstring(u'Use the default home page when the browser is opened, or use a custom home page.'), 'propget'], HRESULT, 'UseDefaultHomePage',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pUseDefault' )),
    COMMETHOD([dispid(2), helpstring(u'The URL of the default home page.'), 'propput'], HRESULT, 'HomePage',
              ( [], BSTR, 'URL' )),
    COMMETHOD([dispid(2), helpstring(u'The URL of the default home page.'), 'propget'], HRESULT, 'HomePage',
              ( ['retval', 'out'], POINTER(BSTR), 'URL' )),
    COMMETHOD([dispid(3), helpstring(u'Use the default search page when using the browser search command, or use a custom search page.'), 'propput'], HRESULT, 'UseDefaultSearchPage',
              ( [], VARIANT_BOOL, 'pUseDefault' )),
    COMMETHOD([dispid(3), helpstring(u'Use the default search page when using the browser search command, or use a custom search page.'), 'propget'], HRESULT, 'UseDefaultSearchPage',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pUseDefault' )),
    COMMETHOD([dispid(4), helpstring(u'The URL of the default search page.'), 'propput'], HRESULT, 'SearchPage',
              ( [], BSTR, 'URL' )),
    COMMETHOD([dispid(4), helpstring(u'The URL of the default search page.'), 'propget'], HRESULT, 'SearchPage',
              ( ['retval', 'out'], POINTER(BSTR), 'URL' )),
    COMMETHOD([dispid(5), helpstring(u'Where the source of a web page is viewed when the view source command is used.'), 'propput'], HRESULT, 'ViewSourceIn',
              ( [], vsBrowserViewSource, 'Location' )),
    COMMETHOD([dispid(5), helpstring(u'Where the source of a web page is viewed when the view source command is used.'), 'propget'], HRESULT, 'ViewSourceIn',
              ( ['retval', 'out'], POINTER(vsBrowserViewSource), 'Location' )),
    COMMETHOD([dispid(6), helpstring(u'The program to use to view the browser source.'), 'propput'], HRESULT, 'ViewSourceExternalProgram',
              ( [], BSTR, 'Path' )),
    COMMETHOD([dispid(6), helpstring(u'The program to use to view the browser source.'), 'propget'], HRESULT, 'ViewSourceExternalProgram',
              ( ['retval', 'out'], POINTER(BSTR), 'Path' )),
]
################################################################
## code template for _EnvironmentWebBrowser implementation
##class _EnvironmentWebBrowser_Impl(object):
##    def _get(self):
##        u'The program to use to view the browser source.'
##        #return Path
##    def _set(self, Path):
##        u'The program to use to view the browser source.'
##    ViewSourceExternalProgram = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The URL of the default search page.'
##        #return URL
##    def _set(self, URL):
##        u'The URL of the default search page.'
##    SearchPage = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Use the default home page when the browser is opened, or use a custom home page.'
##        #return pUseDefault
##    def _set(self, pUseDefault):
##        u'Use the default home page when the browser is opened, or use a custom home page.'
##    UseDefaultHomePage = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Where the source of a web page is viewed when the view source command is used.'
##        #return Location
##    def _set(self, Location):
##        u'Where the source of a web page is viewed when the view source command is used.'
##    ViewSourceIn = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Use the default search page when using the browser search command, or use a custom search page.'
##        #return pUseDefault
##    def _set(self, pUseDefault):
##        u'Use the default search page when using the browser search command, or use a custom search page.'
##    UseDefaultSearchPage = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The URL of the default home page.'
##        #return URL
##    def _set(self, URL):
##        u'The URL of the default home page.'
##    HomePage = property(_get, _set, doc = _set.__doc__)
##

_dispDocumentEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Occurs after a document is saved.')], None, 'DocumentSaved',
               ( ['in'], POINTER(Document), 'Document' )),
    DISPMETHOD([dispid(2), helpstring(u'Occurs just before a document is closed.')], None, 'DocumentClosing',
               ( ['in'], POINTER(Document), 'Document' )),
    DISPMETHOD([dispid(3), helpstring(u'Occurs just before a document is opened.')], None, 'DocumentOpening',
               ( ['in'], BSTR, 'DocumentPath' ),
               ( ['in'], VARIANT_BOOL, 'ReadOnly' )),
    DISPMETHOD([dispid(4), helpstring(u'Occurs just after a document is opened.')], None, 'DocumentOpened',
               ( ['in'], POINTER(Document), 'Document' )),
]

# values for enumeration 'dbgExceptionAction'
dbgExceptionActionDefault = 1
dbgExceptionActionIgnore = 2
dbgExceptionActionBreak = 3
dbgExceptionActionContinue = 4
dbgExceptionAction = c_int # enum
class _ProjectItemsEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The _ProjectItemsEvents object triggers events of actions taken against projects and their items.'
    _iid_ = GUID('{22800963-2811-410D-BF87-A7808EAC977D}')
    _idlflags_ = ['dual', 'oleautomation']
_ProjectItemsEvents._methods_ = [
]
################################################################
## code template for _ProjectItemsEvents implementation
##class _ProjectItemsEvents_Impl(object):

class AddIns(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides information about an add-in to other Add-in objects.'
    _iid_ = GUID('{50590801-D13E-4404-80C2-5CA30A4D0EE8}')
    _idlflags_ = ['dual', 'oleautomation']
_Solution._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Project)), 'lppcReturn' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(10), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(11), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(12), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'lplReturn' )),
    COMMETHOD([dispid(13), helpstring(u'Returns full pathname of solution file.'), 'hidden', 'propget'], HRESULT, 'FileName',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
    COMMETHOD([dispid(14), helpstring(u'Saves the current solution file.')], HRESULT, 'SaveAs',
              ( ['in'], BSTR, 'FileName' )),
    COMMETHOD([dispid(15), helpstring(u'Copies project file to specified location; adds it to solution as project file.')], HRESULT, 'AddFromTemplate',
              ( ['in'], BSTR, 'FileName' ),
              ( ['in'], BSTR, 'Destination' ),
              ( ['in'], BSTR, 'ProjectName' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Exclusive', False ),
              ( ['retval', 'out'], POINTER(POINTER(Project)), 'IppptReturn' )),
    COMMETHOD([dispid(16), helpstring(u'Adds project to solution based on project file already installed in correct location.')], HRESULT, 'AddFromFile',
              ( ['in'], BSTR, 'FileName' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Exclusive', False ),
              ( ['retval', 'out'], POINTER(POINTER(Project)), 'IppptReturn' )),
    COMMETHOD([dispid(17), helpstring(u'Opens the Solution represented by the filename.')], HRESULT, 'Open',
              ( ['in'], BSTR, 'FileName' )),
    COMMETHOD([dispid(18), helpstring(u'Causes the development environment to close the current solution file.')], HRESULT, 'Close',
              ( ['in', 'optional'], VARIANT_BOOL, 'SaveFirst', False )),
    COMMETHOD([dispid(19), helpstring(u'Returns the Properties collection.'), 'propget'], HRESULT, 'Properties',
              ( ['retval', 'out'], POINTER(POINTER(Properties)), 'ppObject' )),
    COMMETHOD([dispid(22), 'hidden', 'propget'], HRESULT, 'IsDirty',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lpfReturn' )),
    COMMETHOD([dispid(22), 'hidden', 'propput'], HRESULT, 'IsDirty',
              ( ['in'], VARIANT_BOOL, 'lpfReturn' )),
    COMMETHOD([dispid(25), helpstring(u'Removes a Project object from the Solution object.')], HRESULT, 'Remove',
              ( ['in'], POINTER(Project), 'proj' )),
    COMMETHOD([dispid(26), helpstring(u'Returns full pathname of directory containing templates in Visual Studio install directory.'), 'propget'], HRESULT, 'TemplatePath',
              ( ['in'], BSTR, 'ProjectType' ),
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrPath' )),
    COMMETHOD([dispid(28), helpstring(u'Returns full pathname of solution file.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
    COMMETHOD([dispid(29), helpstring(u'Returns value indicating whether object was changed since the last time it was saved.'), 'propget'], HRESULT, 'Saved',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lpfReturn' )),
    COMMETHOD([dispid(29), helpstring(u'Returns value indicating whether object was changed since the last time it was saved.'), 'propput'], HRESULT, 'Saved',
              ( ['in'], VARIANT_BOOL, 'lpfReturn' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the Globals object for storing persistent data.'), 'propget'], HRESULT, 'Globals',
              ( ['retval', 'out'], POINTER(POINTER(Globals)), 'ppGlobals' )),
    COMMETHOD([dispid(32), helpstring(u'Returns the Solution Add-ins collection, containing all currently available add-ins associated with the open solution.'), 'propget'], HRESULT, 'AddIns',
              ( ['retval', 'out'], POINTER(POINTER(AddIns)), 'ppAddIns' )),
    COMMETHOD([dispid(33), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(34), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(35), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(36), helpstring(u'Returns a Boolean indicating if there are any projects currently in the solution.'), 'propget'], HRESULT, 'IsOpen',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(38), helpstring(u'Returns the SolutionBuild object.'), 'propget'], HRESULT, 'SolutionBuild',
              ( ['retval', 'out'], POINTER(POINTER(SolutionBuild)), 'ppSolutionBuild' )),
    COMMETHOD([dispid(40), helpstring(u'Creates an empty solution in the specified directory with the specified name.')], HRESULT, 'Create',
              ( [], BSTR, 'Destination' ),
              ( [], BSTR, 'Name' )),
    COMMETHOD([dispid(41), helpstring(u'Returns a collection of projects currently in the solution.'), 'propget'], HRESULT, 'Projects',
              ( ['retval', 'out'], POINTER(POINTER(Projects)), 'ppProjects' )),
    COMMETHOD([dispid(42), helpstring(u'Locates an item in a project.')], HRESULT, 'FindProjectItem',
              ( [], BSTR, 'FileName' ),
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'ppProjectItem' )),
    COMMETHOD([dispid(43), helpstring(u'Returns the location of project items for a specific project.')], HRESULT, 'ProjectItemsTemplatePath',
              ( [], BSTR, 'ProjectKind' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pFullPath' )),
]
################################################################
## code template for _Solution implementation
##class _Solution_Impl(object):
##    def AddFromTemplate(self, FileName, Destination, ProjectName, Exclusive):
##        u'Copies project file to specified location; adds it to solution as project file.'
##        #return IppptReturn
##
##    def ProjectItemsTemplatePath(self, ProjectKind):
##        u'Returns the location of project items for a specific project.'
##        #return pFullPath
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def _get(self):
##        '-no docstring-'
##        #return lpfReturn
##    def _set(self, lpfReturn):
##        '-no docstring-'
##    IsDirty = property(_get, _set, doc = _set.__doc__)
##
##    def FindProjectItem(self, FileName):
##        u'Locates an item in a project.'
##        #return ppProjectItem
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppaReturn
##
##    @property
##    def AddIns(self):
##        u'Returns the Solution Add-ins collection, containing all currently available add-ins associated with the open solution.'
##        #return ppAddIns
##
##    @property
##    def Properties(self):
##        u'Returns the Properties collection.'
##        #return ppObject
##
##    @property
##    def Projects(self):
##        u'Returns a collection of projects currently in the solution.'
##        #return ppProjects
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return lplReturn
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def Remove(self, proj):
##        u'Removes a Project object from the Solution object.'
##        #return 
##
##    def AddFromFile(self, FileName, Exclusive):
##        u'Adds project to solution based on project file already installed in correct location.'
##        #return IppptReturn
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return lppcReturn
##
##    def Create(self, Destination, Name):
##        u'Creates an empty solution in the specified directory with the specified name.'
##        #return 
##
##    @property
##    def SolutionBuild(self):
##        u'Returns the SolutionBuild object.'
##        #return ppSolutionBuild
##
##    def SaveAs(self, FileName):
##        u'Saves the current solution file.'
##        #return 
##
##    @property
##    def IsOpen(self):
##        u'Returns a Boolean indicating if there are any projects currently in the solution.'
##        #return pVal
##
##    def Open(self, FileName):
##        u'Opens the Solution represented by the filename.'
##        #return 
##
##    @property
##    def FileName(self):
##        u'Returns full pathname of solution file.'
##        #return lpbstrReturn
##
##    @property
##    def Globals(self):
##        u'Returns the Globals object for storing persistent data.'
##        #return ppGlobals
##
##    def Close(self, SaveFirst):
##        u'Causes the development environment to close the current solution file.'
##        #return 
##
##    @property
##    def FullName(self):
##        u'Returns full pathname of solution file.'
##        #return lpbstrReturn
##
##    def _get(self):
##        u'Returns value indicating whether object was changed since the last time it was saved.'
##        #return lpfReturn
##    def _set(self, lpfReturn):
##        u'Returns value indicating whether object was changed since the last time it was saved.'
##    Saved = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def TemplatePath(self, ProjectType):
##        u'Returns full pathname of directory containing templates in Visual Studio install directory.'
##        #return lpbstrPath
##

CodeStruct._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ParentObject' )),
    COMMETHOD([dispid(32), helpstring(u'Returns an object defining the parent namespace.'), 'nonbrowsable', 'propget'], HRESULT, 'Namespace',
              ( ['retval', 'out'], POINTER(POINTER(CodeNamespace)), 'ppCodeNamespace' )),
    COMMETHOD([dispid(33), helpstring(u'Returns a collection of classes this item derives from.'), 'nonbrowsable', 'propget'], HRESULT, 'Bases',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(34), helpstring(u'Returns a collection of items contained by this element.'), 'nonbrowsable', 'propget'], HRESULT, 'Members',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(35), helpstring(u'Defines the access attributes of this item.'), 'propput'], HRESULT, 'Access',
              ( [], vsCMAccess, 'pAccess' )),
    COMMETHOD([dispid(35), helpstring(u'Defines the access attributes of this item.'), 'propget'], HRESULT, 'Access',
              ( ['retval', 'out'], POINTER(vsCMAccess), 'pAccess' )),
    COMMETHOD([dispid(36), helpstring(u'Returns a collection of items containing attributes.'), 'nonbrowsable', 'propget'], HRESULT, 'Attributes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(37), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propget'], HRESULT, 'DocComment',
              ( ['retval', 'out'], POINTER(BSTR), 'pDocComment' )),
    COMMETHOD([dispid(37), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propput'], HRESULT, 'DocComment',
              ( [], BSTR, 'pDocComment' )),
    COMMETHOD([dispid(38), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Comment',
              ( ['retval', 'out'], POINTER(BSTR), 'pComment' )),
    COMMETHOD([dispid(38), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propput'], HRESULT, 'Comment',
              ( [], BSTR, 'pComment' )),
    COMMETHOD([dispid(39), helpstring(u'Adds an item to the list of inherited objects.')], HRESULT, 'AddBase',
              ( [], VARIANT, 'Base' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeElement)), 'ppOut' )),
    COMMETHOD([dispid(40), helpstring(u'Creates a new attribute code construct and inserts the code in the correct location.')], HRESULT, 'AddAttribute',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeAttribute)), 'ppCodeAttribute' )),
    COMMETHOD([dispid(41), helpstring(u'Removes an object from the list of bases.')], HRESULT, 'RemoveBase',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(42), helpstring(u'Removes a member code construct.')], HRESULT, 'RemoveMember',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(43), helpstring(u'Returns a Boolean telling if an object has another object as a base.'), 'propget'], HRESULT, 'IsDerivedFrom',
              ( [], BSTR, 'FullName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(44), helpstring(u'Returns a collection of objects derived from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'DerivedTypes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(61), helpstring(u'Returns a collection of interfaces implemented by this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ImplementedInterfaces',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(62), helpstring(u'Returns Boolean indicating if this item is derived from a particular item.'), 'propget'], HRESULT, 'IsAbstract',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsAbstract' )),
    COMMETHOD([dispid(62), helpstring(u'Returns Boolean indicating if this item is derived from a particular item.'), 'propput'], HRESULT, 'IsAbstract',
              ( [], VARIANT_BOOL, 'pIsAbstract' )),
    COMMETHOD([dispid(63), helpstring(u'Adds an interface to the list of inherited objects.')], HRESULT, 'AddImplementedInterface',
              ( [], VARIANT, 'Base' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeInterface)), 'ppCodeInterface' )),
    COMMETHOD([dispid(64), helpstring(u'Creates a new function code construct and inserts the code in the correct location.')], HRESULT, 'AddFunction',
              ( [], BSTR, 'Name' ),
              ( [], vsCMFunction, 'Kind' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['optional'], VARIANT, 'Location' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeFunction)), 'ppCodeFunction' )),
    COMMETHOD([dispid(65), helpstring(u'Creates a new variable code construct and inserts the code in the correct location.')], HRESULT, 'AddVariable',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['optional'], VARIANT, 'Location' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeVariable)), 'ppCodeVariable' )),
    COMMETHOD([dispid(66), helpstring(u'Creates a new property code construct and inserts the code in the correct location.')], HRESULT, 'AddProperty',
              ( [], BSTR, 'GetterName' ),
              ( [], BSTR, 'PutterName' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['optional'], VARIANT, 'Location' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeProperty)), 'ppCodeProperty' )),
    COMMETHOD([dispid(67), helpstring(u'Creates a new class code construct and inserts the code in the correct location.')], HRESULT, 'AddClass',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], VARIANT, 'ImplementedInterfaces' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeClass)), 'ppCodeClass' )),
    COMMETHOD([dispid(68), helpstring(u'Creates a new structure code construct and inserts the code in the correct location.')], HRESULT, 'AddStruct',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], VARIANT, 'ImplementedInterfaces' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeStruct)), 'ppCodeStruct' )),
    COMMETHOD([dispid(69), helpstring(u'Creates a new enumeration code construct and inserts the code in the correct location.')], HRESULT, 'AddEnum',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeEnum)), 'ppCodeEnum' )),
    COMMETHOD([dispid(70), helpstring(u'Creates a new delegate code construct and inserts the code in the correct location.')], HRESULT, 'AddDelegate',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeDelegate)), 'ppCodeDelegate' )),
    COMMETHOD([dispid(71), helpstring(u'Removes an interface from the list of implemented interfaces.')], HRESULT, 'RemoveInterface',
              ( [], VARIANT, 'Element' )),
]
################################################################
## code template for CodeStruct implementation
##class CodeStruct_Impl(object):
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    def AddProperty(self, GetterName, PutterName, Type, Position, Access, Location):
##        u'Creates a new property code construct and inserts the code in the correct location.'
##        #return ppCodeProperty
##
##    def AddStruct(self, Name, Position, Bases, ImplementedInterfaces, Access):
##        u'Creates a new structure code construct and inserts the code in the correct location.'
##        #return ppCodeStruct
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def Namespace(self):
##        u'Returns an object defining the parent namespace.'
##        #return ppCodeNamespace
##
##    def AddBase(self, Base, Position):
##        u'Adds an item to the list of inherited objects.'
##        #return ppOut
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    def _get(self):
##        u'Defines the access attributes of this item.'
##        #return pAccess
##    def _set(self, pAccess):
##        u'Defines the access attributes of this item.'
##    Access = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Bases(self):
##        u'Returns a collection of classes this item derives from.'
##        #return ppCodeElements
##
##    def AddEnum(self, Name, Position, Bases, Access):
##        u'Creates a new enumeration code construct and inserts the code in the correct location.'
##        #return ppCodeEnum
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##
##    def _get(self):
##        u'Returns Boolean indicating if this item is derived from a particular item.'
##        #return pIsAbstract
##    def _set(self, pIsAbstract):
##        u'Returns Boolean indicating if this item is derived from a particular item.'
##    IsAbstract = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def ImplementedInterfaces(self):
##        u'Returns a collection of interfaces implemented by this object.'
##        #return ppCodeElements
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ParentObject
##
##    def AddImplementedInterface(self, Base, Position):
##        u'Adds an interface to the list of inherited objects.'
##        #return ppCodeInterface
##
##    def AddFunction(self, Name, Kind, Type, Position, Access, Location):
##        u'Creates a new function code construct and inserts the code in the correct location.'
##        #return ppCodeFunction
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    def AddAttribute(self, Name, Value, Position):
##        u'Creates a new attribute code construct and inserts the code in the correct location.'
##        #return ppCodeAttribute
##
##    def RemoveMember(self, Element):
##        u'Removes a member code construct.'
##        #return 
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def Members(self):
##        u'Returns a collection of items contained by this element.'
##        #return ppCodeElements
##
##    def AddDelegate(self, Name, Type, Position, Access):
##        u'Creates a new delegate code construct and inserts the code in the correct location.'
##        #return ppCodeDelegate
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def _get(self):
##        u'Returns the document comment on the current code model element.'
##        #return pDocComment
##    def _set(self, pDocComment):
##        u'Returns the document comment on the current code model element.'
##    DocComment = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveInterface(self, Element):
##        u'Removes an interface from the list of implemented interfaces.'
##        #return 
##
##    def RemoveBase(self, Element):
##        u'Removes an object from the list of bases.'
##        #return 
##
##    @property
##    def Attributes(self):
##        u'Returns a collection of items containing attributes.'
##        #return ppCodeElements
##
##    def AddClass(self, Name, Position, Bases, ImplementedInterfaces, Access):
##        u'Creates a new class code construct and inserts the code in the correct location.'
##        #return ppCodeClass
##
##    def _get(self):
##        u'Sets/Returns an object defining the comment for this object.'
##        #return pComment
##    def _set(self, pComment):
##        u'Sets/Returns an object defining the comment for this object.'
##    Comment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsDerivedFrom(self, FullName):
##        u'Returns a Boolean telling if an object has another object as a base.'
##        #return pVal
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    def AddVariable(self, Name, Type, Position, Access, Location):
##        u'Creates a new variable code construct and inserts the code in the correct location.'
##        #return ppCodeVariable
##
##    @property
##    def DerivedTypes(self):
##        u'Returns a collection of objects derived from this object.'
##        #return ppCodeElements
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##

Documents._methods_ = [
    COMMETHOD([dispid(100), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(101), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Document)), 'DocumentObject' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'CountOfDocuments' )),
    COMMETHOD([dispid(4), helpstring(u'Creates a new document and adds it to the Documents collection.'), 'hidden'], HRESULT, 'Add',
              ( ['in'], BSTR, 'Kind' ),
              ( ['retval', 'out'], POINTER(POINTER(Document)), 'ppDocument' )),
    COMMETHOD([dispid(5), helpstring(u'Closes all open documents.')], HRESULT, 'CloseAll',
              ( ['in', 'optional'], vsSaveChanges, 'Save', 3 )),
    COMMETHOD([dispid(6), helpstring(u'Saves all open documents.')], HRESULT, 'SaveAll'),
    COMMETHOD([dispid(7), 'hidden'], HRESULT, 'Open',
              ( [], BSTR, 'PathName' ),
              ( ['optional'], BSTR, 'Kind', u'Auto' ),
              ( ['optional'], VARIANT_BOOL, 'ReadOnly', False ),
              ( ['retval', 'out'], POINTER(POINTER(Document)), 'ppDocument' )),
]
################################################################
## code template for Documents implementation
##class Documents_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return CountOfDocuments
##
##    def SaveAll(self):
##        u'Saves all open documents.'
##        #return 
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return DTEObject
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return DocumentObject
##
##    def Add(self, Kind):
##        u'Creates a new document and adds it to the Documents collection.'
##        #return ppDocument
##
##    def Open(self, PathName, Kind, ReadOnly):
##        '-no docstring-'
##        #return ppDocument
##
##    def CloseAll(self, Save):
##        u'Closes all open documents.'
##        #return 
##

AddIn._methods_ = [
    COMMETHOD([dispid(0), helpstring(u"Returns a string containing the object's description."), 'propget'], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstr' )),
    COMMETHOD([dispid(0), helpstring(u"Returns a string containing the object's description."), 'propput'], HRESULT, 'Description',
              ( ['in'], BSTR, 'lpbstr' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(AddIns)), 'lppaddins' )),
    COMMETHOD([dispid(3), helpstring(u"Returns the ProgID as obtained from the Add-in's registry entry."), 'propget'], HRESULT, 'ProgID',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstr' )),
    COMMETHOD([dispid(4), helpstring(u"Returns the Add-in's CLSID as obtained from the Add-in's registry entry."), 'propget'], HRESULT, 'Guid',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstr' )),
    COMMETHOD([dispid(6), helpstring(u'Returns value indicating whether an Add-ins is loaded and connected.'), 'propget'], HRESULT, 'Connected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lpfConnect' )),
    COMMETHOD([dispid(6), helpstring(u'Returns value indicating whether an Add-ins is loaded and connected.'), 'propput'], HRESULT, 'Connected',
              ( ['in'], VARIANT_BOOL, 'lpfConnect' )),
    COMMETHOD([dispid(7), helpstring(u'Returns an additional OLE automation object for support of other add-ins.'), 'propget'], HRESULT, 'Object',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'lppdisp' )),
    COMMETHOD([dispid(7), helpstring(u'Returns an additional OLE automation object for support of other add-ins.'), 'propput'], HRESULT, 'Object',
              ( ['in'], POINTER(IDispatch), 'lppdisp' )),
    COMMETHOD([dispid(301), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(302), helpstring(u'Returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstr' )),
    COMMETHOD([dispid(303), helpstring(u'Removes the Add-in from the collection of Add-ins, and makes it unavailable.')], HRESULT, 'Remove'),
    COMMETHOD([dispid(304), helpstring(u'Returns the location of a DLL containing localized resources, if available.'), 'propget'], HRESULT, 'SatelliteDllPath',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrPath' )),
]
################################################################
## code template for AddIn implementation
##class AddIn_Impl(object):
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def _get(self):
##        u"Returns a string containing the object's description."
##        #return lpbstr
##    def _set(self, lpbstr):
##        u"Returns a string containing the object's description."
##    Description = property(_get, _set, doc = _set.__doc__)
##
##    def Remove(self):
##        u'Removes the Add-in from the collection of Add-ins, and makes it unavailable.'
##        #return 
##
##    def _get(self):
##        u'Returns an additional OLE automation object for support of other add-ins.'
##        #return lppdisp
##    def _set(self, lppdisp):
##        u'Returns an additional OLE automation object for support of other add-ins.'
##    Object = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return lppaddins
##
##    def _get(self):
##        u'Returns value indicating whether an Add-ins is loaded and connected.'
##        #return lpfConnect
##    def _set(self, lpfConnect):
##        u'Returns value indicating whether an Add-ins is loaded and connected.'
##    Connected = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ProgID(self):
##        u"Returns the ProgID as obtained from the Add-in's registry entry."
##        #return lpbstr
##
##    @property
##    def SatelliteDllPath(self):
##        u'Returns the location of a DLL containing localized resources, if available.'
##        #return pbstrPath
##
##    @property
##    def Guid(self):
##        u"Returns the Add-in's CLSID as obtained from the Add-in's registry entry."
##        #return lpbstr
##
##    @property
##    def Name(self):
##        u'Returns the name of the object.'
##        #return lpbstr
##

vsDocumentKindHTML = u'{C76D83F8-A489-11D0-8195-00A0C91BBEE3}' # Constant STRING

# values for enumeration 'dbgBreakpointConditionType'
dbgBreakpointConditionTypeWhenTrue = 1
dbgBreakpointConditionTypeWhenChanged = 2
dbgBreakpointConditionType = c_int # enum
IExtensibleObjectSite._methods_ = [
    COMMETHOD([], HRESULT, 'NotifyDelete',
              ( ['in'], POINTER(IUnknown), 'punkObj' )),
]
################################################################
## code template for IExtensibleObjectSite implementation
##class IExtensibleObjectSite_Impl(object):
##    def NotifyDelete(self, punkObj):
##        '-no docstring-'
##        #return 
##

class ProjectItemsEvents(CoClass):
    u'The _ProjectItemsEvents object triggers events of actions taken against projects and their items.'
    _reg_clsid_ = GUID('{DE6C1098-93CA-4F49-BEF0-262A13CA1176}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _dispProjectItemsEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The _ProjectItemsEvents object triggers events of actions taken against projects and their items.'
    _iid_ = GUID('{6962753F-EFD5-41C5-B083-D70687166AEB}')
    _idlflags_ = []
    _methods_ = []
ProjectItemsEvents._com_interfaces_ = [_ProjectItemsEvents]
ProjectItemsEvents._outgoing_interfaces_ = [_dispProjectItemsEvents]

class WindowConfigurations(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Collection of window layouts available.'
    _iid_ = GUID('{E577442A-98E1-46C5-BD2E-D25807EC81CE}')
    _idlflags_ = ['dual', 'oleautomation']
class WindowConfiguration(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing a window layout.'
    _iid_ = GUID('{41D02413-8A67-4C28-A980-AD7539ED415D}')
    _idlflags_ = ['dual', 'oleautomation']
WindowConfigurations._methods_ = [
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'ppEnum' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(WindowConfiguration)), 'pWindowConfiguration' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pParent' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([dispid(4), helpstring(u'Adds a window to the collection of currently linked windows.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(WindowConfiguration)), 'pWindowConfiguration' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the name of the currently active window configuration.'), 'propget'], HRESULT, 'ActiveConfigurationName',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrName' )),
]
################################################################
## code template for WindowConfigurations implementation
##class WindowConfigurations_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return ppEnum
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return pParent
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return pWindowConfiguration
##
##    def Add(self, Name):
##        u'Adds a window to the collection of currently linked windows.'
##        #return pWindowConfiguration
##
##    @property
##    def ActiveConfigurationName(self):
##        u'Returns the name of the currently active window configuration.'
##        #return pbstrName
##

class BuildDependency(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object defining which projects must be built before the owning project can be built.'
    _iid_ = GUID('{9C5CEAAC-062F-4434-A2ED-78AB4D6134FE}')
    _idlflags_ = ['dual', 'oleautomation']
BuildDependencies._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(SolutionBuild)), 'ppSolutionBuild' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(BuildDependency)), 'ppOut' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
]
################################################################
## code template for BuildDependencies implementation
##class BuildDependencies_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return ppOut
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppSolutionBuild
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##

class _EnvironmentTaskList(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{4BC18A5B-DBB6-4AF5-A443-2E3F19365304}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_EnvironmentTaskList._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Prompts the user if it is OK to delete a task item.'), 'propget'], HRESULT, 'ConfirmTaskDeletion',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pConfirm' )),
    COMMETHOD([dispid(1), helpstring(u'Prompts the user if it is OK to delete a task item.'), 'propput'], HRESULT, 'ConfirmTaskDeletion',
              ( [], VARIANT_BOOL, 'pConfirm' )),
    COMMETHOD([dispid(2), helpstring(u'Displays UI to the user when a user task created that cannot be shown with the current filter.'), 'propget'], HRESULT, 'WarnOnAddingHiddenItem',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pWarn' )),
    COMMETHOD([dispid(2), helpstring(u'Displays UI to the user when a user task created that cannot be shown with the current filter.'), 'propput'], HRESULT, 'WarnOnAddingHiddenItem',
              ( [], VARIANT_BOOL, 'pWarn' )),
    COMMETHOD([dispid(3), helpstring(u'Gets/Sets the list of items that are comment tokens.'), 'propget'], HRESULT, 'CommentTokens',
              ( ['retval', 'out'], POINTER(VARIANT), 'pTokens' )),
    COMMETHOD([dispid(3), helpstring(u'Gets/Sets the list of items that are comment tokens.'), 'propput'], HRESULT, 'CommentTokens',
              ( [], VARIANT, 'pTokens' )),
]
################################################################
## code template for _EnvironmentTaskList implementation
##class _EnvironmentTaskList_Impl(object):
##    def _get(self):
##        u'Displays UI to the user when a user task created that cannot be shown with the current filter.'
##        #return pWarn
##    def _set(self, pWarn):
##        u'Displays UI to the user when a user task created that cannot be shown with the current filter.'
##    WarnOnAddingHiddenItem = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets the list of items that are comment tokens.'
##        #return pTokens
##    def _set(self, pTokens):
##        u'Gets/Sets the list of items that are comment tokens.'
##    CommentTokens = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Prompts the user if it is OK to delete a task item.'
##        #return pConfirm
##    def _set(self, pConfirm):
##        u'Prompts the user if it is OK to delete a task item.'
##    ConfirmTaskDeletion = property(_get, _set, doc = _set.__doc__)
##

class DebuggerEvents(CoClass):
    u'Events supported by the Debugger.'
    _reg_clsid_ = GUID('{0C763210-0FBB-11D3-B880-00C04F79E479}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _dispDebuggerEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{46209330-0FBA-11D3-B880-00C04F79E479}')
    _idlflags_ = []
    _methods_ = []
DebuggerEvents._com_interfaces_ = [_DebuggerEvents]
DebuggerEvents._outgoing_interfaces_ = [_dispDebuggerEvents]

WindowConfiguration._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(WindowConfigurations)), 'pWindowConfigurations' )),
    COMMETHOD([dispid(3), helpstring(u'Make the window layout the current layout.')], HRESULT, 'Apply',
              ( ['in', 'optional'], VARIANT_BOOL, 'FromCustomViews', True )),
    COMMETHOD([dispid(4), helpstring(u'Removes an object from a collection.')], HRESULT, 'Delete'),
    COMMETHOD([dispid(5), helpstring(u'Set the window layout contained in the object match the currently used layout.')], HRESULT, 'Update'),
]
################################################################
## code template for WindowConfiguration implementation
##class WindowConfiguration_Impl(object):
##    @property
##    def Name(self):
##        u'Returns the name of the object.'
##        #return pName
##
##    def Update(self):
##        u'Set the window layout contained in the object match the currently used layout.'
##        #return 
##
##    @property
##    def Collection(self):
##        u'Returns the parent object.'
##        #return pWindowConfigurations
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    def Apply(self, FromCustomViews):
##        u'Make the window layout the current layout.'
##        #return 
##
##    def Delete(self):
##        u'Removes an object from a collection.'
##        #return 
##

BuildDependency._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(BuildDependencies)), 'ppBuildDependencies' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the project that has a list of dependencies.'), 'propget'], HRESULT, 'Project',
              ( ['retval', 'out'], POINTER(POINTER(Project)), 'ppProject' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the project that has a list of dependencies.'), 'propget'], HRESULT, 'RequiredProjects',
              ( ['retval', 'out'], POINTER(VARIANT), 'pProjects' )),
    COMMETHOD([dispid(5), helpstring(u'Adds a project to the list of projects that must be built first.')], HRESULT, 'AddProject',
              ( [], BSTR, 'ProjectUniqueName' )),
    COMMETHOD([dispid(6), helpstring(u'Removes a project from the list of projects that must be built first.')], HRESULT, 'RemoveProject',
              ( [], BSTR, 'ProjectUniqueName' )),
    COMMETHOD([dispid(7), helpstring(u'Removes all projects from the list of projects that must be built first.')], HRESULT, 'RemoveAllProjects'),
]
################################################################
## code template for BuildDependency implementation
##class BuildDependency_Impl(object):
##    def RemoveProject(self, ProjectUniqueName):
##        u'Removes a project from the list of projects that must be built first.'
##        #return 
##
##    def AddProject(self, ProjectUniqueName):
##        u'Adds a project to the list of projects that must be built first.'
##        #return 
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppBuildDependencies
##
##    @property
##    def Project(self):
##        u'Returns the project that has a list of dependencies.'
##        #return ppProject
##
##    @property
##    def RequiredProjects(self):
##        u'Returns the project that has a list of dependencies.'
##        #return pProjects
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    def RemoveAllProjects(self):
##        u'Removes all projects from the list of projects that must be built first.'
##        #return 
##

class _EnvironmentFontsAndColors(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{F809CAB6-2C9F-41F2-A5AF-E26FB80E62AD}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_EnvironmentFontsAndColors._methods_ = [
]
################################################################
## code template for _EnvironmentFontsAndColors implementation
##class _EnvironmentFontsAndColors_Impl(object):

class _dispFindEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{C5331ACE-C5D5-11D2-8598-006097C68E81}')
    _idlflags_ = []
    _methods_ = []
_dispFindEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Event that is fired when a Find operation finishes.')], None, 'FindDone',
               ( ['in'], vsFindResult, 'Result' ),
               ( ['in'], VARIANT_BOOL, 'Cancelled' )),
]

# values for enumeration 'dbgEventReason'
dbgEventReasonNone = 1
dbgEventReasonGo = 2
dbgEventReasonAttachProgram = 3
dbgEventReasonDetachProgram = 4
dbgEventReasonLaunchProgram = 5
dbgEventReasonEndProgram = 6
dbgEventReasonStopDebugging = 7
dbgEventReasonStep = 8
dbgEventReasonBreakpoint = 9
dbgEventReasonExceptionThrown = 10
dbgEventReasonExceptionNotHandled = 11
dbgEventReasonUserBreak = 12
dbgEventReasonContextSwitch = 13
dbgEventReason = c_int # enum
class Process(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Used to examine and manipulate Processes.'
    _iid_ = GUID('{5C5A0070-F396-4E37-A82A-1B767E272DF9}')
    _idlflags_ = ['dual', 'oleautomation']
class Program(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Used to examine and manipulate Programs.'
    _iid_ = GUID('{6A38D87C-BBA0-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
class Thread(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Used to examine and manipulate Threads.'
    _iid_ = GUID('{9407F466-BBA1-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
class StackFrame(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Used to examine and manipulate stack-frames.  Essentially a stack frame is a function-call.'
    _iid_ = GUID('{1342D0D8-BBA3-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
_dispDebuggerEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Reflecting the overall state of the debugger, this event is fired when entering run-mode.  Note that this event may not fire when stepping.  It is typically best used when updating UI.')], None, 'OnEnterRunMode',
               ( ['in'], dbgEventReason, 'Reason' )),
    DISPMETHOD([dispid(2), helpstring(u'Reflecting the overall state of the debugger, this event is fired when leaving run-mode or debug-mode.  This event is fired whenever design-mode is established after debugging.')], None, 'OnEnterDesignMode',
               ( ['in'], dbgEventReason, 'Reason' )),
    DISPMETHOD([dispid(3), helpstring(u'Reflecting the overall state of the debugger, this event is fired when entering break-mode.  This event is fired regardless of how break mode is established.')], None, 'OnEnterBreakMode',
               ( ['in'], dbgEventReason, 'Reason' ),
               ( ['in', 'out'], POINTER(dbgExecutionAction), 'ExecutionAction' )),
    DISPMETHOD([dispid(4), helpstring(u"Thrown before OnEnterBreakMode.  Setting the action allows the handler to affect the IDE's UI upon exiting the handler.  The parameter is initially set to the value set by any prior handlers.")], None, 'OnExceptionThrown',
               ( ['in'], BSTR, 'ExceptionType' ),
               ( ['in'], BSTR, 'Name' ),
               ( ['in'], c_int, 'Code' ),
               ( ['in'], BSTR, 'Description' ),
               ( ['in', 'out'], POINTER(dbgExceptionAction), 'ExceptionAction' )),
    DISPMETHOD([dispid(5), helpstring(u"Thrown before OnEnterBreakMode.  Setting the action allows the handler to affect the IDE's UI upon exiting the handler.  The parameter is initially set to the value set by any prior handlers.")], None, 'OnExceptionNotHandled',
               ( ['in'], BSTR, 'ExceptionType' ),
               ( ['in'], BSTR, 'Name' ),
               ( ['in'], c_int, 'Code' ),
               ( ['in'], BSTR, 'Description' ),
               ( ['in', 'out'], POINTER(dbgExceptionAction), 'ExceptionAction' )),
    DISPMETHOD([dispid(6), helpstring(u'Fired whenever the current process, program, thread or stack has been changed through the UI or automation model.')], None, 'OnContextChanged',
               ( ['in'], POINTER(Process), 'NewProcess' ),
               ( ['in'], POINTER(Program), 'NewProgram' ),
               ( ['in'], POINTER(Thread), 'NewThread' ),
               ( ['in'], POINTER(StackFrame), 'NewStackFrame' )),
]
class Programs(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of Program objects.'
    _iid_ = GUID('{DC6A118A-BBAB-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
class Debugger(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Used to manipulate the general state of the debugger.'
    _iid_ = GUID('{338FB9A0-BAE5-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
Programs._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Program)), 'Program' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'Debugger' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for Programs implementation
##class Programs_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return Count
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return Program
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Debugger
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##

ISupportVSProperties._methods_ = [
    COMMETHOD([], HRESULT, 'NotifyPropertiesDelete'),
]
################################################################
## code template for ISupportVSProperties implementation
##class ISupportVSProperties_Impl(object):
##    def NotifyPropertiesDelete(self):
##        '-no docstring-'
##        #return 
##

class _OutputWindowEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The OutputWindowEvents object triggers events about the Output Window.'
    _iid_ = GUID('{0A3546A8-6840-11D2-97C1-00C04FB6C6FF}')
    _idlflags_ = ['oleautomation']
_OutputWindowEvents._methods_ = [
]
################################################################
## code template for _OutputWindowEvents implementation
##class _OutputWindowEvents_Impl(object):

class Threads(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of Thread objects.'
    _iid_ = GUID('{6AA23FB4-BBA1-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
Program._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns the name of the program.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD([dispid(100), helpstring(u'Returns the process by which this program is managed.'), 'propget'], HRESULT, 'Process',
              ( ['retval', 'out'], POINTER(POINTER(Process)), 'Process' )),
    COMMETHOD([dispid(101), helpstring(u'Returns the collection of threads being managed by this program.'), 'propget'], HRESULT, 'Threads',
              ( ['retval', 'out'], POINTER(POINTER(Threads)), 'Threads' )),
    COMMETHOD([dispid(102), helpstring(u'Indicates whether a program is being debugged at the instant this call is made.  Note that the program may change debug states even before this function call has a chance to return.'), 'propget'], HRESULT, 'IsBeingDebugged',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsBeingDebugged' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTE' )),
    COMMETHOD([dispid(201), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'Debugger' )),
    COMMETHOD([dispid(202), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(Programs)), 'Programs' )),
]
################################################################
## code template for Program implementation
##class Program_Impl(object):
##    @property
##    def Name(self):
##        u'Returns the name of the program.'
##        #return Name
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Debugger
##
##    @property
##    def Process(self):
##        u'Returns the process by which this program is managed.'
##        #return Process
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTE
##
##    @property
##    def IsBeingDebugged(self):
##        u'Indicates whether a program is being debugged at the instant this call is made.  Note that the program may change debug states even before this function call has a chance to return.'
##        #return IsBeingDebugged
##
##    @property
##    def Threads(self):
##        u'Returns the collection of threads being managed by this program.'
##        #return Threads
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return Programs
##

Threads._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Thread)), 'Thread' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'Debugger' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for Threads implementation
##class Threads_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return Count
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return Thread
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Debugger
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##

class StackFrames(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of StackFrame objects.'
    _iid_ = GUID('{4ED85664-BBA2-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
StackFrames._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(StackFrame)), 'StackFrame' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'Debugger' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for StackFrames implementation
##class StackFrames_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return Count
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return StackFrame
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Debugger
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##


# values for enumeration 'vsMovementOptions'
vsMovementOptionsMove = 0
vsMovementOptionsExtend = 1
vsMovementOptions = c_int # enum

# values for enumeration 'vsSmartFormatOptions'
vsSmartFormatOptionsNone = 0
vsSmartFormatOptionsBlock = 1
vsSmartFormatOptionsSmart = 2
vsSmartFormatOptions = c_int # enum
class _BuildEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides events for solution builds.'
    _iid_ = GUID('{794A2BA5-FFA6-4FC5-BF13-957B2C22EDD7}')
    _idlflags_ = ['oleautomation']
_BuildEvents._methods_ = [
]
################################################################
## code template for _BuildEvents implementation
##class _BuildEvents_Impl(object):


# values for enumeration 'vsGoToLineOptions'
vsGoToLineOptionsLast = -1
vsGoToLineOptionsFirst = -2
vsGoToLineOptions = c_int # enum
vsCATIDMiscFilesProjectItem = u'{610d4613-d0d5-11d2-8599-006097c68e81}' # Constant STRING

# values for enumeration 'vsFilterProperties'
vsFilterPropertiesNone = 0
vsFilterPropertiesAll = 1
vsFilterPropertiesSet = 2
vsFilterProperties = c_int # enum
vsCATIDMiscFilesProject = u'{610d4612-d0d5-11d2-8599-006097c68e81}' # Constant STRING
UIHierarchyItem._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(UIHierarchyItems)), 'ppUIHierarchyItems' )),
    COMMETHOD([dispid(0), helpstring(u'Returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrName' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the collection representing children of the item.'), 'propget'], HRESULT, 'UIHierarchyItems',
              ( ['retval', 'out'], POINTER(POINTER(UIHierarchyItems)), 'ppUIHierarchyItems' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the object behind the item.'), 'propget'], HRESULT, 'Object',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppDispatch' )),
    COMMETHOD([dispid(5), helpstring(u'Causes this item to become active in the user interface.')], HRESULT, 'Select',
              ( ['in'], vsUISelectionType, 'How' )),
    COMMETHOD([dispid(6), helpstring(u'Returns True if the item is selected, False otherwise.'), 'propget'], HRESULT, 'IsSelected',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfSelected' )),
]
################################################################
## code template for UIHierarchyItem implementation
##class UIHierarchyItem_Impl(object):
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    @property
##    def Object(self):
##        u'Returns the object behind the item.'
##        #return ppDispatch
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppUIHierarchyItems
##
##    @property
##    def IsSelected(self):
##        u'Returns True if the item is selected, False otherwise.'
##        #return pfSelected
##
##    @property
##    def UIHierarchyItems(self):
##        u'Returns the collection representing children of the item.'
##        #return ppUIHierarchyItems
##
##    def Select(self, How):
##        u'Causes this item to become active in the user interface.'
##        #return 
##
##    @property
##    def Name(self):
##        u'Returns the name of the object.'
##        #return pbstrName
##

vsCATIDGenericProject = u'{610d4616-d0d5-11d2-8599-006097c68e81}' # Constant STRING
vsCATIDDocument = u'{610d4611-d0d5-11d2-8599-006097c68e81}' # Constant STRING

# values for enumeration 'vsInsertFlags'
vsInsertFlagsCollapseToEnd = 1
vsInsertFlagsCollapseToStart = 2
vsInsertFlagsContainNewText = 4
vsInsertFlagsInsertAtEnd = 8
vsInsertFlagsInsertAtStart = 16
vsInsertFlags = c_int # enum
class BuildEvents(CoClass):
    u'Provides events for solution builds.'
    _reg_clsid_ = GUID('{D83D60E3-229F-4660-8DD0-28B629EEDCDA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _dispBuildEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{1926364E-6B90-46CB-A44D-8A80FB11ACD9}')
    _idlflags_ = []
    _methods_ = []
BuildEvents._com_interfaces_ = [_BuildEvents]
BuildEvents._outgoing_interfaces_ = [_dispBuildEvents]

class TextPanes(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of text panes representing different views on the same document.'
    _iid_ = GUID('{D9013D31-3652-46B2-A25A-29A881B9F86B}')
    _idlflags_ = ['dual', 'oleautomation']
TextPane._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(TextPanes)), 'ppPanes' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the window containing this object.'), 'propget'], HRESULT, 'Window',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'ppWin' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the height of the window in character units.'), 'propget'], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_int), 'pHeight' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the width of the window in character units.'), 'propget'], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_int), 'pWidth' )),
    COMMETHOD([dispid(8), helpstring(u'Returns an object representing the selection on this object.'), 'propget'], HRESULT, 'Selection',
              ( ['retval', 'out'], POINTER(POINTER(TextSelection)), 'ppSel' )),
    COMMETHOD([dispid(9), helpstring(u"Returns a TextPoint object representing the beginning of the object's text."), 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Moves the focus to the current item.')], HRESULT, 'Activate'),
    COMMETHOD([dispid(10), helpstring(u'Returns whether the indicated span of text is fully visible in the pane.')], HRESULT, 'IsVisible',
              ( ['in'], POINTER(TextPoint), 'Point' ),
              ( ['in', 'optional'], VARIANT, 'PointOrCount' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbResult' )),
    COMMETHOD([dispid(11), helpstring(u'Scrolls the pane vertically to make the indicated span of text visible.')], HRESULT, 'TryToShow',
              ( ['in'], POINTER(TextPoint), 'Point' ),
              ( ['in', 'optional'], vsPaneShowHow, 'How', 2 ),
              ( ['in', 'optional'], VARIANT, 'PointOrCount' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbResult' )),
]
################################################################
## code template for TextPane implementation
##class TextPane_Impl(object):
##    def TryToShow(self, Point, How, PointOrCount):
##        u'Scrolls the pane vertically to make the indicated span of text visible.'
##        #return pbResult
##
##    @property
##    def Selection(self):
##        u'Returns an object representing the selection on this object.'
##        #return ppSel
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppPanes
##
##    @property
##    def Height(self):
##        u'Returns the height of the window in character units.'
##        #return pHeight
##
##    @property
##    def Width(self):
##        u'Returns the width of the window in character units.'
##        #return pWidth
##
##    @property
##    def Window(self):
##        u'Returns the window containing this object.'
##        #return ppWin
##
##    def Activate(self):
##        u'Moves the focus to the current item.'
##        #return 
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    def IsVisible(self, Point, PointOrCount):
##        u'Returns whether the indicated span of text is fully visible in the pane.'
##        #return pbResult
##
##    @property
##    def StartPoint(self):
##        u"Returns a TextPoint object representing the beginning of the object's text."
##        #return ppPoint
##

Configurations._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppParent' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Configuration)), 'ppOut' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object type.'), 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(vsConfigurationType), 'pType' )),
]
################################################################
## code template for Configurations implementation
##class Configurations_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Name(self):
##        u'Returns the name of the object.'
##        #return pName
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppParent
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return ppOut
##
##    @property
##    def Type(self):
##        u'Returns an enumeration indicating the object type.'
##        #return pType
##


# values for enumeration 'vsBuildScope'
vsBuildScopeSolution = 1
vsBuildScopeBatch = 2
vsBuildScopeProject = 3
vsBuildScope = c_int # enum

# values for enumeration 'vsBuildAction'
vsBuildActionBuild = 1
vsBuildActionRebuildAll = 2
vsBuildActionClean = 3
vsBuildActionDeploy = 4
vsBuildAction = c_int # enum
_dispBuildEvents._disp_methods_ = [
    DISPMETHOD([dispid(3)], None, 'OnBuildBegin',
               ( [], vsBuildScope, 'Scope' ),
               ( [], vsBuildAction, 'Action' )),
    DISPMETHOD([dispid(4)], None, 'OnBuildDone',
               ( [], vsBuildScope, 'Scope' ),
               ( [], vsBuildAction, 'Action' )),
    DISPMETHOD([dispid(5)], None, 'OnBuildProjConfigBegin',
               ( [], BSTR, 'Project' ),
               ( [], BSTR, 'ProjectConfig' ),
               ( [], BSTR, 'Platform' ),
               ( [], BSTR, 'SolutionConfig' )),
    DISPMETHOD([dispid(6)], None, 'OnBuildProjConfigDone',
               ( [], BSTR, 'Project' ),
               ( [], BSTR, 'ProjectConfig' ),
               ( [], BSTR, 'Platform' ),
               ( [], BSTR, 'SolutionConfig' ),
               ( [], VARIANT_BOOL, 'Success' )),
]
class IExtenderProviderUnk(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object that represents an Extender Provider.'
    _iid_ = GUID('{F69B64A3-9017-4E48-9784-E152B51AA722}')
    _idlflags_ = ['dual', 'oleautomation']
class IExtenderSite(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Site Object for an Automation Extender.'
    _iid_ = GUID('{E57C510B-968B-4A3C-A467-EE4013157DC9}')
    _idlflags_ = ['dual', 'oleautomation']
IExtenderProviderUnk._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Get an Extender for the given object under the specified category.')], HRESULT, 'GetExtender',
              ( ['in'], BSTR, 'ExtenderCATID' ),
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['in'], POINTER(IUnknown), 'ExtendeeObject' ),
              ( ['in'], POINTER(IExtenderSite), 'ExtenderSite' ),
              ( ['in'], c_int, 'Cookie' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(2), helpstring(u'Returns True if the Provider can provide an Extender for the given object under the specified category.')], HRESULT, 'CanExtend',
              ( ['in'], BSTR, 'ExtenderCATID' ),
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['in'], POINTER(IUnknown), 'ExtendeeObject' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'fRetval' )),
]
################################################################
## code template for IExtenderProviderUnk implementation
##class IExtenderProviderUnk_Impl(object):
##    def GetExtender(self, ExtenderCATID, ExtenderName, ExtendeeObject, ExtenderSite, Cookie):
##        u'Get an Extender for the given object under the specified category.'
##        #return Extender
##
##    def CanExtend(self, ExtenderCATID, ExtenderName, ExtendeeObject):
##        u'Returns True if the Provider can provide an Extender for the given object under the specified category.'
##        #return fRetval
##


# values for enumeration 'dbgDebugMode'
dbgDesignMode = 1
dbgBreakMode = 2
dbgRunMode = 3
dbgDebugMode = c_int # enum
vsWindowKindThread = u'{E62CE6A0-B439-11D0-A79D-00A0C9110051}' # Constant STRING
AddIns._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(AddIn)), 'lppaddin' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'lppaReturn' )),
    COMMETHOD([dispid(40), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'lplReturn' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(41), helpstring(u'Updates the collection as if the Add-in Manager Dialog was opened.')], HRESULT, 'Update'),
    COMMETHOD([dispid(100), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(102), helpstring(u'Adds an Add-in to the collection.')], HRESULT, 'Add',
              ( [], BSTR, 'ProgID' ),
              ( [], BSTR, 'Description' ),
              ( [], BSTR, 'Name' ),
              ( [], VARIANT_BOOL, 'Connected' ),
              ( ['retval', 'out'], POINTER(POINTER(AddIn)), '__MIDL__AddIns0000' )),
]
################################################################
## code template for AddIns implementation
##class AddIns_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return lplReturn
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppaReturn
##
##    def Update(self):
##        u'Updates the collection as if the Add-in Manager Dialog was opened.'
##        #return 
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return lppaddin
##
##    def Add(self, ProgID, Description, Name, Connected):
##        u'Adds an Add-in to the collection.'
##        #return __MIDL__AddIns0000
##

class FindEvents(CoClass):
    u'Provides events for Find operations.'
    _reg_clsid_ = GUID('{811322BC-042D-4828-BFF2-640EF8B7209F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
FindEvents._com_interfaces_ = [_FindEvents]
FindEvents._outgoing_interfaces_ = [_dispFindEvents]

vsWindowKindLocals = u'{4A18F9D0-B838-11D0-93EB-00A0C90F2734}' # Constant STRING
class Find(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing Find Symbol.'
    _iid_ = GUID('{40D4B9B6-739B-4965-8D65-692AEC692266}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsFindAction'
vsFindActionFind = 1
vsFindActionFindAll = 2
vsFindActionReplace = 3
vsFindActionReplaceAll = 4
vsFindActionBookmarkAll = 5
vsFindAction = c_int # enum

# values for enumeration 'vsFindTarget'
vsFindTargetCurrentDocument = 1
vsFindTargetCurrentDocumentSelection = 2
vsFindTargetCurrentDocumentFunction = 3
vsFindTargetOpenDocuments = 4
vsFindTargetCurrentProject = 5
vsFindTargetSolution = 6
vsFindTargetFiles = 7
vsFindTarget = c_int # enum
Find._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(3), helpstring(u'Gets/Sets the Find action to be performed.'), 'propget'], HRESULT, 'Action',
              ( ['retval', 'out'], POINTER(vsFindAction), 'pAction' )),
    COMMETHOD([dispid(3), helpstring(u'Gets/Sets the Find action to be performed.'), 'propput'], HRESULT, 'Action',
              ( ['in'], vsFindAction, 'pAction' )),
    COMMETHOD([dispid(4), helpstring(u'Gets/Sets the text/pattern to be searched.'), 'propget'], HRESULT, 'FindWhat',
              ( ['retval', 'out'], POINTER(BSTR), 'pFindWhat' )),
    COMMETHOD([dispid(4), helpstring(u'Gets/Sets the text/pattern to be searched.'), 'propput'], HRESULT, 'FindWhat',
              ( ['in'], BSTR, 'pFindWhat' )),
    COMMETHOD([dispid(5), helpstring(u'Gets/Sets whether or not the search is case sensitive.'), 'propget'], HRESULT, 'MatchCase',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pMatchCase' )),
    COMMETHOD([dispid(5), helpstring(u'Gets/Sets whether or not the search is case sensitive.'), 'propput'], HRESULT, 'MatchCase',
              ( ['in'], VARIANT_BOOL, 'pMatchCase' )),
    COMMETHOD([dispid(6), helpstring(u'Gets/Sets whether or not the search matches whole words.'), 'propget'], HRESULT, 'MatchWholeWord',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pMatchWholeWord' )),
    COMMETHOD([dispid(6), helpstring(u'Gets/Sets whether or not the search matches whole words.'), 'propput'], HRESULT, 'MatchWholeWord',
              ( ['in'], VARIANT_BOOL, 'pMatchWholeWord' )),
    COMMETHOD([dispid(7), helpstring(u'Gets/Sets whether or not hidden text is included in the search.'), 'propget'], HRESULT, 'MatchInHiddenText',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pMatchInHiddenText' )),
    COMMETHOD([dispid(7), helpstring(u'Gets/Sets whether or not hidden text is included in the search.'), 'propput'], HRESULT, 'MatchInHiddenText',
              ( ['in'], VARIANT_BOOL, 'pMatchInHiddenText' )),
    COMMETHOD([dispid(8), helpstring(u'Gets/Sets whether the search is performed backwards from the current position.'), 'propget'], HRESULT, 'Backwards',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pBackwards' )),
    COMMETHOD([dispid(8), helpstring(u'Gets/Sets whether the search is performed backwards from the current position.'), 'propput'], HRESULT, 'Backwards',
              ( ['in'], VARIANT_BOOL, 'pBackwards' )),
    COMMETHOD([dispid(9), helpstring(u'Gets/Sets whether or not sub-folders are searched for a Find in Files operation.'), 'propget'], HRESULT, 'SearchSubfolders',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pSearchSubfolders' )),
    COMMETHOD([dispid(9), helpstring(u'Gets/Sets whether or not sub-folders are searched for a Find in Files operation.'), 'propput'], HRESULT, 'SearchSubfolders',
              ( ['in'], VARIANT_BOOL, 'pSearchSubfolders' )),
    COMMETHOD([dispid(10), helpstring(u'Gets/Sets whether or not modified documents remain open after a Replace operation.'), 'propget'], HRESULT, 'KeepModifiedDocumentsOpen',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pKeepModifiedDocumentsOpen' )),
    COMMETHOD([dispid(10), helpstring(u'Gets/Sets whether or not modified documents remain open after a Replace operation.'), 'propput'], HRESULT, 'KeepModifiedDocumentsOpen',
              ( ['in'], VARIANT_BOOL, 'pKeepModifiedDocumentsOpen' )),
    COMMETHOD([dispid(11), helpstring(u'Gets/Sets the syntax used to specify the search pattern.'), 'propget'], HRESULT, 'PatternSyntax',
              ( ['retval', 'out'], POINTER(vsFindPatternSyntax), 'pPatternSyntax' )),
    COMMETHOD([dispid(11), helpstring(u'Gets/Sets the syntax used to specify the search pattern.'), 'propput'], HRESULT, 'PatternSyntax',
              ( ['in'], vsFindPatternSyntax, 'pPatternSyntax' )),
    COMMETHOD([dispid(12), helpstring(u'Gets/Sets the replacement text for a Replace operation.'), 'propget'], HRESULT, 'ReplaceWith',
              ( ['retval', 'out'], POINTER(BSTR), 'pReplaceWith' )),
    COMMETHOD([dispid(12), helpstring(u'Gets/Sets the replacement text for a Replace operation.'), 'propput'], HRESULT, 'ReplaceWith',
              ( ['in'], BSTR, 'pReplaceWith' )),
    COMMETHOD([dispid(13), helpstring(u'Gets/Sets the target of the search operation.'), 'propget'], HRESULT, 'Target',
              ( ['retval', 'out'], POINTER(vsFindTarget), 'pTarget' )),
    COMMETHOD([dispid(13), helpstring(u'Gets/Sets the target of the search operation.'), 'propput'], HRESULT, 'Target',
              ( ['in'], vsFindTarget, 'pTarget' )),
    COMMETHOD([dispid(14), helpstring(u'Gets/Sets the search path for a Find in Files operation.'), 'propget'], HRESULT, 'SearchPath',
              ( ['retval', 'out'], POINTER(BSTR), 'pSearchPath' )),
    COMMETHOD([dispid(14), helpstring(u'Gets/Sets the search path for a Find in Files operation.'), 'propput'], HRESULT, 'SearchPath',
              ( ['in'], BSTR, 'pSearchPath' )),
    COMMETHOD([dispid(15), helpstring(u'Gets/Sets the file masks for the files to be searched.'), 'propget'], HRESULT, 'FilesOfType',
              ( ['retval', 'out'], POINTER(BSTR), 'pFilesOfType' )),
    COMMETHOD([dispid(15), helpstring(u'Gets/Sets the file masks for the files to be searched.'), 'propput'], HRESULT, 'FilesOfType',
              ( ['in'], BSTR, 'pFilesOfType' )),
    COMMETHOD([dispid(16), helpstring(u'Gets/Sets the location of where the search results are shown for a bulk search operation.'), 'propget'], HRESULT, 'ResultsLocation',
              ( ['retval', 'out'], POINTER(vsFindResultsLocation), 'pResultsLocation' )),
    COMMETHOD([dispid(16), helpstring(u'Gets/Sets the location of where the search results are shown for a bulk search operation.'), 'propput'], HRESULT, 'ResultsLocation',
              ( ['in'], vsFindResultsLocation, 'pResultsLocation' )),
    COMMETHOD([dispid(17), helpstring(u'Performs a search based on the options set on the Find object.')], HRESULT, 'Execute',
              ( ['retval', 'out'], POINTER(vsFindResult), 'pResult' )),
    COMMETHOD([dispid(0), helpstring(u'Performs a search based on options passed in to this method without changing any options on the Find object.')], HRESULT, 'FindReplace',
              ( ['in'], vsFindAction, 'Action' ),
              ( ['in'], BSTR, 'FindWhat' ),
              ( ['in', 'optional'], c_int, 'vsFindOptionsValue', 0 ),
              ( ['in', 'optional'], BSTR, 'ReplaceWith', u'' ),
              ( ['in', 'optional'], vsFindTarget, 'Target', 1 ),
              ( ['in', 'optional'], BSTR, 'SearchPath', u'' ),
              ( ['in', 'optional'], BSTR, 'FilesOfType', u'' ),
              ( ['in', 'optional'], vsFindResultsLocation, 'ResultsLocation', 1 ),
              ( ['retval', 'out'], POINTER(vsFindResult), 'pResult' )),
]
################################################################
## code template for Find implementation
##class Find_Impl(object):
##    def _get(self):
##        u'Gets/Sets whether or not modified documents remain open after a Replace operation.'
##        #return pKeepModifiedDocumentsOpen
##    def _set(self, pKeepModifiedDocumentsOpen):
##        u'Gets/Sets whether or not modified documents remain open after a Replace operation.'
##    KeepModifiedDocumentsOpen = property(_get, _set, doc = _set.__doc__)
##
##    def Execute(self):
##        u'Performs a search based on the options set on the Find object.'
##        #return pResult
##
##    def _get(self):
##        u'Gets/Sets the text/pattern to be searched.'
##        #return pFindWhat
##    def _set(self, pFindWhat):
##        u'Gets/Sets the text/pattern to be searched.'
##    FindWhat = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets the location of where the search results are shown for a bulk search operation.'
##        #return pResultsLocation
##    def _set(self, pResultsLocation):
##        u'Gets/Sets the location of where the search results are shown for a bulk search operation.'
##    ResultsLocation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets the target of the search operation.'
##        #return pTarget
##    def _set(self, pTarget):
##        u'Gets/Sets the target of the search operation.'
##    Target = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppaReturn
##
##    def _get(self):
##        u'Gets/Sets whether or not hidden text is included in the search.'
##        #return pMatchInHiddenText
##    def _set(self, pMatchInHiddenText):
##        u'Gets/Sets whether or not hidden text is included in the search.'
##    MatchInHiddenText = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets the replacement text for a Replace operation.'
##        #return pReplaceWith
##    def _set(self, pReplaceWith):
##        u'Gets/Sets the replacement text for a Replace operation.'
##    ReplaceWith = property(_get, _set, doc = _set.__doc__)
##
##    def FindReplace(self, Action, FindWhat, vsFindOptionsValue, ReplaceWith, Target, SearchPath, FilesOfType, ResultsLocation):
##        u'Performs a search based on options passed in to this method without changing any options on the Find object.'
##        #return pResult
##
##    def _get(self):
##        u'Gets/Sets whether or not sub-folders are searched for a Find in Files operation.'
##        #return pSearchSubfolders
##    def _set(self, pSearchSubfolders):
##        u'Gets/Sets whether or not sub-folders are searched for a Find in Files operation.'
##    SearchSubfolders = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets whether or not the search is case sensitive.'
##        #return pMatchCase
##    def _set(self, pMatchCase):
##        u'Gets/Sets whether or not the search is case sensitive.'
##    MatchCase = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets the file masks for the files to be searched.'
##        #return pFilesOfType
##    def _set(self, pFilesOfType):
##        u'Gets/Sets the file masks for the files to be searched.'
##    FilesOfType = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets the search path for a Find in Files operation.'
##        #return pSearchPath
##    def _set(self, pSearchPath):
##        u'Gets/Sets the search path for a Find in Files operation.'
##    SearchPath = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets whether the search is performed backwards from the current position.'
##        #return pBackwards
##    def _set(self, pBackwards):
##        u'Gets/Sets whether the search is performed backwards from the current position.'
##    Backwards = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def _get(self):
##        u'Gets/Sets whether or not the search matches whole words.'
##        #return pMatchWholeWord
##    def _set(self, pMatchWholeWord):
##        u'Gets/Sets whether or not the search matches whole words.'
##    MatchWholeWord = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets the Find action to be performed.'
##        #return pAction
##    def _set(self, pAction):
##        u'Gets/Sets the Find action to be performed.'
##    Action = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets the syntax used to specify the search pattern.'
##        #return pPatternSyntax
##    def _set(self, pPatternSyntax):
##        u'Gets/Sets the syntax used to specify the search pattern.'
##    PatternSyntax = property(_get, _set, doc = _set.__doc__)
##

class Library(object):
    u'Microsoft Development Environment 8.0 (Version 7.0 Object Model)'
    name = u'EnvDTE'
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)

class OutputWindowPanes(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object containing OutputWindowPanes.'
    _iid_ = GUID('{B02CF62A-9470-4308-A521-9675FBA395AB}')
    _idlflags_ = ['dual', 'oleautomation']
class OutputWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object representing the output window.'
    _iid_ = GUID('{EAB0A63D-C3A8-496E-9ACF-A82CEF6A43B3}')
    _idlflags_ = ['dual', 'oleautomation']
class OutputWindowPane(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object used for displaying text output to the user.'
    _iid_ = GUID('{FFC9DFC4-61CA-4B0C-83C2-0703A24F5C16}')
    _idlflags_ = ['dual', 'oleautomation']
OutputWindowPanes._methods_ = [
    COMMETHOD([dispid(2), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(OutputWindow)), 'pOutputWindow' )),
    COMMETHOD([dispid(4), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([dispid(5), helpstring(u'Creates a new pane and adds it to the collection.')], HRESULT, 'Add',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(OutputWindowPane)), 'pOutputWindowPane' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( [], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(OutputWindowPane)), 'pOutputWindowPane' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
]
################################################################
## code template for OutputWindowPanes implementation
##class OutputWindowPanes_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return pOutputWindow
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return pOutputWindowPane
##
##    def Add(self, Name):
##        u'Creates a new pane and adds it to the collection.'
##        #return pOutputWindowPane
##

class WindowEvents(CoClass):
    u'The WindowEvents object triggers events about Windows.'
    _reg_clsid_ = GUID('{2E260FD4-C130-4E6D-8EBC-4A3BFD188181}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _dispWindowEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The WindowEvents object triggers events about Windows.'
    _iid_ = GUID('{0D3A23A9-67BB-11D2-97C1-00C04FB6C6FF}')
    _idlflags_ = []
    _methods_ = []
WindowEvents._com_interfaces_ = [_WindowEvents]
WindowEvents._outgoing_interfaces_ = [_dispWindowEvents]

class Expressions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of Expression objects.'
    _iid_ = GUID('{2685337A-BB9E-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
StackFrame._methods_ = [
    COMMETHOD([dispid(100), helpstring(u'Returns the programming language associated with this stack frame.'), 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'Language' )),
    COMMETHOD([dispid(0), helpstring(u'Returns the function name of this stack frame.'), 'propget'], HRESULT, 'FunctionName',
              ( ['retval', 'out'], POINTER(BSTR), 'FunctionName' )),
    COMMETHOD([dispid(102), helpstring(u'Returns the return type of this stack frame.'), 'propget'], HRESULT, 'ReturnType',
              ( ['retval', 'out'], POINTER(BSTR), 'ReturnType' )),
    COMMETHOD([dispid(103), helpstring(u'Returns a collection of expressions representing the locals currently known by this frame.'), 'propget'], HRESULT, 'Locals',
              ( ['retval', 'out'], POINTER(POINTER(Expressions)), 'Expressions' )),
    COMMETHOD([dispid(104), helpstring(u'Returns a collection of expressions representing the arguments passed to this frame.'), 'propget'], HRESULT, 'Arguments',
              ( ['retval', 'out'], POINTER(POINTER(Expressions)), 'Expressions' )),
    COMMETHOD([dispid(105), helpstring(u'Returns the module name for this stack frame.'), 'propget'], HRESULT, 'Module',
              ( ['retval', 'out'], POINTER(BSTR), 'Module' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTE' )),
    COMMETHOD([dispid(201), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Thread)), 'Thread' )),
    COMMETHOD([dispid(202), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(StackFrames)), 'StackFrames' )),
]
################################################################
## code template for StackFrame implementation
##class StackFrame_Impl(object):
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return StackFrames
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTE
##
##    @property
##    def FunctionName(self):
##        u'Returns the function name of this stack frame.'
##        #return FunctionName
##
##    @property
##    def Language(self):
##        u'Returns the programming language associated with this stack frame.'
##        #return Language
##
##    @property
##    def Module(self):
##        u'Returns the module name for this stack frame.'
##        #return Module
##
##    @property
##    def Arguments(self):
##        u'Returns a collection of expressions representing the arguments passed to this frame.'
##        #return Expressions
##
##    @property
##    def ReturnType(self):
##        u'Returns the return type of this stack frame.'
##        #return ReturnType
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Thread
##
##    @property
##    def Locals(self):
##        u'Returns a collection of expressions representing the locals currently known by this frame.'
##        #return Expressions
##

class _TaskListEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The TaskListEvents object triggers events about the Task List.'
    _iid_ = GUID('{1125C422-49BD-11D2-8823-00C04FB6C6FF}')
    _idlflags_ = ['oleautomation']
_TaskListEvents._methods_ = [
]
################################################################
## code template for _TaskListEvents implementation
##class _TaskListEvents_Impl(object):


# values for enumeration 'vsMoveToColumnLine'
vsMoveToColumnLineFirst = 0
vsMoveToColumnLineLast = 1
vsMoveToColumnLine = c_int # enum
class OutputGroup(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object detailing which files are build by the project.'
    _iid_ = GUID('{A3A80783-875F-435B-9639-E5CE888DF737}')
    _idlflags_ = ['dual', 'oleautomation']
OutputGroups._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Configuration)), 'ppConfiguration' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(OutputGroup)), 'ppOut' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
]
################################################################
## code template for OutputGroups implementation
##class OutputGroups_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return ppOut
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppConfiguration
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##

_dispWindowEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Occurs just before a window is closed.')], None, 'WindowClosing',
               ( ['in'], POINTER(Window), 'Window' )),
    DISPMETHOD([dispid(2), helpstring(u'Occurs when a window has been moved.')], None, 'WindowMoved',
               ( ['in'], POINTER(Window), 'Window' ),
               ( ['in'], c_int, 'Top' ),
               ( ['in'], c_int, 'Left' ),
               ( ['in'], c_int, 'Width' ),
               ( ['in'], c_int, 'Height' )),
    DISPMETHOD([dispid(3), helpstring(u'Occurs when a window receives focus.')], None, 'WindowActivated',
               ( ['in'], POINTER(Window), 'GotFocus' ),
               ( ['in'], POINTER(Window), 'LostFocus' )),
    DISPMETHOD([dispid(4), helpstring(u'Occurs when a new window is made.')], None, 'WindowCreated',
               ( ['in'], POINTER(Window), 'Window' )),
]

# values for enumeration 'vsEPReplaceTextOptions'
vsEPReplaceTextKeepMarkers = 1
vsEPReplaceTextNormalizeNewlines = 2
vsEPReplaceTextTabsSpaces = 4
vsEPReplaceTextAutoformat = 8
vsEPReplaceTextOptions = c_int # enum
_dispProjectItemsEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Triggered when an item is added to a project.')], None, 'ItemAdded',
               ( ['in'], POINTER(ProjectItem), 'ProjectItem' )),
    DISPMETHOD([dispid(2), helpstring(u'Triggered when an item is removed from a project.')], None, 'ItemRemoved',
               ( ['in'], POINTER(ProjectItem), 'ProjectItem' )),
    DISPMETHOD([dispid(3), helpstring(u'Triggered when an item within a project is renamed.')], None, 'ItemRenamed',
               ( ['in'], POINTER(ProjectItem), 'ProjectItem' ),
               ( ['in'], BSTR, 'OldName' )),
]

# values for enumeration 'vsLinkedWindowType'
vsLinkedWindowTypeDocked = 0
vsLinkedWindowTypeVertical = 2
vsLinkedWindowTypeHorizontal = 3
vsLinkedWindowTypeTabbed = 1
vsLinkedWindowType = c_int # enum
class Processes(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of Process objects.'
    _iid_ = GUID('{9F379969-5EAC-4A54-B2BC-6946CFFB56EF}')
    _idlflags_ = ['dual', 'oleautomation']
Processes._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Process)), 'Process' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'Debugger' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for Processes implementation
##class Processes_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return Count
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return Process
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Debugger
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##

class OutputWindowEvents(CoClass):
    u'The OutputWindowEvents object triggers events about the Output Window.'
    _reg_clsid_ = GUID('{3760037F-B012-44F8-9C23-3609D7A16DEF}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _dispOutputWindowEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The OutputWindowEvents object triggers events about the Output Window.'
    _iid_ = GUID('{0D3A23AF-67BB-11D2-97C1-00C04FB6C6FF}')
    _idlflags_ = []
    _methods_ = []
OutputWindowEvents._com_interfaces_ = [_OutputWindowEvents]
OutputWindowEvents._outgoing_interfaces_ = [_dispOutputWindowEvents]

class IVsTextEditPerLanguage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{5943BD7E-D722-42DB-A251-FE2ADD8711EA}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
IVsTextEditPerLanguage._methods_ = [
    COMMETHOD([dispid(1), 'propput'], HRESULT, 'TabSize',
              ( ['in'], c_short, 'piTabSize' )),
    COMMETHOD([dispid(1), 'propget'], HRESULT, 'TabSize',
              ( ['retval', 'out'], POINTER(c_short), 'piTabSize' )),
    COMMETHOD([dispid(2), 'propput'], HRESULT, 'IndentSize',
              ( ['in'], c_short, 'piIndentSize' )),
    COMMETHOD([dispid(2), 'propget'], HRESULT, 'IndentSize',
              ( ['retval', 'out'], POINTER(c_short), 'piIndentSize' )),
    COMMETHOD([dispid(3), 'propput'], HRESULT, 'InsertTabs',
              ( ['in'], VARIANT_BOOL, 'pfInsertTabs' )),
    COMMETHOD([dispid(3), 'propget'], HRESULT, 'InsertTabs',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfInsertTabs' )),
    COMMETHOD([dispid(4), 'propput'], HRESULT, 'IndentStyle',
              ( ['in'], vsIndentStyle, 'pfIndentStyle' )),
    COMMETHOD([dispid(4), 'propget'], HRESULT, 'IndentStyle',
              ( ['retval', 'out'], POINTER(vsIndentStyle), 'pfIndentStyle' )),
    COMMETHOD([dispid(5), 'propput'], HRESULT, 'AutoListMembers',
              ( ['in'], VARIANT_BOOL, 'pfAutoListMembers' )),
    COMMETHOD([dispid(5), 'propget'], HRESULT, 'AutoListMembers',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfAutoListMembers' )),
    COMMETHOD([dispid(6), 'propput'], HRESULT, 'AutoListParams',
              ( ['in'], VARIANT_BOOL, 'pfAutoListParams' )),
    COMMETHOD([dispid(6), 'propget'], HRESULT, 'AutoListParams',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfAutoListParams' )),
    COMMETHOD([dispid(7), 'propput'], HRESULT, 'VirtualSpace',
              ( ['in'], VARIANT_BOOL, 'pfVirtualSpace' )),
    COMMETHOD([dispid(7), 'propget'], HRESULT, 'VirtualSpace',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfVirtualSpace' )),
    COMMETHOD([dispid(8), 'propput'], HRESULT, 'EnableLeftClickForURLs',
              ( ['in'], VARIANT_BOOL, 'pfHotURLs' )),
    COMMETHOD([dispid(8), 'propget'], HRESULT, 'EnableLeftClickForURLs',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfHotURLs' )),
    COMMETHOD([dispid(9), 'propput'], HRESULT, 'WordWrap',
              ( ['in'], VARIANT_BOOL, 'pfWrap' )),
    COMMETHOD([dispid(9), 'propget'], HRESULT, 'WordWrap',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfWrap' )),
    COMMETHOD([dispid(10), 'propput'], HRESULT, 'ShowLineNumbers',
              ( ['in'], VARIANT_BOOL, 'pfshow' )),
    COMMETHOD([dispid(10), 'propget'], HRESULT, 'ShowLineNumbers',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfshow' )),
    COMMETHOD([dispid(11), 'propput'], HRESULT, 'ShowNavigationBar',
              ( ['in'], VARIANT_BOOL, 'pfshow' )),
    COMMETHOD([dispid(11), 'propget'], HRESULT, 'ShowNavigationBar',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfshow' )),
    COMMETHOD([dispid(13), 'propput'], HRESULT, 'HideAdvancedMembers',
              ( ['in'], VARIANT_BOOL, 'pfHide' )),
    COMMETHOD([dispid(13), 'propget'], HRESULT, 'HideAdvancedMembers',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfHide' )),
]
################################################################
## code template for IVsTextEditPerLanguage implementation
##class IVsTextEditPerLanguage_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return pfIndentStyle
##    def _set(self, pfIndentStyle):
##        '-no docstring-'
##    IndentStyle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfHotURLs
##    def _set(self, pfHotURLs):
##        '-no docstring-'
##    EnableLeftClickForURLs = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfAutoListParams
##    def _set(self, pfAutoListParams):
##        '-no docstring-'
##    AutoListParams = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return piIndentSize
##    def _set(self, piIndentSize):
##        '-no docstring-'
##    IndentSize = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfHide
##    def _set(self, pfHide):
##        '-no docstring-'
##    HideAdvancedMembers = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfAutoListMembers
##    def _set(self, pfAutoListMembers):
##        '-no docstring-'
##    AutoListMembers = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfWrap
##    def _set(self, pfWrap):
##        '-no docstring-'
##    WordWrap = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfInsertTabs
##    def _set(self, pfInsertTabs):
##        '-no docstring-'
##    InsertTabs = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfVirtualSpace
##    def _set(self, pfVirtualSpace):
##        '-no docstring-'
##    VirtualSpace = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfshow
##    def _set(self, pfshow):
##        '-no docstring-'
##    ShowNavigationBar = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfshow
##    def _set(self, pfshow):
##        '-no docstring-'
##    ShowLineNumbers = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return piTabSize
##    def _set(self, piTabSize):
##        '-no docstring-'
##    TabSize = property(_get, _set, doc = _set.__doc__)
##

CodeProperty._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(CodeClass)), 'ParentObject' )),
    COMMETHOD([dispid(33), helpstring(u'Returns a string holding the stub definition of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Prototype',
              ( ['in', 'optional'], c_int, 'Flags', 0 ),
              ( ['retval', 'out'], POINTER(BSTR), 'pFullName' )),
    COMMETHOD([dispid(34), helpstring(u'Sets/Returns an object representing the programmatic type.'), 'nonbrowsable', 'propput'], HRESULT, 'Type',
              ( [], POINTER(CodeTypeRef), 'pCodeTypeRef' )),
    COMMETHOD([dispid(34), helpstring(u'Sets/Returns an object representing the programmatic type.'), 'nonbrowsable', 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(POINTER(CodeTypeRef)), 'pCodeTypeRef' )),
    COMMETHOD([dispid(35), helpstring(u'Sets/Returns an object defining the code to return a property.'), 'nonbrowsable', 'propget'], HRESULT, 'Getter',
              ( ['retval', 'out'], POINTER(POINTER(CodeFunction)), 'ppCodeFunction' )),
    COMMETHOD([dispid(35), helpstring(u'Sets/Returns an object defining the code to return a property.'), 'nonbrowsable', 'propput'], HRESULT, 'Getter',
              ( [], POINTER(CodeFunction), 'ppCodeFunction' )),
    COMMETHOD([dispid(36), helpstring(u'Sets/Returns an object defining the code to set a property.'), 'nonbrowsable', 'propget'], HRESULT, 'Setter',
              ( ['retval', 'out'], POINTER(POINTER(CodeFunction)), 'ppCodeFunction' )),
    COMMETHOD([dispid(36), helpstring(u'Sets/Returns an object defining the code to set a property.'), 'nonbrowsable', 'propput'], HRESULT, 'Setter',
              ( [], POINTER(CodeFunction), 'ppCodeFunction' )),
    COMMETHOD([dispid(37), helpstring(u'Defines the access attributes of this item.'), 'propput'], HRESULT, 'Access',
              ( [], vsCMAccess, 'Access' )),
    COMMETHOD([dispid(37), helpstring(u'Defines the access attributes of this item.'), 'propget'], HRESULT, 'Access',
              ( ['retval', 'out'], POINTER(vsCMAccess), 'Access' )),
    COMMETHOD([dispid(38), helpstring(u'Returns a collection of items containing attributes.'), 'nonbrowsable', 'propget'], HRESULT, 'Attributes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppMembers' )),
    COMMETHOD([dispid(39), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propget'], HRESULT, 'DocComment',
              ( ['retval', 'out'], POINTER(BSTR), 'pDocComment' )),
    COMMETHOD([dispid(39), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propput'], HRESULT, 'DocComment',
              ( [], BSTR, 'pDocComment' )),
    COMMETHOD([dispid(40), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Comment',
              ( ['retval', 'out'], POINTER(BSTR), 'pComment' )),
    COMMETHOD([dispid(40), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propput'], HRESULT, 'Comment',
              ( [], BSTR, 'pComment' )),
    COMMETHOD([dispid(42), helpstring(u'Creates a new attribute code construct and inserts the code in the correct location.')], HRESULT, 'AddAttribute',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeAttribute)), 'ppCodeAttribute' )),
]
################################################################
## code template for CodeProperty implementation
##class CodeProperty_Impl(object):
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    def _get(self):
##        u'Defines the access attributes of this item.'
##        #return Access
##    def _set(self, Access):
##        u'Defines the access attributes of this item.'
##    Access = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    @property
##    def Prototype(self, Flags):
##        u'Returns a string holding the stub definition of this object.'
##        #return pFullName
##
##    def _get(self):
##        u'Sets/Returns an object representing the programmatic type.'
##        #return pCodeTypeRef
##    def _set(self, pCodeTypeRef):
##        u'Sets/Returns an object representing the programmatic type.'
##    Type = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ParentObject
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    def AddAttribute(self, Name, Value, Position):
##        u'Creates a new attribute code construct and inserts the code in the correct location.'
##        #return ppCodeAttribute
##
##    def _get(self):
##        u'Sets/Returns an object defining the code to return a property.'
##        #return ppCodeFunction
##    def _set(self, ppCodeFunction):
##        u'Sets/Returns an object defining the code to return a property.'
##    Getter = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def _get(self):
##        u'Returns the document comment on the current code model element.'
##        #return pDocComment
##    def _set(self, pDocComment):
##        u'Returns the document comment on the current code model element.'
##    DocComment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Attributes(self):
##        u'Returns a collection of items containing attributes.'
##        #return ppMembers
##
##    def _get(self):
##        u'Sets/Returns an object defining the comment for this object.'
##        #return pComment
##    def _set(self, pComment):
##        u'Sets/Returns an object defining the comment for this object.'
##    Comment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##
##    def _get(self):
##        u'Sets/Returns an object defining the code to set a property.'
##        #return ppCodeFunction
##    def _set(self, ppCodeFunction):
##        u'Sets/Returns an object defining the code to set a property.'
##    Setter = property(_get, _set, doc = _set.__doc__)
##

CodeModel._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Project)), 'pProj' )),
    COMMETHOD([dispid(3), helpstring(u'Programming language used to author the code.'), 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(4), helpstring(u'Returns a collection of code elements.'), 'propget'], HRESULT, 'CodeElements',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(5), helpstring(u'Returns a code element based on a fully qualified name.')], HRESULT, 'CodeTypeFromFullName',
              ( [], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeType)), 'ppCodeType' )),
    COMMETHOD([dispid(6), helpstring(u'Creates a new namespace code construct and inserts the code in the correct location.')], HRESULT, 'AddNamespace',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Location' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeNamespace)), 'ppCodeNamespace' )),
    COMMETHOD([dispid(7), helpstring(u'Creates a new class code construct and inserts the code in the correct location.')], HRESULT, 'AddClass',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Location' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], VARIANT, 'ImplementedInterfaces' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeClass)), 'ppCodeClass' )),
    COMMETHOD([dispid(8), helpstring(u'Creates a new interface code construct and inserts the code in the correct location.')], HRESULT, 'AddInterface',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Location' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeInterface)), 'ppCodeInterface' )),
    COMMETHOD([dispid(9), helpstring(u'Creates a new function code construct and inserts the code in the correct location.')], HRESULT, 'AddFunction',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Location' ),
              ( [], vsCMFunction, 'Kind' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeFunction)), 'ppCodeFunction' )),
    COMMETHOD([dispid(10), helpstring(u'Creates a new variable code construct and inserts the code in the correct location.')], HRESULT, 'AddVariable',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Location' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeVariable)), 'ppCodeVariable' )),
    COMMETHOD([dispid(11), helpstring(u'Creates a new structure code construct and inserts the code in the correct location.')], HRESULT, 'AddStruct',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Location' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], VARIANT, 'ImplementedInterfaces' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeStruct)), 'ppCodeStruct' )),
    COMMETHOD([dispid(12), helpstring(u'Creates a new enumeration code construct and inserts the code in the correct location.')], HRESULT, 'AddEnum',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Location' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeEnum)), 'ppCodeEnum' )),
    COMMETHOD([dispid(13), helpstring(u'Creates a new delegate code construct and inserts the code in the correct location.')], HRESULT, 'AddDelegate',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Location' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeDelegate)), 'ppCodeDelegate' )),
    COMMETHOD([dispid(14), helpstring(u'Creates a new attribute code construct and inserts the code in the correct location.')], HRESULT, 'AddAttribute',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Location' ),
              ( [], BSTR, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeAttribute)), 'ppCodeAttribute' )),
    COMMETHOD([dispid(15), helpstring(u'Removes a code element from the source file.')], HRESULT, 'Remove',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a Boolean value determining if the name is a valid programmatic identifier for the current language.')], HRESULT, 'IsValidID',
              ( [], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pValid' )),
    COMMETHOD([dispid(17), helpstring(u'Returns a Boolean value determining if the current language is case sensitive.'), 'propget'], HRESULT, 'IsCaseSensitive',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pSensitive' )),
    COMMETHOD([dispid(18), helpstring(u'Returns a CodeTypeRef object based on the type indicator passed in.')], HRESULT, 'CreateCodeTypeRef',
              ( [], VARIANT, 'Type' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeTypeRef)), 'ppCodeTypeRef' )),
]
################################################################
## code template for CodeModel implementation
##class CodeModel_Impl(object):
##    def CodeTypeFromFullName(self, Name):
##        u'Returns a code element based on a fully qualified name.'
##        #return ppCodeType
##
##    def IsValidID(self, Name):
##        u'Returns a Boolean value determining if the name is a valid programmatic identifier for the current language.'
##        #return pValid
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return pProj
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    def AddStruct(self, Name, Location, Position, Bases, ImplementedInterfaces, Access):
##        u'Creates a new structure code construct and inserts the code in the correct location.'
##        #return ppCodeStruct
##
##    def Remove(self, Element):
##        u'Removes a code element from the source file.'
##        #return 
##
##    def AddFunction(self, Name, Location, Kind, Type, Position, Access):
##        u'Creates a new function code construct and inserts the code in the correct location.'
##        #return ppCodeFunction
##
##    @property
##    def IsCaseSensitive(self):
##        u'Returns a Boolean value determining if the current language is case sensitive.'
##        #return pSensitive
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def AddAttribute(self, Name, Location, Value, Position):
##        u'Creates a new attribute code construct and inserts the code in the correct location.'
##        #return ppCodeAttribute
##
##    def AddVariable(self, Name, Location, Type, Position, Access):
##        u'Creates a new variable code construct and inserts the code in the correct location.'
##        #return ppCodeVariable
##
##    def AddNamespace(self, Name, Location, Position):
##        u'Creates a new namespace code construct and inserts the code in the correct location.'
##        #return ppCodeNamespace
##
##    def AddDelegate(self, Name, Location, Type, Position, Access):
##        u'Creates a new delegate code construct and inserts the code in the correct location.'
##        #return ppCodeDelegate
##
##    @property
##    def CodeElements(self):
##        u'Returns a collection of code elements.'
##        #return ppCodeElements
##
##    def AddEnum(self, Name, Location, Position, Bases, Access):
##        u'Creates a new enumeration code construct and inserts the code in the correct location.'
##        #return ppCodeEnum
##
##    def AddInterface(self, Name, Location, Position, Bases, Access):
##        u'Creates a new interface code construct and inserts the code in the correct location.'
##        #return ppCodeInterface
##
##    def CreateCodeTypeRef(self, Type):
##        u'Returns a CodeTypeRef object based on the type indicator passed in.'
##        #return ppCodeTypeRef
##
##    def AddClass(self, Name, Location, Position, Bases, ImplementedInterfaces, Access):
##        u'Creates a new class code construct and inserts the code in the correct location.'
##        #return ppCodeClass
##

OutputGroup._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(OutputGroups)), 'ppOutputGroups' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the list of files built in this output group.'), 'propget'], HRESULT, 'FileNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'pNames' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the count of files built in this output group.'), 'propget'], HRESULT, 'FileCount',
              ( ['retval', 'out'], POINTER(c_int), 'pCountNames' )),
    COMMETHOD([dispid(0), helpstring(u'Returns the name used in the user interface for this output group.'), 'propget'], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the unique name used for this output group.'), 'propget'], HRESULT, 'CanonicalName',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(6), helpstring(u'Returns the list of files built in this output group.'), 'propget'], HRESULT, 'FileURLs',
              ( ['retval', 'out'], POINTER(VARIANT), 'pURLs' )),
    COMMETHOD([dispid(7), helpstring(u'Text describing the use of this output group.'), 'propget'], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'pDesc' )),
]
################################################################
## code template for OutputGroup implementation
##class OutputGroup_Impl(object):
##    @property
##    def DisplayName(self):
##        u'Returns the name used in the user interface for this output group.'
##        #return pName
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    @property
##    def FileURLs(self):
##        u'Returns the list of files built in this output group.'
##        #return pURLs
##
##    @property
##    def CanonicalName(self):
##        u'Returns the unique name used for this output group.'
##        #return pName
##
##    @property
##    def FileNames(self):
##        u'Returns the list of files built in this output group.'
##        #return pNames
##
##    @property
##    def Collection(self):
##        u'Returns the parent object.'
##        #return ppOutputGroups
##
##    @property
##    def FileCount(self):
##        u'Returns the count of files built in this output group.'
##        #return pCountNames
##
##    @property
##    def Description(self):
##        u'Text describing the use of this output group.'
##        #return pDesc
##

class TextEditor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{9FF3DDCA-1795-4191-A5B1-02D1AE35D074}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
TextEditor._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'Application',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppApp' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppParent' )),
    COMMETHOD([dispid(3), helpstring(u'Returns dsDevStudio for backward compatibility.'), 'propget'], HRESULT, 'Emulation',
              ( ['retval', 'out'], POINTER(c_int), 'pEditorType' )),
    COMMETHOD([dispid(3), helpstring(u'Returns dsDevStudio for backward compatibility.'), 'propput'], HRESULT, 'Emulation',
              ( ['in'], c_int, 'pEditorType' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the overtype mode of the text editor.'), 'propget'], HRESULT, 'Overtype',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbOT' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the overtype mode of the text editor.'), 'propput'], HRESULT, 'Overtype',
              ( ['in'], VARIANT_BOOL, 'pbOT' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the white space mode of the text editor.'), 'propget'], HRESULT, 'VisibleWhitespace',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbVW' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the white space mode of the text editor.'), 'propput'], HRESULT, 'VisibleWhitespace',
              ( ['in'], VARIANT_BOOL, 'pbVW' )),
]
################################################################
## code template for TextEditor implementation
##class TextEditor_Impl(object):
##    def _get(self):
##        u'Returns the overtype mode of the text editor.'
##        #return pbOT
##    def _set(self, pbOT):
##        u'Returns the overtype mode of the text editor.'
##    Overtype = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Application(self):
##        u'Returns the top-level extensibility object.'
##        #return ppApp
##
##    def _get(self):
##        u'Returns dsDevStudio for backward compatibility.'
##        #return pEditorType
##    def _set(self, pEditorType):
##        u'Returns dsDevStudio for backward compatibility.'
##    Emulation = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppParent
##
##    def _get(self):
##        u'Returns the white space mode of the text editor.'
##        #return pbVW
##    def _set(self, pbVW):
##        u'Returns the white space mode of the text editor.'
##    VisibleWhitespace = property(_get, _set, doc = _set.__doc__)
##

Process._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Causes the debugger to attach this process.')], HRESULT, 'Attach'),
    COMMETHOD([dispid(2), helpstring(u'Causes the debugger to attach this process.')], HRESULT, 'Detach',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForBreakOrEnd', True )),
    COMMETHOD([dispid(3), helpstring(u'Causes a debugger break in this process.')], HRESULT, 'Break',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForBreakMode', True )),
    COMMETHOD([dispid(4), helpstring(u'Terminates this process.')], HRESULT, 'Terminate',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForBreakOrEnd', True )),
    COMMETHOD([dispid(0), helpstring(u'Returns the name of the process.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD([dispid(100), helpstring(u'Returns the Win32 process ID for this process.'), 'propget'], HRESULT, 'ProcessID',
              ( ['retval', 'out'], POINTER(c_int), 'ID' )),
    COMMETHOD([dispid(101), helpstring(u'Returns the collection of programs being managed by this process.'), 'propget'], HRESULT, 'Programs',
              ( ['retval', 'out'], POINTER(POINTER(Programs)), 'Programs' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTE' )),
    COMMETHOD([dispid(201), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'Debugger' )),
    COMMETHOD([dispid(202), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(Processes)), 'Processes' )),
]
################################################################
## code template for Process implementation
##class Process_Impl(object):
##    @property
##    def ProcessID(self):
##        u'Returns the Win32 process ID for this process.'
##        #return ID
##
##    @property
##    def Name(self):
##        u'Returns the name of the process.'
##        #return Name
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Debugger
##
##    @property
##    def Programs(self):
##        u'Returns the collection of programs being managed by this process.'
##        #return Programs
##
##    def Terminate(self, WaitForBreakOrEnd):
##        u'Terminates this process.'
##        #return 
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTE
##
##    def Break(self, WaitForBreakMode):
##        u'Causes a debugger break in this process.'
##        #return 
##
##    def Attach(self):
##        u'Causes the debugger to attach this process.'
##        #return 
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return Processes
##
##    def Detach(self, WaitForBreakOrEnd):
##        u'Causes the debugger to attach this process.'
##        #return 
##

class TextRange(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing a contiguous range of text between two points.'
    _iid_ = GUID('{72767524-E3B3-43D0-BB46-BBE1D556A9FF}')
    _idlflags_ = ['dual', 'oleautomation']
TextRange._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(TextRanges)), 'ppParent' )),
    COMMETHOD([dispid(3), helpstring(u"Returns a TextPoint object representing the beginning of the object's text."), 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(EditPoint)), 'ppPoint' )),
    COMMETHOD([dispid(4), helpstring(u"Returns a TextPoint object representing the end of the object's text."), 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(EditPoint)), 'ppPoint' )),
]
################################################################
## code template for TextRange implementation
##class TextRange_Impl(object):
##    @property
##    def EndPoint(self):
##        u"Returns a TextPoint object representing the end of the object's text."
##        #return ppPoint
##
##    @property
##    def StartPoint(self):
##        u"Returns a TextPoint object representing the beginning of the object's text."
##        #return ppPoint
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppParent
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##

Globals._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'pDTE' )),
    COMMETHOD([dispid(0), helpstring(u'Get/Set the value of a named variable.'), 'propget'], HRESULT, 'VariableValue',
              ( [], BSTR, 'VariableName' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Get/Set the value of a named variable.'), 'propput'], HRESULT, 'VariableValue',
              ( [], BSTR, 'VariableName' ),
              ( ['in'], VARIANT, 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Get/Set if a variable is persisted to storage at shutdown, and re-read on startup.'), 'propput'], HRESULT, 'VariablePersists',
              ( [], BSTR, 'VariableName' ),
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Get/Set if a variable is persisted to storage at shutdown, and re-read on startup.'), 'propget'], HRESULT, 'VariablePersists',
              ( [], BSTR, 'VariableName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(5), helpstring(u'Get if a variable with the given name is available for reading.'), 'propget'], HRESULT, 'VariableExists',
              ( [], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(6), helpstring(u'Returns a list of variables.'), 'propget'], HRESULT, 'VariableNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'Names' )),
]
################################################################
## code template for Globals implementation
##class Globals_Impl(object):
##    def _get(self, VariableName):
##        u'Get/Set if a variable is persisted to storage at shutdown, and re-read on startup.'
##        #return pVal
##    def _set(self, VariableName, pVal):
##        u'Get/Set if a variable is persisted to storage at shutdown, and re-read on startup.'
##    VariablePersists = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Parent(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    @property
##    def VariableNames(self):
##        u'Returns a list of variables.'
##        #return Names
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    def _get(self, VariableName):
##        u'Get/Set the value of a named variable.'
##        #return pVal
##    def _set(self, VariableName, pVal):
##        u'Get/Set the value of a named variable.'
##    VariableValue = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def VariableExists(self, Name):
##        u'Get if a variable with the given name is available for reading.'
##        #return pVal
##

_dispOutputWindowEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Occurs when a new OutputWindowPane object is created.')], None, 'PaneAdded',
               ( ['in'], POINTER(OutputWindowPane), 'pPane' )),
    DISPMETHOD([dispid(2), helpstring(u'Occurs when a output window pane is modified.')], None, 'PaneUpdated',
               ( ['in'], POINTER(OutputWindowPane), 'pPane' )),
    DISPMETHOD([dispid(3), helpstring(u'Occurs when all the text in a output window pane is removed.')], None, 'PaneClearing',
               ( ['in'], POINTER(OutputWindowPane), 'pPane' )),
]
class TextWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing a window on a text document, which may contain multiple text panes.'
    _iid_ = GUID('{2FC54DC9-922B-44EB-8CC0-BA182584DC4B}')
    _idlflags_ = ['dual', 'oleautomation']
TextPanes._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(TextWindow)), 'ppParent' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(TextPane)), 'ppPane' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
]
################################################################
## code template for TextPanes implementation
##class TextPanes_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return ppPane
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppParent
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##


# values for enumeration 'vsTaskIcon'
vsTaskIconNone = 0
vsTaskIconCompile = 1
vsTaskIconSquiggle = 2
vsTaskIconComment = 3
vsTaskIconShortcut = 4
vsTaskIconUser = 5
vsTaskIcon = c_int # enum
OutputWindowPane._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(OutputWindowPanes)), 'pOutputWindowPanes' )),
    COMMETHOD([dispid(4), helpstring(u'Returns a string uniquely identifying this pane.'), 'propget'], HRESULT, 'Guid',
              ( ['retval', 'out'], POINTER(BSTR), 'pGUID' )),
    COMMETHOD([dispid(5), helpstring(u'Displays a string on the pane.')], HRESULT, 'OutputString',
              ( ['in'], BSTR, 'Text' )),
    COMMETHOD([dispid(6), helpstring(u'Force display all task items not yet added to the task list.')], HRESULT, 'ForceItemsToTaskList'),
    COMMETHOD([dispid(7), helpstring(u'Moves the focus to the current item.')], HRESULT, 'Activate'),
    COMMETHOD([dispid(8), helpstring(u'Clears all text from the output window pane.')], HRESULT, 'Clear'),
    COMMETHOD([dispid(9), helpstring(u'Displays a string on the pane, and add a corresponding item to the task list.')], HRESULT, 'OutputTaskItemString',
              ( ['in'], BSTR, 'Text' ),
              ( ['in'], vsTaskPriority, 'Priority' ),
              ( ['in'], BSTR, 'SubCategory' ),
              ( ['in'], vsTaskIcon, 'Icon' ),
              ( ['in'], BSTR, 'FileName' ),
              ( ['in'], c_int, 'Line' ),
              ( ['in'], BSTR, 'Description' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Force', True )),
    COMMETHOD([dispid(10), helpstring(u'Returns the TextDocument object in the pane.'), 'propget'], HRESULT, 'TextDocument',
              ( ['retval', 'out'], POINTER(POINTER(TextDocument)), 'pDocument' )),
]
################################################################
## code template for OutputWindowPane implementation
##class OutputWindowPane_Impl(object):
##    def Activate(self):
##        u'Moves the focus to the current item.'
##        #return 
##
##    @property
##    def Name(self):
##        u'Returns the name of the object.'
##        #return pName
##
##    def Clear(self):
##        u'Clears all text from the output window pane.'
##        #return 
##
##    def ForceItemsToTaskList(self):
##        u'Force display all task items not yet added to the task list.'
##        #return 
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return pOutputWindowPanes
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    @property
##    def Guid(self):
##        u'Returns a string uniquely identifying this pane.'
##        #return pGUID
##
##    def OutputString(self, Text):
##        u'Displays a string on the pane.'
##        #return 
##
##    @property
##    def TextDocument(self):
##        u'Returns the TextDocument object in the pane.'
##        #return pDocument
##
##    def OutputTaskItemString(self, Text, Priority, SubCategory, Icon, FileName, Line, Description, Force):
##        u'Displays a string on the pane, and add a corresponding item to the task list.'
##        #return 
##

class Expression(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Used to examine and manipulate the item returned by an expression evaluation.'
    _iid_ = GUID('{27ADC812-BB07-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
class Breakpoints(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of Breakpoint objects.'
    _iid_ = GUID('{25968106-BAFB-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
class Languages(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of Language objects.'
    _iid_ = GUID('{A4F4246C-C131-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
class Breakpoint(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Used to manipulate a breakpoint.'
    _iid_ = GUID('{11C5114C-BB00-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
Debugger._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Evaluates an expression based on the current stack frame.  If the expression is parsable, but could not be evaluated, an object is returned but will not contain a valid value.')], HRESULT, 'GetExpression',
              ( ['in'], BSTR, 'ExpressionText' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'UseAutoExpandRules', False ),
              ( ['in', 'optional'], c_int, 'Timeout', -1 ),
              ( ['retval', 'out'], POINTER(POINTER(Expression)), 'Expression' )),
    COMMETHOD([dispid(2), helpstring(u'Detaches from all attached programs.')], HRESULT, 'DetachAll'),
    COMMETHOD([dispid(3), helpstring(u'Steps over the next statement unless it is a function call.  If so, will step to the beginning of the called function.')], HRESULT, 'StepInto',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForBreakOrEnd', True )),
    COMMETHOD([dispid(4), helpstring(u'Steps over the next statement regardless of whether or not it is function call.')], HRESULT, 'StepOver',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForBreakOrEnd', True )),
    COMMETHOD([dispid(5), helpstring(u'Steps out of the current function.')], HRESULT, 'StepOut',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForBreakOrEnd', True )),
    COMMETHOD([dispid(6), helpstring(u'Starts executing the program from the current statement, or launches the active project.')], HRESULT, 'Go',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForBreakOrEnd', True )),
    COMMETHOD([dispid(7), helpstring(u'Breaks the execution of all programs currently being debugged.')], HRESULT, 'Break',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForBreakMode', True )),
    COMMETHOD([dispid(8), helpstring(u'Stops debugging, terminating or detaching from all programs being debugged.')], HRESULT, 'Stop',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForDesignMode', True )),
    COMMETHOD([dispid(9), helpstring(u'Sets the next instruction to be executed according to the current source file cursor position.')], HRESULT, 'SetNextStatement'),
    COMMETHOD([dispid(10), helpstring(u'Executes the program to the current position of the source file cursor.')], HRESULT, 'RunToCursor',
              ( ['in', 'optional'], VARIANT_BOOL, 'WaitForBreakOrEnd', True )),
    COMMETHOD([dispid(11), helpstring(u'Executes a statement.  If the TreatAsExpression flag is true, then the string is interpreted as an expression.  Output is sent to the Command Window.')], HRESULT, 'ExecuteStatement',
              ( ['in'], BSTR, 'Statement' ),
              ( ['in', 'optional'], c_int, 'Timeout', -1 ),
              ( ['in', 'optional'], VARIANT_BOOL, 'TreatAsExpression', False )),
    COMMETHOD([dispid(100), helpstring(u'Returns a collection of breakpoints.'), 'propget'], HRESULT, 'Breakpoints',
              ( ['retval', 'out'], POINTER(POINTER(Breakpoints)), 'Breakpoints' )),
    COMMETHOD([dispid(101), helpstring(u'Returns a list of languages that the debugger supports.'), 'propget'], HRESULT, 'Languages',
              ( ['retval', 'out'], POINTER(POINTER(Languages)), 'Languages' )),
    COMMETHOD([dispid(102), helpstring(u'Returns the current mode of the debugger within the context of the IDE.'), 'propget'], HRESULT, 'CurrentMode',
              ( ['retval', 'out'], POINTER(dbgDebugMode), 'Mode' )),
    COMMETHOD([dispid(103), helpstring(u'Sets/Returns the active process.  Though the debugger supports debugging more than one process at a time, only one process can be active.'), 'propget'], HRESULT, 'CurrentProcess',
              ( ['retval', 'out'], POINTER(POINTER(Process)), 'Process' )),
    COMMETHOD([dispid(103), helpstring(u'Sets/Returns the active process.  Though the debugger supports debugging more than one process at a time, only one process can be active.'), 'propput'], HRESULT, 'CurrentProcess',
              ( ['in'], POINTER(Process), 'Process' )),
    COMMETHOD([dispid(104), helpstring(u'Sets/Returns the active program.  Though the debugger supports debugging more than one program at a time, only one program can be active.'), 'propget'], HRESULT, 'CurrentProgram',
              ( ['retval', 'out'], POINTER(POINTER(Program)), 'Program' )),
    COMMETHOD([dispid(104), helpstring(u'Sets/Returns the active program.  Though the debugger supports debugging more than one program at a time, only one program can be active.'), 'propput'], HRESULT, 'CurrentProgram',
              ( ['in'], POINTER(Program), 'Program' )),
    COMMETHOD([dispid(105), helpstring(u'Sets/Returns the current thread being debugged.'), 'propget'], HRESULT, 'CurrentThread',
              ( ['retval', 'out'], POINTER(POINTER(Thread)), 'Thread' )),
    COMMETHOD([dispid(105), helpstring(u'Sets/Returns the current thread being debugged.'), 'propput'], HRESULT, 'CurrentThread',
              ( ['in'], POINTER(Thread), 'Thread' )),
    COMMETHOD([dispid(106), helpstring(u'Sets/Returns the current stack frame.'), 'propget'], HRESULT, 'CurrentStackFrame',
              ( ['retval', 'out'], POINTER(POINTER(StackFrame)), 'StackFrame' )),
    COMMETHOD([dispid(106), helpstring(u'Sets/Returns the current stack frame.'), 'propput'], HRESULT, 'CurrentStackFrame',
              ( ['in'], POINTER(StackFrame), 'StackFrame' )),
    COMMETHOD([dispid(107), helpstring(u'Sets/Returns the output radix used when evaluating expressions.'), 'propget'], HRESULT, 'HexDisplayMode',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'HexModeOn' )),
    COMMETHOD([dispid(107), helpstring(u'Sets/Returns the output radix used when evaluating expressions.'), 'propput'], HRESULT, 'HexDisplayMode',
              ( ['in'], VARIANT_BOOL, 'HexModeOn' )),
    COMMETHOD([dispid(108), helpstring(u'Sets/Returns the input radix used when evaluating expressions.'), 'propget'], HRESULT, 'HexInputMode',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'HexModeOn' )),
    COMMETHOD([dispid(108), helpstring(u'Sets/Returns the input radix used when evaluating expressions.'), 'propput'], HRESULT, 'HexInputMode',
              ( ['in'], VARIANT_BOOL, 'HexModeOn' )),
    COMMETHOD([dispid(109), helpstring(u'Returns the last reason that a program was broken.  If the program is running it returns DBG_REASON_NONE.'), 'propget'], HRESULT, 'LastBreakReason',
              ( ['retval', 'out'], POINTER(dbgEventReason), 'Reason' )),
    COMMETHOD([dispid(110), helpstring(u'The last breakpoint hit.  If multiple breakpoints were hit simultaneously, it is undefined which breakpoint in particular will be returned.  See also: AllBreakpointsLastHit.'), 'propget'], HRESULT, 'BreakpointLastHit',
              ( ['retval', 'out'], POINTER(POINTER(Breakpoint)), 'Breakpoint' )),
    COMMETHOD([dispid(111), helpstring(u'A collection of the breakpoints that were last simultaneously hit.  See also: BreakpointLastHit.'), 'propget'], HRESULT, 'AllBreakpointsLastHit',
              ( ['retval', 'out'], POINTER(POINTER(Breakpoints)), 'Breakpoints' )),
    COMMETHOD([dispid(112), helpstring(u'The collection of processes currently being debugged.'), 'propget'], HRESULT, 'DebuggedProcesses',
              ( ['retval', 'out'], POINTER(POINTER(Processes)), 'Processes' )),
    COMMETHOD([dispid(113), helpstring(u'The collection of processes currently running on this machine.'), 'propget'], HRESULT, 'LocalProcesses',
              ( ['retval', 'out'], POINTER(POINTER(Processes)), 'Processes' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTE' )),
    COMMETHOD([dispid(201), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTE' )),
    COMMETHOD([dispid(300), helpstring(u'Terminates all attached programs.')], HRESULT, 'TerminateAll'),
]
################################################################
## code template for Debugger implementation
##class Debugger_Impl(object):
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTE
##
##    def DetachAll(self):
##        u'Detaches from all attached programs.'
##        #return 
##
##    @property
##    def Languages(self):
##        u'Returns a list of languages that the debugger supports.'
##        #return Languages
##
##    @property
##    def LastBreakReason(self):
##        u'Returns the last reason that a program was broken.  If the program is running it returns DBG_REASON_NONE.'
##        #return Reason
##
##    def StepOver(self, WaitForBreakOrEnd):
##        u'Steps over the next statement regardless of whether or not it is function call.'
##        #return 
##
##    @property
##    def BreakpointLastHit(self):
##        u'The last breakpoint hit.  If multiple breakpoints were hit simultaneously, it is undefined which breakpoint in particular will be returned.  See also: AllBreakpointsLastHit.'
##        #return Breakpoint
##
##    @property
##    def AllBreakpointsLastHit(self):
##        u'A collection of the breakpoints that were last simultaneously hit.  See also: BreakpointLastHit.'
##        #return Breakpoints
##
##    def StepOut(self, WaitForBreakOrEnd):
##        u'Steps out of the current function.'
##        #return 
##
##    def _get(self):
##        u'Sets/Returns the current thread being debugged.'
##        #return Thread
##    def _set(self, Thread):
##        u'Sets/Returns the current thread being debugged.'
##    CurrentThread = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Sets/Returns the active program.  Though the debugger supports debugging more than one program at a time, only one program can be active.'
##        #return Program
##    def _set(self, Program):
##        u'Sets/Returns the active program.  Though the debugger supports debugging more than one program at a time, only one program can be active.'
##    CurrentProgram = property(_get, _set, doc = _set.__doc__)
##
##    def Stop(self, WaitForDesignMode):
##        u'Stops debugging, terminating or detaching from all programs being debugged.'
##        #return 
##
##    @property
##    def CurrentMode(self):
##        u'Returns the current mode of the debugger within the context of the IDE.'
##        #return Mode
##
##    def Break(self, WaitForBreakMode):
##        u'Breaks the execution of all programs currently being debugged.'
##        #return 
##
##    @property
##    def DebuggedProcesses(self):
##        u'The collection of processes currently being debugged.'
##        #return Processes
##
##    def SetNextStatement(self):
##        u'Sets the next instruction to be executed according to the current source file cursor position.'
##        #return 
##
##    def RunToCursor(self, WaitForBreakOrEnd):
##        u'Executes the program to the current position of the source file cursor.'
##        #return 
##
##    def GetExpression(self, ExpressionText, UseAutoExpandRules, Timeout):
##        u'Evaluates an expression based on the current stack frame.  If the expression is parsable, but could not be evaluated, an object is returned but will not contain a valid value.'
##        #return Expression
##
##    def StepInto(self, WaitForBreakOrEnd):
##        u'Steps over the next statement unless it is a function call.  If so, will step to the beginning of the called function.'
##        #return 
##
##    def _get(self):
##        u'Sets/Returns the current stack frame.'
##        #return StackFrame
##    def _set(self, StackFrame):
##        u'Sets/Returns the current stack frame.'
##    CurrentStackFrame = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Sets/Returns the active process.  Though the debugger supports debugging more than one process at a time, only one process can be active.'
##        #return Process
##    def _set(self, Process):
##        u'Sets/Returns the active process.  Though the debugger supports debugging more than one process at a time, only one process can be active.'
##    CurrentProcess = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def LocalProcesses(self):
##        u'The collection of processes currently running on this machine.'
##        #return Processes
##
##    def _get(self):
##        u'Sets/Returns the input radix used when evaluating expressions.'
##        #return HexModeOn
##    def _set(self, HexModeOn):
##        u'Sets/Returns the input radix used when evaluating expressions.'
##    HexInputMode = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Breakpoints(self):
##        u'Returns a collection of breakpoints.'
##        #return Breakpoints
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return DTE
##
##    def TerminateAll(self):
##        u'Terminates all attached programs.'
##        #return 
##
##    def _get(self):
##        u'Sets/Returns the output radix used when evaluating expressions.'
##        #return HexModeOn
##    def _set(self, HexModeOn):
##        u'Sets/Returns the output radix used when evaluating expressions.'
##    HexDisplayMode = property(_get, _set, doc = _set.__doc__)
##
##    def Go(self, WaitForBreakOrEnd):
##        u'Starts executing the program from the current statement, or launches the active project.'
##        #return 
##
##    def ExecuteStatement(self, Statement, Timeout, TreatAsExpression):
##        u'Executes a statement.  If the TreatAsExpression flag is true, then the string is interpreted as an expression.  Output is sent to the Command Window.'
##        #return 
##

vsWizardNewProject = u'{0F90E1D0-4999-11D1-B6D1-00A0C90F2744}' # Constant STRING
class IDTCommandTarget(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Called to determine the status or execute a command added through Commands.AddNamedCommand. Implemented by the Add-in writer.'
    _iid_ = GUID('{7EF39A3E-590D-4879-88D4-C9BE5BCFD92E}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'vsCommandStatusTextWanted'
vsCommandStatusTextWantedNone = 0
vsCommandStatusTextWantedName = 1
vsCommandStatusTextWantedStatus = 2
vsCommandStatusTextWanted = c_int # enum

# values for enumeration 'vsCommandStatus'
vsCommandStatusUnsupported = 0
vsCommandStatusSupported = 1
vsCommandStatusEnabled = 2
vsCommandStatusLatched = 4
vsCommandStatusNinched = 8
vsCommandStatusInvisible = 16
vsCommandStatus = c_int # enum

# values for enumeration 'vsCommandExecOption'
vsCommandExecOptionDoDefault = 0
vsCommandExecOptionPromptUser = 1
vsCommandExecOptionDoPromptUser = 2
vsCommandExecOptionShowHelp = 3
vsCommandExecOption = c_int # enum
IDTCommandTarget._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Called to determine the status of a command added through Commands.AddNamedCommand. Implemented by the Add-in writer.')], HRESULT, 'QueryStatus',
              ( ['in'], BSTR, 'CmdName' ),
              ( ['in'], vsCommandStatusTextWanted, 'NeededText' ),
              ( ['in', 'out'], POINTER(vsCommandStatus), 'StatusOption' ),
              ( ['in', 'out'], POINTER(VARIANT), 'CommandText' )),
    COMMETHOD([dispid(2), helpstring(u'Called to execute a command added through Commands.AddNamedCommand. Implemented by the Add-in writer.')], HRESULT, 'Exec',
              ( ['in'], BSTR, 'CmdName' ),
              ( ['in'], vsCommandExecOption, 'ExecuteOption' ),
              ( ['in'], POINTER(VARIANT), 'VariantIn' ),
              ( ['in', 'out'], POINTER(VARIANT), 'VariantOut' ),
              ( ['in', 'out'], POINTER(VARIANT_BOOL), 'Handled' )),
]
################################################################
## code template for IDTCommandTarget implementation
##class IDTCommandTarget_Impl(object):
##    def QueryStatus(self, CmdName, NeededText):
##        u'Called to determine the status of a command added through Commands.AddNamedCommand. Implemented by the Add-in writer.'
##        #return StatusOption, CommandText
##
##    def Exec(self, CmdName, ExecuteOption, VariantIn):
##        u'Called to execute a command added through Commands.AddNamedCommand. Implemented by the Add-in writer.'
##        #return VariantOut, Handled
##


# values for enumeration 'dbgHitCountType'
dbgHitCountTypeNone = 1
dbgHitCountTypeEqual = 2
dbgHitCountTypeGreaterOrEqual = 3
dbgHitCountTypeMultiple = 4
dbgHitCountType = c_int # enum
Breakpoints._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Breakpoint)), 'Breakpoint' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'Debugger' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([dispid(4), helpstring(u'Creates and enables a new breakpoint.  If no parameters are given, the new breakpoint dialog is displayed.')], HRESULT, 'Add',
              ( ['in', 'optional'], BSTR, 'Function', u'' ),
              ( ['in', 'optional'], BSTR, 'File', u'' ),
              ( ['in', 'optional'], c_int, 'Line', 1 ),
              ( ['in', 'optional'], c_int, 'Column', 1 ),
              ( ['in', 'optional'], BSTR, 'Condition', u'' ),
              ( ['in', 'optional'], dbgBreakpointConditionType, 'ConditionType', 1 ),
              ( ['in', 'optional'], BSTR, 'Language', u'' ),
              ( ['in', 'optional'], BSTR, 'Data', u'' ),
              ( ['in', 'optional'], c_int, 'DataCount', 1 ),
              ( ['in', 'optional'], BSTR, 'Address', u'' ),
              ( ['in', 'optional'], c_int, 'HitCount', 0 ),
              ( ['in', 'optional'], dbgHitCountType, 'HitCountType', 1 ),
              ( ['retval', 'out'], POINTER(POINTER(Breakpoints)), 'Breakpoints' )),
]
################################################################
## code template for Breakpoints implementation
##class Breakpoints_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return Count
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Debugger
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return Breakpoint
##
##    def Add(self, Function, File, Line, Column, Condition, ConditionType, Language, Data, DataCount, Address, HitCount, HitCountType):
##        u'Creates and enables a new breakpoint.  If no parameters are given, the new breakpoint dialog is displayed.'
##        #return Breakpoints
##

vsProjectKindMisc = u'{66A2671D-8FB5-11D2-AA7E-00C04F688DDE}' # Constant STRING
SolutionConfiguration._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(SolutionConfigurations)), 'ppSolutionConfigurations' )),
    COMMETHOD([dispid(0), helpstring(u'Returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns a collection of SolutionContext objects.'), 'propget'], HRESULT, 'SolutionContexts',
              ( ['retval', 'out'], POINTER(POINTER(SolutionContexts)), 'ppOut' )),
    COMMETHOD([dispid(4), helpstring(u'Removes the SolutionConfiguration object from use.')], HRESULT, 'Delete'),
    COMMETHOD([dispid(5), helpstring(u'Sets the SolutionConfiguration object as the currently active SolutionConfiguration.')], HRESULT, 'Activate'),
]
################################################################
## code template for SolutionConfiguration implementation
##class SolutionConfiguration_Impl(object):
##    def Activate(self):
##        u'Sets the SolutionConfiguration object as the currently active SolutionConfiguration.'
##        #return 
##
##    @property
##    def SolutionContexts(self):
##        u'Returns a collection of SolutionContext objects.'
##        #return ppOut
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppSolutionConfigurations
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##
##    @property
##    def Name(self):
##        u'Returns the name of the object.'
##        #return pVal
##
##    def Delete(self):
##        u'Removes the SolutionConfiguration object from use.'
##        #return 
##

class CommandWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object representing the Command Window.'
    _iid_ = GUID('{509B9955-7303-48C9-90D4-E165B974E6BA}')
    _idlflags_ = ['dual', 'oleautomation']
CommandWindow._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'pParent' )),
    COMMETHOD([dispid(3), helpstring(u'Places a command into the Command Window, and optionally executes.')], HRESULT, 'SendInput',
              ( [], BSTR, 'Command' ),
              ( [], VARIANT_BOOL, 'Execute' )),
    COMMETHOD([dispid(4), helpstring(u'Places informational text into the Command Window.')], HRESULT, 'OutputString',
              ( [], BSTR, 'Text' )),
    COMMETHOD([dispid(5), helpstring(u'Clears all text from the command window.')], HRESULT, 'Clear'),
    COMMETHOD([dispid(6), helpstring(u'Returns the TextDocument object for the Command Window.'), 'propget'], HRESULT, 'TextDocument',
              ( ['retval', 'out'], POINTER(POINTER(TextDocument)), 'ppTextDocument' )),
]
################################################################
## code template for CommandWindow implementation
##class CommandWindow_Impl(object):
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return pParent
##
##    @property
##    def TextDocument(self):
##        u'Returns the TextDocument object for the Command Window.'
##        #return ppTextDocument
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def SendInput(self, Command, Execute):
##        u'Places a command into the Command Window, and optionally executes.'
##        #return 
##
##    def OutputString(self, Text):
##        u'Places informational text into the Command Window.'
##        #return 
##
##    def Clear(self):
##        u'Clears all text from the command window.'
##        #return 
##

class UndoContext(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Allows actions within the source editor to be undone as one atomic unit.'
    _iid_ = GUID('{D8DEC44D-CAF2-4B39-A539-B91AE921BA92}')
    _idlflags_ = ['dual', 'oleautomation']
UndoContext._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(3), helpstring(u'Starts a new undo operation.')], HRESULT, 'Open',
              ( ['in'], BSTR, 'Name' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Strict', False )),
    COMMETHOD([dispid(4), helpstring(u'Ends an undo operation.')], HRESULT, 'Close'),
    COMMETHOD([dispid(5), helpstring(u'Aborts an undo context, discarding all undo state.')], HRESULT, 'SetAborted'),
    COMMETHOD([dispid(6), helpstring(u'Reflects if the Undo Context is strict.'), 'propget'], HRESULT, 'IsStrict',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsStrict' )),
    COMMETHOD([dispid(7), helpstring(u'Determines if an undo context has been aborted.'), 'propget'], HRESULT, 'IsAborted',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsAborted' )),
    COMMETHOD([dispid(8), helpstring(u'Determines if an undo context is currently in use.'), 'propget'], HRESULT, 'IsOpen',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsOpen' )),
]
################################################################
## code template for UndoContext implementation
##class UndoContext_Impl(object):
##    @property
##    def IsOpen(self):
##        u'Determines if an undo context is currently in use.'
##        #return pIsOpen
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return DTEObject
##
##    @property
##    def IsStrict(self):
##        u'Reflects if the Undo Context is strict.'
##        #return pIsStrict
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    @property
##    def IsAborted(self):
##        u'Determines if an undo context has been aborted.'
##        #return pIsAborted
##
##    def Close(self):
##        u'Ends an undo operation.'
##        #return 
##
##    def SetAborted(self):
##        u'Aborts an undo context, discarding all undo state.'
##        #return 
##
##    def Open(self, Name, Strict):
##        u'Starts a new undo operation.'
##        #return 
##

TextBuffer._methods_ = [
    COMMETHOD([dispid(1610743808), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'retval' )),
    COMMETHOD([dispid(1610743809), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(1), helpstring(u'Adds a string to the TextBuffer object.')], HRESULT, 'AddFromString',
              ( ['in'], BSTR, 'String' ),
              ( ['in', 'optional'], c_int, 'StartLine', 1 )),
    COMMETHOD([dispid(2), helpstring(u'Adds the contents of a file to a TextBuffer object.')], HRESULT, 'AddFromFile',
              ( ['in'], BSTR, 'FileName' ),
              ( ['in', 'optional'], c_int, 'StartLine', 1 )),
    COMMETHOD([dispid(3), helpstring(u'Returns the specified block of lines.'), 'propget'], HRESULT, 'Lines',
              ( ['in'], c_int, 'StartLine' ),
              ( ['in'], c_int, 'Count' ),
              ( ['retval', 'out'], POINTER(BSTR), 'String' )),
    COMMETHOD([dispid(4), helpstring(u'Returns number of new line sequences in buffer.'), 'propget'], HRESULT, 'CountOfLines',
              ( ['retval', 'out'], POINTER(c_int), 'CountOfLines' )),
    COMMETHOD([dispid(6), helpstring(u'Deletes a single line of code or a specified range of lines in a TextBuffer object.')], HRESULT, 'DeleteLines',
              ( ['in'], c_int, 'StartLine' ),
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(14), helpstring(u'Searches a TextBuffer for a specified string.')], HRESULT, 'Find',
              ( ['in'], BSTR, 'Target' ),
              ( ['in', 'out'], POINTER(c_int), 'StartLine' ),
              ( ['in', 'out'], POINTER(c_int), 'StartColumn' ),
              ( ['in', 'out'], POINTER(c_int), 'EndLine' ),
              ( ['in', 'out'], POINTER(c_int), 'EndColumn' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'WholeWord', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'MatchCase', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'PatternSearch', False ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfFound' )),
]
################################################################
## code template for TextBuffer implementation
##class TextBuffer_Impl(object):
##    def AddFromString(self, String, StartLine):
##        u'Adds a string to the TextBuffer object.'
##        #return 
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return retval
##
##    @property
##    def Lines(self, StartLine, Count):
##        u'Returns the specified block of lines.'
##        #return String
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def AddFromFile(self, FileName, StartLine):
##        u'Adds the contents of a file to a TextBuffer object.'
##        #return 
##
##    def DeleteLines(self, StartLine, Count):
##        u'Deletes a single line of code or a specified range of lines in a TextBuffer object.'
##        #return 
##
##    def Find(self, Target, WholeWord, MatchCase, PatternSearch):
##        u'Searches a TextBuffer for a specified string.'
##        #return StartLine, StartColumn, EndLine, EndColumn, pfFound
##
##    @property
##    def CountOfLines(self):
##        u'Returns number of new line sequences in buffer.'
##        #return CountOfLines
##

class SelectedItems(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Represents selected project(s) or project item(s).'
    _iid_ = GUID('{6CAA67CF-43AE-4184-AAAB-0200DDF6B240}')
    _idlflags_ = ['dual', 'oleautomation']
class SelectedItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Represents selected project(s) or project item(s).'
    _iid_ = GUID('{049D2CDF-3731-4CB6-A233-BE97BCE922D3}')
    _idlflags_ = ['dual', 'oleautomation']
class SelectionContainer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Represents the selection context with objects that model the selection below the project item level.'
    _iid_ = GUID('{02273422-8DD4-4A9F-8A8B-D70443D510F4}')
    _idlflags_ = ['dual', 'oleautomation']
SelectedItems._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(SelectedItem)), 'lplppReturn' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(1), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'lplReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(4), helpstring(u'Returns value indicating whether the selection includes multiple items.'), 'propget'], HRESULT, 'MultiSelect',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfMultiSelect' )),
    COMMETHOD([dispid(5), helpstring(u'Returns collection of objects representing selection context at finer granularity than Project/ProjectItem.'), 'propget'], HRESULT, 'SelectionContainer',
              ( ['retval', 'out'], POINTER(POINTER(SelectionContainer)), 'lppdispSelContainer' )),
]
################################################################
## code template for SelectedItems implementation
##class SelectedItems_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return lplReturn
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppaReturn
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return lplppReturn
##
##    @property
##    def MultiSelect(self):
##        u'Returns value indicating whether the selection includes multiple items.'
##        #return pfMultiSelect
##
##    @property
##    def SelectionContainer(self):
##        u'Returns collection of objects representing selection context at finer granularity than Project/ProjectItem.'
##        #return lppdispSelContainer
##

class _FontsAndColors(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{256068F6-1ADD-4F7B-BA76-571314C413AD}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
class FontsAndColorsItems(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Collection of objects detailing the color, appearance, and other attributes of an item.'
    _iid_ = GUID('{F25AE7E6-1460-4BA4-8E5E-BBBE746DE353}')
    _idlflags_ = ['dual', 'oleautomation']
_FontsAndColors._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns a String expression indicating the face used to display text in the editor.'), 'propget'], HRESULT, 'FontFamily',
              ( ['retval', 'out'], POINTER(BSTR), 'pFamily' )),
    COMMETHOD([dispid(1), helpstring(u'Returns a String expression indicating the face used to display text in the editor.'), 'propput'], HRESULT, 'FontFamily',
              ( [], BSTR, 'pFamily' )),
    COMMETHOD([dispid(2), helpstring(u'Returns enumerated type indicating the character set used to display text in editor.'), 'propget'], HRESULT, 'FontCharacterSet',
              ( ['retval', 'out'], POINTER(vsFontCharSet), 'pFontCharSet' )),
    COMMETHOD([dispid(2), helpstring(u'Returns enumerated type indicating the character set used to display text in editor.'), 'propput'], HRESULT, 'FontCharacterSet',
              ( [], vsFontCharSet, 'pFontCharSet' )),
    COMMETHOD([dispid(3), helpstring(u'Returns/sets the size of the font used to display text in the editor.'), 'propget'], HRESULT, 'FontSize',
              ( ['retval', 'out'], POINTER(c_short), 'pSize' )),
    COMMETHOD([dispid(3), helpstring(u'Returns/sets the size of the font used to display text in the editor.'), 'propput'], HRESULT, 'FontSize',
              ( [], c_short, 'pSize' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the FontsAndColorsItems collection.'), 'propget'], HRESULT, 'FontsAndColorsItems',
              ( ['retval', 'out'], POINTER(POINTER(FontsAndColorsItems)), 'ppColorableItems' )),
]
################################################################
## code template for _FontsAndColors implementation
##class _FontsAndColors_Impl(object):
##    def _get(self):
##        u'Returns enumerated type indicating the character set used to display text in editor.'
##        #return pFontCharSet
##    def _set(self, pFontCharSet):
##        u'Returns enumerated type indicating the character set used to display text in editor.'
##    FontCharacterSet = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Returns a String expression indicating the face used to display text in the editor.'
##        #return pFamily
##    def _set(self, pFamily):
##        u'Returns a String expression indicating the face used to display text in the editor.'
##    FontFamily = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Returns/sets the size of the font used to display text in the editor.'
##        #return pSize
##    def _set(self, pSize):
##        u'Returns/sets the size of the font used to display text in the editor.'
##    FontSize = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def FontsAndColorsItems(self):
##        u'Returns the FontsAndColorsItems collection.'
##        #return ppColorableItems
##


# values for enumeration 'dbgBreakpointType'
dbgBreakpointTypePending = 1
dbgBreakpointTypeBound = 2
dbgBreakpointType = c_int # enum

# values for enumeration 'dbgBreakpointLocationType'
dbgBreakpointLocationTypeNone = 1
dbgBreakpointLocationTypeFunction = 2
dbgBreakpointLocationTypeFile = 3
dbgBreakpointLocationTypeData = 4
dbgBreakpointLocationTypeAddress = 5
dbgBreakpointLocationType = c_int # enum
Breakpoint._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Deletes this breakpoint.')], HRESULT, 'Delete'),
    COMMETHOD([dispid(100), helpstring(u'The type of breakpoint this object represents.'), 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(dbgBreakpointType), 'Type' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/Returns the user-defined name of this breakpoint.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/Returns the user-defined name of this breakpoint.'), 'propput'], HRESULT, 'Name',
              ( ['in'], BSTR, 'Name' )),
    COMMETHOD([dispid(101), helpstring(u'The location type this breakpoint represents.'), 'propget'], HRESULT, 'LocationType',
              ( ['retval', 'out'], POINTER(dbgBreakpointLocationType), 'LocationType' )),
    COMMETHOD([dispid(102), helpstring(u'The language-specific name at which this breakpoint is set.'), 'propget'], HRESULT, 'FunctionName',
              ( ['retval', 'out'], POINTER(BSTR), 'FunctionName' )),
    COMMETHOD([dispid(103), helpstring(u'The line offset from the name for a function breakpoint.'), 'propget'], HRESULT, 'FunctionLineOffset',
              ( ['retval', 'out'], POINTER(c_int), 'Offset' )),
    COMMETHOD([dispid(104), helpstring(u'The column offset from the name for a function breakpoint.'), 'propget'], HRESULT, 'FunctionColumnOffset',
              ( ['retval', 'out'], POINTER(c_int), 'Offset' )),
    COMMETHOD([dispid(105), helpstring(u'The file in which this breakpoint is or will be set for file-based breakpoints.'), 'propget'], HRESULT, 'File',
              ( ['retval', 'out'], POINTER(BSTR), 'File' )),
    COMMETHOD([dispid(106), helpstring(u'The line within a file for a file breakpoint.'), 'propget'], HRESULT, 'FileLine',
              ( ['retval', 'out'], POINTER(c_int), 'Line' )),
    COMMETHOD([dispid(107), helpstring(u'The column within a file for a file breakpoint.'), 'propget'], HRESULT, 'FileColumn',
              ( ['retval', 'out'], POINTER(c_int), 'Column' )),
    COMMETHOD([dispid(108), helpstring(u'The condition type; i.e. break when true, or break when changed.'), 'propget'], HRESULT, 'ConditionType',
              ( ['retval', 'out'], POINTER(dbgBreakpointConditionType), 'ConditionType' )),
    COMMETHOD([dispid(109), helpstring(u'The condition for any type of breakpoint.'), 'propget'], HRESULT, 'Condition',
              ( ['retval', 'out'], POINTER(BSTR), 'Condition' )),
    COMMETHOD([dispid(110), helpstring(u'The language for name or conditional breakpoints.'), 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'Language' )),
    COMMETHOD([dispid(111), helpstring(u'The hitcount type.  Describes how to interpret a hit count.'), 'propget'], HRESULT, 'HitCountType',
              ( ['retval', 'out'], POINTER(dbgHitCountType), 'HitCountType' )),
    COMMETHOD([dispid(112), helpstring(u'The hitcount target for any type of breakpoint.  Interpreted based on the hitcount type.'), 'propget'], HRESULT, 'HitCountTarget',
              ( ['retval', 'out'], POINTER(c_int), 'HitCountTarget' )),
    COMMETHOD([dispid(113), helpstring(u'Sets/Returns the enabled state of this breakpoint.'), 'propget'], HRESULT, 'Enabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Enabled' )),
    COMMETHOD([dispid(113), helpstring(u'Sets/Returns the enabled state of this breakpoint.'), 'propput'], HRESULT, 'Enabled',
              ( ['in'], VARIANT_BOOL, 'Enabled' )),
    COMMETHOD([dispid(114), helpstring(u'Set/Returns a user-defined string identifying this breakpoint.'), 'propget'], HRESULT, 'Tag',
              ( ['retval', 'out'], POINTER(BSTR), 'Tag' )),
    COMMETHOD([dispid(114), helpstring(u'Set/Returns a user-defined string identifying this breakpoint.'), 'propput'], HRESULT, 'Tag',
              ( ['in'], BSTR, 'Tag' )),
    COMMETHOD([dispid(115), helpstring(u'The number of times this breakpoint has been hit during this debugging session.'), 'propget'], HRESULT, 'CurrentHits',
              ( ['retval', 'out'], POINTER(c_int), 'CurHitCount' )),
    COMMETHOD([dispid(116), helpstring(u'The program to which this breakpoint is bound.'), 'propget'], HRESULT, 'Program',
              ( ['retval', 'out'], POINTER(POINTER(Program)), 'Program' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTE' )),
    COMMETHOD([dispid(201), helpstring(u"Returns this breakpoint's parent breakpoint.  If this breakpoint does not have a parent, then nothing is returned."), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Breakpoint)), 'Breakpoint' )),
    COMMETHOD([dispid(202), helpstring(u'Returns the collection in which this bound breakpoint resides, essentially providing the set of children owned by a pending breakpoint.  If this object is a pending breakpoint, then nothing is returned.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(Breakpoints)), 'Breakpoints' )),
    COMMETHOD([dispid(203), helpstring(u"Returns a collection of breakpoints that represent this breakpoint's children.  If the breakpoint has no children then nothing is returned."), 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(Breakpoints)), 'Breakpoints' )),
    COMMETHOD([dispid(300), helpstring(u'Resets the hit count for this breakpoint back to 0')], HRESULT, 'ResetHitCount'),
]
################################################################
## code template for Breakpoint implementation
##class Breakpoint_Impl(object):
##    @property
##    def LocationType(self):
##        u'The location type this breakpoint represents.'
##        #return LocationType
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTE
##
##    @property
##    def Program(self):
##        u'The program to which this breakpoint is bound.'
##        #return Program
##
##    @property
##    def FunctionLineOffset(self):
##        u'The line offset from the name for a function breakpoint.'
##        #return Offset
##
##    @property
##    def Type(self):
##        u'The type of breakpoint this object represents.'
##        #return Type
##
##    @property
##    def FunctionName(self):
##        u'The language-specific name at which this breakpoint is set.'
##        #return FunctionName
##
##    @property
##    def CurrentHits(self):
##        u'The number of times this breakpoint has been hit during this debugging session.'
##        #return CurHitCount
##
##    @property
##    def Parent(self):
##        u"Returns this breakpoint's parent breakpoint.  If this breakpoint does not have a parent, then nothing is returned."
##        #return Breakpoint
##
##    @property
##    def Collection(self):
##        u'Returns the collection in which this bound breakpoint resides, essentially providing the set of children owned by a pending breakpoint.  If this object is a pending breakpoint, then nothing is returned.'
##        #return Breakpoints
##
##    @property
##    def FunctionColumnOffset(self):
##        u'The column offset from the name for a function breakpoint.'
##        #return Offset
##
##    @property
##    def FileLine(self):
##        u'The line within a file for a file breakpoint.'
##        #return Line
##
##    @property
##    def Condition(self):
##        u'The condition for any type of breakpoint.'
##        #return Condition
##
##    @property
##    def ConditionType(self):
##        u'The condition type; i.e. break when true, or break when changed.'
##        #return ConditionType
##
##    def _get(self):
##        u'Sets/Returns the user-defined name of this breakpoint.'
##        #return Name
##    def _set(self, Name):
##        u'Sets/Returns the user-defined name of this breakpoint.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'The language for name or conditional breakpoints.'
##        #return Language
##
##    def ResetHitCount(self):
##        u'Resets the hit count for this breakpoint back to 0'
##        #return 
##
##    def _get(self):
##        u'Sets/Returns the enabled state of this breakpoint.'
##        #return Enabled
##    def _set(self, Enabled):
##        u'Sets/Returns the enabled state of this breakpoint.'
##    Enabled = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def FileColumn(self):
##        u'The column within a file for a file breakpoint.'
##        #return Column
##
##    @property
##    def HitCountTarget(self):
##        u'The hitcount target for any type of breakpoint.  Interpreted based on the hitcount type.'
##        #return HitCountTarget
##
##    @property
##    def HitCountType(self):
##        u'The hitcount type.  Describes how to interpret a hit count.'
##        #return HitCountType
##
##    def Delete(self):
##        u'Deletes this breakpoint.'
##        #return 
##
##    def _get(self):
##        u'Set/Returns a user-defined string identifying this breakpoint.'
##        #return Tag
##    def _set(self, Tag):
##        u'Set/Returns a user-defined string identifying this breakpoint.'
##    Tag = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def File(self):
##        u'The file in which this breakpoint is or will be set for file-based breakpoints.'
##        #return File
##
##    @property
##    def Children(self):
##        u"Returns a collection of breakpoints that represent this breakpoint's children.  If the breakpoint has no children then nothing is returned."
##        #return Breakpoints
##

class Events(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Allows access to all events in the extensibility model.'
    _iid_ = GUID('{134170F8-93B1-42DD-9F89-A2AC7010BA07}')
    _idlflags_ = ['dual', 'oleautomation']
class StatusBar(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object for manipulating the Status Bar.'
    _iid_ = GUID('{C34301A1-3EF1-41D8-932A-FEA4A8A8CE0C}')
    _idlflags_ = ['dual', 'oleautomation']
class ObjectExtenders(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object that provides access to Automation Extenders.'
    _iid_ = GUID('{8D0AA9CC-8465-42F3-AD6E-DFDE28CCC75D}')
    _idlflags_ = ['dual', 'oleautomation']
class Macros(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object allowing access to the macro recorder.'
    _iid_ = GUID('{F9F99155-6D4D-49B1-AD63-C78C3E8A5916}')
    _idlflags_ = ['dual', 'oleautomation']
_DTE._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
    COMMETHOD([dispid(10), 'hidden', 'propget'], HRESULT, 'FileName',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
    COMMETHOD([dispid(100), helpstring(u"Returns the host application's version number as a String."), 'propget'], HRESULT, 'Version',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
    COMMETHOD([dispid(108), helpstring(u"Returns reference to development environment's CommandBars object."), 'propget'], HRESULT, 'CommandBars',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppcbs' )),
    COMMETHOD([dispid(110), helpstring(u'Returns the Windows collection.'), 'propget'], HRESULT, 'Windows',
              ( ['retval', 'out'], POINTER(POINTER(Windows)), 'ppwnsVBWindows' )),
    COMMETHOD([dispid(111), helpstring(u'Returns a reference to the Events object.'), 'propget'], HRESULT, 'Events',
              ( ['retval', 'out'], POINTER(POINTER(Events)), 'ppevtEvents' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the Add-ins collection, containing all currently available add-ins.'), 'propget'], HRESULT, 'AddIns',
              ( ['retval', 'out'], POINTER(POINTER(AddIns)), 'lpppAddIns' )),
    COMMETHOD([dispid(204), helpstring(u'Returns a Window object representing the main environment window.'), 'propget'], HRESULT, 'MainWindow',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'ppWin' )),
    COMMETHOD([dispid(205), helpstring(u'Returns the current active window.'), 'propget'], HRESULT, 'ActiveWindow',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'ppwinActive' )),
    COMMETHOD([dispid(207), helpstring(u'Closes the environment.')], HRESULT, 'Quit'),
    COMMETHOD([dispid(208), helpstring(u'Returns string indicating whether the project is displayed in SDI or MDI mode.'), 'propget'], HRESULT, 'DisplayMode',
              ( ['retval', 'out'], POINTER(vsDisplay), 'lpDispMode' )),
    COMMETHOD([dispid(208), helpstring(u'Returns string indicating whether the project is displayed in SDI or MDI mode.'), 'propput'], HRESULT, 'DisplayMode',
              ( ['in'], vsDisplay, 'lpDispMode' )),
    COMMETHOD([dispid(209), helpstring(u'Returns the Solution object.'), 'propget'], HRESULT, 'Solution',
              ( ['retval', 'out'], POINTER(POINTER(Solution)), 'ppSolution' )),
    COMMETHOD([dispid(210), helpstring(u'Returns the Commands object.'), 'propget'], HRESULT, 'Commands',
              ( ['retval', 'out'], POINTER(POINTER(Commands)), 'ppCommands' )),
    COMMETHOD([dispid(211), helpstring(u'Returns an interface or object that can be accessed at run time by name.')], HRESULT, 'GetObject',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppObject' )),
    COMMETHOD([dispid(212), helpstring(u'Returns collection object representing all available categories and subcategories of environment-level properties.'), 'propget'], HRESULT, 'Properties',
              ( [], BSTR, 'Category' ),
              ( [], BSTR, 'Page' ),
              ( ['retval', 'out'], POINTER(POINTER(Properties)), 'ppObject' )),
    COMMETHOD([dispid(213), helpstring(u'Returns a collection containing the items currently selected in the environment.'), 'propget'], HRESULT, 'SelectedItems',
              ( ['retval', 'out'], POINTER(POINTER(SelectedItems)), 'ppSelectedItems' )),
    COMMETHOD([dispid(214), helpstring(u'Returns a string representing the command-line arguments.'), 'propget'], HRESULT, 'CommandLineArguments',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
    COMMETHOD([dispid(215), helpstring(u'Opens a file as though the user invoked a open file command from the UI.'), 'hidden'], HRESULT, 'OpenFile',
              ( ['in'], BSTR, 'ViewKind' ),
              ( ['in'], BSTR, 'FileName' ),
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'ppWin' )),
    COMMETHOD([dispid(216), helpstring(u'Returns True if the file is open in the specified view.'), 'hidden', 'propget'], HRESULT, 'IsOpenFile',
              ( ['in'], BSTR, 'ViewKind' ),
              ( ['in'], BSTR, 'FileName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lpfReturn' )),
    COMMETHOD([dispid(217), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(218), helpstring(u'Returns the ID of the locale in which the environment is running.'), 'propget'], HRESULT, 'LocaleID',
              ( ['retval', 'out'], POINTER(c_int), 'lpReturn' )),
    COMMETHOD([dispid(219), helpstring(u'Returns the WindowConfigurations collection, representing all window configurations available.'), 'propget'], HRESULT, 'WindowConfigurations',
              ( ['retval', 'out'], POINTER(POINTER(WindowConfigurations)), 'WindowConfigurationsObject' )),
    COMMETHOD([dispid(220), helpstring(u'Returns the Documents collection, representing all open documents.'), 'propget'], HRESULT, 'Documents',
              ( ['retval', 'out'], POINTER(POINTER(Documents)), 'ppDocuments' )),
    COMMETHOD([dispid(221), helpstring(u'Returns the current active Document.'), 'propget'], HRESULT, 'ActiveDocument',
              ( ['retval', 'out'], POINTER(POINTER(Document)), 'ppDocument' )),
    COMMETHOD([dispid(222), helpstring(u"Executes a environment command based on it's name.")], HRESULT, 'ExecuteCommand',
              ( ['in'], BSTR, 'CommandName' ),
              ( ['in', 'optional'], BSTR, 'CommandArgs', u'' )),
    COMMETHOD([dispid(223), helpstring(u'Returns the Globals object for storing persistent data.'), 'propget'], HRESULT, 'Globals',
              ( ['retval', 'out'], POINTER(POINTER(Globals)), 'ppGlobals' )),
    COMMETHOD([dispid(225), helpstring(u'Returns the StatusBar object, representing the status bar on the main window.'), 'propget'], HRESULT, 'StatusBar',
              ( ['retval', 'out'], POINTER(POINTER(StatusBar)), 'ppStatusBar' )),
    COMMETHOD([dispid(226), helpstring(u'Returns the full pathname to the environment executable.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
    COMMETHOD([dispid(227), helpstring(u'Gets/Sets who has control of the program, an Automation Controller or the user.'), 'propget'], HRESULT, 'UserControl',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'UserControl' )),
    COMMETHOD([dispid(227), helpstring(u'Gets/Sets who has control of the program, an Automation Controller or the user.'), 'propput'], HRESULT, 'UserControl',
              ( ['in'], VARIANT_BOOL, 'UserControl' )),
    COMMETHOD([dispid(228), helpstring(u'Returns the ObjectExtenders object.'), 'propget'], HRESULT, 'ObjectExtenders',
              ( ['retval', 'out'], POINTER(POINTER(ObjectExtenders)), 'ppObjectExtenders' )),
    COMMETHOD([dispid(229), helpstring(u'Returns the Find object.'), 'propget'], HRESULT, 'Find',
              ( ['retval', 'out'], POINTER(POINTER(Find)), 'ppFind' )),
    COMMETHOD([dispid(230), helpstring(u'Gets the mode of the program, design or debug.'), 'propget'], HRESULT, 'Mode',
              ( ['retval', 'out'], POINTER(vsIDEMode), 'pVal' )),
    COMMETHOD([dispid(232), helpstring(u'Runs a wizard with the user supplied parameters.')], HRESULT, 'LaunchWizard',
              ( ['in'], BSTR, 'VSZFile' ),
              ( ['in'], POINTER(_midlSAFEARRAY(VARIANT)), 'ContextParams' ),
              ( ['retval', 'out'], POINTER(wizardResult), 'pResult' )),
    COMMETHOD([dispid(233), helpstring(u'Returns the ItemOperations object.'), 'propget'], HRESULT, 'ItemOperations',
              ( ['retval', 'out'], POINTER(POINTER(ItemOperations)), 'ppItemOperations' )),
    COMMETHOD([dispid(235), helpstring(u'Returns the UndoContext object.'), 'propget'], HRESULT, 'UndoContext',
              ( ['retval', 'out'], POINTER(POINTER(UndoContext)), 'ppUndoContext' )),
    COMMETHOD([dispid(236), helpstring(u'Returns the Macros object.'), 'propget'], HRESULT, 'Macros',
              ( ['retval', 'out'], POINTER(POINTER(Macros)), 'ppMacros' )),
    COMMETHOD([dispid(237), helpstring(u'Returns an array of currently selected projects.'), 'propget'], HRESULT, 'ActiveSolutionProjects',
              ( ['retval', 'out'], POINTER(VARIANT), 'pProjects' )),
    COMMETHOD([dispid(238), helpstring(u'Returns the root extensibility object for the Macros IDE.'), 'propget'], HRESULT, 'MacrosIDE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(239), helpstring(u'Returns the location for storing registry information for this application.'), 'propget'], HRESULT, 'RegistryRoot',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(240), 'hidden', 'propget'], HRESULT, 'Application',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pVal' )),
    COMMETHOD([dispid(241), helpstring(u'Get the global ContextAttributes collection.'), 'propget'], HRESULT, 'ContextAttributes',
              ( ['retval', 'out'], POINTER(POINTER(ContextAttributes)), 'ppVal' )),
    COMMETHOD([dispid(242), helpstring(u'Returns the SourceControl object for managing file source code control status.'), 'propget'], HRESULT, 'SourceControl',
              ( ['retval', 'out'], POINTER(POINTER(SourceControl)), 'ppVal' )),
    COMMETHOD([dispid(243), helpstring(u'Enables/Disables certain UI elements when calling automation functions.'), 'propget'], HRESULT, 'SuppressUI',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(243), helpstring(u'Enables/Disables certain UI elements when calling automation functions.'), 'propput'], HRESULT, 'SuppressUI',
              ( ['in'], VARIANT_BOOL, 'pVal' )),
    COMMETHOD([dispid(244), helpstring(u'Returns the Debugger objects.'), 'propget'], HRESULT, 'Debugger',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'ppDebugger' )),
    COMMETHOD([dispid(245), helpstring(u'Returns the location of a DLL containing localized resources, if available.')], HRESULT, 'SatelliteDllPath',
              ( [], BSTR, 'Path' ),
              ( [], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pFullPath' )),
    COMMETHOD([dispid(246), 'propget'], HRESULT, 'Edition',
              ( ['retval', 'out'], POINTER(BSTR), 'ProductEdition' )),
]
################################################################
## code template for _DTE implementation
##class _DTE_Impl(object):
##    @property
##    def ObjectExtenders(self):
##        u'Returns the ObjectExtenders object.'
##        #return ppObjectExtenders
##
##    def Quit(self):
##        u'Closes the environment.'
##        #return 
##
##    @property
##    def Documents(self):
##        u'Returns the Documents collection, representing all open documents.'
##        #return ppDocuments
##
##    @property
##    def LocaleID(self):
##        u'Returns the ID of the locale in which the environment is running.'
##        #return lpReturn
##
##    def _get(self):
##        u'Returns string indicating whether the project is displayed in SDI or MDI mode.'
##        #return lpDispMode
##    def _set(self, lpDispMode):
##        u'Returns string indicating whether the project is displayed in SDI or MDI mode.'
##    DisplayMode = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ContextAttributes(self):
##        u'Get the global ContextAttributes collection.'
##        #return ppVal
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    @property
##    def Macros(self):
##        u'Returns the Macros object.'
##        #return ppMacros
##
##    @property
##    def Version(self):
##        u"Returns the host application's version number as a String."
##        #return lpbstrReturn
##
##    @property
##    def IsOpenFile(self, ViewKind, FileName):
##        u'Returns True if the file is open in the specified view.'
##        #return lpfReturn
##
##    @property
##    def ActiveSolutionProjects(self):
##        u'Returns an array of currently selected projects.'
##        #return pProjects
##
##    @property
##    def MainWindow(self):
##        u'Returns a Window object representing the main environment window.'
##        #return ppWin
##
##    @property
##    def Edition(self):
##        '-no docstring-'
##        #return ProductEdition
##
##    def _get(self):
##        u'Enables/Disables certain UI elements when calling automation functions.'
##        #return pVal
##    def _set(self, pVal):
##        u'Enables/Disables certain UI elements when calling automation functions.'
##    SuppressUI = property(_get, _set, doc = _set.__doc__)
##
##    def OpenFile(self, ViewKind, FileName):
##        u'Opens a file as though the user invoked a open file command from the UI.'
##        #return ppWin
##
##    @property
##    def CommandLineArguments(self):
##        u'Returns a string representing the command-line arguments.'
##        #return lpbstrReturn
##
##    @property
##    def UndoContext(self):
##        u'Returns the UndoContext object.'
##        #return ppUndoContext
##
##    @property
##    def MacrosIDE(self):
##        u'Returns the root extensibility object for the Macros IDE.'
##        #return pDTE
##
##    @property
##    def Events(self):
##        u'Returns a reference to the Events object.'
##        #return ppevtEvents
##
##    def GetObject(self, Name):
##        u'Returns an interface or object that can be accessed at run time by name.'
##        #return ppObject
##
##    @property
##    def ActiveDocument(self):
##        u'Returns the current active Document.'
##        #return ppDocument
##
##    @property
##    def AddIns(self):
##        u'Returns the Add-ins collection, containing all currently available add-ins.'
##        #return lpppAddIns
##
##    def SatelliteDllPath(self, Path, Name):
##        u'Returns the location of a DLL containing localized resources, if available.'
##        #return pFullPath
##
##    @property
##    def Properties(self, Category, Page):
##        u'Returns collection object representing all available categories and subcategories of environment-level properties.'
##        #return ppObject
##
##    @property
##    def RegistryRoot(self):
##        u'Returns the location for storing registry information for this application.'
##        #return pVal
##
##    @property
##    def WindowConfigurations(self):
##        u'Returns the WindowConfigurations collection, representing all window configurations available.'
##        #return WindowConfigurationsObject
##
##    @property
##    def Commands(self):
##        u'Returns the Commands object.'
##        #return ppCommands
##
##    @property
##    def Name(self):
##        u'Returns the name of the object.'
##        #return lpbstrReturn
##
##    @property
##    def Windows(self):
##        u'Returns the Windows collection.'
##        #return ppwnsVBWindows
##
##    @property
##    def Solution(self):
##        u'Returns the Solution object.'
##        #return ppSolution
##
##    @property
##    def Mode(self):
##        u'Gets the mode of the program, design or debug.'
##        #return pVal
##
##    @property
##    def ActiveWindow(self):
##        u'Returns the current active window.'
##        #return ppwinActive
##
##    def LaunchWizard(self, VSZFile, ContextParams):
##        u'Runs a wizard with the user supplied parameters.'
##        #return pResult
##
##    @property
##    def Debugger(self):
##        u'Returns the Debugger objects.'
##        #return ppDebugger
##
##    @property
##    def Application(self):
##        '-no docstring-'
##        #return pVal
##
##    @property
##    def StatusBar(self):
##        u'Returns the StatusBar object, representing the status bar on the main window.'
##        #return ppStatusBar
##
##    def ExecuteCommand(self, CommandName, CommandArgs):
##        u"Executes a environment command based on it's name."
##        #return 
##
##    @property
##    def SourceControl(self):
##        u'Returns the SourceControl object for managing file source code control status.'
##        #return ppVal
##
##    @property
##    def SelectedItems(self):
##        u'Returns a collection containing the items currently selected in the environment.'
##        #return ppSelectedItems
##
##    @property
##    def FileName(self):
##        '-no docstring-'
##        #return lpbstrReturn
##
##    @property
##    def ItemOperations(self):
##        u'Returns the ItemOperations object.'
##        #return ppItemOperations
##
##    @property
##    def Globals(self):
##        u'Returns the Globals object for storing persistent data.'
##        #return ppGlobals
##
##    def _get(self):
##        u'Gets/Sets who has control of the program, an Automation Controller or the user.'
##        #return UserControl
##    def _set(self, UserControl):
##        u'Gets/Sets who has control of the program, an Automation Controller or the user.'
##    UserControl = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def FullName(self):
##        u'Returns the full pathname to the environment executable.'
##        #return lpbstrReturn
##
##    @property
##    def Find(self):
##        u'Returns the Find object.'
##        #return ppFind
##
##    @property
##    def CommandBars(self):
##        u"Returns reference to development environment's CommandBars object."
##        #return ppcbs
##

class _ProjectsEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The _ProjectsEvents object triggers events of actions taken against projects.'
    _iid_ = GUID('{85451F83-B5CA-437F-A619-0CB705707420}')
    _idlflags_ = ['dual', 'oleautomation']
_ProjectsEvents._methods_ = [
]
################################################################
## code template for _ProjectsEvents implementation
##class _ProjectsEvents_Impl(object):

SelectedItem._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(SelectedItems)), 'lppReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppReturn' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the Project object associated with the object the Project property was invoked on.'), 'propget'], HRESULT, 'Project',
              ( ['retval', 'out'], POINTER(POINTER(Project)), 'lppReturn' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'lppReturn' )),
    COMMETHOD([dispid(0), helpstring(u'Returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
    COMMETHOD([dispid(8), helpstring(u'Returns an integer indicating the number of strings included in the Info property.'), 'restricted', 'hidden', 'propget'], HRESULT, 'InfoCount',
              ( ['retval', 'out'], POINTER(c_short), 'lpnCount' )),
    COMMETHOD([dispid(9), helpstring(u'Returns a string providing information on the selected item.'), 'restricted', 'hidden', 'propget'], HRESULT, 'Info',
              ( ['in'], c_short, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'lpbstrReturn' )),
]
################################################################
## code template for SelectedItem implementation
##class SelectedItem_Impl(object):
##    @property
##    def Info(self, index):
##        u'Returns a string providing information on the selected item.'
##        #return lpbstrReturn
##
##    @property
##    def Name(self):
##        u'Returns the name of the object.'
##        #return lpbstrReturn
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppReturn
##
##    @property
##    def Project(self):
##        u'Returns the Project object associated with the object the Project property was invoked on.'
##        #return lppReturn
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return lppReturn
##
##    @property
##    def InfoCount(self):
##        u'Returns an integer indicating the number of strings included in the Info property.'
##        #return lpnCount
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return lppReturn
##

class _EnvironmentGeneral(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{48E61D9C-8C8D-42D3-914B-46D70C8B7A40}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_EnvironmentGeneral._methods_ = [
    COMMETHOD([dispid(1), helpstring(u"Sets/ returns a value indicating Visual Studio's startup behavior."), 'propput'], HRESULT, 'OnStartUp',
              ( ['in'], vsStartUp, 'pstartup' )),
    COMMETHOD([dispid(1), helpstring(u"Sets/ returns a value indicating Visual Studio's startup behavior."), 'propget'], HRESULT, 'OnStartUp',
              ( ['retval', 'out'], POINTER(vsStartUp), 'pstartup' )),
    COMMETHOD([dispid(2), helpstring(u'Sets/returns value determining whether the status bar is visible.'), 'propput'], HRESULT, 'ShowStatusBar',
              ( ['in'], VARIANT_BOOL, 'pfshow' )),
    COMMETHOD([dispid(2), helpstring(u'Sets/returns value determining whether the status bar is visible.'), 'propget'], HRESULT, 'ShowStatusBar',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfshow' )),
    COMMETHOD([dispid(3), helpstring(u'Sets/returns value determining maximum number of document windows listed on Windows menu.'), 'propput'], HRESULT, 'WindowMenuContainsNItems',
              ( ['in'], c_int, 'plCount' )),
    COMMETHOD([dispid(3), helpstring(u'Sets/returns value determining maximum number of document windows listed on Windows menu.'), 'propget'], HRESULT, 'WindowMenuContainsNItems',
              ( ['retval', 'out'], POINTER(c_int), 'plCount' )),
    COMMETHOD([dispid(4), helpstring(u'Sets/returns value indicating the number of files stored in the most recently used submenu.'), 'propput'], HRESULT, 'MRUListContainsNItems',
              ( ['in'], c_int, 'plCount' )),
    COMMETHOD([dispid(4), helpstring(u'Sets/returns value indicating the number of files stored in the most recently used submenu.'), 'propget'], HRESULT, 'MRUListContainsNItems',
              ( ['retval', 'out'], POINTER(c_int), 'plCount' )),
    COMMETHOD([dispid(5), helpstring(u'The speed at which certain animations are shown.'), 'propget'], HRESULT, 'AnimationSpeed',
              ( ['retval', 'out'], POINTER(c_short), 'pSpeed' )),
    COMMETHOD([dispid(5), helpstring(u'The speed at which certain animations are shown.'), 'propput'], HRESULT, 'AnimationSpeed',
              ( [], c_short, 'pSpeed' )),
    COMMETHOD([dispid(6), helpstring(u'If animations should be shown in the user interface.'), 'propget'], HRESULT, 'Animations',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pAnimations' )),
    COMMETHOD([dispid(6), helpstring(u'If animations should be shown in the user interface.'), 'propput'], HRESULT, 'Animations',
              ( [], VARIANT_BOOL, 'pAnimations' )),
    COMMETHOD([dispid(7), helpstring(u'Display the drop-down completion window in the Command Window.'), 'propget'], HRESULT, 'ShowCommandWindowCompletion',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pComplete' )),
    COMMETHOD([dispid(7), helpstring(u'Display the drop-down completion window in the Command Window.'), 'propput'], HRESULT, 'ShowCommandWindowCompletion',
              ( [], VARIANT_BOOL, 'pComplete' )),
    COMMETHOD([dispid(11), 'propput'], HRESULT, 'CloseButtonActiveTabOnly',
              ( [], VARIANT_BOOL, 'CloseActiveOnly' )),
    COMMETHOD([dispid(11), 'propget'], HRESULT, 'CloseButtonActiveTabOnly',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'CloseActiveOnly' )),
    COMMETHOD([dispid(12), 'propput'], HRESULT, 'AutohidePinActiveTabOnly',
              ( [], VARIANT_BOOL, 'AutohidePinActiveOnly' )),
    COMMETHOD([dispid(12), 'propget'], HRESULT, 'AutohidePinActiveTabOnly',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'AutohidePinActiveOnly' )),
]
################################################################
## code template for _EnvironmentGeneral implementation
##class _EnvironmentGeneral_Impl(object):
##    def _get(self):
##        u'Sets/returns value determining whether the status bar is visible.'
##        #return pfshow
##    def _set(self, pfshow):
##        u'Sets/returns value determining whether the status bar is visible.'
##    ShowStatusBar = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return CloseActiveOnly
##    def _set(self, CloseActiveOnly):
##        '-no docstring-'
##    CloseButtonActiveTabOnly = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Sets/returns value indicating the number of files stored in the most recently used submenu.'
##        #return plCount
##    def _set(self, plCount):
##        u'Sets/returns value indicating the number of files stored in the most recently used submenu.'
##    MRUListContainsNItems = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return AutohidePinActiveOnly
##    def _set(self, AutohidePinActiveOnly):
##        '-no docstring-'
##    AutohidePinActiveTabOnly = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u"Sets/ returns a value indicating Visual Studio's startup behavior."
##        #return pstartup
##    def _set(self, pstartup):
##        u"Sets/ returns a value indicating Visual Studio's startup behavior."
##    OnStartUp = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The speed at which certain animations are shown.'
##        #return pSpeed
##    def _set(self, pSpeed):
##        u'The speed at which certain animations are shown.'
##    AnimationSpeed = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'If animations should be shown in the user interface.'
##        #return pAnimations
##    def _set(self, pAnimations):
##        u'If animations should be shown in the user interface.'
##    Animations = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Sets/returns value determining maximum number of document windows listed on Windows menu.'
##        #return plCount
##    def _set(self, plCount):
##        u'Sets/returns value determining maximum number of document windows listed on Windows menu.'
##    WindowMenuContainsNItems = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Display the drop-down completion window in the Command Window.'
##        #return pComplete
##    def _set(self, pComplete):
##        u'Display the drop-down completion window in the Command Window.'
##    ShowCommandWindowCompletion = property(_get, _set, doc = _set.__doc__)
##

_DTEEvents._methods_ = [
]
################################################################
## code template for _DTEEvents implementation
##class _DTEEvents_Impl(object):

class _EnvironmentProjectsAndSolution(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{478F06D4-5D57-473F-9B74-5F8E88EFA5E7}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_EnvironmentProjectsAndSolution._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Sets/returns value determining whether environment should save everything before running or previewing.'), 'propput'], HRESULT, 'OnRunOrPreview',
              ( ['in'], vsSaveChanges, 'pbld' )),
    COMMETHOD([dispid(1), helpstring(u'Sets/returns value determining whether environment should save everything before running or previewing.'), 'propget'], HRESULT, 'OnRunOrPreview',
              ( ['retval', 'out'], POINTER(vsSaveChanges), 'pbld' )),
    COMMETHOD([dispid(2), 'propput'], HRESULT, 'ProjectsLocation',
              ( ['in'], BSTR, 'pLocation' )),
    COMMETHOD([dispid(2), 'propget'], HRESULT, 'ProjectsLocation',
              ( ['retval', 'out'], POINTER(BSTR), 'pLocation' )),
    COMMETHOD([dispid(3), 'propput'], HRESULT, 'ShowOutputWindowBeforeBuild',
              ( ['in'], VARIANT_BOOL, 'pfshow' )),
    COMMETHOD([dispid(3), 'propget'], HRESULT, 'ShowOutputWindowBeforeBuild',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfshow' )),
    COMMETHOD([dispid(4), 'propput'], HRESULT, 'ShowTaskListAfterBuild',
              ( ['in'], VARIANT_BOOL, 'pfshow' )),
    COMMETHOD([dispid(4), 'propget'], HRESULT, 'ShowTaskListAfterBuild',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfshow' )),
]
################################################################
## code template for _EnvironmentProjectsAndSolution implementation
##class _EnvironmentProjectsAndSolution_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return pfshow
##    def _set(self, pfshow):
##        '-no docstring-'
##    ShowTaskListAfterBuild = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Sets/returns value determining whether environment should save everything before running or previewing.'
##        #return pbld
##    def _set(self, pbld):
##        u'Sets/returns value determining whether environment should save everything before running or previewing.'
##    OnRunOrPreview = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pLocation
##    def _set(self, pLocation):
##        '-no docstring-'
##    ProjectsLocation = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return pfshow
##    def _set(self, pfshow):
##        '-no docstring-'
##    ShowOutputWindowBeforeBuild = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'vsext_StartUp'
vsext_su_EMPTY_ENVIRONMENT = 0
vsext_su_NEW_SOLUTION_DIALOG = 1
vsext_su_LOAD_LAST_SOLUTION = 2
vsext_StartUp = c_int # enum
class _dispProjectsEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'The _ProjectsEvents object triggers events of actions taken against projects.'
    _iid_ = GUID('{7F508D55-627F-4D7F-BE0B-9E3D829FF0ED}')
    _idlflags_ = []
    _methods_ = []
_dispProjectsEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Triggered when a project is added to the solution.')], None, 'ItemAdded',
               ( ['in'], POINTER(Project), 'Project' )),
    DISPMETHOD([dispid(2), helpstring(u'Triggered when a project is removed from a solution.')], None, 'ItemRemoved',
               ( ['in'], POINTER(Project), 'Project' )),
    DISPMETHOD([dispid(3), helpstring(u'Triggered when a project within a solution is renamed.')], None, 'ItemRenamed',
               ( ['in'], POINTER(Project), 'Project' ),
               ( ['in'], BSTR, 'OldName' )),
]
class ProjectsEvents(CoClass):
    u'The _ProjectsEvents object triggers events of actions taken against projects.'
    _reg_clsid_ = GUID('{536A4BE3-A376-408E-954C-471C779E216F}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
ProjectsEvents._com_interfaces_ = [_ProjectsEvents]
ProjectsEvents._outgoing_interfaces_ = [_dispProjectsEvents]

Macros._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(3), helpstring(u'Returns true if the macro recorder is recording actions (Not to be used from within a macro).'), 'propget'], HRESULT, 'IsRecording',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'vbIsRecording' )),
    COMMETHOD([dispid(4), helpstring(u'Writes the line of code to the macro being recorded (Not to be used from within a macro).')], HRESULT, 'EmitMacroCode',
              ( [], BSTR, 'Code' )),
    COMMETHOD([dispid(5), helpstring(u'Pause the macro recorder so no code is written to the recording macro (Not to be used from within a macro).')], HRESULT, 'Pause'),
    COMMETHOD([dispid(6), helpstring(u'Resumes the macro recorder from the paused state so code is written to the recording macro (Not to be used from within a macro).')], HRESULT, 'Resume'),
]
################################################################
## code template for Macros implementation
##class Macros_Impl(object):
##    def Pause(self):
##        u'Pause the macro recorder so no code is written to the recording macro (Not to be used from within a macro).'
##        #return 
##
##    def EmitMacroCode(self, Code):
##        u'Writes the line of code to the macro being recorded (Not to be used from within a macro).'
##        #return 
##
##    @property
##    def Parent(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    def Resume(self):
##        u'Resumes the macro recorder from the paused state so code is written to the recording macro (Not to be used from within a macro).'
##        #return 
##
##    @property
##    def IsRecording(self):
##        u'Returns true if the macro recorder is recording actions (Not to be used from within a macro).'
##        #return vbIsRecording
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##

class CodeParameter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An object defining a parameter to a function, property, etc. in a source file.'
    _iid_ = GUID('{0CFBC2BD-0D4E-11D3-8997-00C04F688DDE}')
    _idlflags_ = ['dual', 'oleautomation']
CodeDelegate._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ParentObject' )),
    COMMETHOD([dispid(32), helpstring(u'Returns an object defining the parent namespace.'), 'nonbrowsable', 'propget'], HRESULT, 'Namespace',
              ( ['retval', 'out'], POINTER(POINTER(CodeNamespace)), 'ppCodeNamespace' )),
    COMMETHOD([dispid(33), helpstring(u'Returns a collection of classes this item derives from.'), 'nonbrowsable', 'propget'], HRESULT, 'Bases',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(34), helpstring(u'Returns a collection of items contained by this element.'), 'nonbrowsable', 'propget'], HRESULT, 'Members',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(35), helpstring(u'Defines the access attributes of this item.'), 'propput'], HRESULT, 'Access',
              ( [], vsCMAccess, 'pAccess' )),
    COMMETHOD([dispid(35), helpstring(u'Defines the access attributes of this item.'), 'propget'], HRESULT, 'Access',
              ( ['retval', 'out'], POINTER(vsCMAccess), 'pAccess' )),
    COMMETHOD([dispid(36), helpstring(u'Returns a collection of items containing attributes.'), 'nonbrowsable', 'propget'], HRESULT, 'Attributes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(37), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propget'], HRESULT, 'DocComment',
              ( ['retval', 'out'], POINTER(BSTR), 'pDocComment' )),
    COMMETHOD([dispid(37), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propput'], HRESULT, 'DocComment',
              ( [], BSTR, 'pDocComment' )),
    COMMETHOD([dispid(38), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Comment',
              ( ['retval', 'out'], POINTER(BSTR), 'pComment' )),
    COMMETHOD([dispid(38), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propput'], HRESULT, 'Comment',
              ( [], BSTR, 'pComment' )),
    COMMETHOD([dispid(39), helpstring(u'Adds an item to the list of inherited objects.')], HRESULT, 'AddBase',
              ( [], VARIANT, 'Base' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeElement)), 'ppOut' )),
    COMMETHOD([dispid(40), helpstring(u'Creates a new attribute code construct and inserts the code in the correct location.')], HRESULT, 'AddAttribute',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeAttribute)), 'ppCodeAttribute' )),
    COMMETHOD([dispid(41), helpstring(u'Removes an object from the list of bases.')], HRESULT, 'RemoveBase',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(42), helpstring(u'Removes a member code construct.')], HRESULT, 'RemoveMember',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(43), helpstring(u'Returns a Boolean telling if an object has another object as a base.'), 'propget'], HRESULT, 'IsDerivedFrom',
              ( [], BSTR, 'FullName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(44), helpstring(u'Returns a collection of objects derived from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'DerivedTypes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(61), helpstring(u'Returns the class this object inherits from.'), 'nonbrowsable', 'propget'], HRESULT, 'BaseClass',
              ( ['retval', 'out'], POINTER(POINTER(CodeClass)), 'ppCodeClass' )),
    COMMETHOD([dispid(62), helpstring(u'Returns a string holding the stub definition of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Prototype',
              ( ['optional'], c_int, 'Flags', 0 ),
              ( ['retval', 'out'], POINTER(BSTR), 'pPrototype' )),
    COMMETHOD([dispid(63), helpstring(u'Sets/Returns an object representing the programmatic type.'), 'nonbrowsable', 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(POINTER(CodeTypeRef)), 'pCodeTypeRef' )),
    COMMETHOD([dispid(63), helpstring(u'Sets/Returns an object representing the programmatic type.'), 'nonbrowsable', 'propput'], HRESULT, 'Type',
              ( [], POINTER(CodeTypeRef), 'pCodeTypeRef' )),
    COMMETHOD([dispid(64), helpstring(u'Returns a collection of parameters for this item.'), 'nonbrowsable', 'propget'], HRESULT, 'Parameters',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppParameters' )),
    COMMETHOD([dispid(65), helpstring(u'Creates a new parameter code construct and inserts the code in the correct location.')], HRESULT, 'AddParameter',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeParameter)), 'ppCodeParameter' )),
    COMMETHOD([dispid(66), helpstring(u'Removes a parameter from the argument list.')], HRESULT, 'RemoveParameter',
              ( [], VARIANT, 'Element' )),
]
################################################################
## code template for CodeDelegate implementation
##class CodeDelegate_Impl(object):
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Parameters(self):
##        u'Returns a collection of parameters for this item.'
##        #return ppParameters
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def Namespace(self):
##        u'Returns an object defining the parent namespace.'
##        #return ppCodeNamespace
##
##    def AddBase(self, Base, Position):
##        u'Adds an item to the list of inherited objects.'
##        #return ppOut
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    def _get(self):
##        u'Defines the access attributes of this item.'
##        #return pAccess
##    def _set(self, pAccess):
##        u'Defines the access attributes of this item.'
##    Access = property(_get, _set, doc = _set.__doc__)
##
##    def AddParameter(self, Name, Type, Position):
##        u'Creates a new parameter code construct and inserts the code in the correct location.'
##        #return ppCodeParameter
##
##    @property
##    def Bases(self):
##        u'Returns a collection of classes this item derives from.'
##        #return ppCodeElements
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    @property
##    def Prototype(self, Flags):
##        u'Returns a string holding the stub definition of this object.'
##        #return pPrototype
##
##    def _get(self):
##        u'Sets/Returns an object representing the programmatic type.'
##        #return pCodeTypeRef
##    def _set(self, pCodeTypeRef):
##        u'Sets/Returns an object representing the programmatic type.'
##    Type = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ParentObject
##
##    def RemoveParameter(self, Element):
##        u'Removes a parameter from the argument list.'
##        #return 
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    def AddAttribute(self, Name, Value, Position):
##        u'Creates a new attribute code construct and inserts the code in the correct location.'
##        #return ppCodeAttribute
##
##    def RemoveMember(self, Element):
##        u'Removes a member code construct.'
##        #return 
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def Members(self):
##        u'Returns a collection of items contained by this element.'
##        #return ppCodeElements
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def _get(self):
##        u'Returns the document comment on the current code model element.'
##        #return pDocComment
##    def _set(self, pDocComment):
##        u'Returns the document comment on the current code model element.'
##    DocComment = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveBase(self, Element):
##        u'Removes an object from the list of bases.'
##        #return 
##
##    @property
##    def Attributes(self):
##        u'Returns a collection of items containing attributes.'
##        #return ppCodeElements
##
##    def _get(self):
##        u'Sets/Returns an object defining the comment for this object.'
##        #return pComment
##    def _set(self, pComment):
##        u'Sets/Returns an object defining the comment for this object.'
##    Comment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsDerivedFrom(self, FullName):
##        u'Returns a Boolean telling if an object has another object as a base.'
##        #return pVal
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    @property
##    def DerivedTypes(self):
##        u'Returns a collection of objects derived from this object.'
##        #return ppCodeElements
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    @property
##    def BaseClass(self):
##        u'Returns the class this object inherits from.'
##        #return ppCodeClass
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##

_CommandBarControlEvents._methods_ = [
]
################################################################
## code template for _CommandBarControlEvents implementation
##class _CommandBarControlEvents_Impl(object):

TextRanges._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(TextDocument)), 'ppParent' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(TextRange)), 'ppRange' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
]
################################################################
## code template for TextRanges implementation
##class TextRanges_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return ppRange
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppParent
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##

_dispDTEEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Occurs when the environment has completed initializing.')], None, 'OnStartupComplete'),
    DISPMETHOD([dispid(2), helpstring(u'Occurs when the environment is beginning to close.')], None, 'OnBeginShutdown'),
    DISPMETHOD([dispid(3), helpstring(u'Occurs when the state of the environment has changed.')], None, 'ModeChanged',
               ( ['in'], vsIDEMode, 'LastMode' )),
    DISPMETHOD([dispid(4), helpstring(u"Occurs when the macro engine has reset it's state, clearing all variable data.")], None, 'OnMacrosRuntimeReset'),
]
_dispCommandBarControlEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Occurs when OnAction property for corresponding CommandBarControl object is set or returned.')], None, 'Click',
               ( ['in'], POINTER(IDispatch), 'CommandBarControl' ),
               ( ['in'], POINTER(VARIANT_BOOL), 'Handled' ),
               ( ['in'], POINTER(VARIANT_BOOL), 'CancelDefault' )),
]
vsProjectKindSolutionItems = u'{66A26720-8FB5-11D2-AA7E-00C04F688DDE}' # Constant STRING
vsProjectItemKindSubProject = u'{EA6618E8-6E24-4528-94BE-6889FE16485C}' # Constant STRING
vsext_GUID_AddItemWizard = u'{0F90E1D1-4999-11D1-B6D1-00A0C90F2744}' # Constant STRING
vsWindowKindFindResults1 = u'{0F887920-C2B6-11D2-9375-0080C747D9A0}' # Constant STRING
vsWindowKindFindResults2 = u'{0F887921-C2B6-11D2-9375-0080C747D9A0}' # Constant STRING
vsext_wk_PropertyBrowser = u'{EEFA5220-E298-11D0-8F78-00A0C9110057}' # Constant STRING
class _EnvironmentHelp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{AEBDED64-A206-11D3-B8B5-00C04F79F802}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
_EnvironmentHelp._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Gets/Sets preffered help language.'), 'propget'], HRESULT, 'PreferredLanguage',
              ( ['retval', 'out'], POINTER(c_int), 'LCID' )),
    COMMETHOD([dispid(0), helpstring(u'Gets/Sets preffered help language.'), 'propput'], HRESULT, 'PreferredLanguage',
              ( ['in'], c_int, 'LCID' )),
    COMMETHOD([dispid(1), helpstring(u'Gets/Sets preferred collection file or namespace.'), 'propget'], HRESULT, 'PreferredCollection',
              ( ['retval', 'out'], POINTER(BSTR), 'Namespace' )),
    COMMETHOD([dispid(1), helpstring(u'Gets/Sets preferred collection file or namespace.'), 'propput'], HRESULT, 'PreferredCollection',
              ( ['in'], BSTR, 'Namespace' )),
    COMMETHOD([dispid(2), helpstring(u'Use external help viewer.'), 'propget'], HRESULT, 'External',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ExternalHelp' )),
    COMMETHOD([dispid(2), helpstring(u'Use external help viewer.'), 'propput'], HRESULT, 'External',
              ( ['in'], VARIANT_BOOL, 'ExternalHelp' )),
]
################################################################
## code template for _EnvironmentHelp implementation
##class _EnvironmentHelp_Impl(object):
##    def _get(self):
##        u'Gets/Sets preffered help language.'
##        #return LCID
##    def _set(self, LCID):
##        u'Gets/Sets preffered help language.'
##    PreferredLanguage = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets preferred collection file or namespace.'
##        #return Namespace
##    def _set(self, Namespace):
##        u'Gets/Sets preferred collection file or namespace.'
##    PreferredCollection = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Use external help viewer.'
##        #return ExternalHelp
##    def _set(self, ExternalHelp):
##        u'Use external help viewer.'
##    External = property(_get, _set, doc = _set.__doc__)
##

vsWindowKindMainWindow = u'{9DDABE98-1D02-11D3-89A1-00C04F688DDE}' # Constant STRING
vsWindowKindLinkedWindowFrame = u'{9DDABE99-1D02-11D3-89A1-00C04F688DDE}' # Constant STRING
vsWindowKindWebBrowser = u'{E8B06F52-6D01-11D2-AA7D-00C04F990343}' # Constant STRING
vsWizardAddSubProject = u'{0F90E1D2-4999-11D1-B6D1-00A0C90F2744}' # Constant STRING
vsWizardAddItem = u'{0F90E1D1-4999-11D1-B6D1-00A0C90F2744}' # Constant STRING
CodeNamespace._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ParentObject' )),
    COMMETHOD([dispid(32), helpstring(u'Returns a collection of items contained by this element.'), 'nonbrowsable', 'propget'], HRESULT, 'Members',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppMembers' )),
    COMMETHOD([dispid(35), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propget'], HRESULT, 'DocComment',
              ( ['retval', 'out'], POINTER(BSTR), 'pDocComment' )),
    COMMETHOD([dispid(35), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propput'], HRESULT, 'DocComment',
              ( [], BSTR, 'pDocComment' )),
    COMMETHOD([dispid(36), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Comment',
              ( ['retval', 'out'], POINTER(BSTR), 'pComment' )),
    COMMETHOD([dispid(36), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propput'], HRESULT, 'Comment',
              ( [], BSTR, 'pComment' )),
    COMMETHOD([dispid(37), helpstring(u'Creates a new namespace code construct and inserts the code in the correct location.')], HRESULT, 'AddNamespace',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeNamespace)), 'ppCodeNamespace' )),
    COMMETHOD([dispid(38), helpstring(u'Creates a new class code construct and inserts the code in the correct location.')], HRESULT, 'AddClass',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], VARIANT, 'ImplementedInterfaces' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeClass)), 'ppCodeClass' )),
    COMMETHOD([dispid(39), helpstring(u'Creates a new interface code construct and inserts the code in the correct location.')], HRESULT, 'AddInterface',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeInterface)), 'ppCodeInterface' )),
    COMMETHOD([dispid(40), helpstring(u'Creates a new structure code construct and inserts the code in the correct location.')], HRESULT, 'AddStruct',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], VARIANT, 'ImplementedInterfaces' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeStruct)), 'ppCodeStruct' )),
    COMMETHOD([dispid(41), helpstring(u'Creates a new enumeration code construct and inserts the code in the correct location.')], HRESULT, 'AddEnum',
              ( [], BSTR, 'Name' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], VARIANT, 'Bases' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeEnum)), 'ppCodeEnum' )),
    COMMETHOD([dispid(42), helpstring(u'Creates a new delegate code construct and inserts the code in the correct location.')], HRESULT, 'AddDelegate',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['optional'], vsCMAccess, 'Access', 32 ),
              ( ['retval', 'out'], POINTER(POINTER(CodeDelegate)), 'ppCodeDelegate' )),
    COMMETHOD([dispid(43), helpstring(u'Removes a code element from the source file.')], HRESULT, 'Remove',
              ( [], VARIANT, 'Element' )),
]
################################################################
## code template for CodeNamespace implementation
##class CodeNamespace_Impl(object):
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    def AddStruct(self, Name, Position, Bases, ImplementedInterfaces, Access):
##        u'Creates a new structure code construct and inserts the code in the correct location.'
##        #return ppCodeStruct
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    def AddEnum(self, Name, Position, Bases, Access):
##        u'Creates a new enumeration code construct and inserts the code in the correct location.'
##        #return ppCodeEnum
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    def AddInterface(self, Name, Position, Bases, Access):
##        u'Creates a new interface code construct and inserts the code in the correct location.'
##        #return ppCodeInterface
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ParentObject
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def Members(self):
##        u'Returns a collection of items contained by this element.'
##        #return ppMembers
##
##    def AddDelegate(self, Name, Type, Position, Access):
##        u'Creates a new delegate code construct and inserts the code in the correct location.'
##        #return ppCodeDelegate
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def _get(self):
##        u'Returns the document comment on the current code model element.'
##        #return pDocComment
##    def _set(self, pDocComment):
##        u'Returns the document comment on the current code model element.'
##    DocComment = property(_get, _set, doc = _set.__doc__)
##
##    def Remove(self, Element):
##        u'Removes a code element from the source file.'
##        #return 
##
##    def AddNamespace(self, Name, Position):
##        u'Creates a new namespace code construct and inserts the code in the correct location.'
##        #return ppCodeNamespace
##
##    def AddClass(self, Name, Position, Bases, ImplementedInterfaces, Access):
##        u'Creates a new class code construct and inserts the code in the correct location.'
##        #return ppCodeClass
##
##    def _get(self):
##        u'Sets/Returns an object defining the comment for this object.'
##        #return pComment
##    def _set(self, pComment):
##        u'Sets/Returns an object defining the comment for this object.'
##    Comment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##

class IVsGlobals(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{192AC688-E7C6-4F9D-8180-4B37EFBF6F3A}')
    _idlflags_ = ['hidden', 'restricted']
IVsGlobals._methods_ = [
    COMMETHOD([], HRESULT, 'Load'),
    COMMETHOD([], HRESULT, 'Save'),
    COMMETHOD([], HRESULT, 'Empty'),
]
################################################################
## code template for IVsGlobals implementation
##class IVsGlobals_Impl(object):
##    def Load(self):
##        '-no docstring-'
##        #return 
##
##    def Save(self):
##        '-no docstring-'
##        #return 
##
##    def Empty(self):
##        '-no docstring-'
##        #return 
##

vsProjectItemsKindMisc = u'{66A2671E-8FB5-11D2-AA7E-00C04F688DDE}' # Constant STRING
vsProjectItemKindMisc = u'{66A2671F-8FB5-11D2-AA7E-00C04F688DDE}' # Constant STRING
vsProjectKindUnmodeled = u'{67294A52-A4F0-11D2-AA88-00C04F688DDE}' # Constant STRING
vsContextSolutionBuilding = u'{ADFC4E60-0397-11D1-9F4E-00A0C911004F}' # Constant STRING
vsProjectItemsKindSolutionItems = u'{66A26721-8FB5-11D2-AA7E-00C04F688DDE}' # Constant STRING
vsProjectItemKindSolutionItems = u'{66A26722-8FB5-11D2-AA7E-00C04F688DDE}' # Constant STRING
vsProjectsKindSolution = u'{96410B9F-3542-4A14-877F-BC7227B51D3B}' # Constant STRING
vsAddInCmdGroup = u'{1E58696E-C90F-11D2-AAB2-00C04F688DDE}' # Constant STRING
EditPoint._methods_ = [
    COMMETHOD([dispid(101), helpstring(u'Moves the object the specified number of characters to the left. The default is 1 character.')], HRESULT, 'CharLeft',
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(102), helpstring(u'Moves the object the specified number of characters to the right. The default is 1 character.')], HRESULT, 'CharRight',
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(103), helpstring(u'Moves the object to the end of the current line.')], HRESULT, 'EndOfLine'),
    COMMETHOD([dispid(104), helpstring(u'Moves the object to the beginning of the current line.')], HRESULT, 'StartOfLine'),
    COMMETHOD([dispid(105), helpstring(u'Moves the object to the end of the document.')], HRESULT, 'EndOfDocument'),
    COMMETHOD([dispid(106), helpstring(u'Moves the object to the beginning of the document.')], HRESULT, 'StartOfDocument'),
    COMMETHOD([dispid(107), helpstring(u'Moves the object the specified number of words to the left. The default is 1 word.')], HRESULT, 'WordLeft',
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(108), helpstring(u'Moves the object the specified number of words to the right. The default is 1 word.')], HRESULT, 'WordRight',
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(109), helpstring(u'Moves the object up by the specified number of lines. The default is 1 line.')], HRESULT, 'LineUp',
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(110), helpstring(u'Moves the object down by the specified number of lines. The default is 1 line.')], HRESULT, 'LineDown',
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(170), helpstring(u'Moves the active point to the given position.')], HRESULT, 'MoveToPoint',
              ( ['in'], POINTER(TextPoint), 'Point' )),
    COMMETHOD([dispid(171), helpstring(u'Moves the active point to the given position.')], HRESULT, 'MoveToLineAndOffset',
              ( ['in'], c_int, 'Line' ),
              ( ['in'], c_int, 'Offset' )),
    COMMETHOD([dispid(172), helpstring(u'Moves the active point to the given 1-based absolute character offset.')], HRESULT, 'MoveToAbsoluteOffset',
              ( ['in'], c_int, 'Offset' )),
    COMMETHOD([dispid(121), helpstring(u'Sets an unnamed bookmark on the current line.')], HRESULT, 'SetBookmark'),
    COMMETHOD([dispid(122), helpstring(u'Clears any unnamed bookmarks on the current line.')], HRESULT, 'ClearBookmark'),
    COMMETHOD([dispid(123), helpstring(u'Moves to the location of the next bookmark in the document.')], HRESULT, 'NextBookmark',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbFound' )),
    COMMETHOD([dispid(124), helpstring(u'Moves to the location of the previous bookmark in the document.')], HRESULT, 'PreviousBookmark',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbFound' )),
    COMMETHOD([dispid(131), helpstring(u'Fills the current line with white space to the given column.')], HRESULT, 'PadToColumn',
              ( ['in'], c_int, 'Column' )),
    COMMETHOD([dispid(132), helpstring(u'Inserts the given string at the current location.')], HRESULT, 'Insert',
              ( ['in'], BSTR, 'Text' )),
    COMMETHOD([dispid(133), helpstring(u'Inserts the contents of the specified file at the current location.')], HRESULT, 'InsertFromFile',
              ( ['in'], BSTR, 'File' )),
    COMMETHOD([dispid(134), helpstring(u'Returns the text between the current location and the specified location.')], HRESULT, 'GetText',
              ( ['in'], VARIANT, 'PointOrCount' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrText' )),
    COMMETHOD([dispid(173), helpstring(u'Returns the text between the indicated lines (and including the beginning line).')], HRESULT, 'GetLines',
              ( ['in'], c_int, 'Start' ),
              ( ['in'], c_int, 'ExclusiveEnd' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrText' )),
    COMMETHOD([dispid(136), helpstring(u'Copies the indicated span of text to the clipboard.')], HRESULT, 'Copy',
              ( ['in'], VARIANT, 'PointOrCount' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Append', False )),
    COMMETHOD([dispid(137), helpstring(u'Copies the indicated span of text to the clipboard and deletes it.')], HRESULT, 'Cut',
              ( ['in'], VARIANT, 'PointOrCount' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'Append', False )),
    COMMETHOD([dispid(135), helpstring(u'Deletes the indicated span of text.')], HRESULT, 'Delete',
              ( ['in'], VARIANT, 'PointOrCount' )),
    COMMETHOD([dispid(138), helpstring(u'Inserts the clipboard contents at the current location.')], HRESULT, 'Paste'),
    COMMETHOD([dispid(139), helpstring(u'Returns whether the indicated span contains any read-only text.')], HRESULT, 'ReadOnly',
              ( ['in'], VARIANT, 'PointOrCount' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lfResult' )),
    COMMETHOD([dispid(151), helpstring(u'Finds a pattern of text in the given span.')], HRESULT, 'FindPattern',
              ( ['in'], BSTR, 'Pattern' ),
              ( ['in', 'optional'], c_int, 'vsFindOptionsValue', 0 ),
              ( ['in', 'out', 'optional'], POINTER(POINTER(EditPoint)), 'EndPoint', 0 ),
              ( ['in', 'out', 'optional'], POINTER(POINTER(TextRanges)), 'Tags', 0 ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbFound' )),
    COMMETHOD([dispid(152), helpstring(u'Finds a pattern of text in the given span and replaces it with the specified text.')], HRESULT, 'ReplacePattern',
              ( ['in'], POINTER(TextPoint), 'Point' ),
              ( ['in'], BSTR, 'Pattern' ),
              ( ['in'], BSTR, 'Replace' ),
              ( ['in', 'optional'], c_int, 'vsFindOptionsValue', 0 ),
              ( ['in', 'out', 'optional'], POINTER(POINTER(TextRanges)), 'Tags', 0 ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pbFound' )),
    COMMETHOD([dispid(161), helpstring(u'Indents the indicated span of lines by the number of indentation levels given. The defaults are the current line and 1 indentation level.')], HRESULT, 'Indent',
              ( ['in', 'optional'], POINTER(TextPoint), 'Point', 0 ),
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(162), helpstring(u'Removes indents from the indicated span of lines by the number of indentation levels given. The defaults are the current line and 1 indentation level.')], HRESULT, 'Unindent',
              ( ['in', 'optional'], POINTER(TextPoint), 'Point', 0 ),
              ( ['in', 'optional'], c_int, 'Count', 1 )),
    COMMETHOD([dispid(163), helpstring(u'Formats the indicated span of text based on the current language.')], HRESULT, 'SmartFormat',
              ( ['in'], POINTER(TextPoint), 'Point' )),
    COMMETHOD([dispid(167), helpstring(u'Creates an outlining section between the current point and the specified point.')], HRESULT, 'OutlineSection',
              ( ['in'], VARIANT, 'PointOrCount' )),
    COMMETHOD([dispid(164), helpstring(u'Replaces the indicated span of text with the given text.')], HRESULT, 'ReplaceText',
              ( ['in'], VARIANT, 'PointOrCount' ),
              ( ['in'], BSTR, 'Text' ),
              ( ['in'], c_int, 'Flags' )),
    COMMETHOD([dispid(165), helpstring(u'Changes the case of the text in the indicated span.')], HRESULT, 'ChangeCase',
              ( ['in'], VARIANT, 'PointOrCount' ),
              ( ['in'], vsCaseOptions, 'How' )),
    COMMETHOD([dispid(166), helpstring(u'Deletes white space horizontally or vertically around the current location.')], HRESULT, 'DeleteWhitespace',
              ( ['in', 'optional'], vsWhitespaceOptions, 'Direction', 0 )),
]
################################################################
## code template for EditPoint implementation
##class EditPoint_Impl(object):
##    def Cut(self, PointOrCount, Append):
##        u'Copies the indicated span of text to the clipboard and deletes it.'
##        #return 
##
##    def EndOfDocument(self):
##        u'Moves the object to the end of the document.'
##        #return 
##
##    def StartOfDocument(self):
##        u'Moves the object to the beginning of the document.'
##        #return 
##
##    def SmartFormat(self, Point):
##        u'Formats the indicated span of text based on the current language.'
##        #return 
##
##    def WordLeft(self, Count):
##        u'Moves the object the specified number of words to the left. The default is 1 word.'
##        #return 
##
##    def ReplaceText(self, PointOrCount, Text, Flags):
##        u'Replaces the indicated span of text with the given text.'
##        #return 
##
##    def FindPattern(self, Pattern, vsFindOptionsValue):
##        u'Finds a pattern of text in the given span.'
##        #return EndPoint, Tags, pbFound
##
##    def CharRight(self, Count):
##        u'Moves the object the specified number of characters to the right. The default is 1 character.'
##        #return 
##
##    def PreviousBookmark(self):
##        u'Moves to the location of the previous bookmark in the document.'
##        #return pbFound
##
##    def MoveToAbsoluteOffset(self, Offset):
##        u'Moves the active point to the given 1-based absolute character offset.'
##        #return 
##
##    def SetBookmark(self):
##        u'Sets an unnamed bookmark on the current line.'
##        #return 
##
##    def MoveToPoint(self, Point):
##        u'Moves the active point to the given position.'
##        #return 
##
##    def GetText(self, PointOrCount):
##        u'Returns the text between the current location and the specified location.'
##        #return pbstrText
##
##    def WordRight(self, Count):
##        u'Moves the object the specified number of words to the right. The default is 1 word.'
##        #return 
##
##    def MoveToLineAndOffset(self, Line, Offset):
##        u'Moves the active point to the given position.'
##        #return 
##
##    def ReplacePattern(self, Point, Pattern, Replace, vsFindOptionsValue):
##        u'Finds a pattern of text in the given span and replaces it with the specified text.'
##        #return Tags, pbFound
##
##    def Copy(self, PointOrCount, Append):
##        u'Copies the indicated span of text to the clipboard.'
##        #return 
##
##    def Paste(self):
##        u'Inserts the clipboard contents at the current location.'
##        #return 
##
##    def Insert(self, Text):
##        u'Inserts the given string at the current location.'
##        #return 
##
##    def Unindent(self, Point, Count):
##        u'Removes indents from the indicated span of lines by the number of indentation levels given. The defaults are the current line and 1 indentation level.'
##        #return 
##
##    def Indent(self, Point, Count):
##        u'Indents the indicated span of lines by the number of indentation levels given. The defaults are the current line and 1 indentation level.'
##        #return 
##
##    def PadToColumn(self, Column):
##        u'Fills the current line with white space to the given column.'
##        #return 
##
##    def CharLeft(self, Count):
##        u'Moves the object the specified number of characters to the left. The default is 1 character.'
##        #return 
##
##    def NextBookmark(self):
##        u'Moves to the location of the next bookmark in the document.'
##        #return pbFound
##
##    def GetLines(self, Start, ExclusiveEnd):
##        u'Returns the text between the indicated lines (and including the beginning line).'
##        #return pbstrText
##
##    def ChangeCase(self, PointOrCount, How):
##        u'Changes the case of the text in the indicated span.'
##        #return 
##
##    def OutlineSection(self, PointOrCount):
##        u'Creates an outlining section between the current point and the specified point.'
##        #return 
##
##    def Delete(self, PointOrCount):
##        u'Deletes the indicated span of text.'
##        #return 
##
##    def EndOfLine(self):
##        u'Moves the object to the end of the current line.'
##        #return 
##
##    def StartOfLine(self):
##        u'Moves the object to the beginning of the current line.'
##        #return 
##
##    def ReadOnly(self, PointOrCount):
##        u'Returns whether the indicated span contains any read-only text.'
##        #return lfResult
##
##    def DeleteWhitespace(self, Direction):
##        u'Deletes white space horizontally or vertically around the current location.'
##        #return 
##
##    def ClearBookmark(self):
##        u'Clears any unnamed bookmarks on the current line.'
##        #return 
##
##    def LineUp(self, Count):
##        u'Moves the object up by the specified number of lines. The default is 1 line.'
##        #return 
##
##    def LineDown(self, Count):
##        u'Moves the object down by the specified number of lines. The default is 1 line.'
##        #return 
##
##    def InsertFromFile(self, File):
##        u'Inserts the contents of the specified file at the current location.'
##        #return 
##

vsext_wk_CallStackWindow = u'{0504FF91-9D61-11D0-A794-00A0C9110051}' # Constant STRING
vsContextDebugging = u'{ADFC4E61-0397-11D1-9F4E-00A0C911004F}' # Constant STRING

# values for enumeration 'DsSaveChanges'
dsSaveChangesYes = 1
dsSaveChangesNo = 2
dsSaveChangesPrompt = 3
DsSaveChanges = c_int # enum
vsContextFullScreenMode = u'{ADFC4E62-0397-11D1-9F4E-00A0C911004F}' # Constant STRING
vsContextDesignMode = u'{ADFC4E63-0397-11D1-9F4E-00A0C911004F}' # Constant STRING
vsContextNoSolution = u'{ADFC4E64-0397-11D1-9F4E-00A0C911004F}' # Constant STRING
vsContextEmptySolution = u'{ADFC4E65-0397-11D1-9F4E-00A0C911004F}' # Constant STRING
vsContextSolutionHasSingleProject = u'{ADFC4E66-0397-11D1-9F4E-00A0C911004F}' # Constant STRING
vsContextSolutionHasMultipleProjects = u'{93694FA0-0397-11D1-9F4E-00A0C911004F}' # Constant STRING
vsContextMacroRecording = u'{04BBF6A5-4697-11D2-890E-0060083196C6}' # Constant STRING
Windows._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'lppcReturn' )),
    COMMETHOD([dispid(201), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'lplReturn' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(300), helpstring(u'Creates a new tool window containing the indicated ActiveX document or control.')], HRESULT, 'CreateToolWindow',
              ( ['in'], POINTER(AddIn), 'AddInInst' ),
              ( ['in'], BSTR, 'ProgID' ),
              ( ['in'], BSTR, 'Caption' ),
              ( ['in'], BSTR, 'GuidPosition' ),
              ( ['in', 'out'], POINTER(POINTER(IDispatch)), 'DocObj' ),
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'lppcReturn' )),
    COMMETHOD([dispid(301), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(302), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(303), helpstring(u'Creates a Window object for a linked window frame, and places two windows on it.')], HRESULT, 'CreateLinkedWindowFrame',
              ( ['in'], POINTER(Window), 'Window1' ),
              ( ['in'], POINTER(Window), 'Window2' ),
              ( ['in'], vsLinkedWindowType, 'Link' ),
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'LinkedWindowFrame' )),
]
################################################################
## code template for Windows implementation
##class Windows_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return lplReturn
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppaReturn
##
##    def CreateLinkedWindowFrame(self, Window1, Window2, Link):
##        u'Creates a Window object for a linked window frame, and places two windows on it.'
##        #return LinkedWindowFrame
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return lppcReturn
##
##    def CreateToolWindow(self, AddInInst, ProgID, Caption, GuidPosition):
##        u'Creates a new tool window containing the indicated ActiveX document or control.'
##        #return DocObj, lppcReturn
##

vsMiscFilesProjectUniqueName = u'<MiscFiles>' # Constant STRING
vsSolutionItemsProjectUniqueName = u'<SolnItems>' # Constant STRING
vsProjectItemKindPhysicalFile = u'{6BB5F8EE-4483-11D3-8BCF-00C04F8EC28C}' # Constant STRING
CodeFunction._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ParentObject' )),
    COMMETHOD([dispid(32), helpstring(u'Returns an enumeration describing how a function is used.'), 'nonbrowsable', 'propget'], HRESULT, 'FunctionKind',
              ( ['retval', 'out'], POINTER(vsCMFunction), 'ppFunctionKind' )),
    COMMETHOD([dispid(34), helpstring(u'Returns a string holding the stub definition of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Prototype',
              ( ['in', 'optional'], c_int, 'Flags', 0 ),
              ( ['retval', 'out'], POINTER(BSTR), 'pFullName' )),
    COMMETHOD([dispid(35), helpstring(u'Sets/Returns an object representing the programmatic type.'), 'nonbrowsable', 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(POINTER(CodeTypeRef)), 'ppCodeTypeRef' )),
    COMMETHOD([dispid(35), helpstring(u'Sets/Returns an object representing the programmatic type.'), 'nonbrowsable', 'propput'], HRESULT, 'Type',
              ( [], POINTER(CodeTypeRef), 'ppCodeTypeRef' )),
    COMMETHOD([dispid(36), helpstring(u'Returns a collection of parameters for this item.'), 'nonbrowsable', 'propget'], HRESULT, 'Parameters',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppMembers' )),
    COMMETHOD([dispid(38), helpstring(u'Defines the access attributes of this item.'), 'propput'], HRESULT, 'Access',
              ( [], vsCMAccess, 'Access' )),
    COMMETHOD([dispid(38), helpstring(u'Defines the access attributes of this item.'), 'propget'], HRESULT, 'Access',
              ( ['retval', 'out'], POINTER(vsCMAccess), 'Access' )),
    COMMETHOD([dispid(39), helpstring(u'Returns if a code element object has multiple signatures.'), 'propget'], HRESULT, 'IsOverloaded',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pvbOverloaded' )),
    COMMETHOD([dispid(40), helpstring(u'Sets/Returns if the item is statically defined or not.'), 'propget'], HRESULT, 'IsShared',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Shared' )),
    COMMETHOD([dispid(40), helpstring(u'Sets/Returns if the item is statically defined or not.'), 'propput'], HRESULT, 'IsShared',
              ( [], VARIANT_BOOL, 'Shared' )),
    COMMETHOD([dispid(41), helpstring(u'Sets/Returns if the item is declared abstract or not.'), 'propget'], HRESULT, 'MustImplement',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'MustImplement' )),
    COMMETHOD([dispid(41), helpstring(u'Sets/Returns if the item is declared abstract or not.'), 'propput'], HRESULT, 'MustImplement',
              ( [], VARIANT_BOOL, 'MustImplement' )),
    COMMETHOD([dispid(42), helpstring(u'Returns a collection of overloaded methods for this item.'), 'nonbrowsable', 'propget'], HRESULT, 'Overloads',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppMembers' )),
    COMMETHOD([dispid(43), helpstring(u'Returns a collection of items containing attributes.'), 'nonbrowsable', 'propget'], HRESULT, 'Attributes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppMembers' )),
    COMMETHOD([dispid(44), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propget'], HRESULT, 'DocComment',
              ( ['retval', 'out'], POINTER(BSTR), 'pDocComment' )),
    COMMETHOD([dispid(44), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propput'], HRESULT, 'DocComment',
              ( [], BSTR, 'pDocComment' )),
    COMMETHOD([dispid(45), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Comment',
              ( ['retval', 'out'], POINTER(BSTR), 'pComment' )),
    COMMETHOD([dispid(45), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propput'], HRESULT, 'Comment',
              ( [], BSTR, 'pComment' )),
    COMMETHOD([dispid(47), helpstring(u'Creates a new parameter code construct and inserts the code in the correct location.')], HRESULT, 'AddParameter',
              ( [], BSTR, 'Name' ),
              ( [], VARIANT, 'Type' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeParameter)), 'ppCodeParameter' )),
    COMMETHOD([dispid(48), helpstring(u'Creates a new attribute code construct and inserts the code in the correct location.')], HRESULT, 'AddAttribute',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeAttribute)), 'ppCodeAttribute' )),
    COMMETHOD([dispid(49), helpstring(u'Removes a parameter from the argument list.')], HRESULT, 'RemoveParameter',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(50), helpstring(u'Sets/Returns if the function can be overridden.'), 'propget'], HRESULT, 'CanOverride',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pCanOverride' )),
    COMMETHOD([dispid(50), helpstring(u'Sets/Returns if the function can be overridden.'), 'propput'], HRESULT, 'CanOverride',
              ( [], VARIANT_BOOL, 'pCanOverride' )),
]
################################################################
## code template for CodeFunction implementation
##class CodeFunction_Impl(object):
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Parameters(self):
##        u'Returns a collection of parameters for this item.'
##        #return ppMembers
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    def _get(self):
##        u'Defines the access attributes of this item.'
##        #return Access
##    def _set(self, Access):
##        u'Defines the access attributes of this item.'
##    Access = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def FunctionKind(self):
##        u'Returns an enumeration describing how a function is used.'
##        #return ppFunctionKind
##
##    @property
##    def IsOverloaded(self):
##        u'Returns if a code element object has multiple signatures.'
##        #return pvbOverloaded
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    @property
##    def Prototype(self, Flags):
##        u'Returns a string holding the stub definition of this object.'
##        #return pFullName
##
##    def _get(self):
##        u'Sets/Returns an object representing the programmatic type.'
##        #return ppCodeTypeRef
##    def _set(self, ppCodeTypeRef):
##        u'Sets/Returns an object representing the programmatic type.'
##    Type = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ParentObject
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    def AddAttribute(self, Name, Value, Position):
##        u'Creates a new attribute code construct and inserts the code in the correct location.'
##        #return ppCodeAttribute
##
##    def RemoveParameter(self, Element):
##        u'Removes a parameter from the argument list.'
##        #return 
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    def _get(self):
##        u'Sets/Returns if the function can be overridden.'
##        #return pCanOverride
##    def _set(self, pCanOverride):
##        u'Sets/Returns if the function can be overridden.'
##    CanOverride = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def _get(self):
##        u'Returns the document comment on the current code model element.'
##        #return pDocComment
##    def _set(self, pDocComment):
##        u'Returns the document comment on the current code model element.'
##    DocComment = property(_get, _set, doc = _set.__doc__)
##
##    def AddParameter(self, Name, Type, Position):
##        u'Creates a new parameter code construct and inserts the code in the correct location.'
##        #return ppCodeParameter
##
##    @property
##    def Attributes(self):
##        u'Returns a collection of items containing attributes.'
##        #return ppMembers
##
##    def _get(self):
##        u'Sets/Returns if the item is statically defined or not.'
##        #return Shared
##    def _set(self, Shared):
##        u'Sets/Returns if the item is statically defined or not.'
##    IsShared = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Sets/Returns an object defining the comment for this object.'
##        #return pComment
##    def _set(self, pComment):
##        u'Sets/Returns an object defining the comment for this object.'
##    Comment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Overloads(self):
##        u'Returns a collection of overloaded methods for this item.'
##        #return ppMembers
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    def _get(self):
##        u'Sets/Returns if the item is declared abstract or not.'
##        #return MustImplement
##    def _set(self, MustImplement):
##        u'Sets/Returns if the item is declared abstract or not.'
##    MustImplement = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##

class Language(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Used to examine and manipulate Language objects.'
    _iid_ = GUID('{B3CCFA68-C145-11D2-8AD1-00C04F79E479}')
    _idlflags_ = ['dual', 'oleautomation']
Languages._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Language)), 'Language' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'Debugger' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for Languages implementation
##class Languages_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return Count
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return Language
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Debugger
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##

vsProjectItemKindVirtualFolder = u'{6BB5F8F0-4483-11D3-8BCF-00C04F8EC28C}' # Constant STRING
CodeParameter._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(CodeElement)), 'ppCodeElement' )),
    COMMETHOD([dispid(32), helpstring(u'Sets/Returns an object representing the programmatic type.'), 'nonbrowsable', 'propput'], HRESULT, 'Type',
              ( [], POINTER(CodeTypeRef), 'pCodeTypeRef' )),
    COMMETHOD([dispid(32), helpstring(u'Sets/Returns an object representing the programmatic type.'), 'nonbrowsable', 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(POINTER(CodeTypeRef)), 'pCodeTypeRef' )),
    COMMETHOD([dispid(33), helpstring(u'Returns a collection of items containing attributes.'), 'nonbrowsable', 'propget'], HRESULT, 'Attributes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppMembers' )),
    COMMETHOD([dispid(34), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propget'], HRESULT, 'DocComment',
              ( ['retval', 'out'], POINTER(BSTR), 'pDocComment' )),
    COMMETHOD([dispid(34), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propput'], HRESULT, 'DocComment',
              ( [], BSTR, 'pDocComment' )),
    COMMETHOD([dispid(35), helpstring(u'Creates a new attribute code construct and inserts the code in the correct location.')], HRESULT, 'AddAttribute',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeAttribute)), 'ppCodeAttribute' )),
]
################################################################
## code template for CodeParameter implementation
##class CodeParameter_Impl(object):
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    def _get(self):
##        u'Sets/Returns an object representing the programmatic type.'
##        #return pCodeTypeRef
##    def _set(self, pCodeTypeRef):
##        u'Sets/Returns an object representing the programmatic type.'
##    Type = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppCodeElement
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    def AddAttribute(self, Name, Value, Position):
##        u'Creates a new attribute code construct and inserts the code in the correct location.'
##        #return ppCodeAttribute
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def _get(self):
##        u'Returns the document comment on the current code model element.'
##        #return pDocComment
##    def _set(self, pDocComment):
##        u'Returns the document comment on the current code model element.'
##    DocComment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Attributes(self):
##        u'Returns a collection of items containing attributes.'
##        #return ppMembers
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##

vsext_wk_AutoLocalsWindow = u'{F2E84780-2AF1-11D1-A7FA-00A0C9110051}' # Constant STRING
vsext_vk_Primary = u'{00000000-0000-0000-0000-000000000000}' # Constant STRING
vsext_vk_Debugging = u'{7651A700-06E5-11D1-8EBD-00A0C90F26EA}' # Constant STRING
vsext_vk_Code = u'{7651A701-06E5-11D1-8EBD-00A0C90F26EA}' # Constant STRING
vsext_vk_Designer = u'{7651A702-06E5-11D1-8EBD-00A0C90F26EA}' # Constant STRING

# values for enumeration 'vsWindowType'
vsWindowTypeCodeWindow = 0
vsWindowTypeDesigner = 1
vsWindowTypeBrowser = 2
vsWindowTypeWatch = 3
vsWindowTypeLocals = 4
vsWindowTypeImmediate = 5
vsWindowTypeSolutionExplorer = 6
vsWindowTypeProperties = 7
vsWindowTypeFind = 8
vsWindowTypeFindReplace = 9
vsWindowTypeToolbox = 10
vsWindowTypeLinkedWindowFrame = 11
vsWindowTypeMainWindow = 12
vsWindowTypePreview = 13
vsWindowTypeColorPalette = 14
vsWindowTypeToolWindow = 15
vsWindowTypeDocument = 16
vsWindowTypeOutput = 17
vsWindowTypeTaskList = 18
vsWindowTypeAutos = 19
vsWindowTypeCallStack = 20
vsWindowTypeThreads = 21
vsWindowTypeDocumentOutline = 22
vsWindowTypeRunningDocuments = 23
vsWindowType = c_int # enum
Window._methods_ = [
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(Windows)), 'lppaReturn' )),
    COMMETHOD([dispid(106), helpstring(u'Sets/returns value determining whether the window is visible.'), 'propget'], HRESULT, 'Visible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pfVisible' )),
    COMMETHOD([dispid(106), helpstring(u'Sets/returns value determining whether the window is visible.'), 'propput'], HRESULT, 'Visible',
              ( ['in'], VARIANT_BOOL, 'pfVisible' )),
    COMMETHOD([dispid(101), helpstring(u'Returns/sets distance between internal left/top edge of an object and left/top edge of its container.'), 'propget'], HRESULT, 'Left',
              ( ['retval', 'out'], POINTER(c_int), 'plLeft' )),
    COMMETHOD([dispid(101), helpstring(u'Returns/sets distance between internal left/top edge of an object and left/top edge of its container.'), 'propput'], HRESULT, 'Left',
              ( ['in'], c_int, 'plLeft' )),
    COMMETHOD([dispid(103), helpstring(u'Returns/sets distance between internal left/top edge of an object and left/top edge of its container.'), 'propget'], HRESULT, 'Top',
              ( ['retval', 'out'], POINTER(c_int), 'plTop' )),
    COMMETHOD([dispid(103), helpstring(u'Returns/sets distance between internal left/top edge of an object and left/top edge of its container.'), 'propput'], HRESULT, 'Top',
              ( ['in'], c_int, 'plTop' )),
    COMMETHOD([dispid(105), helpstring(u'Sets/returns a Single value indicating the dimensions of the window in pixels.'), 'propget'], HRESULT, 'Width',
              ( ['retval', 'out'], POINTER(c_int), 'plWidth' )),
    COMMETHOD([dispid(105), helpstring(u'Sets/returns a Single value indicating the dimensions of the window in pixels.'), 'propput'], HRESULT, 'Width',
              ( ['in'], c_int, 'plWidth' )),
    COMMETHOD([dispid(107), helpstring(u'Sets/returns a Single value indicating the dimensions of the window in pixels.'), 'propget'], HRESULT, 'Height',
              ( ['retval', 'out'], POINTER(c_int), 'plHeight' )),
    COMMETHOD([dispid(107), helpstring(u'Sets/returns a Single value indicating the dimensions of the window in pixels.'), 'propput'], HRESULT, 'Height',
              ( ['in'], c_int, 'plHeight' )),
    COMMETHOD([dispid(109), helpstring(u'Sets/returns string determining the state of the window.'), 'propget'], HRESULT, 'WindowState',
              ( ['retval', 'out'], POINTER(vsWindowState), 'plWindowState' )),
    COMMETHOD([dispid(109), helpstring(u'Sets/returns string determining the state of the window.'), 'propput'], HRESULT, 'WindowState',
              ( ['in'], vsWindowState, 'plWindowState' )),
    COMMETHOD([dispid(111), helpstring(u'Moves the focus to the specified window.'), 'hidden'], HRESULT, 'SetFocus'),
    COMMETHOD([dispid(112), helpstring(u'Returns an enumerated string indicating the object type.'), 'hidden', 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(vsWindowType), 'pKind' )),
    COMMETHOD([dispid(113), 'restricted', 'hidden'], HRESULT, 'SetKind',
              ( ['in'], vsWindowType, 'eKind' )),
    COMMETHOD([dispid(116), helpstring(u'Returns a LinkedWindows collection.'), 'propget'], HRESULT, 'LinkedWindows',
              ( ['retval', 'out'], POINTER(POINTER(LinkedWindows)), 'ppwnsCollection' )),
    COMMETHOD([dispid(117), helpstring(u'Returns Window object representing window frame containing window.'), 'propget'], HRESULT, 'LinkedWindowFrame',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'ppwinFrame' )),
    COMMETHOD([dispid(118), 'restricted', 'hidden'], HRESULT, 'Detach'),
    COMMETHOD([dispid(119), 'restricted', 'hidden'], HRESULT, 'Attach',
              ( ['in'], c_int, 'lWindowHandle' )),
    COMMETHOD([dispid(120), 'hidden', 'propget'], HRESULT, 'HWnd',
              ( ['retval', 'out'], POINTER(c_int), 'plWindowHandle' )),
    COMMETHOD([dispid(121), helpstring(u'Returns a GUID String indicating the kind or type of the object.'), 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrType' )),
    COMMETHOD([dispid(122), helpstring(u'Returns the type of the Window.Object object, a GUID string representing the tool contained in the window.'), 'propget'], HRESULT, 'ObjectKind',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrTypeGUID' )),
    COMMETHOD([dispid(123), helpstring(u'Returns the extensibility object for the tool represented by the window.'), 'propget'], HRESULT, 'Object',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppToolObject' )),
    COMMETHOD([dispid(124), helpstring(u'Returns an OLE automation object that models the data in the document.'), 'hidden', 'propget'], HRESULT, 'DocumentData',
              ( ['in', 'optional'], BSTR, 'bstrWhichData', u'' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppDataObject' )),
    COMMETHOD([dispid(125), helpstring(u'Returns the ProjectItem object associated with the window.'), 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'ppProjItem' )),
    COMMETHOD([dispid(126), helpstring(u'Returns the Project object associated with the object the Project property was invoked on.'), 'propget'], HRESULT, 'Project',
              ( ['retval', 'out'], POINTER(POINTER(Project)), 'ppProj' )),
    COMMETHOD([dispid(127), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(128), helpstring(u'Returns the document this window displays.'), 'propget'], HRESULT, 'Document',
              ( ['retval', 'out'], POINTER(POINTER(Document)), 'ppDocument' )),
    COMMETHOD([dispid(129), helpstring(u'Returns an object representing the selection on this object.'), 'propget'], HRESULT, 'Selection',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppDocument' )),
    COMMETHOD([dispid(130), helpstring(u'Gets/Sets if the window can be tab-linked.'), 'propget'], HRESULT, 'Linkable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pLinkable' )),
    COMMETHOD([dispid(130), helpstring(u'Gets/Sets if the window can be tab-linked.'), 'propput'], HRESULT, 'Linkable',
              ( ['in'], VARIANT_BOOL, 'pLinkable' )),
    COMMETHOD([dispid(131), helpstring(u'Moves the focus to the current item.')], HRESULT, 'Activate'),
    COMMETHOD([dispid(132), helpstring(u'Closes and destroys the window.')], HRESULT, 'Close',
              ( ['in', 'optional'], vsSaveChanges, 'SaveChanges', 2 )),
    COMMETHOD([dispid(0), helpstring(u"Returns the string displayed in the window's title bar."), 'propget'], HRESULT, 'Caption',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrTitle' )),
    COMMETHOD([dispid(0), helpstring(u"Returns the string displayed in the window's title bar."), 'propput'], HRESULT, 'Caption',
              ( ['in'], BSTR, 'pbstrTitle' )),
    COMMETHOD([dispid(133), helpstring(u'Allows setting objects to be active in the Properties Window when this window is active.')], HRESULT, 'SetSelectionContainer',
              ( [], POINTER(_midlSAFEARRAY(VARIANT)), 'Objects' )),
    COMMETHOD([dispid(135), helpstring(u'Gets/Sets if the window is a tool window, unable to be docked.'), 'propget'], HRESULT, 'IsFloating',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Floating' )),
    COMMETHOD([dispid(135), helpstring(u'Gets/Sets if the window is a tool window, unable to be docked.'), 'propput'], HRESULT, 'IsFloating',
              ( ['in'], VARIANT_BOOL, 'Floating' )),
    COMMETHOD([dispid(136), helpstring(u'Gets/Sets if the window is a hide-able tool window.'), 'propget'], HRESULT, 'AutoHides',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Hides' )),
    COMMETHOD([dispid(136), helpstring(u'Gets/Sets if the window is a hide-able tool window.'), 'propput'], HRESULT, 'AutoHides',
              ( ['in'], VARIANT_BOOL, 'Hides' )),
    COMMETHOD([dispid(138), helpstring(u'Sets the picture to display on a tool window.')], HRESULT, 'SetTabPicture',
              ( [], VARIANT, 'Picture' )),
    COMMETHOD([dispid(139), helpstring(u'Get the ContextAttributes collection for the window.'), 'propget'], HRESULT, 'ContextAttributes',
              ( ['retval', 'out'], POINTER(POINTER(ContextAttributes)), 'ppVal' )),
]
################################################################
## code template for Window implementation
##class Window_Impl(object):
##    def SetFocus(self):
##        u'Moves the focus to the specified window.'
##        #return 
##
##    def _get(self):
##        u'Returns/sets distance between internal left/top edge of an object and left/top edge of its container.'
##        #return plTop
##    def _set(self, plTop):
##        u'Returns/sets distance between internal left/top edge of an object and left/top edge of its container.'
##    Top = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ContextAttributes(self):
##        u'Get the ContextAttributes collection for the window.'
##        #return ppVal
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def _get(self):
##        u'Sets/returns string determining the state of the window.'
##        #return plWindowState
##    def _set(self, plWindowState):
##        u'Sets/returns string determining the state of the window.'
##    WindowState = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Sets/returns a Single value indicating the dimensions of the window in pixels.'
##        #return plWidth
##    def _set(self, plWidth):
##        u'Sets/returns a Single value indicating the dimensions of the window in pixels.'
##    Width = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object associated with the window.'
##        #return ppProjItem
##
##    @property
##    def Document(self):
##        u'Returns the document this window displays.'
##        #return ppDocument
##
##    @property
##    def Type(self):
##        u'Returns an enumerated string indicating the object type.'
##        #return pKind
##
##    @property
##    def HWnd(self):
##        '-no docstring-'
##        #return plWindowHandle
##
##    @property
##    def Object(self):
##        u'Returns the extensibility object for the tool represented by the window.'
##        #return ppToolObject
##
##    def _get(self):
##        u'Gets/Sets if the window is a hide-able tool window.'
##        #return Hides
##    def _set(self, Hides):
##        u'Gets/Sets if the window is a hide-able tool window.'
##    AutoHides = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return lppaReturn
##
##    @property
##    def LinkedWindows(self):
##        u'Returns a LinkedWindows collection.'
##        #return ppwnsCollection
##
##    def _get(self):
##        u'Gets/Sets if the window is a tool window, unable to be docked.'
##        #return Floating
##    def _set(self, Floating):
##        u'Gets/Sets if the window is a tool window, unable to be docked.'
##    IsFloating = property(_get, _set, doc = _set.__doc__)
##
##    def Detach(self):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        u'Gets/Sets if the window can be tab-linked.'
##        #return pLinkable
##    def _set(self, pLinkable):
##        u'Gets/Sets if the window can be tab-linked.'
##    Linkable = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Kind(self):
##        u'Returns a GUID String indicating the kind or type of the object.'
##        #return pbstrType
##
##    @property
##    def DocumentData(self, bstrWhichData):
##        u'Returns an OLE automation object that models the data in the document.'
##        #return ppDataObject
##
##    @property
##    def Project(self):
##        u'Returns the Project object associated with the object the Project property was invoked on.'
##        #return ppProj
##
##    def _get(self):
##        u"Returns the string displayed in the window's title bar."
##        #return pbstrTitle
##    def _set(self, pbstrTitle):
##        u"Returns the string displayed in the window's title bar."
##    Caption = property(_get, _set, doc = _set.__doc__)
##
##    def Activate(self):
##        u'Moves the focus to the current item.'
##        #return 
##
##    @property
##    def LinkedWindowFrame(self):
##        u'Returns Window object representing window frame containing window.'
##        #return ppwinFrame
##
##    def SetSelectionContainer(self, Objects):
##        u'Allows setting objects to be active in the Properties Window when this window is active.'
##        #return 
##
##    def _get(self):
##        u'Returns/sets distance between internal left/top edge of an object and left/top edge of its container.'
##        #return plLeft
##    def _set(self, plLeft):
##        u'Returns/sets distance between internal left/top edge of an object and left/top edge of its container.'
##    Left = property(_get, _set, doc = _set.__doc__)
##
##    def SetKind(self, eKind):
##        '-no docstring-'
##        #return 
##
##    @property
##    def Selection(self):
##        u'Returns an object representing the selection on this object.'
##        #return ppDocument
##
##    def Attach(self, lWindowHandle):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        u'Sets/returns a Single value indicating the dimensions of the window in pixels.'
##        #return plHeight
##    def _set(self, plHeight):
##        u'Sets/returns a Single value indicating the dimensions of the window in pixels.'
##    Height = property(_get, _set, doc = _set.__doc__)
##
##    def SetTabPicture(self, Picture):
##        u'Sets the picture to display on a tool window.'
##        #return 
##
##    def _get(self):
##        u'Sets/returns value determining whether the window is visible.'
##        #return pfVisible
##    def _set(self, pfVisible):
##        u'Sets/returns value determining whether the window is visible.'
##    Visible = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ObjectKind(self):
##        u'Returns the type of the Window.Object object, a GUID string representing the tool contained in the window.'
##        #return pbstrTypeGUID
##
##    def Close(self, SaveChanges):
##        u'Closes and destroys the window.'
##        #return 
##

vsext_wk_TaskList = u'{4A9B7E51-AA16-11D0-A8C5-00A0C921A4D2}' # Constant STRING
vsext_wk_Toolbox = u'{B1E99781-AB81-11D0-B683-00AA00A3EE26}' # Constant STRING
dsIDL = u'ODL/IDL' # Constant STRING
vsext_wk_ThreadWindow = u'{E62CE6A0-B439-11D0-A79D-00A0C9110051}' # Constant STRING
vsext_wk_LocalsWindow = u'{4A18F9D0-B838-11D0-93EB-00A0C90F2734}' # Constant STRING
dsJava = u'Java' # Constant STRING
class TaskListEvents(CoClass):
    u'The TaskListEvents object triggers events about the Task List.'
    _reg_clsid_ = GUID('{29617ACD-7859-4328-BE09-298F91F48196}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
TaskListEvents._com_interfaces_ = [_TaskListEvents]
TaskListEvents._outgoing_interfaces_ = [_dispTaskListEvents]

vsext_wk_ImmedWindow = u'{98731960-965C-11D0-A78F-00A0C9110051}' # Constant STRING
dsVBSMacro = u'VBS Macro' # Constant STRING
vsext_wk_SProjectWindow = u'{3AE79031-E1BC-11D0-8F78-00A0C9110057}' # Constant STRING
CodeType._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'nonbrowsable', 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the collection containing the object supporting this property.'), 'nonbrowsable', 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCollection' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the object.'), 'propput'], HRESULT, 'Name',
              ( [], BSTR, 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the fully qualified name of the object.'), 'propget'], HRESULT, 'FullName',
              ( ['retval', 'out'], POINTER(BSTR), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the ProjectItem object.'), 'nonbrowsable', 'propget'], HRESULT, 'ProjectItem',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItem)), 'pProjItem' )),
    COMMETHOD([dispid(5), helpstring(u'Returns an enumeration indicating the object kind.'), 'nonbrowsable', 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(vsCMElement), 'pCodeEltKind' )),
    COMMETHOD([dispid(6), helpstring(u'Returns if a CodeType object can be obtained from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'IsCodeType',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pIsCodeType' )),
    COMMETHOD([dispid(7), helpstring(u'Describes the capabilities of the code model.'), 'nonbrowsable', 'propget'], HRESULT, 'InfoLocation',
              ( ['retval', 'out'], POINTER(vsCMInfoLocation), 'pInfoLocation' )),
    COMMETHOD([dispid(8), helpstring(u'Returns a collection of objects contained within this code construct.'), 'nonbrowsable', 'propget'], HRESULT, 'Children',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(9), helpstring(u'Programming language used to author the code.'), 'nonbrowsable', 'propget'], HRESULT, 'Language',
              ( ['retval', 'out'], POINTER(BSTR), 'pLanguage' )),
    COMMETHOD([dispid(10), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'StartPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(11), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable', 'propget'], HRESULT, 'EndPoint',
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(12), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(13), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( [], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(14), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(15), helpstring(u'Returns a TextPoint object defining the beginning of the code item.'), 'nonbrowsable'], HRESULT, 'GetStartPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(16), helpstring(u'Returns a TextPoint object defining the end of the code item.'), 'nonbrowsable'], HRESULT, 'GetEndPoint',
              ( ['in', 'optional'], vsCMPart, 'Part', 10 ),
              ( ['retval', 'out'], POINTER(POINTER(TextPoint)), 'ppTextPoint' )),
    COMMETHOD([dispid(31), helpstring(u'Returns the parent object.'), 'nonbrowsable', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ParentObject' )),
    COMMETHOD([dispid(32), helpstring(u'Returns an object defining the parent namespace.'), 'nonbrowsable', 'propget'], HRESULT, 'Namespace',
              ( ['retval', 'out'], POINTER(POINTER(CodeNamespace)), 'ppCodeNamespace' )),
    COMMETHOD([dispid(33), helpstring(u'Returns a collection of classes this item derives from.'), 'nonbrowsable', 'propget'], HRESULT, 'Bases',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(34), helpstring(u'Returns a collection of items contained by this element.'), 'nonbrowsable', 'propget'], HRESULT, 'Members',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(35), helpstring(u'Defines the access attributes of this item.'), 'propput'], HRESULT, 'Access',
              ( [], vsCMAccess, 'pAccess' )),
    COMMETHOD([dispid(35), helpstring(u'Defines the access attributes of this item.'), 'propget'], HRESULT, 'Access',
              ( ['retval', 'out'], POINTER(vsCMAccess), 'pAccess' )),
    COMMETHOD([dispid(36), helpstring(u'Returns a collection of items containing attributes.'), 'nonbrowsable', 'propget'], HRESULT, 'Attributes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
    COMMETHOD([dispid(37), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propget'], HRESULT, 'DocComment',
              ( ['retval', 'out'], POINTER(BSTR), 'pDocComment' )),
    COMMETHOD([dispid(37), helpstring(u'Returns the document comment on the current code model element.'), 'nonbrowsable', 'propput'], HRESULT, 'DocComment',
              ( [], BSTR, 'pDocComment' )),
    COMMETHOD([dispid(38), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propget'], HRESULT, 'Comment',
              ( ['retval', 'out'], POINTER(BSTR), 'pComment' )),
    COMMETHOD([dispid(38), helpstring(u'Sets/Returns an object defining the comment for this object.'), 'nonbrowsable', 'propput'], HRESULT, 'Comment',
              ( [], BSTR, 'pComment' )),
    COMMETHOD([dispid(39), helpstring(u'Adds an item to the list of inherited objects.')], HRESULT, 'AddBase',
              ( [], VARIANT, 'Base' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeElement)), 'ppOut' )),
    COMMETHOD([dispid(40), helpstring(u'Creates a new attribute code construct and inserts the code in the correct location.')], HRESULT, 'AddAttribute',
              ( [], BSTR, 'Name' ),
              ( [], BSTR, 'Value' ),
              ( ['optional'], VARIANT, 'Position' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeAttribute)), 'ppCodeAttribute' )),
    COMMETHOD([dispid(41), helpstring(u'Removes an object from the list of bases.')], HRESULT, 'RemoveBase',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(42), helpstring(u'Removes a member code construct.')], HRESULT, 'RemoveMember',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(43), helpstring(u'Returns a Boolean telling if an object has another object as a base.'), 'propget'], HRESULT, 'IsDerivedFrom',
              ( [], BSTR, 'FullName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pVal' )),
    COMMETHOD([dispid(44), helpstring(u'Returns a collection of objects derived from this object.'), 'nonbrowsable', 'propget'], HRESULT, 'DerivedTypes',
              ( ['retval', 'out'], POINTER(POINTER(CodeElements)), 'ppCodeElements' )),
]
################################################################
## code template for CodeType implementation
##class CodeType_Impl(object):
##    def GetEndPoint(self, Part):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def Namespace(self):
##        u'Returns an object defining the parent namespace.'
##        #return ppCodeNamespace
##
##    def AddBase(self, Base, Position):
##        u'Adds an item to the list of inherited objects.'
##        #return ppOut
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def GetStartPoint(self, Part):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    def _get(self):
##        u'Defines the access attributes of this item.'
##        #return pAccess
##    def _set(self, pAccess):
##        u'Defines the access attributes of this item.'
##    Access = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Bases(self):
##        u'Returns a collection of classes this item derives from.'
##        #return ppCodeElements
##
##    @property
##    def ProjectItem(self):
##        u'Returns the ProjectItem object.'
##        #return pProjItem
##
##    @property
##    def InfoLocation(self):
##        u'Describes the capabilities of the code model.'
##        #return pInfoLocation
##
##    @property
##    def EndPoint(self):
##        u'Returns a TextPoint object defining the end of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ParentObject
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return ppCollection
##
##    def AddAttribute(self, Name, Value, Position):
##        u'Creates a new attribute code construct and inserts the code in the correct location.'
##        #return ppCodeAttribute
##
##    def RemoveMember(self, Element):
##        u'Removes a member code construct.'
##        #return 
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def Members(self):
##        u'Returns a collection of items contained by this element.'
##        #return ppCodeElements
##
##    @property
##    def StartPoint(self):
##        u'Returns a TextPoint object defining the beginning of the code item.'
##        #return ppTextPoint
##
##    @property
##    def Kind(self):
##        u'Returns an enumeration indicating the object kind.'
##        #return pCodeEltKind
##
##    def _get(self):
##        u'Sets/returns the name of the object.'
##        #return pVal
##    def _set(self, pVal):
##        u'Sets/returns the name of the object.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Language(self):
##        u'Programming language used to author the code.'
##        #return pLanguage
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    def _get(self):
##        u'Returns the document comment on the current code model element.'
##        #return pDocComment
##    def _set(self, pDocComment):
##        u'Returns the document comment on the current code model element.'
##    DocComment = property(_get, _set, doc = _set.__doc__)
##
##    def RemoveBase(self, Element):
##        u'Removes an object from the list of bases.'
##        #return 
##
##    @property
##    def Attributes(self):
##        u'Returns a collection of items containing attributes.'
##        #return ppCodeElements
##
##    def _get(self):
##        u'Sets/Returns an object defining the comment for this object.'
##        #return pComment
##    def _set(self, pComment):
##        u'Sets/Returns an object defining the comment for this object.'
##    Comment = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsDerivedFrom(self, FullName):
##        u'Returns a Boolean telling if an object has another object as a base.'
##        #return pVal
##
##    @property
##    def IsCodeType(self):
##        u'Returns if a CodeType object can be obtained from this object.'
##        #return pIsCodeType
##
##    @property
##    def DerivedTypes(self):
##        u'Returns a collection of objects derived from this object.'
##        #return ppCodeElements
##
##    @property
##    def FullName(self):
##        u'Returns the fully qualified name of the object.'
##        #return pVal
##
##    @property
##    def Children(self):
##        u'Returns a collection of objects contained within this code construct.'
##        #return ppCodeElements
##

vsext_wk_OutputWindow = u'{34E76E81-EE4A-11D0-AE2E-00A0C90FFFC3}' # Constant STRING
vsext_wk_ObjectBrowser = u'{269A02DC-6AF8-11D3-BDC4-00C04F688E50}' # Constant STRING
class ColorableItems(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{E5D17051-D6E5-4DA7-8B3A-CA888617A5E7}')
    _idlflags_ = ['dual', 'oleautomation']
FontsAndColorsItems._methods_ = [
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(ColorableItems)), 'pFontsAndColorsItem' )),
    COMMETHOD([dispid(1), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'pCount' )),
]
################################################################
## code template for FontsAndColorsItems implementation
##class FontsAndColorsItems_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return pCount
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return pFontsAndColorsItem
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##

vsext_wk_ContextWindow = u'{66DBA47C-61DF-11D2-AA79-00C04F990343}' # Constant STRING
vsext_wk_ClassView = u'{C9C0AE26-AA77-11D2-B3F0-0000F87570EE}' # Constant STRING
VirtualPoint._methods_ = [
    COMMETHOD([dispid(101), helpstring(u'Returns the column index of a virtual point in virtual space.'), 'propget'], HRESULT, 'VirtualCharOffset',
              ( ['retval', 'out'], POINTER(c_int), 'pOffset' )),
    COMMETHOD([dispid(102), helpstring(u'Returns the display column of the current position.'), 'propget'], HRESULT, 'VirtualDisplayColumn',
              ( ['retval', 'out'], POINTER(c_int), 'lppaReturn' )),
]
################################################################
## code template for VirtualPoint implementation
##class VirtualPoint_Impl(object):
##    @property
##    def VirtualCharOffset(self):
##        u'Returns the column index of a virtual point in virtual space.'
##        #return pOffset
##
##    @property
##    def VirtualDisplayColumn(self):
##        u'Returns the display column of the current position.'
##        #return lppaReturn
##

vsext_GUID_NewProjectWizard = u'{0F90E1D0-4999-11D1-B6D1-00A0C90F2744}' # Constant STRING
vsCATIDSolution = u'{52AEFF70-BBD8-11d2-8598-006097C68E81}' # Constant STRING
dsCPP = u'C/C++' # Constant STRING
dsHTML_IE3 = u'HTML - IE 3.0' # Constant STRING
dsHTML_RFC1866 = u'HTML 2.0 (RFC 1866)' # Constant STRING
dsFortran_Fixed = u'Fortran Fixed' # Constant STRING
dsFortran_Free = u'Fortran Free' # Constant STRING
Language._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns the human-readable name of this language.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTE' )),
    COMMETHOD([dispid(201), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'Debugger' )),
    COMMETHOD([dispid(202), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(Languages)), 'Languages' )),
]
################################################################
## code template for Language implementation
##class Language_Impl(object):
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Debugger
##
##    @property
##    def Name(self):
##        u'Returns the human-readable name of this language.'
##        #return Name
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTE
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return Languages
##

TextWindow._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'ppDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'ppParent' )),
    COMMETHOD([dispid(3), helpstring(u'Returns an object representing the selection on this object.'), 'propget'], HRESULT, 'Selection',
              ( ['retval', 'out'], POINTER(POINTER(TextSelection)), 'ppSel' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the most recently active pane in the text window.'), 'propget'], HRESULT, 'ActivePane',
              ( ['retval', 'out'], POINTER(POINTER(TextPane)), 'ppPane' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the collection of panes in the text window.'), 'propget'], HRESULT, 'Panes',
              ( ['retval', 'out'], POINTER(POINTER(TextPanes)), 'ppPanes' )),
]
################################################################
## code template for TextWindow implementation
##class TextWindow_Impl(object):
##    @property
##    def Panes(self):
##        u'Returns the collection of panes in the text window.'
##        #return ppPanes
##
##    @property
##    def Selection(self):
##        u'Returns an object representing the selection on this object.'
##        #return ppSel
##
##    @property
##    def ActivePane(self):
##        u'Returns the most recently active pane in the text window.'
##        #return ppPane
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return ppParent
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return ppDTE
##

StatusBar._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(4), helpstring(u'Resets the text in the status bar to the default text.')], HRESULT, 'Clear'),
    COMMETHOD([dispid(5), helpstring(u'Display an animated picture in the status bar.')], HRESULT, 'Animate',
              ( [], VARIANT_BOOL, 'On' ),
              ( [], VARIANT, 'AnimationType' )),
    COMMETHOD([dispid(6), helpstring(u'Creates, modifies, and clears the meter control inside the status bar.')], HRESULT, 'Progress',
              ( [], VARIANT_BOOL, 'InProgress' ),
              ( ['in', 'optional'], BSTR, 'Label', u'' ),
              ( ['in', 'optional'], c_int, 'AmountCompleted', 0 ),
              ( ['in', 'optional'], c_int, 'Total', 0 )),
    COMMETHOD([dispid(7), helpstring(u'Sets x, y, width, and height coordinates in the status bar.')], HRESULT, 'SetXYWidthHeight',
              ( [], c_int, 'X' ),
              ( [], c_int, 'Y' ),
              ( [], c_int, 'Width' ),
              ( [], c_int, 'Height' )),
    COMMETHOD([dispid(8), helpstring(u'Sets the text column and character position in the status bar.')], HRESULT, 'SetLineColumnCharacter',
              ( [], c_int, 'Line' ),
              ( [], c_int, 'Column' ),
              ( [], c_int, 'Character' )),
    COMMETHOD([dispid(0), helpstring(u'The text displayed in the status bar.'), 'propput'], HRESULT, 'Text',
              ( ['in'], BSTR, 'pTextc' )),
    COMMETHOD([dispid(0), helpstring(u'The text displayed in the status bar.'), 'propget'], HRESULT, 'Text',
              ( ['retval', 'out'], POINTER(BSTR), 'pTextc' )),
    COMMETHOD([dispid(9), helpstring(u'Turn on or off the highlight within the status bar.')], HRESULT, 'Highlight',
              ( [], VARIANT_BOOL, 'Highlight' )),
    COMMETHOD([dispid(10), helpstring(u'Allows or disallows text updates in the status bar.')], HRESULT, 'ShowTextUpdates',
              ( [], VARIANT_BOOL, 'TextUpdates' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'WillShowUpdates' )),
]
################################################################
## code template for StatusBar implementation
##class StatusBar_Impl(object):
##    def SetXYWidthHeight(self, X, Y, Width, Height):
##        u'Sets x, y, width, and height coordinates in the status bar.'
##        #return 
##
##    @property
##    def Parent(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    def _get(self):
##        u'The text displayed in the status bar.'
##        #return pTextc
##    def _set(self, pTextc):
##        u'The text displayed in the status bar.'
##    Text = property(_get, _set, doc = _set.__doc__)
##
##    def Clear(self):
##        u'Resets the text in the status bar to the default text.'
##        #return 
##
##    def SetLineColumnCharacter(self, Line, Column, Character):
##        u'Sets the text column and character position in the status bar.'
##        #return 
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##
##    def ShowTextUpdates(self, TextUpdates):
##        u'Allows or disallows text updates in the status bar.'
##        #return WillShowUpdates
##
##    def Highlight(self, Highlight):
##        u'Turn on or off the highlight within the status bar.'
##        #return 
##
##    def Progress(self, InProgress, Label, AmountCompleted, Total):
##        u'Creates, modifies, and clears the meter control inside the status bar.'
##        #return 
##
##    def Animate(self, On, AnimationType):
##        u'Display an animated picture in the status bar.'
##        #return 
##

ProjectItem._methods_ = [
    COMMETHOD([dispid(10), helpstring(u'Returns value indicating whether object was changed since the last time it was saved.'), 'hidden', 'propget'], HRESULT, 'IsDirty',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lpfReturn' )),
    COMMETHOD([dispid(10), helpstring(u'Returns value indicating whether object was changed since the last time it was saved.'), 'hidden', 'propput'], HRESULT, 'IsDirty',
              ( ['in'], VARIANT_BOOL, 'lpfReturn' )),
    COMMETHOD([dispid(11), helpstring(u'Returns the full pathnames of the files associated with a project item.'), 'propget'], HRESULT, 'FileNames',
              ( ['in'], c_short, 'index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
    COMMETHOD([dispid(12), helpstring(u'Saves the project.')], HRESULT, 'SaveAs',
              ( ['in'], BSTR, 'NewFileName' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lpfReturn' )),
    COMMETHOD([dispid(13), helpstring(u'Returns the number of files associated with the project item.'), 'propget'], HRESULT, 'FileCount',
              ( ['retval', 'out'], POINTER(c_short), 'lpsReturn' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the project.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pbstrReturn' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/returns the name of the project.'), 'propput'], HRESULT, 'Name',
              ( ['in'], BSTR, 'pbstrReturn' )),
    COMMETHOD([dispid(54), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItems)), 'lppcReturn' )),
    COMMETHOD([dispid(56), helpstring(u'Returns the Properties collection.'), 'propget'], HRESULT, 'Properties',
              ( ['retval', 'out'], POINTER(POINTER(Properties)), 'ppObject' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(201), helpstring(u'Returns a GUID String indicating the kind or type of the object.'), 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrFileName' )),
    COMMETHOD([dispid(203), helpstring(u'Returns a ProjectItems collection for the object.'), 'propget'], HRESULT, 'ProjectItems',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItems)), 'lppcReturn' )),
    COMMETHOD([dispid(204), helpstring(u'Returns value indicating whether the ProjectItem is open for a particular view.'), 'propget'], HRESULT, 'IsOpen',
              ( ['in', 'optional'], BSTR, 'ViewKind', u'{FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF}' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lpfReturn' )),
    COMMETHOD([dispid(205), helpstring(u'Opens the ProjectItem object in the specified view.')], HRESULT, 'Open',
              ( ['in', 'optional'], BSTR, 'ViewKind', u'{00000000-0000-0000-0000-000000000000}' ),
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'lppfReturn' )),
    COMMETHOD([dispid(206), helpstring(u'Removes an object from a collection.')], HRESULT, 'Remove'),
    COMMETHOD([dispid(107), helpstring(u'Expands views of the project structure to show the ProjectItem.')], HRESULT, 'ExpandView'),
    COMMETHOD([dispid(108), helpstring(u'Returns an interface or object that can be accessed at run time by name.'), 'propget'], HRESULT, 'Object',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ProjectItemModel' )),
    COMMETHOD([dispid(109), helpstring(u'Get an Extender for this object under the specified category.'), 'nonbrowsable', 'propget'], HRESULT, 'Extender',
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(110), helpstring(u'Get a list of available Extenders on this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderNames',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(111), helpstring(u'Get the Extension Category ID of this object.'), 'nonbrowsable', 'propget'], HRESULT, 'ExtenderCATID',
              ( ['retval', 'out'], POINTER(BSTR), 'pRetval' )),
    COMMETHOD([dispid(113), helpstring(u'Returns value indicating whether object was changed since the last time it was saved.'), 'propget'], HRESULT, 'Saved',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'lpfReturn' )),
    COMMETHOD([dispid(113), helpstring(u'Returns value indicating whether object was changed since the last time it was saved.'), 'propput'], HRESULT, 'Saved',
              ( ['in'], VARIANT_BOOL, 'lpfReturn' )),
    COMMETHOD([dispid(116), helpstring(u'Returns the ConfigurationManager object for this item.'), 'propget'], HRESULT, 'ConfigurationManager',
              ( ['retval', 'out'], POINTER(POINTER(ConfigurationManager)), 'ppConfigurationManager' )),
    COMMETHOD([dispid(117), helpstring(u'Returns the CodeModel object for this item.'), 'propget'], HRESULT, 'FileCodeModel',
              ( ['retval', 'out'], POINTER(POINTER(FileCodeModel)), 'ppFileCodeModel' )),
    COMMETHOD([dispid(118), helpstring(u'Causes the item to be saved to storage.')], HRESULT, 'Save',
              ( ['optional'], BSTR, 'FileName', u'' )),
    COMMETHOD([dispid(119), helpstring(u'Returns the Document object for this item.'), 'propget'], HRESULT, 'Document',
              ( ['retval', 'out'], POINTER(POINTER(Document)), 'ppDocument' )),
    COMMETHOD([dispid(120), helpstring(u'If the project item is the root of a sub-project, then returns the Project object for the sub-project.'), 'propget'], HRESULT, 'SubProject',
              ( ['retval', 'out'], POINTER(POINTER(Project)), 'ppProject' )),
    COMMETHOD([dispid(121), helpstring(u'Returns the project that hosts this ProjectItem object.'), 'propget'], HRESULT, 'ContainingProject',
              ( ['retval', 'out'], POINTER(POINTER(Project)), 'ppProject' )),
    COMMETHOD([dispid(122), helpstring(u"Removes the item from the project and it's storage.")], HRESULT, 'Delete'),
]
################################################################
## code template for ProjectItem implementation
##class ProjectItem_Impl(object):
##    @property
##    def ConfigurationManager(self):
##        u'Returns the ConfigurationManager object for this item.'
##        #return ppConfigurationManager
##
##    @property
##    def ExtenderNames(self):
##        u'Get a list of available Extenders on this object.'
##        #return ExtenderNames
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    @property
##    def FileNames(self, index):
##        u'Returns the full pathnames of the files associated with a project item.'
##        #return lpbstrReturn
##
##    def Save(self, FileName):
##        u'Causes the item to be saved to storage.'
##        #return 
##
##    @property
##    def FileCount(self):
##        u'Returns the number of files associated with the project item.'
##        #return lpsReturn
##
##    @property
##    def Document(self):
##        u'Returns the Document object for this item.'
##        #return ppDocument
##
##    def ExpandView(self):
##        u'Expands views of the project structure to show the ProjectItem.'
##        #return 
##
##    @property
##    def Object(self):
##        u'Returns an interface or object that can be accessed at run time by name.'
##        #return ProjectItemModel
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return lppcReturn
##
##    @property
##    def FileCodeModel(self):
##        u'Returns the CodeModel object for this item.'
##        #return ppFileCodeModel
##
##    @property
##    def ExtenderCATID(self):
##        u'Get the Extension Category ID of this object.'
##        #return pRetval
##
##    @property
##    def Properties(self):
##        u'Returns the Properties collection.'
##        #return ppObject
##
##    @property
##    def Extender(self, ExtenderName):
##        u'Get an Extender for this object under the specified category.'
##        #return Extender
##
##    @property
##    def Kind(self):
##        u'Returns a GUID String indicating the kind or type of the object.'
##        #return lpbstrFileName
##
##    def _get(self):
##        u'Sets/returns the name of the project.'
##        #return pbstrReturn
##    def _set(self, pbstrReturn):
##        u'Sets/returns the name of the project.'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ProjectItems(self):
##        u'Returns a ProjectItems collection for the object.'
##        #return lppcReturn
##
##    def Remove(self):
##        u'Removes an object from a collection.'
##        #return 
##
##    @property
##    def ContainingProject(self):
##        u'Returns the project that hosts this ProjectItem object.'
##        #return ppProject
##
##    def Delete(self):
##        u"Removes the item from the project and it's storage."
##        #return 
##
##    def SaveAs(self, NewFileName):
##        u'Saves the project.'
##        #return lpfReturn
##
##    @property
##    def IsOpen(self, ViewKind):
##        u'Returns value indicating whether the ProjectItem is open for a particular view.'
##        #return lpfReturn
##
##    def Open(self, ViewKind):
##        u'Opens the ProjectItem object in the specified view.'
##        #return lppfReturn
##
##    def _get(self):
##        u'Returns value indicating whether object was changed since the last time it was saved.'
##        #return lpfReturn
##    def _set(self, lpfReturn):
##        u'Returns value indicating whether object was changed since the last time it was saved.'
##    IsDirty = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def SubProject(self):
##        u'If the project item is the root of a sub-project, then returns the Project object for the sub-project.'
##        #return ppProject
##
##    def _get(self):
##        u'Returns value indicating whether object was changed since the last time it was saved.'
##        #return lpfReturn
##    def _set(self, lpfReturn):
##        u'Returns value indicating whether object was changed since the last time it was saved.'
##    Saved = property(_get, _set, doc = _set.__doc__)
##

Thread._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Stops the thread from executing.')], HRESULT, 'Freeze'),
    COMMETHOD([dispid(2), helpstring(u'Allows the thread to execute.')], HRESULT, 'Thaw'),
    COMMETHOD([dispid(0), helpstring(u'Sets/Returns the name of the thread.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD([dispid(100), helpstring(u'Returns the number of times this thread has been suspended by the debuggee.'), 'propget'], HRESULT, 'SuspendCount',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
    COMMETHOD([dispid(101), helpstring(u'Returns the thread ID.'), 'propget'], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(c_int), 'ID' )),
    COMMETHOD([dispid(102), helpstring(u'Returns the collection of stack frames through which this thread is executing.'), 'propget'], HRESULT, 'StackFrames',
              ( ['retval', 'out'], POINTER(POINTER(StackFrames)), 'StackFrames' )),
    COMMETHOD([dispid(103), helpstring(u'Returns the program that manages this thread.'), 'propget'], HRESULT, 'Program',
              ( ['retval', 'out'], POINTER(POINTER(Program)), 'Program' )),
    COMMETHOD([dispid(104), helpstring(u'Is the actual thread to which this object references still alive?  Note that the actual state may change before this function returns.'), 'propget'], HRESULT, 'IsAlive',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsAlive' )),
    COMMETHOD([dispid(105), helpstring(u'Returns the priority of this thread.'), 'propget'], HRESULT, 'Priority',
              ( ['retval', 'out'], POINTER(BSTR), 'Priority' )),
    COMMETHOD([dispid(106), helpstring(u'Returns the address at which the thread was executing prior to being stopped for debugging.'), 'propget'], HRESULT, 'Location',
              ( ['retval', 'out'], POINTER(BSTR), 'Location' )),
    COMMETHOD([dispid(107), helpstring(u'Returns true if the thread was frozen by the debugger.'), 'propget'], HRESULT, 'IsFrozen',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'IsFrozen' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTE' )),
    COMMETHOD([dispid(201), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'Debugger' )),
    COMMETHOD([dispid(202), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(Threads)), 'Threads' )),
]
################################################################
## code template for Thread implementation
##class Thread_Impl(object):
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return Threads
##
##    def Thaw(self):
##        u'Allows the thread to execute.'
##        #return 
##
##    @property
##    def Name(self):
##        u'Sets/Returns the name of the thread.'
##        #return Name
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Debugger
##
##    @property
##    def StackFrames(self):
##        u'Returns the collection of stack frames through which this thread is executing.'
##        #return StackFrames
##
##    @property
##    def IsFrozen(self):
##        u'Returns true if the thread was frozen by the debugger.'
##        #return IsFrozen
##
##    @property
##    def ID(self):
##        u'Returns the thread ID.'
##        #return ID
##
##    @property
##    def Priority(self):
##        u'Returns the priority of this thread.'
##        #return Priority
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTE
##
##    @property
##    def Program(self):
##        u'Returns the program that manages this thread.'
##        #return Program
##
##    @property
##    def Location(self):
##        u'Returns the address at which the thread was executing prior to being stopped for debugging.'
##        #return Location
##
##    @property
##    def IsAlive(self):
##        u'Is the actual thread to which this object references still alive?  Note that the actual state may change before this function returns.'
##        #return IsAlive
##
##    def Freeze(self):
##        u'Stops the thread from executing.'
##        #return 
##
##    @property
##    def SuspendCount(self):
##        u'Returns the number of times this thread has been suspended by the debuggee.'
##        #return Count
##


# values for enumeration 'vsext_WindowState'
vsext_ws_Normal = 0
vsext_ws_Minimize = 1
vsext_ws_Maximize = 2
vsext_WindowState = c_int # enum
vsProjectItemKindPhysicalFolder = u'{6BB5F8EF-4483-11D3-8BCF-00C04F8EC28C}' # Constant STRING

# values for enumeration 'vsext_Build'
vsext_bld_SAVE_CHANGES = 0
vsext_bld_CONFIRM_SAVE = 1
vsext_bld_NO_SAVE = 2
vsext_Build = c_int # enum
Projects._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Project)), 'lppcReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(10), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'lplReturn' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(201), helpstring(u'Returns the Properties collection.'), 'propget'], HRESULT, 'Properties',
              ( ['retval', 'out'], POINTER(POINTER(Properties)), 'ppObject' )),
    COMMETHOD([dispid(202), helpstring(u'Returns a GUID String indicating the kind or type of the object.'), 'propget'], HRESULT, 'Kind',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
]
################################################################
## code template for Projects implementation
##class Projects_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return lplReturn
##
##    @property
##    def Kind(self):
##        u'Returns a GUID String indicating the kind or type of the object.'
##        #return lpbstrReturn
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppaReturn
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return lppcReturn
##
##    @property
##    def Properties(self):
##        u'Returns the Properties collection.'
##        #return ppObject
##


# values for enumeration 'DsWhitespaceOptions'
dsHorizontal = 0
dsVertical = 1
DsWhitespaceOptions = c_int # enum

# values for enumeration 'vsext_WindowType'
vsext_wt_CodeWindow = 0
vsext_wt_Designer = 1
vsext_wt_Browser = 2
vsext_wt_Watch = 3
vsext_wt_Locals = 4
vsext_wt_Immediate = 5
vsext_wt_ProjectWindow = 6
vsext_wt_PropertyWindow = 7
vsext_wt_Find = 8
vsext_wt_FindReplace = 9
vsext_wt_Toolbox = 10
vsext_wt_LinkedWindowFrame = 11
vsext_wt_MainWindow = 12
vsext_wt_Preview = 13
vsext_wt_ColorPalette = 14
vsext_wt_ToolWindow = 15
vsext_wt_Document = 16
vsext_wt_OutPutWindow = 17
vsext_wt_TaskList = 18
vsext_wt_Autos = 19
vsext_wt_CallStack = 20
vsext_wt_Threads = 21
vsext_wt_DocumentOutline = 22
vsext_wt_RunningDocuments = 23
vsext_WindowType = c_int # enum
class CommandEvents(CoClass):
    u'Provides command events for add-ins.'
    _reg_clsid_ = GUID('{1DED92B5-9A46-4B29-93EF-B5E07016659E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _CommandEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides command events for add-ins.'
    _iid_ = GUID('{A79FC678-0D0A-496A-B9DC-0D5B9E1CA9FC}')
    _idlflags_ = ['oleautomation']
class _dispCommandEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Provides command events for add-ins.'
    _iid_ = GUID('{FF2D5C12-FEEA-11D0-BBC8-00A0C90F2744}')
    _idlflags_ = []
    _methods_ = []
CommandEvents._com_interfaces_ = [_CommandEvents]
CommandEvents._outgoing_interfaces_ = [_dispCommandEvents]

class SelectionEvents(CoClass):
    u'Provides events for changes to a selection.'
    _reg_clsid_ = GUID('{AF37511E-9E9D-4234-A5A1-7584D290E061}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _SelectionEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides events for changes to a selection.'
    _iid_ = GUID('{EB6783DB-1819-496D-84A4-3CFF883010F6}')
    _idlflags_ = ['oleautomation']
class _dispSelectionEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{DEEB28B3-23E6-11D1-AE5C-00A0C90F26F4}')
    _idlflags_ = []
    _methods_ = []
SelectionEvents._com_interfaces_ = [_SelectionEvents]
SelectionEvents._outgoing_interfaces_ = [_dispSelectionEvents]

class SolutionEvents(CoClass):
    u'Provides events for changes to a solution.'
    _reg_clsid_ = GUID('{88AC98C7-B38C-404B-BD86-D2A4F2E89DCA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}', 8, 0)
class _SolutionEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Provides events for changes to a solution.'
    _iid_ = GUID('{BF8BBF37-5415-46A9-940D-594CAD9DEC26}')
    _idlflags_ = ['oleautomation']
class _dispSolutionEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{FBCFF1C2-261C-11D1-AE5E-00A0C90F26F4}')
    _idlflags_ = []
    _methods_ = []
SolutionEvents._com_interfaces_ = [_SolutionEvents]
SolutionEvents._outgoing_interfaces_ = [_dispSolutionEvents]

Events._methods_ = [
    COMMETHOD([dispid(205), helpstring(u'Returns an object providing events fired when the supplied CommandBarControl object is clicked.'), 'propget'], HRESULT, 'CommandBarEvents',
              ( ['in'], POINTER(IDispatch), 'CommandBarControl' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'prceNew' )),
    COMMETHOD([dispid(300), helpstring(u'Returns the CommandEvents object for the specified command.'), 'propget'], HRESULT, 'CommandEvents',
              ( ['in', 'optional'], BSTR, 'Guid', u'{00000000-0000-0000-0000-000000000000}' ),
              ( ['in', 'optional'], c_int, 'ID', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(CommandEvents)), 'ppceNew' )),
    COMMETHOD([dispid(301), helpstring(u'Returns the Events object for the solution.'), 'propget'], HRESULT, 'SelectionEvents',
              ( ['retval', 'out'], POINTER(POINTER(SelectionEvents)), 'ppceNew' )),
    COMMETHOD([dispid(302), helpstring(u'Returns the Events object for the selection.'), 'propget'], HRESULT, 'SolutionEvents',
              ( ['retval', 'out'], POINTER(POINTER(SolutionEvents)), 'ppceNew' )),
    COMMETHOD([dispid(303), helpstring(u'Returns the object that sources solution build events.'), 'propget'], HRESULT, 'BuildEvents',
              ( ['retval', 'out'], POINTER(POINTER(BuildEvents)), 'ppceNew' )),
    COMMETHOD([dispid(304), helpstring(u'Returns the object that sources Window events.'), 'propget'], HRESULT, 'WindowEvents',
              ( ['in', 'optional'], POINTER(Window), 'WindowFilter', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(WindowEvents)), 'ppceNew' )),
    COMMETHOD([dispid(305), helpstring(u'Returns the object that sources output Window events.'), 'propget'], HRESULT, 'OutputWindowEvents',
              ( ['in', 'optional'], BSTR, 'Pane', u'' ),
              ( ['retval', 'out'], POINTER(POINTER(OutputWindowEvents)), 'ppceNew' )),
    COMMETHOD([dispid(306), helpstring(u'Returns the object that sources Find events.'), 'propget'], HRESULT, 'FindEvents',
              ( ['retval', 'out'], POINTER(POINTER(FindEvents)), 'ppFindEvents' )),
    COMMETHOD([dispid(307), helpstring(u'Returns the object that sources events on the Task List.'), 'propget'], HRESULT, 'TaskListEvents',
              ( ['in', 'optional'], BSTR, 'Filter', u'' ),
              ( ['retval', 'out'], POINTER(POINTER(TaskListEvents)), 'ppceNew' )),
    COMMETHOD([dispid(308), helpstring(u'Returns the object that sources events on the environment.'), 'propget'], HRESULT, 'DTEEvents',
              ( ['retval', 'out'], POINTER(POINTER(DTEEvents)), 'ppceNew' )),
    COMMETHOD([dispid(309), helpstring(u'Returns the object that sources events on Documents.'), 'propget'], HRESULT, 'DocumentEvents',
              ( ['in', 'optional'], POINTER(Document), 'Document', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(DocumentEvents)), 'ppceNew' )),
    COMMETHOD([dispid(310), helpstring(u'Returns the object that sources events on Solution Items.'), 'propget'], HRESULT, 'SolutionItemsEvents',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItemsEvents)), 'ppeNew' )),
    COMMETHOD([dispid(311), helpstring(u'Returns the object that sources events on Miscellaneous Items.'), 'propget'], HRESULT, 'MiscFilesEvents',
              ( ['retval', 'out'], POINTER(POINTER(ProjectItemsEvents)), 'ppeNew' )),
    COMMETHOD([dispid(312), helpstring(u'Returns the object that sources events from the debugger.'), 'propget'], HRESULT, 'DebuggerEvents',
              ( ['retval', 'out'], POINTER(POINTER(DebuggerEvents)), 'ppeNew' )),
    COMMETHOD([dispid(313), helpstring(u'Returns the object that sources events from the text editor.'), 'propget'], HRESULT, 'TextEditorEvents',
              ( ['in', 'optional'], POINTER(TextDocument), 'TextDocumentFilter', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(TextEditorEvents)), 'ppeNew' )),
    COMMETHOD([dispid(314), helpstring(u'Returns an interface or object that can be accessed at run time by name.')], HRESULT, 'GetObject',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppObject' )),
]
################################################################
## code template for Events implementation
##class Events_Impl(object):
##    @property
##    def SolutionEvents(self):
##        u'Returns the Events object for the selection.'
##        #return ppceNew
##
##    @property
##    def BuildEvents(self):
##        u'Returns the object that sources solution build events.'
##        #return ppceNew
##
##    @property
##    def SolutionItemsEvents(self):
##        u'Returns the object that sources events on Solution Items.'
##        #return ppeNew
##
##    @property
##    def TaskListEvents(self, Filter):
##        u'Returns the object that sources events on the Task List.'
##        #return ppceNew
##
##    @property
##    def DebuggerEvents(self):
##        u'Returns the object that sources events from the debugger.'
##        #return ppeNew
##
##    def GetObject(self, Name):
##        u'Returns an interface or object that can be accessed at run time by name.'
##        #return ppObject
##
##    @property
##    def WindowEvents(self, WindowFilter):
##        u'Returns the object that sources Window events.'
##        #return ppceNew
##
##    @property
##    def OutputWindowEvents(self, Pane):
##        u'Returns the object that sources output Window events.'
##        #return ppceNew
##
##    @property
##    def DTEEvents(self):
##        u'Returns the object that sources events on the environment.'
##        #return ppceNew
##
##    @property
##    def FindEvents(self):
##        u'Returns the object that sources Find events.'
##        #return ppFindEvents
##
##    @property
##    def CommandBarEvents(self, CommandBarControl):
##        u'Returns an object providing events fired when the supplied CommandBarControl object is clicked.'
##        #return prceNew
##
##    @property
##    def TextEditorEvents(self, TextDocumentFilter):
##        u'Returns the object that sources events from the text editor.'
##        #return ppeNew
##
##    @property
##    def SelectionEvents(self):
##        u'Returns the Events object for the solution.'
##        #return ppceNew
##
##    @property
##    def MiscFilesEvents(self):
##        u'Returns the object that sources events on Miscellaneous Items.'
##        #return ppeNew
##
##    @property
##    def CommandEvents(self, Guid, ID):
##        u'Returns the CommandEvents object for the specified command.'
##        #return ppceNew
##
##    @property
##    def DocumentEvents(self, Document):
##        u'Returns the object that sources events on Documents.'
##        #return ppceNew
##


# values for enumeration 'DsTextSearchOptions'
dsMatchWord = 2
dsMatchCase = 4
dsMatchNoRegExp = 0
dsMatchRegExp = 8
dsMatchRegExpB = 16
dsMatchRegExpE = 32
dsMatchRegExpCur = 64
dsMatchForward = 0
dsMatchBackward = 128
dsMatchFromStart = 256
DsTextSearchOptions = c_int # enum

# values for enumeration 'vsext_LinkedWindowType'
vsext_lwt_Docked = 0
vsext_lwt_Tabbed = 1
vsext_LinkedWindowType = c_int # enum
_CommandEvents._methods_ = [
]
################################################################
## code template for _CommandEvents implementation
##class _CommandEvents_Impl(object):

class Property(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Generic object representing property of another object/containing all currently available Property objects.'
    _iid_ = GUID('{7B988E06-2581-485E-9322-04881E0600D0}')
    _idlflags_ = ['dual', 'oleautomation']
Properties._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Property)), 'lplppReturn' )),
    COMMETHOD([dispid(1), 'restricted', 'hidden', 'propget'], HRESULT, 'Application',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'lppidReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'lppidReturn' )),
    COMMETHOD([dispid(40), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'lplReturn' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(100), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
]
################################################################
## code template for Properties implementation
##class Properties_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return lplReturn
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppidReturn
##
##    @property
##    def Application(self):
##        '-no docstring-'
##        #return lppidReturn
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return lplppReturn
##

_dispCommandEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Occurs before a command executes.')], None, 'BeforeExecute',
               ( ['in'], BSTR, 'Guid' ),
               ( ['in'], c_int, 'ID' ),
               ( ['in'], VARIANT, 'CustomIn' ),
               ( ['in'], VARIANT, 'CustomOut' ),
               ( ['in', 'out'], POINTER(VARIANT_BOOL), 'CancelDefault' )),
    DISPMETHOD([dispid(2), helpstring(u'Occurs after a command executes.')], None, 'AfterExecute',
               ( ['in'], BSTR, 'Guid' ),
               ( ['in'], c_int, 'ID' ),
               ( ['in'], VARIANT, 'CustomIn' ),
               ( ['in'], VARIANT, 'CustomOut' )),
]
_SelectionEvents._methods_ = [
]
################################################################
## code template for _SelectionEvents implementation
##class _SelectionEvents_Impl(object):

class IExtenderProvider(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Object that represents an Extender Provider.'
    _iid_ = GUID('{4DB06329-23F4-443B-9ABD-9CF611E8AE07}')
    _idlflags_ = ['dual', 'oleautomation']
ObjectExtenders._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
    COMMETHOD([dispid(3), helpstring(u'Registers an Extender Provider for a specific Extender category.')], HRESULT, 'RegisterExtenderProvider',
              ( ['in'], BSTR, 'ExtenderCATID' ),
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['in'], POINTER(IExtenderProvider), 'ExtenderProvider' ),
              ( ['in', 'optional'], BSTR, 'LocalizedName', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'Cookie' )),
    COMMETHOD([dispid(4), helpstring(u'Unregister a previously registered Extender Provider.')], HRESULT, 'UnregisterExtenderProvider',
              ( ['in'], c_int, 'Cookie' )),
    COMMETHOD([dispid(5), helpstring(u'Get an Extender for the given object under the specified category.')], HRESULT, 'GetExtender',
              ( ['in'], BSTR, 'ExtenderCATID' ),
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['in'], POINTER(IUnknown), 'ExtendeeObject' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(6), helpstring(u'List all Extenders for the given object under the specified category.')], HRESULT, 'GetExtenderNames',
              ( ['in'], BSTR, 'ExtenderCATID' ),
              ( ['in'], POINTER(IUnknown), 'ExtendeeObject' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderNames' )),
    COMMETHOD([dispid(7), helpstring(u'List all Contextual Extender CATIDs for the current selection.')], HRESULT, 'GetContextualExtenderCATIDs',
              ( ['retval', 'out'], POINTER(VARIANT), 'ExtenderCATIDs' )),
    COMMETHOD([dispid(8), 'hidden'], HRESULT, 'GetLocalizedExtenderName',
              ( ['in'], BSTR, 'ExtenderCATID' ),
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pLocalizedName' )),
    COMMETHOD([dispid(9)], HRESULT, 'RegisterExtenderProviderUnk',
              ( ['in'], BSTR, 'ExtenderCATID' ),
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['in'], POINTER(IExtenderProviderUnk), 'ExtenderProvider' ),
              ( ['in', 'optional'], BSTR, 'LocalizedName', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'Cookie' )),
]
################################################################
## code template for ObjectExtenders implementation
##class ObjectExtenders_Impl(object):
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppaReturn
##
##    def GetLocalizedExtenderName(self, ExtenderCATID, ExtenderName):
##        '-no docstring-'
##        #return pLocalizedName
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    def RegisterExtenderProviderUnk(self, ExtenderCATID, ExtenderName, ExtenderProvider, LocalizedName):
##        '-no docstring-'
##        #return Cookie
##
##    def UnregisterExtenderProvider(self, Cookie):
##        u'Unregister a previously registered Extender Provider.'
##        #return 
##
##    def GetContextualExtenderCATIDs(self):
##        u'List all Contextual Extender CATIDs for the current selection.'
##        #return ExtenderCATIDs
##
##    def RegisterExtenderProvider(self, ExtenderCATID, ExtenderName, ExtenderProvider, LocalizedName):
##        u'Registers an Extender Provider for a specific Extender category.'
##        #return Cookie
##
##    def GetExtender(self, ExtenderCATID, ExtenderName, ExtendeeObject):
##        u'Get an Extender for the given object under the specified category.'
##        #return Extender
##
##    def GetExtenderNames(self, ExtenderCATID, ExtendeeObject):
##        u'List all Extenders for the given object under the specified category.'
##        #return ExtenderNames
##

Expressions._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(Expression)), 'Expression' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Enumerator' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'Debugger' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Count' )),
]
################################################################
## code template for Expressions implementation
##class Expressions_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return Count
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return Expression
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Enumerator
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Debugger
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##

class IVsProfferCommands(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{8CC0CDE1-C16A-4749-99AF-6F7523C34A57}')
    _idlflags_ = ['hidden', 'restricted']
IVsProfferCommands._methods_ = [
    COMMETHOD([], HRESULT, 'AddNamedCommand',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pguidPackage' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pguidCmdGroup' ),
              ( ['in'], WSTRING, 'pszCmdNameCanonical' ),
              ( ['out'], POINTER(c_ulong), 'pdwCmdId' ),
              ( ['in'], WSTRING, 'pszCmdNameLocalized' ),
              ( ['in'], WSTRING, 'pszBtnText' ),
              ( ['in'], WSTRING, 'pszCmdTooltip' ),
              ( ['in'], WSTRING, 'pszSatelliteDLL' ),
              ( ['in'], c_ulong, 'dwBitmapResourceId' ),
              ( ['in'], c_ulong, 'dwBitmapImageIndex' ),
              ( ['in'], c_ulong, 'dwCmdFlagsDefault' ),
              ( ['in'], c_ulong, 'cUIContexts' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'rgguidUIContexts' )),
    COMMETHOD([], HRESULT, 'RemoveNamedCommand',
              ( ['in'], WSTRING, 'pszCmdNameCanonical' )),
    COMMETHOD([], HRESULT, 'RenameNamedCommand',
              ( ['in'], WSTRING, 'pszCmdNameCanonical' ),
              ( ['in'], WSTRING, 'pszCmdNameCanonicalNew' ),
              ( ['in'], WSTRING, 'pszCmdNameLocalizedNew' )),
    COMMETHOD([], HRESULT, 'AddCommandBarControl',
              ( ['in'], WSTRING, 'pszCmdNameCanonical' ),
              ( ['in'], POINTER(IDispatch), 'pCmdBarParent' ),
              ( ['in'], c_ulong, 'dwIndex' ),
              ( ['in'], c_ulong, 'dwCmdType' ),
              ( ['out'], POINTER(POINTER(IDispatch)), 'ppCmdBarCtrl' )),
    COMMETHOD([], HRESULT, 'RemoveCommandBarControl',
              ( ['in'], POINTER(IDispatch), 'pCmdBarCtrl' )),
    COMMETHOD([], HRESULT, 'AddCommandBar',
              ( ['in'], WSTRING, 'pszCmdBarName' ),
              ( ['in'], vsCommandBarType, 'dwType' ),
              ( ['in'], POINTER(IDispatch), 'pCmdBarParent' ),
              ( ['in'], c_ulong, 'dwIndex' ),
              ( ['out'], POINTER(POINTER(IDispatch)), 'ppCmdBar' )),
    COMMETHOD([], HRESULT, 'RemoveCommandBar',
              ( ['in'], POINTER(IDispatch), 'pCmdBar' )),
    COMMETHOD([], HRESULT, 'FindCommandBar',
              ( ['in'], c_void_p, 'pToolbarSet' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pguidCmdGroup' ),
              ( ['in'], c_ulong, 'dwMenuId' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppdispCmdBar' )),
]
################################################################
## code template for IVsProfferCommands implementation
##class IVsProfferCommands_Impl(object):
##    def AddNamedCommand(self, pguidPackage, pguidCmdGroup, pszCmdNameCanonical, pszCmdNameLocalized, pszBtnText, pszCmdTooltip, pszSatelliteDLL, dwBitmapResourceId, dwBitmapImageIndex, dwCmdFlagsDefault, cUIContexts, rgguidUIContexts):
##        '-no docstring-'
##        #return pdwCmdId
##
##    def FindCommandBar(self, pToolbarSet, pguidCmdGroup, dwMenuId):
##        '-no docstring-'
##        #return ppdispCmdBar
##
##    def AddCommandBar(self, pszCmdBarName, dwType, pCmdBarParent, dwIndex):
##        '-no docstring-'
##        #return ppCmdBar
##
##    def RemoveNamedCommand(self, pszCmdNameCanonical):
##        '-no docstring-'
##        #return 
##
##    def AddCommandBarControl(self, pszCmdNameCanonical, pCmdBarParent, dwIndex, dwCmdType):
##        '-no docstring-'
##        #return ppCmdBarCtrl
##
##    def RemoveCommandBarControl(self, pCmdBarCtrl):
##        '-no docstring-'
##        #return 
##
##    def RemoveCommandBar(self, pCmdBar):
##        '-no docstring-'
##        #return 
##
##    def RenameNamedCommand(self, pszCmdNameCanonical, pszCmdNameCanonicalNew, pszCmdNameLocalizedNew):
##        '-no docstring-'
##        #return 
##

CodeElements._methods_ = [
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(1), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTEObject' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ParentObject' )),
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( [], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(CodeElement)), 'ppCodeElement' )),
    COMMETHOD([dispid(3), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'CountOfCodeElements' )),
    COMMETHOD([dispid(4), 'restricted', 'hidden'], HRESULT, 'Reserved1',
              ( [], VARIANT, 'Element' )),
    COMMETHOD([dispid(5), helpstring(u'Creates a programmatic identifier that does not collide with other identifiers in the scope, and follows the current language naming rules.')], HRESULT, 'CreateUniqueID',
              ( ['in'], BSTR, 'Prefix' ),
              ( ['in', 'out', 'optional'], POINTER(BSTR), 'NewName', u'0' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'pRootUnique' )),
]
################################################################
## code template for CodeElements implementation
##class CodeElements_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return CountOfCodeElements
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def Parent(self):
##        u'Returns the top-level extensibility object.'
##        #return ParentObject
##
##    def CreateUniqueID(self, Prefix):
##        u'Creates a programmatic identifier that does not collide with other identifiers in the scope, and follows the current language naming rules.'
##        #return NewName, pRootUnique
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTEObject
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return ppCodeElement
##
##    def Reserved1(self, Element):
##        '-no docstring-'
##        #return 
##

SelectionContainer._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Returns an indexed member of a collection.')], HRESULT, 'Item',
              ( ['in'], VARIANT, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'lplppReturn' )),
    COMMETHOD([dispid(-4), 'restricted'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'lppiuReturn' )),
    COMMETHOD([dispid(1), helpstring(u'Returns value indicating the count of objects in the collection.'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'lplReturn' )),
    COMMETHOD([dispid(2), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(SelectedItems)), 'lppReturn' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppReturn' )),
]
################################################################
## code template for SelectionContainer implementation
##class SelectionContainer_Impl(object):
##    @property
##    def Count(self):
##        u'Returns value indicating the count of objects in the collection.'
##        #return lplReturn
##
##    def Item(self, index):
##        u'Returns an indexed member of a collection.'
##        #return lplppReturn
##
##    def _NewEnum(self):
##        '-no docstring-'
##        #return lppiuReturn
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppReturn
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return lppReturn
##

OutputWindow._methods_ = [
    COMMETHOD([dispid(2), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'pDTE' )),
    COMMETHOD([dispid(3), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Window)), 'pParent' )),
    COMMETHOD([dispid(4), helpstring(u'Returns the OutputWindowPanes collection for the object.'), 'propget'], HRESULT, 'OutputWindowPanes',
              ( ['retval', 'out'], POINTER(POINTER(OutputWindowPanes)), 'pOutputWindowPanes' )),
    COMMETHOD([dispid(5), helpstring(u'Returns the currently active item in the collection.'), 'propget'], HRESULT, 'ActivePane',
              ( ['retval', 'out'], POINTER(POINTER(OutputWindowPane)), 'pOutputWindowPane' )),
]
################################################################
## code template for OutputWindow implementation
##class OutputWindow_Impl(object):
##    @property
##    def OutputWindowPanes(self):
##        u'Returns the OutputWindowPanes collection for the object.'
##        #return pOutputWindowPanes
##
##    @property
##    def ActivePane(self):
##        u'Returns the currently active item in the collection.'
##        #return pOutputWindowPane
##
##    @property
##    def Parent(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return pParent
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return pDTE
##

class IFilterProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Interface an Automation Extender should support if it wants to filters one or more Extendee properties.'
    _iid_ = GUID('{AADE1F59-6ACE-43D1-8FCA-42AF3A5C4F3C}')
    _idlflags_ = ['dual', 'oleautomation']
IFilterProperties._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Returns whether the specified property is filtered (hidden).')], HRESULT, 'IsPropertyHidden',
              ( ['in'], BSTR, 'PropertyName' ),
              ( ['retval', 'out'], POINTER(vsFilterProperties), 'pRetval' )),
]
################################################################
## code template for IFilterProperties implementation
##class IFilterProperties_Impl(object):
##    def IsPropertyHidden(self, PropertyName):
##        u'Returns whether the specified property is filtered (hidden).'
##        #return pRetval
##

Expression._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'The name of the expression.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Name' )),
    COMMETHOD([dispid(100), helpstring(u'The type of the expression.'), 'propget'], HRESULT, 'Type',
              ( ['retval', 'out'], POINTER(BSTR), 'Type' )),
    COMMETHOD([dispid(101), helpstring(u'If the expression represents a class or structure, retrieve a list of member variables, as expression objects.'), 'propget'], HRESULT, 'DataMembers',
              ( ['retval', 'out'], POINTER(POINTER(Expressions)), 'Expressions' )),
    COMMETHOD([dispid(102), helpstring(u'Sets/Returns the current value of the expression as a string.'), 'propget'], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(102), helpstring(u'Sets/Returns the current value of the expression as a string.'), 'propput'], HRESULT, 'Value',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(103), helpstring(u'Is the value valid?'), 'propget'], HRESULT, 'IsValidValue',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'ValidValue' )),
    COMMETHOD([dispid(200), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'DTE' )),
    COMMETHOD([dispid(201), helpstring(u'Returns the parent object.'), 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Debugger)), 'Debugger' )),
    COMMETHOD([dispid(202), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(Expressions)), 'Expressions' )),
]
################################################################
## code template for Expression implementation
##class Expression_Impl(object):
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return Expressions
##
##    @property
##    def Name(self):
##        u'The name of the expression.'
##        #return Name
##
##    @property
##    def Parent(self):
##        u'Returns the parent object.'
##        #return Debugger
##
##    @property
##    def IsValidValue(self):
##        u'Is the value valid?'
##        #return ValidValue
##
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return DTE
##
##    @property
##    def DataMembers(self):
##        u'If the expression represents a class or structure, retrieve a list of member variables, as expression objects.'
##        #return Expressions
##
##    def _get(self):
##        u'Sets/Returns the current value of the expression as a string.'
##        #return Value
##    def _set(self, Value):
##        u'Sets/Returns the current value of the expression as a string.'
##    Value = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Type(self):
##        u'The type of the expression.'
##        #return Type
##

Property._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Sets/ returns the value of property returned by the Property object.'), 'propget'], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(VARIANT), 'lppvReturn' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/ returns the value of property returned by the Property object.'), 'propput'], HRESULT, 'Value',
              ( ['in'], VARIANT, 'lppvReturn' )),
    COMMETHOD([dispid(0), helpstring(u'Sets/ returns the value of property returned by the Property object.'), 'propputref'], HRESULT, 'Value',
              ( ['in'], VARIANT, 'lppvReturn' )),
    COMMETHOD([dispid(3), helpstring(u'Returns one element of a list.'), 'propget'], HRESULT, 'IndexedValue',
              ( ['in'], VARIANT, 'Index1' ),
              ( ['in', 'optional'], VARIANT, 'Index2' ),
              ( ['in', 'optional'], VARIANT, 'Index3' ),
              ( ['in', 'optional'], VARIANT, 'Index4' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'Val' )),
    COMMETHOD([dispid(3), helpstring(u'Returns one element of a list.'), 'propput'], HRESULT, 'IndexedValue',
              ( ['in'], VARIANT, 'Index1' ),
              ( ['in', 'optional'], VARIANT, 'Index2' ),
              ( ['in', 'optional'], VARIANT, 'Index3' ),
              ( ['in', 'optional'], VARIANT, 'Index4' ),
              ( ['in'], VARIANT, 'Val' )),
    COMMETHOD([dispid(4), helpstring(u'Returns a value representing the number of items in the list value.'), 'propget'], HRESULT, 'NumIndices',
              ( ['retval', 'out'], POINTER(c_short), 'lpiRetVal' )),
    COMMETHOD([dispid(1), 'restricted', 'hidden', 'propget'], HRESULT, 'Application',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'lppidReturn' )),
    COMMETHOD([dispid(2), 'restricted', 'hidden', 'propget'], HRESULT, 'Parent',
              ( ['retval', 'out'], POINTER(POINTER(Properties)), 'lpppReturn' )),
    COMMETHOD([dispid(40), helpstring(u'Returns the name of the object.'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'lpbstrReturn' )),
    COMMETHOD([dispid(42), helpstring(u'Returns the collection containing the object supporting this property.'), 'propget'], HRESULT, 'Collection',
              ( ['retval', 'out'], POINTER(POINTER(Properties)), 'lpppReturn' )),
    COMMETHOD([dispid(45), helpstring(u'Sets/returns value of Property object when type of value is Object.'), 'propget'], HRESULT, 'Object',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'lppunk' )),
    COMMETHOD([dispid(45), helpstring(u'Sets/returns value of Property object when type of value is Object.'), 'propputref'], HRESULT, 'Object',
              ( ['in'], POINTER(IUnknown), 'lppunk' )),
    COMMETHOD([dispid(100), helpstring(u'Returns the top-level extensibility object.'), 'propget'], HRESULT, 'DTE',
              ( ['retval', 'out'], POINTER(POINTER(DTE)), 'lppaReturn' )),
]
################################################################
## code template for Property implementation
##class Property_Impl(object):
##    @property
##    def DTE(self):
##        u'Returns the top-level extensibility object.'
##        #return lppaReturn
##
##    @property
##    def NumIndices(self):
##        u'Returns a value representing the number of items in the list value.'
##        #return lpiRetVal
##
##    @property
##    def Parent(self):
##        '-no docstring-'
##        #return lpppReturn
##
##    def Object(self, lppunk):
##        u'Sets/returns value of Property object when type of value is Object.'
##        #return 
##
##    def Value(self, lppvReturn):
##        u'Sets/ returns the value of property returned by the Property object.'
##        #return 
##
##    @property
##    def Application(self):
##        '-no docstring-'
##        #return lppidReturn
##
##    @property
##    def Collection(self):
##        u'Returns the collection containing the object supporting this property.'
##        #return lpppReturn
##
##    def _get(self, Index1, Index2, Index3, Index4):
##        u'Returns one element of a list.'
##        #return Val
##    def _set(self, Index1, Index2, Index3, Index4, Val):
##        u'Returns one element of a list.'
##    IndexedValue = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Name(self):
##        u'Returns the name of the object.'
##        #return lpbstrReturn
##


# values for enumeration 'vsNavigateBrowser'
vsNavigateBrowserDefault = 0
vsNavigateBrowserHelp = 1
vsNavigateBrowserNewWindow = 2
vsNavigateBrowser = c_int # enum
_dispSelectionEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Occurs just after the selection model changes.')], None, 'OnChange'),
]
_SolutionEvents._methods_ = [
]
################################################################
## code template for _SolutionEvents implementation
##class _SolutionEvents_Impl(object):

vsext_vk_TextView = u'{7651A703-06E5-11D1-8EBD-00A0C90F26EA}' # Constant STRING
IExtenderProvider._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Get an Extender for the given object under the specified category.')], HRESULT, 'GetExtender',
              ( ['in'], BSTR, 'ExtenderCATID' ),
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['in'], POINTER(IDispatch), 'ExtendeeObject' ),
              ( ['in'], POINTER(IExtenderSite), 'ExtenderSite' ),
              ( ['in'], c_int, 'Cookie' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'Extender' )),
    COMMETHOD([dispid(2), helpstring(u'Returns True if the Provider can provide an Extender for the given object under the specified category.')], HRESULT, 'CanExtend',
              ( ['in'], BSTR, 'ExtenderCATID' ),
              ( ['in'], BSTR, 'ExtenderName' ),
              ( ['in'], POINTER(IDispatch), 'ExtendeeObject' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'fRetval' )),
]
################################################################
## code template for IExtenderProvider implementation
##class IExtenderProvider_Impl(object):
##    def GetExtender(self, ExtenderCATID, ExtenderName, ExtendeeObject, ExtenderSite, Cookie):
##        u'Get an Extender for the given object under the specified category.'
##        #return Extender
##
##    def CanExtend(self, ExtenderCATID, ExtenderName, ExtendeeObject):
##        u'Returns True if the Provider can provide an Extender for the given object under the specified category.'
##        #return fRetval
##

ColorableItems._methods_ = [
    COMMETHOD([dispid(0), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'pName' )),
    COMMETHOD([dispid(1), helpstring(u'Gets/Sets the foreground color of the item.'), 'propget'], HRESULT, 'Foreground',
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_COLOR), 'pColor' )),
    COMMETHOD([dispid(1), helpstring(u'Gets/Sets the foreground color of the item.'), 'propput'], HRESULT, 'Foreground',
              ( [], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_COLOR, 'pColor' )),
    COMMETHOD([dispid(2), helpstring(u'Gets/Sets the background color of the item.'), 'propget'], HRESULT, 'Background',
              ( ['retval', 'out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_COLOR), 'pColor' )),
    COMMETHOD([dispid(2), helpstring(u'Gets/Sets the background color of the item.'), 'propput'], HRESULT, 'Background',
              ( [], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.OLE_COLOR, 'pColor' )),
    COMMETHOD([dispid(3), helpstring(u'Gets/Sets if the item should be shown bold.'), 'propget'], HRESULT, 'Bold',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Bold' )),
    COMMETHOD([dispid(3), helpstring(u'Gets/Sets if the item should be shown bold.'), 'propput'], HRESULT, 'Bold',
              ( [], VARIANT_BOOL, 'Bold' )),
]
################################################################
## code template for ColorableItems implementation
##class ColorableItems_Impl(object):
##    def _get(self):
##        u'Gets/Sets the foreground color of the item.'
##        #return pColor
##    def _set(self, pColor):
##        u'Gets/Sets the foreground color of the item.'
##    Foreground = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Name(self):
##        '-no docstring-'
##        #return pName
##
##    def _get(self):
##        u'Gets/Sets the background color of the item.'
##        #return pColor
##    def _set(self, pColor):
##        u'Gets/Sets the background color of the item.'
##    Background = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Gets/Sets if the item should be shown bold.'
##        #return Bold
##    def _set(self, Bold):
##        u'Gets/Sets if the item should be shown bold.'
##    Bold = property(_get, _set, doc = _set.__doc__)
##

_dispSolutionEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Occurs just after opening a Solution/Project.')], None, 'Opened'),
    DISPMETHOD([dispid(2), helpstring(u'Occurs just before closing a Solution/Project.')], None, 'BeforeClosing'),
    DISPMETHOD([dispid(3)], None, 'AfterClosing'),
    DISPMETHOD([dispid(4)], None, 'QueryCloseSolution',
               ( ['in', 'out'], POINTER(VARIANT_BOOL), 'fCancel' )),
    DISPMETHOD([dispid(5), helpstring(u'Occurs just after renaming a solution.')], None, 'Renamed',
               ( ['in'], BSTR, 'OldName' )),
    DISPMETHOD([dispid(6), helpstring(u'Occurs just after adding a Project to the solution.')], None, 'ProjectAdded',
               ( ['in'], POINTER(Project), 'Project' )),
    DISPMETHOD([dispid(7), helpstring(u'Occurs just after removing a Project from the solution.')], None, 'ProjectRemoved',
               ( ['in'], POINTER(Project), 'Project' )),
    DISPMETHOD([dispid(8), helpstring(u'Occurs just after renaming a Project.')], None, 'ProjectRenamed',
               ( ['in'], POINTER(Project), 'Project' ),
               ( ['in'], BSTR, 'OldName' )),
]
IExtenderSite._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Method an Automation Extender is expected to call back upon when being destroyed to notify its site.')], HRESULT, 'NotifyDelete',
              ( ['in'], c_int, 'Cookie' )),
    COMMETHOD([dispid(2), helpstring(u'Returns an interface or object that can be accessed at run time by name.')], HRESULT, 'GetObject',
              ( ['in', 'optional'], BSTR, 'Name', u'' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppObject' )),
]
################################################################
## code template for IExtenderSite implementation
##class IExtenderSite_Impl(object):
##    def GetObject(self, Name):
##        u'Returns an interface or object that can be accessed at run time by name.'
##        #return ppObject
##
##    def NotifyDelete(self, Cookie):
##        u'Method an Automation Extender is expected to call back upon when being destroyed to notify its site.'
##        #return 
##

__all__ = ['vsCMElementLocalDeclStmt', 'vsext_lwt_Tabbed',
           'vsBuildStateInProgress', 'CodeEnum',
           'vsToolBoxItemFormatGUID', 'ContextAttributes',
           'vsCATIDMiscFilesProjectItem',
           'vsCMAccessAssemblyOrFamily', 'Macros',
           '_dispSolutionEvents', 'vsBuildActionDeploy',
           '_TaskListEvents', 'vsBuildScopeSolution',
           '_dispBuildEvents', 'vsCMInfoLocation', 'dsSaveChangesNo',
           'dbgHitCountTypeMultiple', 'vsext_wt_MainWindow',
           'vsCMPrototypeInitExpression',
           'vsFindOptionsRegularExpression', 'UndoContext',
           'vsStatusAnimationGeneral', 'vsCMPartHeaderWithAttributes',
           'vsFindTargetCurrentDocument', 'vsFontCharSetHangeul',
           'vsext_fontcs_RUSSIAN', 'vsNavigateBrowserDefault',
           'dsUppercase', 'dsFirstColumn', 'vsTaskIconUser',
           'vsCommandStatusSupported', 'vsInsertFlagsCollapseToEnd',
           'vsWindowKindAutoLocals', 'vsWindowStateNormal',
           'vsStatusAnimationPrint', 'CodeAttribute',
           'vsext_fontcs_HEBREW', 'vsext_fontcs_CHINESEBIG5',
           'vsCMElementIDLLibrary', 'vsTaskCategoryUser',
           '_dispProjectsEvents', 'vsWizardNewProject',
           'vsCMPrototypeParamTypes', 'vsMoveToColumnLine',
           '_DocumentEvents',
           'vsFindOptionsKeepModifiedDocumentsOpen', 'dsMatchCase',
           'vsCMElementParameter', '_ProjectsEvents', 'dsMatchWord',
           'vsInitializeModeReset', 'vsProjectItemKindSubProject',
           'Breakpoint', 'DsSaveChanges', 'vsCMPrototypeClassName',
           'vsCommandStatusNinched', 'vsWindowKindCommandWindow',
           'dbgExecutionActionDefault',
           'vsWindowTypeLinkedWindowFrame',
           'vsStartUpOpenProjectDialog', 'vsWhitespaceOptions',
           'vsTextChangedNewline', 'vsCMTypeRef',
           'vsWindowKindProperties', 'vsContextNoSolution',
           'vsLinkedWindowTypeTabbed', '_EnvironmentWebBrowser',
           'vsCMAccessPrivate', 'vsStartUpEmptyEnvironment',
           'vsCMPrototypeUniqueSignature', 'vsCMAccessDefault',
           'VirtualPoint', 'DTE', 'vsCMTypeRefDecimal',
           'CodeElements', 'vsWizardAddSubProject',
           'vsext_wk_AutoLocalsWindow', 'vsContextSolutionBuilding',
           'vsCATIDMiscFilesProject', 'vsStartOfLineOptions',
           'vsext_GUID_NewProjectWizard', 'vsCMFunction',
           'vsCMTypeRefString', 'WindowConfiguration',
           'vsCMFunctionInline', 'vsext_wt_Immediate',
           'vsext_wt_Document', 'vsWindowStateMinimize',
           'vsFindPatternSyntaxLiteral', 'vsext_fontcs_VIETNAMESE',
           'dbgBreakpointLocationTypeAddress', 'vsIDEModeDesign',
           'WindowConfigurations', 'vsCommandExecOption',
           'vsContextAttributeLookupF1', 'dbgEventReasonUserBreak',
           'vsCMElementUsingStmt', 'vsMiscFilesProjectUniqueName',
           'vsCMElementDeclareDecl', 'UIHierarchyItem',
           'vsWizardAddItem', 'vsProjectKindUnmodeled',
           'vsext_wt_Designer', 'vsWindowKindLocals',
           'vsViewKindDebugging', 'vsCMElementPropertySetStmt',
           'vsext_fontcs_HANGEUL', 'vsFontCharSetBaltic',
           'vsCMElementOther', 'dsMatchRegExp', '_DTEEvents',
           'vsCommandExecOptionShowHelp', 'vsTaskCategoryShortcut',
           'vsTaskPriority', 'HTMLWindow', 'vsTaskListColumnFile',
           'vsTaskCategoryBuildCompile', 'CodeElement',
           'vsCMPartAttributes', 'IVsGlobalsCallback', 'Languages',
           'vsext_wt_ColorPalette', 'vsPaneShowAsIs', 'TextPanes',
           'vsWindowKindFindResults1', 'vsWindowKindFindResults2',
           'vsCMElementOptionStmt', 'vsext_wt_Toolbox',
           'vsext_su_LOAD_LAST_SOLUTION',
           'vsCMPartAttributesWithDelimiter', 'TextRange',
           'SolutionEvents', 'vsext_fontcs_GREEK', 'vsBuildAction',
           'vsext_DisplayMode', 'VSEXECRESULT', 'vsCMTypeRefObject',
           'RESULT_Cancel', '_dispSelectionEvents',
           'vsNavigateBrowser', 'vsCommandBarTypeMenu',
           'vsSaveChanges', 'DsStartOfLineOptions',
           'vsSmartFormatOptionsNone', 'vsCMFunctionTopLevel',
           'dbgBreakpointLocationTypeNone', 'vsSaveCancelled',
           'vsext_vk_Primary', 'wizardResultFailure',
           'vsCMElementUnion', 'Processes',
           'vsTextChangedFindStarting', 'vsCMTypeRefVariant',
           'dbgBreakpointConditionTypeWhenTrue', 'vsCMTypeRefFloat',
           'vsext_vk_Debugging', 'vsGoToLineOptionsFirst',
           'vsWindowKindFindSymbolResults', '_dispFindEvents',
           'dbgHitCountTypeEqual', 'vsWindowKindToolbox', 'TaskItems',
           'vsContextEmptySolution', 'vsCMElementImportStmt',
           'vsSaveChangesPrompt', 'vsBuildActionRebuildAll',
           'vsCMElementAssignmentStmt', 'dbgExceptionActionBreak',
           'vsLinkedWindowTypeVertical', 'vsCMLanguageMC',
           'dbgExecutionActionRunToCursor', 'vsBuildKindSolution',
           'vsCMInfoLocationProject', 'CodeVariable',
           'vsCommandDisabledFlagsHidden', 'vsext_wt_Threads',
           'vsTaskCategoryMisc', 'vsext_wt_Browser',
           'vsProjectKindSolutionItems', 'vsext_wk_ImmedWindow',
           'vsFontCharSet', 'vsCMElementEnum', 'vsCaseOptions',
           'vsBuildKind', 'vsext_LinkedWindowType',
           'vsCMElementTypeDef', 'dbgExceptionActionContinue',
           'vsViewKindTextView', 'vsBuildKindProjectItem',
           'vsext_fontcs_JOHAB', 'vsWindowKindTaskList',
           'ToolBoxItem', 'dsVBSMacro',
           'dbgExecutionActionStopDebugging', 'dsLowercase',
           'vsCMFunctionPropertyLet', 'Globals',
           '_DebuggerEventsRoot', 'OutputWindowPanes',
           'dbgBreakpointTypeBound', 'vsFindActionReplace',
           'vsext_wt_Autos', 'vsCMTypeRefChar',
           'vsFindActionReplaceAll', 'CodeClass',
           'vsCommandDisabledFlagsEnabled', 'FindEvents',
           'vsFindTargetSolution', 'vsCommandStatusTextWantedStatus',
           'vsToolBoxItemFormatHTML', 'vsext_fontcs_ANSI',
           'vsFindOptionsNone', 'vsCMFunctionPropertyAssign',
           '_FindEvents', 'StatusBar', 'vsFindActionBookmarkAll',
           'IVsTextEditGeneral', 'vsCMElementInheritsStmt',
           'vsCMPart', 'vsWindowTypeFind', 'vsCMTypeRefShort',
           'vsext_wt_Locals', 'vsCMAccessProtected',
           'vsext_fontcs_THAI', '_dispDocumentEvents',
           'vsCMElementIDLImport', 'vsStartUpNewProjectDialog',
           '_dispProjectItemsEvents', 'vsMoveToColumnLineFirst',
           'vsBuildScopeProject', 'vsWindowTypeImmediate',
           'dbgRunMode', 'vsWindowKindFindSymbol', 'dsJava',
           'vsStartOfLineOptionsFirstText', 'vsViewKindAny',
           'vsFontCharSetHebrew', 'CodeParameter',
           'vsContextFullScreenMode', 'vsTaskCategoryHTML',
           'vsCMLanguageCSharp', 'vsCMElementDelegate',
           'vsStatusAnimationSync', 'dbgEventReasonBreakpoint',
           '_BuildEvents', 'vsext_wt_Find',
           'dbgEventReasonExceptionNotHandled',
           'vsext_wk_ObjectBrowser', '_DTE', 'vsFilterPropertiesSet',
           'vsWindowKindLinkedWindowFrame', 'vsFilterPropertiesNone',
           'vsWindowKindThread', 'vsContextAttributesHighPriority',
           'vsConfigurationType', 'vsext_wk_OutputWindow',
           'dbgBreakpointConditionType', 'vsInitializeMode',
           'vsViewKindPrimary', 'CodeTypeRef', '_EnvironmentKeyboard',
           'vsSolutionItemsProjectUniqueName',
           'vsWindowKindMainWindow',
           'vsToolBoxItemFormatDotNETComponent',
           'vsFindPatternSyntaxRegExpr', 'vsStatusAnimationFind',
           'vsSelectionModeStream', 'dbgEventReasonStopDebugging',
           'vsext_WindowType', 'vsext_fontcs_SHIFTJIS',
           'vsext_GUID_AddItemWizard', '_CommandBarControlEvents',
           'dbgBreakpointLocationTypeFunction',
           'vsTaskListColumnCheck', 'vsContextDebugging',
           'RESULT_Failure', '_dispDTEEvents', 'vsProjectKindMisc',
           'AddIns', 'vsEPReplaceTextAutoformat', 'Debugger',
           'vsCMAccess', 'IDTToolsOptionsPage', 'vsCommandBarType',
           'vsContextSolutionHasSingleProject', 'vsCMTypeRefPointer',
           'vsBuildStateNotStarted', 'vsFontCharSetDefault',
           'vsUISelectionTypeSetCaret', 'vsCMPrototype',
           'dbgExecutionAction', 'vsext_ws_Normal', 'vsCMElementMap',
           'vsCMFunctionPropertySet', 'vsLinkedWindowTypeHorizontal',
           'dbgEventReasonContextSwitch', 'vsCommandStatusEnabled',
           'vsCMTypeRefInt', 'TaskListEvents',
           'vsEPReplaceTextNormalizeNewlines', 'vsext_Build',
           'vsCATIDSolution', 'vsCMElementVCBase',
           'BuildDependencies', 'vsWindowTypeDocument',
           'vsCMPartBody', 'ItemOperations', 'vsext_bld_CONFIRM_SAVE',
           'vsext_fontcs_ARABIC', 'vsext_su_NEW_SOLUTION_DIALOG',
           'Threads', 'dsCapitalize', 'vsCMTypeRefOther',
           'vsWindowKindDynamicHelp', 'vsCMFunctionOperator',
           'dsVertical', 'vsFindOptionsMatchCase',
           'wizardResultSuccess', 'vsWhitespaceOptionsHorizontal',
           'vsWindowTypeDesigner', 'vsTaskIconNone',
           'vsCaseOptionsCapitalize', 'vsTextChanged',
           'vsDocumentKindHTML', 'vsFontCharSetGB2312',
           'vsProjectItemKindPhysicalFolder',
           'vsCaseOptionsUppercase', 'vsToolBoxItemFormatText',
           'vsEPReplaceTextOptions', 'vsCMLanguageVC',
           'vsCMLanguageVB', 'vsInsertFlags',
           'dbgBreakpointLocationTypeData',
           'vsCATIDSolutionBrowseObject', 'vsCMElementImplementsStmt',
           'DsWhitespaceOptions', 'vsCMElementEventsDeclaration',
           'vsFontCharSetShiftJIS', 'vsext_bld_SAVE_CHANGES',
           'vsInsertFlagsInsertAtStart', 'dbgExceptionActionIgnore',
           'vsDisplayMDI', 'vsProjectItemKindMisc',
           'vsext_vk_Designer', 'vsFindOptions', 'Program',
           'vsContextAttributeFilter', 'SelectionContainer',
           'vsProjectItemKindSolutionItems', 'vsWindowKindWebBrowser',
           'vsext_dm_SDI', '_OutputWindowEvents', 'WindowEvents',
           'vsWindowKindResourceView', 'SolutionConfiguration',
           'vsProjectItemsKindSolutionItems', 'dsLastLine',
           'TextEditorEvents', 'vsFindResultReplaced',
           'ProjectItemsEvents', 'vsWindowType',
           'vsCMElementAttribute', 'vsIndentStyleDefault',
           'vsPaneShowHow', 'vsCMFunctionConstant', 'Language',
           'vsBuildScope', 'dbgEventReasonNone', 'vsFindTarget',
           'dsHTML_RFC1866', '_DocumentEventsRoot', 'CodeNamespace',
           'vsLinkedWindowType', 'dbgExecutionActionStepOver',
           'vsFontCharSetJohab', 'vsCMLanguageIDL',
           'OutputWindowEvents', 'vsFindResultsLocation',
           'BuildDependency', 'dsMatchRegExpB', 'CodeType',
           'vsSmartFormatOptions', 'vsCMElementNamespace',
           'vsDisplayMDITabs', 'vsWindowTypeCodeWindow',
           'vsCMTypeRefLong', 'vsCMFunctionSub',
           '_OutputWindowEventsRoot', 'SolutionBuild',
           'vsFindActionFind', 'ObjectExtenders',
           'vsWindowTypeDocumentOutline', 'vsStartUpLoadLastSolution',
           '_dispCommandEvents', 'vsCMElementInterface',
           'vsFontCharSetThai', 'vsext_wt_CodeWindow',
           'dbgExceptionAction', '_dispWindowEvents', 'Breakpoints',
           'vsCMElementVBAttributeGroup', 'Window',
           'vsMovementOptionsExtend', 'vsCMAccessProjectOrProtected',
           'vsext_wt_FindReplace', 'DTEEvents',
           'vsCommandStatusTextWantedNone', 'TextRanges',
           'vsSelectionMode', 'vsCMInfoLocationNone', 'vsCMPartName',
           'vsCMFunctionPutRef', 'vsTextChangedMultiLine',
           'vsext_wt_OutPutWindow', 'vsext_fontcs_GB2312',
           'vsTextChangedCaretMoved', 'dsSaveChangesPrompt',
           'vsDocumentKindBinary', 'dsSaveCancelled',
           'vsCMElementMapEntry', 'TextBuffer',
           '_MiscSlnFilesEventsRoot', 'vsWindowKindClassView',
           'vsext_wk_TaskList', 'vsCMPrototypeFullname',
           '_dispTextEditorEvents', 'ISupportVSProperties',
           'vsInsertFlagsInsertAtEnd', 'dbgBreakMode',
           'vsPaneShowTop', 'vsTaskIconComment', 'vsUISelectionType',
           'UIHierarchy', 'vsCMElementDefineStmt', 'dsFortran_Free',
           'vsCommandStatusTextWanted', 'Expression',
           'vsStatusAnimation', '_Solution', 'TextPoint',
           'vsCMElementProperty', 'vsNavigateOptionsDefault',
           'vs_exec_Result', 'vsHTMLTabs', 'SelectedItem',
           'vsFindResultsNone', 'vsext_ws_Maximize',
           'vsFindPatternSyntaxWildcards', 'dbgDebugMode',
           '_dispTaskListEvents', 'vsStatusAnimationSave',
           'vsTaskCategoryComment', '_SelectionEvents', 'Document',
           'vsFindTargetOpenDocuments', 'dsSaveSucceeded',
           'vsCMTypeRefByte', 'dsMove', 'vsLinkedWindowTypeDocked',
           '_EnvironmentFontsAndColors', '_EnvironmentHelp',
           'dsHTML_IE3', 'vsext_fontcs_DEFAULT', 'CommandEvents',
           'CommandBarEvents', 'vsPromptResultCancelled',
           'dsMatchRegExpCur', 'dsSaveStatus', 'vsCMPartHeader',
           'dsMatchRegExpE', 'vsWindowTypeCallStack', 'AddIn',
           '_EnvironmentTaskList', 'vsWindowKindOutput',
           'vsCMElementIDLImportLib', 'vsTaskIcon', 'TextEditor',
           'DsCaseOptions', '_dispCommandBarControlEvents',
           '_dispOutputWindowEvents', 'vsext_wt_ProjectWindow',
           'vsHTMLTabsDesign', '_TextEditorEvents',
           'vsCMInfoLocationExternal', 'CodeInterface',
           'vsCMFunctionPropertyGet', 'vsext_lwt_Docked',
           'vsWindowTypeMainWindow', 'dbgEventReasonLaunchProgram',
           'vsFindResult', 'dbgEventReasonDetachProgram',
           'vsSmartFormatOptionsSmart', 'DsMovementOptions',
           'vsext_wt_LinkedWindowFrame', 'StackFrame',
           'vsCMFunctionPure', 'vsCMElementFunctionInvokeStmt',
           'vsWindowTypeWatch', 'IDTWizard', 'ToolBoxItems', 'dsIDL',
           'vsCommandBarTypePopup', 'vsext_wk_PropertyBrowser',
           'dbgEventReasonAttachProgram', 'vsCMPartNavigate',
           'vsFontCharSetGreek', 'vsFindTargetFiles', 'LinkedWindows',
           '_WindowEvents', 'vsBuildScopeBatch', 'vsTaskIconCompile',
           'vsCMElementStruct', 'vsext_wk_ClassView',
           'vsFindResultNotFound', 'vsInitializeModeStartup',
           'dsFirstText', 'IVsProfferCommands', 'vsext_ws_Minimize',
           'vsContextAttributes', 'vsCommandDisabledFlagsGrey',
           'vsFontCharSetOEM', 'vsCMFunctionConstructor',
           'SolutionConfigurations', 'vsUISelectionTypeToggle',
           'vsext_fontcs_EASTEUROPE', 'vsTextChangedSave',
           'vsext_fontcs_BALTIC', 'vsext_FontCharSet',
           'vsContextSolutionHasMultipleProjects',
           'vsFindTargetCurrentDocumentFunction', 'IExtensibleObject',
           'vsBrowserViewSourceDesign', 'vsBrowserViewSourceExternal',
           'dbgExceptionActionDefault', 'vsContextAttributesGlobal',
           'SourceControl', 'vsCommandStatusUnsupported',
           'vsProjectsKindSolution', 'vsCMTypeRefVoid', 'vsIDEMode',
           'vsext_wt_ToolWindow', 'IVsExtensibility',
           'SolutionContexts', 'TaskList', 'vsAddInCmdGroup',
           'vsFindResults1', '_dispDebuggerEvents',
           'vsWindowKindServerExplorer', 'vsEPReplaceTextTabsSpaces',
           'vsContextAttributeType', 'vsFindResultError',
           'IExtensibleObjectSite', 'IExtenderSite',
           'vsConfigurationTypeProject', 'vsIndentStyle', 'Events',
           'dbgBreakpointConditionTypeWhenChanged',
           'vsCMFunctionFunction', 'ColorableItems', 'StackFrames',
           'wizardResultCancel', 'vsFilterPropertiesAll',
           'vsext_StartUp', 'vsProjectItemsKindMisc',
           'vsFontCharSetANSI', 'vsFindTargetCurrentProject',
           'vsUISelectionTypeExtend', 'Properties',
           'vsStatusAnimationDeploy', 'BuildEvents',
           'vsCMAccessWithEvents', 'vsFontCharSetVietnamese',
           'vsTaskPriorityLow', 'vsext_fontcs_MAC', 'IVsGlobals',
           'vsCommandExecOptionDoPromptUser', 'vsCATIDDocument',
           'vsCommandStatusTextWantedName', 'vsFontCharSetEastEurope',
           'vsWindowKindWatch', 'vsext_wt_RunningDocuments',
           '_EnvironmentProjectsAndSolution', 'dsMatchNoRegExp',
           'vsWindowStateMaximize', 'vsext_bld_NO_SAVE',
           'vsCMElementVBAttributeStmt', 'Process',
           'vsBuildActionBuild', 'vsCMInfoLocationVirtual',
           'SolutionContext', 'vsext_vk_TextView', 'vsCMElementClass',
           'vsCMFunctionComMethod', '_SolutionEvents',
           'vsContextMacroRecordingToolbar', 'DsTextSearchOptions',
           'vsContextAttributesWindow', 'SelectedItems',
           'vsCMAccessPublic', 'TextPane', 'vsext_wk_ContextWindow',
           'vsBuildStateDone', 'vsStartOfLineOptionsFirstColumn',
           'ProjectsEvents', 'CommandWindow', '_vsIndentStyle',
           'vsMoveToColumnLineLast', 'vsCMElementMacro',
           'OutputGroup', 'IExtenderProvider', 'DocumentEvents',
           'vsCMPrototypeParamNames', 'dbgDesignMode',
           'dsMatchBackward', 'vsFindResultReplaceAndNotFound',
           'vsCaseOptionsLowercase', 'vsIDEModeDebug',
           'vsTextChangedReplaceAll', 'vsCMElementEvent',
           'vsCMElementUDTDecl', 'dsExtend', 'vsCMPartWhole',
           'dbgHitCountType', 'IDTCommandTarget', 'dbgBreakpointType',
           'vsCommandDisabledFlags', 'vsTaskPriorityHigh',
           'vsext_dm_MDI', 'dbgBreakpointLocationTypeFile',
           'vsNavigateOptions', 'wizardResult', 'EditPoint',
           'ProjectItems', 'vsStartUpShowHomePage',
           'vsHTMLTabsSource', '_FontsAndColors',
           'vsNavigateBrowserHelp', 'dbgEventReasonGo',
           'IVsTextEditPerLanguage', 'Configurations',
           'vsFindOptionsMatchWholeWord', 'vsDocumentKindResource',
           'ContextAttribute', 'dsSaveChangesYes', 'ToolBoxTabs',
           'Expressions', 'vsCommandStatusInvisible',
           'vsCMTypeRefArray', 'Project', 'dsHorizontal',
           'vsWindowState', 'TextDocument', 'vsCMPrototypeNoName',
           'vsext_wk_LocalsWindow', 'dbgHitCountTypeNone',
           'vsext_wk_CallStackWindow',
           'vsFindOptionsMatchInHiddenText', '_TaskListEventsRoot',
           'vsProjectItemKindVirtualFolder', '_TextEditorEventsRoot',
           'vsTaskPriorityMedium', 'dbgBreakpointTypePending',
           'vsGoToLineOptionsLast', 'vsext_wt_CallStack',
           'vsPromptResultNo', 'vsWindowTypeToolWindow',
           'vsext_su_EMPTY_ENVIRONMENT', 'FontsAndColorsItems',
           'vsFontCharSetTurkish', 'CodeFunction',
           'vsWindowTypeBrowser', 'vsTaskListColumnDescription',
           'vsBuildState', 'vsFontCharSetMac', 'FileCodeModel',
           'vsTaskListColumnLine', 'vsInsertFlagsContainNewText',
           'dsMatchForward', 'Thread', 'Programs',
           'vsConfigurationTypeProjectItem',
           'vsext_wt_PropertyWindow', '_WindowEventsRoot',
           'vsSaveChangesNo', 'ToolBoxTab', 'UIHierarchyItems',
           'vsDisplay', 'vsCMElementIncludeStmt',
           'vsWindowTypeSolutionExplorer', 'vsTaskListColumnGlyph',
           'vsWindowTypePreview', 'vsWindowTypeThreads',
           'vsWindowKindMacroExplorer', 'wizardResultBackOut',
           '_EnvironmentGeneral', 'vsViewKindDesigner',
           'CodeDelegate', '_ProjectItemsEvents',
           'vsPaneShowCentered', 'Find', 'dbgExecutionActionStepInto',
           'vsFindOptionsFromStart', 'Documents', 'dsMatchFromStart',
           'CodeModel', 'vsWindowTypeColorPalette', 'vsSaveStatus',
           'dbgEventReason', 'vsStatusAnimationBuild',
           'vsCMPrototypeType', 'dbgExecutionActionStepOut',
           '_DebuggerEvents', 'vsWindowTypeOutput',
           'vsWhitespaceOptionsVertical',
           'vsCommandExecOptionDoDefault', 'DsGoToLineOptions',
           'vsCMElementFunction', 'ToolBox', 'vsFilterProperties',
           'vsWindowKindObjectBrowser', 'vsFindResultFound',
           'vsFindActionFindAll', 'vsFontCharSetSymbol',
           'vsCommandBarTypeToolbar', 'IVsTextEditFonts', 'Windows',
           'vsext_vk_Code', 'Configuration', 'Projects',
           'IFilterProperties', 'vsWindowKindDocumentOutline',
           'vsCMElementIDLCoClass', 'vsCMElementModule',
           'vsFindOptionsBackwards', 'Solution', 'Command',
           'vsCMElement', 'Property', 'vsSmartFormatOptionsBlock',
           'vsContextMacroRecording', 'vsCMFunctionShared',
           'RESULT_Success', 'TaskItem', 'vsext_fontcs_TURKISH',
           'LONG_PTR', 'vsext_wk_WatchWindow', 'vsStartUp',
           'dbgEventReasonExceptionThrown', 'vsSaveChangesYes',
           'vsEPReplaceTextKeepMarkers', 'vsext_wt_TaskList',
           'vsCMFunctionOther', 'ConfigurationManager',
           'vsTaskListColumn', 'TextWindow', 'vsCMTypeRefDouble',
           'vsCMPartBodyWithDelimiter', 'ProjectItem',
           'vsext_wk_SProjectWindow', 'vsWindowTypeRunningDocuments',
           'vsFindOptionsSearchSubfolders', 'vsext_wk_ThreadWindow',
           'vsNavigateBrowserNewWindow', 'vsTaskIconShortcut',
           'vsBuildActionClean', 'vsSaveSucceeded',
           '_EnvironmentDocuments',
           'vsFindTargetCurrentDocumentSelection', 'Commands',
           'dbgEventReasonStep', 'vsBuildKindProject',
           'vsCommandStatus', 'vsext_WindowState', 'vsext_wt_Watch',
           'OutputWindow', 'vsBrowserViewSourceSource',
           'vsContextAttributeLookup', 'vsWindowTypeLocals',
           'vsCommandExecOptionPromptUser', 'vsDocumentKindText',
           'vsCMElementVariable', 'vsWindowTypeAutos',
           'vsTaskIconSquiggle', 'vsGoToLineOptions',
           'OutputWindowPane', 'dbgBreakpointLocationType',
           'vsCMFunctionDestructor', 'vsext_wk_Toolbox',
           'vsext_fontcs_OEM', 'dbgExecutionActionGo',
           'vsNavigateOptionsNewWindow', 'vsSelectionModeBox',
           'vsFindResults2', 'dbgHitCountTypeGreaterOrEqual',
           'DebuggerEvents', 'vsInsertFlagsCollapseToStart',
           'vsCMTypeRefBool', 'vsFindResultPending',
           'SelectionEvents', 'dsFortran_Fixed',
           'vsUISelectionTypeSelect', 'vsWindowKindSolutionExplorer',
           'vsTaskListColumnPriority', 'vsCMFunctionVirtual',
           'vsContextDesignMode', 'vsFindOptionsWildcards',
           'OutputGroups', 'TextSelection', 'vsext_wt_Preview',
           'vsIndentStyleSmart', 'vsCommandStatusLatched',
           'vsCMAccessProject', 'IExtenderProviderUnk',
           'vsWindowKindCallStack', 'dbgEventReasonEndProgram',
           '_CommandEvents', 'vsCMPrototypeParamDefaultValues',
           'vsCMPartWholeWithAttributes', 'vsext_fontcs_SYMBOL',
           'vsWindowKindFindReplace', 'dsCPP', 'vsWindowTypeToolbox',
           'vsMovementOptionsMove', 'vsFontCharSetRussian',
           'vsFindPatternSyntax', 'vsext_wt_DocumentOutline',
           'vsPromptResultYes', 'vsIndentStyleNone',
           'vsFontCharSetChineseBig5', 'vsViewKindCode',
           'vsWindowTypeFindReplace', 'vsCATIDGenericProject',
           'vsFontCharSetArabic', 'CodeStruct', 'vsFindAction',
           'vsBrowserViewSource', 'CodeProperty',
           'vsWindowTypeTaskList', 'vsFindResultReplaceAndFound',
           'vsWindowTypeProperties', 'vsToolBoxItemFormat',
           'vsProjectItemKindPhysicalFile', 'vsCMTypeRefCodeType',
           'vsMovementOptions', 'vsPromptResult']
from comtypes import _check_version; _check_version('501')
