# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:06:53) [MSC v.1600 64 bit (AMD64)]
# From type library '{80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2}'
# On Wed Jun  5 20:58:11 2013
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

class constants:
	vsCMLanguageCSharp            ='{B5E9BD34-6D3E-4B5D-925E-8A43B79820B4}' # from enum CodeModelLanguageConstants
	vsCMLanguageIDL               ='{B5E9BD35-6D3E-4B5D-925E-8A43B79820B4}' # from enum CodeModelLanguageConstants
	vsCMLanguageMC                ='{B5E9BD36-6D3E-4B5D-925E-8A43B79820B4}' # from enum CodeModelLanguageConstants
	vsCMLanguageVB                ='{B5E9BD33-6D3E-4B5D-925E-8A43B79820B4}' # from enum CodeModelLanguageConstants
	vsCMLanguageVC                ='{B5E9BD32-6D3E-4B5D-925E-8A43B79820B4}' # from enum CodeModelLanguageConstants
	dsCPP                         ='C/C++'    # from enum Constants
	dsFortran_Fixed               ='Fortran Fixed' # from enum Constants
	dsFortran_Free                ='Fortran Free' # from enum Constants
	dsHTML_IE3                    ='HTML - IE 3.0' # from enum Constants
	dsHTML_RFC1866                ='HTML 2.0 (RFC 1866)' # from enum Constants
	dsIDL                         ='ODL/IDL'  # from enum Constants
	dsJava                        ='Java'     # from enum Constants
	dsVBSMacro                    ='VBS Macro' # from enum Constants
	vsAddInCmdGroup               ='{1E58696E-C90F-11D2-AAB2-00C04F688DDE}' # from enum Constants
	vsCATIDDocument               ='{610d4611-d0d5-11d2-8599-006097c68e81}' # from enum Constants
	vsCATIDGenericProject         ='{610d4616-d0d5-11d2-8599-006097c68e81}' # from enum Constants
	vsCATIDMiscFilesProject       ='{610d4612-d0d5-11d2-8599-006097c68e81}' # from enum Constants
	vsCATIDMiscFilesProjectItem   ='{610d4613-d0d5-11d2-8599-006097c68e81}' # from enum Constants
	vsCATIDSolution               ='{52AEFF70-BBD8-11d2-8598-006097C68E81}' # from enum Constants
	vsCATIDSolutionBrowseObject   ='{A2392464-7C22-11d3-BDCA-00C04F688E50}' # from enum Constants
	vsContextDebugging            ='{ADFC4E61-0397-11D1-9F4E-00A0C911004F}' # from enum Constants
	vsContextDesignMode           ='{ADFC4E63-0397-11D1-9F4E-00A0C911004F}' # from enum Constants
	vsContextEmptySolution        ='{ADFC4E65-0397-11D1-9F4E-00A0C911004F}' # from enum Constants
	vsContextFullScreenMode       ='{ADFC4E62-0397-11D1-9F4E-00A0C911004F}' # from enum Constants
	vsContextMacroRecording       ='{04BBF6A5-4697-11D2-890E-0060083196C6}' # from enum Constants
	vsContextMacroRecordingToolbar='{85A70471-270A-11D2-88F9-0060083196C6}' # from enum Constants
	vsContextNoSolution           ='{ADFC4E64-0397-11D1-9F4E-00A0C911004F}' # from enum Constants
	vsContextSolutionBuilding     ='{ADFC4E60-0397-11D1-9F4E-00A0C911004F}' # from enum Constants
	vsContextSolutionHasMultipleProjects='{93694FA0-0397-11D1-9F4E-00A0C911004F}' # from enum Constants
	vsContextSolutionHasSingleProject='{ADFC4E66-0397-11D1-9F4E-00A0C911004F}' # from enum Constants
	vsDocumentKindBinary          ='{25834150-CD7E-11D0-92DF-00A0C9138C45}' # from enum Constants
	vsDocumentKindHTML            ='{C76D83F8-A489-11D0-8195-00A0C91BBEE3}' # from enum Constants
	vsDocumentKindResource        ='{00000000-0000-0000-0000-000000000000}' # from enum Constants
	vsDocumentKindText            ='{8E7B96A8-E33D-11D0-A6D5-00C04FB67F6A}' # from enum Constants
	vsMiscFilesProjectUniqueName  ='<MiscFiles>' # from enum Constants
	vsProjectItemKindMisc         ='{66A2671F-8FB5-11D2-AA7E-00C04F688DDE}' # from enum Constants
	vsProjectItemKindPhysicalFile ='{6BB5F8EE-4483-11D3-8BCF-00C04F8EC28C}' # from enum Constants
	vsProjectItemKindPhysicalFolder='{6BB5F8EF-4483-11D3-8BCF-00C04F8EC28C}' # from enum Constants
	vsProjectItemKindSolutionItems='{66A26722-8FB5-11D2-AA7E-00C04F688DDE}' # from enum Constants
	vsProjectItemKindSubProject   ='{EA6618E8-6E24-4528-94BE-6889FE16485C}' # from enum Constants
	vsProjectItemKindVirtualFolder='{6BB5F8F0-4483-11D3-8BCF-00C04F8EC28C}' # from enum Constants
	vsProjectItemsKindMisc        ='{66A2671E-8FB5-11D2-AA7E-00C04F688DDE}' # from enum Constants
	vsProjectItemsKindSolutionItems='{66A26721-8FB5-11D2-AA7E-00C04F688DDE}' # from enum Constants
	vsProjectKindMisc             ='{66A2671D-8FB5-11D2-AA7E-00C04F688DDE}' # from enum Constants
	vsProjectKindSolutionItems    ='{66A26720-8FB5-11D2-AA7E-00C04F688DDE}' # from enum Constants
	vsProjectKindUnmodeled        ='{67294A52-A4F0-11D2-AA88-00C04F688DDE}' # from enum Constants
	vsProjectsKindSolution        ='{96410B9F-3542-4A14-877F-BC7227B51D3B}' # from enum Constants
	vsSolutionItemsProjectUniqueName='<SolnItems>' # from enum Constants
	vsViewKindAny                 ='{FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF}' # from enum Constants
	vsViewKindCode                ='{7651A701-06E5-11D1-8EBD-00A0C90F26EA}' # from enum Constants
	vsViewKindDebugging           ='{7651A700-06E5-11D1-8EBD-00A0C90F26EA}' # from enum Constants
	vsViewKindDesigner            ='{7651A702-06E5-11D1-8EBD-00A0C90F26EA}' # from enum Constants
	vsViewKindPrimary             ='{00000000-0000-0000-0000-000000000000}' # from enum Constants
	vsViewKindTextView            ='{7651A703-06E5-11D1-8EBD-00A0C90F26EA}' # from enum Constants
	vsWindowKindAutoLocals        ='{F2E84780-2AF1-11D1-A7FA-00A0C9110051}' # from enum Constants
	vsWindowKindCallStack         ='{0504FF91-9D61-11D0-A794-00A0C9110051}' # from enum Constants
	vsWindowKindClassView         ='{C9C0AE26-AA77-11D2-B3F0-0000F87570EE}' # from enum Constants
	vsWindowKindCommandWindow     ='{28836128-FC2C-11D2-A433-00C04F72D18A}' # from enum Constants
	vsWindowKindDocumentOutline   ='{25F7E850-FFA1-11D0-B63F-00A0C922E851}' # from enum Constants
	vsWindowKindDynamicHelp       ='{66DBA47C-61DF-11D2-AA79-00C04F990343}' # from enum Constants
	vsWindowKindFindReplace       ='{CF2DDC32-8CAD-11D2-9302-005345000000}' # from enum Constants
	vsWindowKindFindResults1      ='{0F887920-C2B6-11D2-9375-0080C747D9A0}' # from enum Constants
	vsWindowKindFindResults2      ='{0F887921-C2B6-11D2-9375-0080C747D9A0}' # from enum Constants
	vsWindowKindFindSymbol        ='{53024D34-0EF5-11D3-87E0-00C04F7971A5}' # from enum Constants
	vsWindowKindFindSymbolResults ='{68487888-204A-11D3-87EB-00C04F7971A5}' # from enum Constants
	vsWindowKindLinkedWindowFrame ='{9DDABE99-1D02-11D3-89A1-00C04F688DDE}' # from enum Constants
	vsWindowKindLocals            ='{4A18F9D0-B838-11D0-93EB-00A0C90F2734}' # from enum Constants
	vsWindowKindMacroExplorer     ='{07CD18B4-3BA1-11D2-890A-0060083196C6}' # from enum Constants
	vsWindowKindMainWindow        ='{9DDABE98-1D02-11D3-89A1-00C04F688DDE}' # from enum Constants
	vsWindowKindObjectBrowser     ='{269A02DC-6AF8-11D3-BDC4-00C04F688E50}' # from enum Constants
	vsWindowKindOutput            ='{34E76E81-EE4A-11D0-AE2E-00A0C90FFFC3}' # from enum Constants
	vsWindowKindProperties        ='{EEFA5220-E298-11D0-8F78-00A0C9110057}' # from enum Constants
	vsWindowKindResourceView      ='{2D7728C2-DE0A-45b5-99AA-89B609DFDE73}' # from enum Constants
	vsWindowKindServerExplorer    ='{74946827-37A0-11D2-A273-00C04F8EF4FF}' # from enum Constants
	vsWindowKindSolutionExplorer  ='{3AE79031-E1BC-11D0-8F78-00A0C9110057}' # from enum Constants
	vsWindowKindTaskList          ='{4A9B7E51-AA16-11D0-A8C5-00A0C921A4D2}' # from enum Constants
	vsWindowKindThread            ='{E62CE6A0-B439-11D0-A79D-00A0C9110051}' # from enum Constants
	vsWindowKindToolbox           ='{B1E99781-AB81-11D0-B683-00AA00A3EE26}' # from enum Constants
	vsWindowKindWatch             ='{90243340-BD7A-11D0-93EF-00A0C90F2734}' # from enum Constants
	vsWindowKindWebBrowser        ='{E8B06F52-6D01-11D2-AA7D-00C04F990343}' # from enum Constants
	vsWizardAddItem               ='{0F90E1D1-4999-11D1-B6D1-00A0C90F2744}' # from enum Constants
	vsWizardAddSubProject         ='{0F90E1D2-4999-11D1-B6D1-00A0C90F2744}' # from enum Constants
	vsWizardNewProject            ='{0F90E1D0-4999-11D1-B6D1-00A0C90F2744}' # from enum Constants
	vsext_GUID_AddItemWizard      ='{0F90E1D1-4999-11D1-B6D1-00A0C90F2744}' # from enum Constants
	vsext_GUID_NewProjectWizard   ='{0F90E1D0-4999-11D1-B6D1-00A0C90F2744}' # from enum Constants
	vsext_vk_Code                 ='{7651A701-06E5-11D1-8EBD-00A0C90F26EA}' # from enum Constants
	vsext_vk_Debugging            ='{7651A700-06E5-11D1-8EBD-00A0C90F26EA}' # from enum Constants
	vsext_vk_Designer             ='{7651A702-06E5-11D1-8EBD-00A0C90F26EA}' # from enum Constants
	vsext_vk_Primary              ='{00000000-0000-0000-0000-000000000000}' # from enum Constants
	vsext_vk_TextView             ='{7651A703-06E5-11D1-8EBD-00A0C90F26EA}' # from enum Constants
	vsext_wk_AutoLocalsWindow     ='{F2E84780-2AF1-11D1-A7FA-00A0C9110051}' # from enum Constants
	vsext_wk_CallStackWindow      ='{0504FF91-9D61-11D0-A794-00A0C9110051}' # from enum Constants
	vsext_wk_ClassView            ='{C9C0AE26-AA77-11D2-B3F0-0000F87570EE}' # from enum Constants
	vsext_wk_ContextWindow        ='{66DBA47C-61DF-11D2-AA79-00C04F990343}' # from enum Constants
	vsext_wk_ImmedWindow          ='{98731960-965C-11D0-A78F-00A0C9110051}' # from enum Constants
	vsext_wk_LocalsWindow         ='{4A18F9D0-B838-11D0-93EB-00A0C90F2734}' # from enum Constants
	vsext_wk_ObjectBrowser        ='{269A02DC-6AF8-11D3-BDC4-00C04F688E50}' # from enum Constants
	vsext_wk_OutputWindow         ='{34E76E81-EE4A-11D0-AE2E-00A0C90FFFC3}' # from enum Constants
	vsext_wk_PropertyBrowser      ='{EEFA5220-E298-11D0-8F78-00A0C9110057}' # from enum Constants
	vsext_wk_SProjectWindow       ='{3AE79031-E1BC-11D0-8F78-00A0C9110057}' # from enum Constants
	vsext_wk_TaskList             ='{4A9B7E51-AA16-11D0-A8C5-00A0C921A4D2}' # from enum Constants
	vsext_wk_ThreadWindow         ='{E62CE6A0-B439-11D0-A79D-00A0C9110051}' # from enum Constants
	vsext_wk_Toolbox              ='{B1E99781-AB81-11D0-B683-00AA00A3EE26}' # from enum Constants
	vsext_wk_WatchWindow          ='{90243340-BD7A-11D0-93EF-00A0C90F2734}' # from enum Constants
	dsCapitalize                  =3          # from enum DsCaseOptions
	dsLowercase                   =1          # from enum DsCaseOptions
	dsUppercase                   =2          # from enum DsCaseOptions
	dsLastLine                    =-1         # from enum DsGoToLineOptions
	dsExtend                      =1          # from enum DsMovementOptions
	dsMove                        =0          # from enum DsMovementOptions
	dsSaveChangesNo               =2          # from enum DsSaveChanges
	dsSaveChangesPrompt           =3          # from enum DsSaveChanges
	dsSaveChangesYes              =1          # from enum DsSaveChanges
	dsFirstColumn                 =0          # from enum DsStartOfLineOptions
	dsFirstText                   =1          # from enum DsStartOfLineOptions
	dsMatchBackward               =128        # from enum DsTextSearchOptions
	dsMatchCase                   =4          # from enum DsTextSearchOptions
	dsMatchForward                =0          # from enum DsTextSearchOptions
	dsMatchFromStart              =256        # from enum DsTextSearchOptions
	dsMatchNoRegExp               =0          # from enum DsTextSearchOptions
	dsMatchRegExp                 =8          # from enum DsTextSearchOptions
	dsMatchRegExpB                =16         # from enum DsTextSearchOptions
	dsMatchRegExpCur              =64         # from enum DsTextSearchOptions
	dsMatchRegExpE                =32         # from enum DsTextSearchOptions
	dsMatchWord                   =2          # from enum DsTextSearchOptions
	dsHorizontal                  =0          # from enum DsWhitespaceOptions
	dsVertical                    =1          # from enum DsWhitespaceOptions
	RESULT_Cancel                 =1          # from enum VSEXECRESULT
	RESULT_Failure                =0          # from enum VSEXECRESULT
	RESULT_Success                =-1         # from enum VSEXECRESULT
	vsIndentStyleDefault          =1          # from enum _vsIndentStyle
	vsIndentStyleNone             =0          # from enum _vsIndentStyle
	vsIndentStyleSmart            =2          # from enum _vsIndentStyle
	dbgBreakpointConditionTypeWhenChanged=2          # from enum dbgBreakpointConditionType
	dbgBreakpointConditionTypeWhenTrue=1          # from enum dbgBreakpointConditionType
	dbgBreakpointLocationTypeAddress=5          # from enum dbgBreakpointLocationType
	dbgBreakpointLocationTypeData =4          # from enum dbgBreakpointLocationType
	dbgBreakpointLocationTypeFile =3          # from enum dbgBreakpointLocationType
	dbgBreakpointLocationTypeFunction=2          # from enum dbgBreakpointLocationType
	dbgBreakpointLocationTypeNone =1          # from enum dbgBreakpointLocationType
	dbgBreakpointTypeBound        =2          # from enum dbgBreakpointType
	dbgBreakpointTypePending      =1          # from enum dbgBreakpointType
	dbgBreakMode                  =2          # from enum dbgDebugMode
	dbgDesignMode                 =1          # from enum dbgDebugMode
	dbgRunMode                    =3          # from enum dbgDebugMode
	dbgEventReasonAttachProgram   =3          # from enum dbgEventReason
	dbgEventReasonBreakpoint      =9          # from enum dbgEventReason
	dbgEventReasonContextSwitch   =13         # from enum dbgEventReason
	dbgEventReasonDetachProgram   =4          # from enum dbgEventReason
	dbgEventReasonEndProgram      =6          # from enum dbgEventReason
	dbgEventReasonExceptionNotHandled=11         # from enum dbgEventReason
	dbgEventReasonExceptionThrown =10         # from enum dbgEventReason
	dbgEventReasonGo              =2          # from enum dbgEventReason
	dbgEventReasonLaunchProgram   =5          # from enum dbgEventReason
	dbgEventReasonNone            =1          # from enum dbgEventReason
	dbgEventReasonStep            =8          # from enum dbgEventReason
	dbgEventReasonStopDebugging   =7          # from enum dbgEventReason
	dbgEventReasonUserBreak       =12         # from enum dbgEventReason
	dbgExceptionActionBreak       =3          # from enum dbgExceptionAction
	dbgExceptionActionContinue    =4          # from enum dbgExceptionAction
	dbgExceptionActionDefault     =1          # from enum dbgExceptionAction
	dbgExceptionActionIgnore      =2          # from enum dbgExceptionAction
	dbgExecutionActionDefault     =1          # from enum dbgExecutionAction
	dbgExecutionActionGo          =2          # from enum dbgExecutionAction
	dbgExecutionActionRunToCursor =7          # from enum dbgExecutionAction
	dbgExecutionActionStepInto    =4          # from enum dbgExecutionAction
	dbgExecutionActionStepOut     =5          # from enum dbgExecutionAction
	dbgExecutionActionStepOver    =6          # from enum dbgExecutionAction
	dbgExecutionActionStopDebugging=3          # from enum dbgExecutionAction
	dbgHitCountTypeEqual          =2          # from enum dbgHitCountType
	dbgHitCountTypeGreaterOrEqual =3          # from enum dbgHitCountType
	dbgHitCountTypeMultiple       =4          # from enum dbgHitCountType
	dbgHitCountTypeNone           =1          # from enum dbgHitCountType
	dsSaveCancelled               =2          # from enum dsSaveStatus
	dsSaveSucceeded               =1          # from enum dsSaveStatus
	vsBrowserViewSourceDesign     =2          # from enum vsBrowserViewSource
	vsBrowserViewSourceExternal   =3          # from enum vsBrowserViewSource
	vsBrowserViewSourceSource     =1          # from enum vsBrowserViewSource
	vsBuildActionBuild            =1          # from enum vsBuildAction
	vsBuildActionClean            =3          # from enum vsBuildAction
	vsBuildActionDeploy           =4          # from enum vsBuildAction
	vsBuildActionRebuildAll       =2          # from enum vsBuildAction
	vsBuildKindProject            =1          # from enum vsBuildKind
	vsBuildKindProjectItem        =2          # from enum vsBuildKind
	vsBuildKindSolution           =0          # from enum vsBuildKind
	vsBuildScopeBatch             =2          # from enum vsBuildScope
	vsBuildScopeProject           =3          # from enum vsBuildScope
	vsBuildScopeSolution          =1          # from enum vsBuildScope
	vsBuildStateDone              =3          # from enum vsBuildState
	vsBuildStateInProgress        =2          # from enum vsBuildState
	vsBuildStateNotStarted        =1          # from enum vsBuildState
	vsCMAccessAssemblyOrFamily    =64         # from enum vsCMAccess
	vsCMAccessDefault             =32         # from enum vsCMAccess
	vsCMAccessPrivate             =2          # from enum vsCMAccess
	vsCMAccessProject             =4          # from enum vsCMAccess
	vsCMAccessProjectOrProtected  =12         # from enum vsCMAccess
	vsCMAccessProtected           =8          # from enum vsCMAccess
	vsCMAccessPublic              =1          # from enum vsCMAccess
	vsCMAccessWithEvents          =128        # from enum vsCMAccess
	vsCMElementAssignmentStmt     =16         # from enum vsCMElement
	vsCMElementAttribute          =7          # from enum vsCMElement
	vsCMElementClass              =1          # from enum vsCMElement
	vsCMElementDeclareDecl        =24         # from enum vsCMElement
	vsCMElementDefineStmt         =25         # from enum vsCMElement
	vsCMElementDelegate           =9          # from enum vsCMElement
	vsCMElementEnum               =10         # from enum vsCMElement
	vsCMElementEvent              =38         # from enum vsCMElement
	vsCMElementEventsDeclaration  =22         # from enum vsCMElement
	vsCMElementFunction           =2          # from enum vsCMElement
	vsCMElementFunctionInvokeStmt =14         # from enum vsCMElement
	vsCMElementIDLCoClass         =33         # from enum vsCMElement
	vsCMElementIDLImport          =31         # from enum vsCMElement
	vsCMElementIDLImportLib       =32         # from enum vsCMElement
	vsCMElementIDLLibrary         =34         # from enum vsCMElement
	vsCMElementImplementsStmt     =18         # from enum vsCMElement
	vsCMElementImportStmt         =35         # from enum vsCMElement
	vsCMElementIncludeStmt        =27         # from enum vsCMElement
	vsCMElementInheritsStmt       =17         # from enum vsCMElement
	vsCMElementInterface          =8          # from enum vsCMElement
	vsCMElementLocalDeclStmt      =13         # from enum vsCMElement
	vsCMElementMacro              =29         # from enum vsCMElement
	vsCMElementMap                =30         # from enum vsCMElement
	vsCMElementMapEntry           =36         # from enum vsCMElement
	vsCMElementModule             =39         # from enum vsCMElement
	vsCMElementNamespace          =5          # from enum vsCMElement
	vsCMElementOptionStmt         =19         # from enum vsCMElement
	vsCMElementOther              =0          # from enum vsCMElement
	vsCMElementParameter          =6          # from enum vsCMElement
	vsCMElementProperty           =4          # from enum vsCMElement
	vsCMElementPropertySetStmt    =15         # from enum vsCMElement
	vsCMElementStruct             =11         # from enum vsCMElement
	vsCMElementTypeDef            =26         # from enum vsCMElement
	vsCMElementUDTDecl            =23         # from enum vsCMElement
	vsCMElementUnion              =12         # from enum vsCMElement
	vsCMElementUsingStmt          =28         # from enum vsCMElement
	vsCMElementVBAttributeGroup   =21         # from enum vsCMElement
	vsCMElementVBAttributeStmt    =20         # from enum vsCMElement
	vsCMElementVCBase             =37         # from enum vsCMElement
	vsCMElementVariable           =3          # from enum vsCMElement
	vsCMFunctionComMethod         =65536      # from enum vsCMFunction
	vsCMFunctionConstant          =8192       # from enum vsCMFunction
	vsCMFunctionConstructor       =1          # from enum vsCMFunction
	vsCMFunctionDestructor        =512        # from enum vsCMFunction
	vsCMFunctionFunction          =128        # from enum vsCMFunction
	vsCMFunctionInline            =32768      # from enum vsCMFunction
	vsCMFunctionOperator          =1024       # from enum vsCMFunction
	vsCMFunctionOther             =0          # from enum vsCMFunction
	vsCMFunctionPropertyAssign    =32         # from enum vsCMFunction
	vsCMFunctionPropertyGet       =2          # from enum vsCMFunction
	vsCMFunctionPropertyLet       =4          # from enum vsCMFunction
	vsCMFunctionPropertySet       =8          # from enum vsCMFunction
	vsCMFunctionPure              =4096       # from enum vsCMFunction
	vsCMFunctionPutRef            =16         # from enum vsCMFunction
	vsCMFunctionShared            =16384      # from enum vsCMFunction
	vsCMFunctionSub               =64         # from enum vsCMFunction
	vsCMFunctionTopLevel          =256        # from enum vsCMFunction
	vsCMFunctionVirtual           =2048       # from enum vsCMFunction
	vsCMInfoLocationExternal      =2          # from enum vsCMInfoLocation
	vsCMInfoLocationNone          =4          # from enum vsCMInfoLocation
	vsCMInfoLocationProject       =1          # from enum vsCMInfoLocation
	vsCMInfoLocationVirtual       =8          # from enum vsCMInfoLocation
	vsCMPartAttributes            =2          # from enum vsCMPart
	vsCMPartAttributesWithDelimiter=68         # from enum vsCMPart
	vsCMPartBody                  =16         # from enum vsCMPart
	vsCMPartBodyWithDelimiter     =80         # from enum vsCMPart
	vsCMPartHeader                =4          # from enum vsCMPart
	vsCMPartHeaderWithAttributes  =6          # from enum vsCMPart
	vsCMPartName                  =1          # from enum vsCMPart
	vsCMPartNavigate              =32         # from enum vsCMPart
	vsCMPartWhole                 =8          # from enum vsCMPart
	vsCMPartWholeWithAttributes   =10         # from enum vsCMPart
	vsCMPrototypeClassName        =4          # from enum vsCMPrototype
	vsCMPrototypeFullname         =1          # from enum vsCMPrototype
	vsCMPrototypeInitExpression   =256        # from enum vsCMPrototype
	vsCMPrototypeNoName           =2          # from enum vsCMPrototype
	vsCMPrototypeParamDefaultValues=32         # from enum vsCMPrototype
	vsCMPrototypeParamNames       =16         # from enum vsCMPrototype
	vsCMPrototypeParamTypes       =8          # from enum vsCMPrototype
	vsCMPrototypeType             =128        # from enum vsCMPrototype
	vsCMPrototypeUniqueSignature  =64         # from enum vsCMPrototype
	vsCMTypeRefArray              =2          # from enum vsCMTypeRef
	vsCMTypeRefBool               =15         # from enum vsCMTypeRef
	vsCMTypeRefByte               =7          # from enum vsCMTypeRef
	vsCMTypeRefChar               =8          # from enum vsCMTypeRef
	vsCMTypeRefCodeType           =1          # from enum vsCMTypeRef
	vsCMTypeRefDecimal            =14         # from enum vsCMTypeRef
	vsCMTypeRefDouble             =13         # from enum vsCMTypeRef
	vsCMTypeRefFloat              =12         # from enum vsCMTypeRef
	vsCMTypeRefInt                =10         # from enum vsCMTypeRef
	vsCMTypeRefLong               =11         # from enum vsCMTypeRef
	vsCMTypeRefObject             =6          # from enum vsCMTypeRef
	vsCMTypeRefOther              =0          # from enum vsCMTypeRef
	vsCMTypeRefPointer            =4          # from enum vsCMTypeRef
	vsCMTypeRefShort              =9          # from enum vsCMTypeRef
	vsCMTypeRefString             =5          # from enum vsCMTypeRef
	vsCMTypeRefVariant            =16         # from enum vsCMTypeRef
	vsCMTypeRefVoid               =3          # from enum vsCMTypeRef
	vsCaseOptionsCapitalize       =3          # from enum vsCaseOptions
	vsCaseOptionsLowercase        =1          # from enum vsCaseOptions
	vsCaseOptionsUppercase        =2          # from enum vsCaseOptions
	vsCommandBarTypeMenu          =24         # from enum vsCommandBarType
	vsCommandBarTypePopup         =10         # from enum vsCommandBarType
	vsCommandBarTypeToolbar       =23         # from enum vsCommandBarType
	vsCommandDisabledFlagsEnabled =0          # from enum vsCommandDisabledFlags
	vsCommandDisabledFlagsGrey    =16         # from enum vsCommandDisabledFlags
	vsCommandDisabledFlagsHidden  =32         # from enum vsCommandDisabledFlags
	vsCommandExecOptionDoDefault  =0          # from enum vsCommandExecOption
	vsCommandExecOptionDoPromptUser=2          # from enum vsCommandExecOption
	vsCommandExecOptionPromptUser =1          # from enum vsCommandExecOption
	vsCommandExecOptionShowHelp   =3          # from enum vsCommandExecOption
	vsCommandStatusEnabled        =2          # from enum vsCommandStatus
	vsCommandStatusInvisible      =16         # from enum vsCommandStatus
	vsCommandStatusLatched        =4          # from enum vsCommandStatus
	vsCommandStatusNinched        =8          # from enum vsCommandStatus
	vsCommandStatusSupported      =1          # from enum vsCommandStatus
	vsCommandStatusUnsupported    =0          # from enum vsCommandStatus
	vsCommandStatusTextWantedName =1          # from enum vsCommandStatusTextWanted
	vsCommandStatusTextWantedNone =0          # from enum vsCommandStatusTextWanted
	vsCommandStatusTextWantedStatus=2          # from enum vsCommandStatusTextWanted
	vsConfigurationTypeProject    =1          # from enum vsConfigurationType
	vsConfigurationTypeProjectItem=2          # from enum vsConfigurationType
	vsContextAttributeFilter      =1          # from enum vsContextAttributeType
	vsContextAttributeLookup      =2          # from enum vsContextAttributeType
	vsContextAttributeLookupF1    =3          # from enum vsContextAttributeType
	vsContextAttributesGlobal     =1          # from enum vsContextAttributes
	vsContextAttributesHighPriority=3          # from enum vsContextAttributes
	vsContextAttributesWindow     =2          # from enum vsContextAttributes
	vsDisplayMDI                  =1          # from enum vsDisplay
	vsDisplayMDITabs              =2          # from enum vsDisplay
	vsEPReplaceTextAutoformat     =8          # from enum vsEPReplaceTextOptions
	vsEPReplaceTextKeepMarkers    =1          # from enum vsEPReplaceTextOptions
	vsEPReplaceTextNormalizeNewlines=2          # from enum vsEPReplaceTextOptions
	vsEPReplaceTextTabsSpaces     =4          # from enum vsEPReplaceTextOptions
	vsFilterPropertiesAll         =1          # from enum vsFilterProperties
	vsFilterPropertiesNone        =0          # from enum vsFilterProperties
	vsFilterPropertiesSet         =2          # from enum vsFilterProperties
	vsFindActionBookmarkAll       =5          # from enum vsFindAction
	vsFindActionFind              =1          # from enum vsFindAction
	vsFindActionFindAll           =2          # from enum vsFindAction
	vsFindActionReplace           =3          # from enum vsFindAction
	vsFindActionReplaceAll        =4          # from enum vsFindAction
	vsFindOptionsBackwards        =128        # from enum vsFindOptions
	vsFindOptionsFromStart        =256        # from enum vsFindOptions
	vsFindOptionsKeepModifiedDocumentsOpen=8192       # from enum vsFindOptions
	vsFindOptionsMatchCase        =4          # from enum vsFindOptions
	vsFindOptionsMatchInHiddenText=512        # from enum vsFindOptions
	vsFindOptionsMatchWholeWord   =2          # from enum vsFindOptions
	vsFindOptionsNone             =0          # from enum vsFindOptions
	vsFindOptionsRegularExpression=8          # from enum vsFindOptions
	vsFindOptionsSearchSubfolders =4096       # from enum vsFindOptions
	vsFindOptionsWildcards        =1024       # from enum vsFindOptions
	vsFindPatternSyntaxLiteral    =0          # from enum vsFindPatternSyntax
	vsFindPatternSyntaxRegExpr    =1          # from enum vsFindPatternSyntax
	vsFindPatternSyntaxWildcards  =2          # from enum vsFindPatternSyntax
	vsFindResultError             =6          # from enum vsFindResult
	vsFindResultFound             =1          # from enum vsFindResult
	vsFindResultNotFound          =0          # from enum vsFindResult
	vsFindResultPending           =5          # from enum vsFindResult
	vsFindResultReplaceAndFound   =3          # from enum vsFindResult
	vsFindResultReplaceAndNotFound=2          # from enum vsFindResult
	vsFindResultReplaced          =4          # from enum vsFindResult
	vsFindResults1                =1          # from enum vsFindResultsLocation
	vsFindResults2                =2          # from enum vsFindResultsLocation
	vsFindResultsNone             =0          # from enum vsFindResultsLocation
	vsFindTargetCurrentDocument   =1          # from enum vsFindTarget
	vsFindTargetCurrentDocumentFunction=3          # from enum vsFindTarget
	vsFindTargetCurrentDocumentSelection=2          # from enum vsFindTarget
	vsFindTargetCurrentProject    =5          # from enum vsFindTarget
	vsFindTargetFiles             =7          # from enum vsFindTarget
	vsFindTargetOpenDocuments     =4          # from enum vsFindTarget
	vsFindTargetSolution          =6          # from enum vsFindTarget
	vsFontCharSetANSI             =0          # from enum vsFontCharSet
	vsFontCharSetArabic           =178        # from enum vsFontCharSet
	vsFontCharSetBaltic           =186        # from enum vsFontCharSet
	vsFontCharSetChineseBig5      =136        # from enum vsFontCharSet
	vsFontCharSetDefault          =1          # from enum vsFontCharSet
	vsFontCharSetEastEurope       =238        # from enum vsFontCharSet
	vsFontCharSetGB2312           =134        # from enum vsFontCharSet
	vsFontCharSetGreek            =161        # from enum vsFontCharSet
	vsFontCharSetHangeul          =129        # from enum vsFontCharSet
	vsFontCharSetHebrew           =177        # from enum vsFontCharSet
	vsFontCharSetJohab            =130        # from enum vsFontCharSet
	vsFontCharSetMac              =77         # from enum vsFontCharSet
	vsFontCharSetOEM              =255        # from enum vsFontCharSet
	vsFontCharSetRussian          =204        # from enum vsFontCharSet
	vsFontCharSetShiftJIS         =128        # from enum vsFontCharSet
	vsFontCharSetSymbol           =2          # from enum vsFontCharSet
	vsFontCharSetThai             =222        # from enum vsFontCharSet
	vsFontCharSetTurkish          =162        # from enum vsFontCharSet
	vsFontCharSetVietnamese       =163        # from enum vsFontCharSet
	vsGoToLineOptionsFirst        =-2         # from enum vsGoToLineOptions
	vsGoToLineOptionsLast         =-1         # from enum vsGoToLineOptions
	vsHTMLTabsDesign              =1          # from enum vsHTMLTabs
	vsHTMLTabsSource              =0          # from enum vsHTMLTabs
	vsIDEModeDebug                =2          # from enum vsIDEMode
	vsIDEModeDesign               =1          # from enum vsIDEMode
	vsInitializeModeReset         =1          # from enum vsInitializeMode
	vsInitializeModeStartup       =0          # from enum vsInitializeMode
	vsInsertFlagsCollapseToEnd    =1          # from enum vsInsertFlags
	vsInsertFlagsCollapseToStart  =2          # from enum vsInsertFlags
	vsInsertFlagsContainNewText   =4          # from enum vsInsertFlags
	vsInsertFlagsInsertAtEnd      =8          # from enum vsInsertFlags
	vsInsertFlagsInsertAtStart    =16         # from enum vsInsertFlags
	vsLinkedWindowTypeDocked      =0          # from enum vsLinkedWindowType
	vsLinkedWindowTypeHorizontal  =3          # from enum vsLinkedWindowType
	vsLinkedWindowTypeTabbed      =1          # from enum vsLinkedWindowType
	vsLinkedWindowTypeVertical    =2          # from enum vsLinkedWindowType
	vsMoveToColumnLineFirst       =0          # from enum vsMoveToColumnLine
	vsMoveToColumnLineLast        =1          # from enum vsMoveToColumnLine
	vsMovementOptionsExtend       =1          # from enum vsMovementOptions
	vsMovementOptionsMove         =0          # from enum vsMovementOptions
	vsNavigateBrowserDefault      =0          # from enum vsNavigateBrowser
	vsNavigateBrowserHelp         =1          # from enum vsNavigateBrowser
	vsNavigateBrowserNewWindow    =2          # from enum vsNavigateBrowser
	vsNavigateOptionsDefault      =0          # from enum vsNavigateOptions
	vsNavigateOptionsNewWindow    =1          # from enum vsNavigateOptions
	vsPaneShowAsIs                =2          # from enum vsPaneShowHow
	vsPaneShowCentered            =0          # from enum vsPaneShowHow
	vsPaneShowTop                 =1          # from enum vsPaneShowHow
	vsPromptResultCancelled       =3          # from enum vsPromptResult
	vsPromptResultNo              =2          # from enum vsPromptResult
	vsPromptResultYes             =1          # from enum vsPromptResult
	vsSaveChangesNo               =2          # from enum vsSaveChanges
	vsSaveChangesPrompt           =3          # from enum vsSaveChanges
	vsSaveChangesYes              =1          # from enum vsSaveChanges
	vsSaveCancelled               =2          # from enum vsSaveStatus
	vsSaveSucceeded               =1          # from enum vsSaveStatus
	vsSelectionModeBox            =1          # from enum vsSelectionMode
	vsSelectionModeStream         =0          # from enum vsSelectionMode
	vsSmartFormatOptionsBlock     =1          # from enum vsSmartFormatOptions
	vsSmartFormatOptionsNone      =0          # from enum vsSmartFormatOptions
	vsSmartFormatOptionsSmart     =2          # from enum vsSmartFormatOptions
	vsStartOfLineOptionsFirstColumn=0          # from enum vsStartOfLineOptions
	vsStartOfLineOptionsFirstText =1          # from enum vsStartOfLineOptions
	vsStartUpEmptyEnvironment     =4          # from enum vsStartUp
	vsStartUpLoadLastSolution     =1          # from enum vsStartUp
	vsStartUpNewProjectDialog     =3          # from enum vsStartUp
	vsStartUpOpenProjectDialog    =2          # from enum vsStartUp
	vsStartUpShowHomePage         =0          # from enum vsStartUp
	vsStatusAnimationBuild        =5          # from enum vsStatusAnimation
	vsStatusAnimationDeploy       =3          # from enum vsStatusAnimation
	vsStatusAnimationFind         =6          # from enum vsStatusAnimation
	vsStatusAnimationGeneral      =0          # from enum vsStatusAnimation
	vsStatusAnimationPrint        =1          # from enum vsStatusAnimation
	vsStatusAnimationSave         =2          # from enum vsStatusAnimation
	vsStatusAnimationSync         =4          # from enum vsStatusAnimation
	vsTaskCategoryBuildCompile    ='BuildCompile' # from enum vsTaskCategories
	vsTaskCategoryComment         ='Comment'  # from enum vsTaskCategories
	vsTaskCategoryHTML            ='HTML'     # from enum vsTaskCategories
	vsTaskCategoryMisc            ='Misc'     # from enum vsTaskCategories
	vsTaskCategoryShortcut        ='Shortcut' # from enum vsTaskCategories
	vsTaskCategoryUser            ='User'     # from enum vsTaskCategories
	vsTaskIconComment             =3          # from enum vsTaskIcon
	vsTaskIconCompile             =1          # from enum vsTaskIcon
	vsTaskIconNone                =0          # from enum vsTaskIcon
	vsTaskIconShortcut            =4          # from enum vsTaskIcon
	vsTaskIconSquiggle            =2          # from enum vsTaskIcon
	vsTaskIconUser                =5          # from enum vsTaskIcon
	vsTaskListColumnCheck         =4          # from enum vsTaskListColumn
	vsTaskListColumnDescription   =8          # from enum vsTaskListColumn
	vsTaskListColumnFile          =16         # from enum vsTaskListColumn
	vsTaskListColumnGlyph         =2          # from enum vsTaskListColumn
	vsTaskListColumnLine          =32         # from enum vsTaskListColumn
	vsTaskListColumnPriority      =1          # from enum vsTaskListColumn
	vsTaskPriorityHigh            =3          # from enum vsTaskPriority
	vsTaskPriorityLow             =1          # from enum vsTaskPriority
	vsTaskPriorityMedium          =2          # from enum vsTaskPriority
	vsTextChangedCaretMoved       =4          # from enum vsTextChanged
	vsTextChangedFindStarting     =32         # from enum vsTextChanged
	vsTextChangedMultiLine        =1          # from enum vsTextChanged
	vsTextChangedNewline          =16         # from enum vsTextChanged
	vsTextChangedReplaceAll       =8          # from enum vsTextChanged
	vsTextChangedSave             =2          # from enum vsTextChanged
	vsToolBoxItemFormatDotNETComponent=8          # from enum vsToolBoxItemFormat
	vsToolBoxItemFormatGUID       =4          # from enum vsToolBoxItemFormat
	vsToolBoxItemFormatHTML       =2          # from enum vsToolBoxItemFormat
	vsToolBoxItemFormatText       =1          # from enum vsToolBoxItemFormat
	vsUISelectionTypeExtend       =3          # from enum vsUISelectionType
	vsUISelectionTypeSelect       =1          # from enum vsUISelectionType
	vsUISelectionTypeSetCaret     =4          # from enum vsUISelectionType
	vsUISelectionTypeToggle       =2          # from enum vsUISelectionType
	vsWhitespaceOptionsHorizontal =0          # from enum vsWhitespaceOptions
	vsWhitespaceOptionsVertical   =1          # from enum vsWhitespaceOptions
	vsWindowStateMaximize         =2          # from enum vsWindowState
	vsWindowStateMinimize         =1          # from enum vsWindowState
	vsWindowStateNormal           =0          # from enum vsWindowState
	vsWindowTypeAutos             =19         # from enum vsWindowType
	vsWindowTypeBrowser           =2          # from enum vsWindowType
	vsWindowTypeCallStack         =20         # from enum vsWindowType
	vsWindowTypeCodeWindow        =0          # from enum vsWindowType
	vsWindowTypeColorPalette      =14         # from enum vsWindowType
	vsWindowTypeDesigner          =1          # from enum vsWindowType
	vsWindowTypeDocument          =16         # from enum vsWindowType
	vsWindowTypeDocumentOutline   =22         # from enum vsWindowType
	vsWindowTypeFind              =8          # from enum vsWindowType
	vsWindowTypeFindReplace       =9          # from enum vsWindowType
	vsWindowTypeImmediate         =5          # from enum vsWindowType
	vsWindowTypeLinkedWindowFrame =11         # from enum vsWindowType
	vsWindowTypeLocals            =4          # from enum vsWindowType
	vsWindowTypeMainWindow        =12         # from enum vsWindowType
	vsWindowTypeOutput            =17         # from enum vsWindowType
	vsWindowTypePreview           =13         # from enum vsWindowType
	vsWindowTypeProperties        =7          # from enum vsWindowType
	vsWindowTypeRunningDocuments  =23         # from enum vsWindowType
	vsWindowTypeSolutionExplorer  =6          # from enum vsWindowType
	vsWindowTypeTaskList          =18         # from enum vsWindowType
	vsWindowTypeThreads           =21         # from enum vsWindowType
	vsWindowTypeToolWindow        =15         # from enum vsWindowType
	vsWindowTypeToolbox           =10         # from enum vsWindowType
	vsWindowTypeWatch             =3          # from enum vsWindowType
	vsext_bld_CONFIRM_SAVE        =1          # from enum vsext_Build
	vsext_bld_NO_SAVE             =2          # from enum vsext_Build
	vsext_bld_SAVE_CHANGES        =0          # from enum vsext_Build
	vsext_dm_MDI                  =1          # from enum vsext_DisplayMode
	vsext_dm_SDI                  =0          # from enum vsext_DisplayMode
	vsext_fontcs_ANSI             =0          # from enum vsext_FontCharSet
	vsext_fontcs_ARABIC           =178        # from enum vsext_FontCharSet
	vsext_fontcs_BALTIC           =186        # from enum vsext_FontCharSet
	vsext_fontcs_CHINESEBIG5      =136        # from enum vsext_FontCharSet
	vsext_fontcs_DEFAULT          =1          # from enum vsext_FontCharSet
	vsext_fontcs_EASTEUROPE       =238        # from enum vsext_FontCharSet
	vsext_fontcs_GB2312           =134        # from enum vsext_FontCharSet
	vsext_fontcs_GREEK            =161        # from enum vsext_FontCharSet
	vsext_fontcs_HANGEUL          =129        # from enum vsext_FontCharSet
	vsext_fontcs_HEBREW           =177        # from enum vsext_FontCharSet
	vsext_fontcs_JOHAB            =130        # from enum vsext_FontCharSet
	vsext_fontcs_MAC              =77         # from enum vsext_FontCharSet
	vsext_fontcs_OEM              =255        # from enum vsext_FontCharSet
	vsext_fontcs_RUSSIAN          =204        # from enum vsext_FontCharSet
	vsext_fontcs_SHIFTJIS         =128        # from enum vsext_FontCharSet
	vsext_fontcs_SYMBOL           =2          # from enum vsext_FontCharSet
	vsext_fontcs_THAI             =222        # from enum vsext_FontCharSet
	vsext_fontcs_TURKISH          =162        # from enum vsext_FontCharSet
	vsext_fontcs_VIETNAMESE       =163        # from enum vsext_FontCharSet
	vsext_lwt_Docked              =0          # from enum vsext_LinkedWindowType
	vsext_lwt_Tabbed              =1          # from enum vsext_LinkedWindowType
	vsext_su_EMPTY_ENVIRONMENT    =0          # from enum vsext_StartUp
	vsext_su_LOAD_LAST_SOLUTION   =2          # from enum vsext_StartUp
	vsext_su_NEW_SOLUTION_DIALOG  =1          # from enum vsext_StartUp
	vsext_ws_Maximize             =2          # from enum vsext_WindowState
	vsext_ws_Minimize             =1          # from enum vsext_WindowState
	vsext_ws_Normal               =0          # from enum vsext_WindowState
	vsext_wt_Autos                =19         # from enum vsext_WindowType
	vsext_wt_Browser              =2          # from enum vsext_WindowType
	vsext_wt_CallStack            =20         # from enum vsext_WindowType
	vsext_wt_CodeWindow           =0          # from enum vsext_WindowType
	vsext_wt_ColorPalette         =14         # from enum vsext_WindowType
	vsext_wt_Designer             =1          # from enum vsext_WindowType
	vsext_wt_Document             =16         # from enum vsext_WindowType
	vsext_wt_DocumentOutline      =22         # from enum vsext_WindowType
	vsext_wt_Find                 =8          # from enum vsext_WindowType
	vsext_wt_FindReplace          =9          # from enum vsext_WindowType
	vsext_wt_Immediate            =5          # from enum vsext_WindowType
	vsext_wt_LinkedWindowFrame    =11         # from enum vsext_WindowType
	vsext_wt_Locals               =4          # from enum vsext_WindowType
	vsext_wt_MainWindow           =12         # from enum vsext_WindowType
	vsext_wt_OutPutWindow         =17         # from enum vsext_WindowType
	vsext_wt_Preview              =13         # from enum vsext_WindowType
	vsext_wt_ProjectWindow        =6          # from enum vsext_WindowType
	vsext_wt_PropertyWindow       =7          # from enum vsext_WindowType
	vsext_wt_RunningDocuments     =23         # from enum vsext_WindowType
	vsext_wt_TaskList             =18         # from enum vsext_WindowType
	vsext_wt_Threads              =21         # from enum vsext_WindowType
	vsext_wt_ToolWindow           =15         # from enum vsext_WindowType
	vsext_wt_Toolbox              =10         # from enum vsext_WindowType
	vsext_wt_Watch                =3          # from enum vsext_WindowType
	wizardResultBackOut           =2          # from enum wizardResult
	wizardResultCancel            =1          # from enum wizardResult
	wizardResultFailure           =0          # from enum wizardResult
	wizardResultSuccess           =-1         # from enum wizardResult

RecordMap = {
}

CLSIDToClassMap = {}
CLSIDToPackageMap = {
	'{A3A80783-875F-435B-9639-E5CE888DF737}' : 'OutputGroup',
	'{88AC98C7-B38C-404B-BD86-D2A4F2E89DCA}' : 'SolutionEvents',
	'{63EB5C39-CA8F-498E-9A66-6DD4A27AC95B}' : 'Document',
	'{F69B64A3-9017-4E48-9784-E152B51AA722}' : 'IExtenderProviderUnk',
	'{DC6A118A-BBAB-11D2-8AD1-00C04F79E479}' : 'Programs',
	'{BDCAF240-2692-4713-902A-B110B1D0F100}' : 'IDTToolsOptionsPage',
	'{DC5437F7-F114-11D2-AACF-00C04F688DDE}' : 'DocumentEvents',
	'{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}' : 'Window',
	'{90813589-FE21-4AA4-A2E5-053FD274E980}' : 'Configuration',
	'{26F6CC4B-7A48-4E4D-8AF5-9E960232E05F}' : '_Solution',
	'{56FCD5AF-7F17-4C5C-AA8D-AE2BB2DDBF38}' : 'ToolBox',
	'{9E2CF3EA-140F-413E-BD4B-7D46740CD2F4}' : 'Documents',
	'{5C5A0070-F396-4E37-A82A-1B767E272DF9}' : 'Process',
	'{CE2DEF9E-3387-4BF2-967B-A1F7F70DF325}' : 'ToolBoxTab',
	'{6AA23FB4-BBA1-11D2-8AD1-00C04F79E479}' : 'Threads',
	'{F9FA748E-E302-44CF-891B-E263189D585E}' : 'OutputGroups',
	'{AF37511E-9E9D-4234-A5A1-7584D290E061}' : 'SelectionEvents',
	'{4B51103D-513C-4773-B56A-354D0928FD04}' : 'TaskItems',
	'{D83D60E3-229F-4660-8DD0-28B629EEDCDA}' : 'BuildEvents',
	'{B02CF62A-9470-4308-A521-9675FBA395AB}' : 'OutputWindowPanes',
	'{B1F42510-91CD-4D3A-8B25-A317D8032B24}' : 'CodeInterface',
	'{B1F42511-91CD-4D3A-8B25-A317D8032B24}' : 'CodeStruct',
	'{B1F42512-91CD-4D3A-8B25-A317D8032B24}' : 'CodeEnum',
	'{B1F42513-91CD-4D3A-8B25-A317D8032B24}' : 'CodeDelegate',
	'{B1F42514-91CD-4D3A-8B25-A317D8032B24}' : 'CodeClass',
	'{F25AE7E6-1460-4BA4-8E5E-BBBE746DE353}' : 'FontsAndColorsItems',
	'{1125C423-49BD-11D2-8823-00C04FB6C6FF}' : '_dispTaskListEvents',
	'{E57C510B-968B-4A3C-A467-EE4013157DC9}' : 'IExtenderSite',
	'{478F06D4-5D57-473F-9B74-5F8E88EFA5E7}' : '_EnvironmentProjectsAndSolution',
	'{134170F8-93B1-42DD-9F89-A2AC7010BA07}' : 'Events',
	'{FA1BB6D7-CA83-11D2-AAB2-00C04F688DDE}' : '_DTEEvents',
	'{FBCFF1C2-261C-11D1-AE5E-00A0C90F26F4}' : '_dispSolutionEvents',
	'{41D02413-8A67-4C28-A980-AD7539ED415D}' : 'WindowConfiguration',
	'{2699DD44-C507-4DA3-AA34-314A6C21DFE2}' : '_dispTextEditorEvents',
	'{536A4BE3-A376-408E-954C-471C779E216F}' : 'ProjectsEvents',
	'{72767524-E3B3-43D0-BB46-BBE1D556A9FF}' : 'TextRange',
	'{DB8406B0-A916-449C-A277-BB04028F4394}' : 'UIHierarchyItems',
	'{EAB0A63D-C3A8-496E-9ACF-A82CEF6A43B3}' : 'OutputWindow',
	'{AEBDED64-A206-11D3-B8B5-00C04F79F802}' : '_EnvironmentHelp',
	'{CF177B52-4F2F-42A0-8DA3-CE78679A0D2D}' : 'ToolBoxTabs',
	'{A4F4246C-C131-11D2-8AD1-00C04F79E479}' : 'Languages',
	'{17D12026-BA99-403E-A359-71FD1E5A72CD}' : '_WindowEventsRoot',
	'{0685B546-FB84-4917-AB98-98D40F892D61}' : 'SolutionContexts',
	'{B3CCFA68-C145-11D2-8AD1-00C04F79E479}' : 'Language',
	'{BF8BBF37-5415-46A9-940D-594CAD9DEC26}' : '_SolutionEvents',
	'{4E4F0569-E16A-4DA1-92DE-10882A4DDD8C}' : 'TaskList',
	'{9C722678-490D-408F-98AE-B6B9A68AA45D}' : '_EnvironmentKeyboard',
	'{9F379969-5EAC-4A54-B2BC-6946CFFB56EF}' : 'Processes',
	'{F47DC7E7-84B6-474F-BB91-631640AA0560}' : 'TextBuffer',
	'{04A72314-32E9-48E2-9B87-A63603454F3E}' : '_DTE',
	'{256068F6-1ADD-4F7B-BA76-571314C413AD}' : '_FontsAndColors',
	'{CB218890-1382-472B-9118-782700C88115}' : 'TextDocument',
	'{2FC54DC9-922B-44EB-8CC0-BA182584DC4B}' : 'TextWindow',
	'{F6576203-FBCE-477E-A66B-EDA237BB68A7}' : 'HTMLWindow',
	'{72A2A2EF-C209-408C-A377-76871774ADB7}' : 'UIHierarchy',
	'{6A38D87C-BBA0-11D2-8AD1-00C04F79E479}' : 'Program',
	'{BFD4B2B2-9EEC-4DB8-ABA0-AC316F4C7328}' : 'CommandBarEvents',
	'{7658B944-F37B-11D2-AACF-00C04F688DDE}' : '_MiscSlnFilesEventsRoot',
	'{29617ACD-7859-4328-BE09-298F91F48196}' : 'TaskListEvents',
	'{02273422-8DD4-4A9F-8A8B-D70443D510F4}' : 'SelectionContainer',
	'{F39AB913-E6C9-4546-A265-1E43F8DE924C}' : 'IVsTextEditFonts',
	'{48E61D9C-8C8D-42D3-914B-46D70C8B7A40}' : '_EnvironmentGeneral',
	'{B6B4C8D6-4D27-43B9-B45C-52BD16B6BA38}' : 'Configurations',
	'{4DB06329-23F4-443B-9ABD-9CF611E8AE07}' : 'IExtenderProvider',
	'{50590801-D13E-4404-80C2-5CA30A4D0EE8}' : 'AddIns',
	'{40D4B9B6-739B-4965-8D65-692AEC692266}' : 'Find',
	'{D8DEC44D-CAF2-4B39-A539-B91AE921BA92}' : 'UndoContext',
	'{0A3546A8-6840-11D2-97C1-00C04FB6C6FF}' : '_OutputWindowEvents',
	'{ADF22C37-0069-4ADF-B12D-D8D47C38FE79}' : 'TextEditorEvents',
	'{A3286B03-5AC6-44F0-8CC3-EBED7F1124E5}' : '_EnvironmentWebBrowser',
	'{6BC8C372-C6F0-4BE6-B255-827AC190BF71}' : '_TaskListEventsRoot',
	'{A79FC678-0D0A-496A-B9DC-0D5B9E1CA9FC}' : '_CommandEvents',
	'{23B7A868-6C89-436A-94FA-25D755456A77}' : '_TextEditorEvents',
	'{E577442A-98E1-46C5-BD2E-D25807EC81CE}' : 'WindowConfigurations',
	'{11C5114C-BB00-11D2-8AD1-00C04F79E479}' : 'Breakpoint',
	'{9407F466-BBA1-11D2-8AD1-00C04F79E479}' : 'Thread',
	'{5FE10FB0-91A1-4E55-BAAA-ECCAE5CCEB94}' : 'Command',
	'{6CAA67CF-43AE-4184-AAAB-0200DDF6B240}' : 'SelectedItems',
	'{AADE1F59-6ACE-43D1-8FCA-42AF3A5C4F3C}' : 'IFilterProperties',
	'{46209330-0FBA-11D3-B880-00C04F79E479}' : '_dispDebuggerEvents',
	'{AA6F4085-33B6-4629-B9EA-692101007CC2}' : '_OutputWindowEventsRoot',
	'{85451F83-B5CA-437F-A619-0CB705707420}' : '_ProjectsEvents',
	'{1DED92B5-9A46-4B29-93EF-B5E07016659E}' : 'CommandEvents',
	'{EB6783DB-1819-496D-84A4-3CFF883010F6}' : '_SelectionEvents',
	'{DC5437F4-F114-11D2-AACF-00C04F688DDE}' : '_DocumentEventsRoot',
	'{DC5437F5-F114-11D2-AACF-00C04F688DDE}' : '_DocumentEvents',
	'{DC5437F6-F114-11D2-AACF-00C04F688DDE}' : '_dispDocumentEvents',
	'{3760037F-B012-44F8-9C23-3609D7A16DEF}' : 'OutputWindowEvents',
	'{8D0AA9CC-8465-42F3-AD6E-DFDE28CCC75D}' : 'ObjectExtenders',
	'{FC6A1A82-9C8A-47BB-A046-6E965DF5A99B}' : 'SolutionContext',
	'{DEEB28B3-23E6-11D1-AE5C-00A0C90F26F4}' : '_dispSelectionEvents',
	'{7F508D55-627F-4D7F-BE0B-9E3D829FF0ED}' : '_dispProjectsEvents',
	'{5943BD7E-D722-42DB-A251-FE2ADD8711EA}' : 'IVsTextEditPerLanguage',
	'{D4EAE958-0FBA-11D3-B880-00C04F79E479}' : '_DebuggerEvents',
	'{395C7DFB-F158-431C-8F43-DDA83B4EF54E}' : 'ToolBoxItems',
	'{8E2F1269-185E-43C7-8899-950AD2769CCF}' : 'ProjectItems',
	'{B3C38885-B288-44A8-B290-34FE63BF3C76}' : '_TextEditorEventsRoot',
	'{0CFBC2B5-0D4E-11D3-8997-00C04F688DDE}' : 'CodeElements',
	'{9043FDA1-345B-4364-900F-BC8598EB8E4F}' : 'ConfigurationManager',
	'{A3C1C40C-9218-4D4C-9DAA-075F64F6922C}' : 'SolutionBuild',
	'{7EF39A3E-590D-4879-88D4-C9BE5BCFD92E}' : 'IDTCommandTarget',
	'{DE6C1098-93CA-4F49-BEF0-262A13CA1176}' : 'ProjectItemsEvents',
	'{794A2BA5-FFA6-4FC5-BF13-957B2C22EDD7}' : '_BuildEvents',
	'{4ED85664-BBA2-11D2-8AD1-00C04F79E479}' : 'StackFrames',
	'{7F59E94E-4939-40D2-9F7F-B7651C25905D}' : 'TextPoint',
	'{23E78ED7-C9E1-462D-8BC6-366003486ED9}' : 'SolutionConfigurations',
	'{3C9CFE1E-389F-4118-9FAD-365385190329}' : 'DTE',
	'{D5DBE57B-C074-4E95-B015-ABEEAA391693}' : 'ItemOperations',
	'{0D3A23A9-67BB-11D2-97C1-00C04FB6C6FF}' : '_dispWindowEvents',
	'{6962753F-EFD5-41C5-B083-D70687166AEB}' : '_dispProjectItemsEvents',
	'{C6304BAB-6765-4C63-9017-4940AEB6F207}' : 'DTEEvents',
	'{F9F99155-6D4D-49B1-AD63-C78C3E8A5916}' : 'Macros',
	'{0D3A23AF-67BB-11D2-97C1-00C04FB6C6FF}' : '_dispOutputWindowEvents',
	'{7B988E06-2581-485E-9322-04881E0600D0}' : 'Property',
	'{58E4D419-6B8C-4C63-92DE-70161CD95890}' : 'TaskItem',
	'{1342D0D8-BBA3-11D2-8AD1-00C04F79E479}' : 'StackFrame',
	'{2E260FD4-C130-4E6D-8EBC-4A3BFD188181}' : 'WindowEvents',
	'{2E1BFD1C-5B26-4ACA-B97B-ED9D261BA3E7}' : 'IVsTextEditGeneral',
	'{338FB9A0-BAE5-11D2-8AD1-00C04F79E479}' : 'Debugger',
	'{866311E6-C887-4143-9833-645F5B93F6F1}' : 'Project',
	'{0B48100A-473E-433C-AB8F-66B9739AB620}' : 'ProjectItem',
	'{049D2CDF-3731-4CB6-A233-BE97BCE922D3}' : 'SelectedItem',
	'{B50C9708-C909-4B87-A03D-AF6CC4BFB422}' : '_dispDTEEvents',
	'{0A3BF283-05F8-4669-9BCB-A84B6423349A}' : 'TextPane',
	'{E3EC0ADD-31B3-461F-8303-8A5E6931257A}' : 'Projects',
	'{1926364E-6B90-46CB-A44D-8A80FB11ACD9}' : '_dispBuildEvents',
	'{FF2D5C12-FEEA-11D0-BBC8-00A0C90F2744}' : '_dispCommandEvents',
	'{F00EF34A-A654-4C1B-897A-585D5BCBB35A}' : 'LinkedWindows',
	'{987FB893-F96D-11D0-BBBB-00A0C90F2744}' : '_dispCommandBarControlEvents',
	'{60AAAD75-CB8D-4C62-9959-24D6A6A50DE7}' : 'SolutionConfiguration',
	'{2294311A-B7BC-4789-B365-1C15FF2CD17C}' : 'Windows',
	'{46538D1B-4D81-4002-8BB4-DBDB65BABB23}' : 'ToolBoxItem',
	'{53A87FA1-CE93-48BF-958B-C6DA793C5028}' : 'AddIn',
	'{1FA0E135-399A-4D2C-A4FE-D21E2480F921}' : 'TextSelection',
	'{811322BC-042D-4828-BFF2-640EF8B7209F}' : 'FindEvents',
	'{509B9955-7303-48C9-90D4-E165B974E6BA}' : 'CommandWindow',
	'{D9013D31-3652-46B2-A25A-29A881B9F86B}' : 'TextPanes',
	'{2685337A-BB9E-11D2-8AD1-00C04F79E479}' : 'Expressions',
	'{E5D17051-D6E5-4DA7-8B3A-CA888617A5E7}' : 'ColorableItems',
	'{33C5EBB8-244E-449D-9CEE-FAD70A774E59}' : 'ContextAttributes',
	'{42320454-626C-4DD0-9ECB-357C4F1966D8}' : 'VirtualPoint',
	'{E6B96CAC-B8C7-40AE-B705-5C81878C4A9E}' : 'Commands',
	'{F809CAB6-2C9F-41F2-A5AF-E26FB80E62AD}' : '_EnvironmentFontsAndColors',
	'{FFC9DFC4-61CA-4B0C-83C2-0703A24F5C16}' : 'OutputWindowPane',
	'{1125C422-49BD-11D2-8823-00C04FB6C6FF}' : '_TaskListEvents',
	'{0D3A23A8-67BB-11D2-97C1-00C04FB6C6FF}' : '_WindowEvents',
	'{E68A3E0E-B435-4DDE-86B7-F5ADEFC19DF2}' : 'Globals',
	'{1A6E2CB3-B897-42EB-96BE-FF0FDB65DB2F}' : 'ContextAttribute',
	'{C5331ACD-C5D5-11D2-8598-006097C68E81}' : '_FindEvents',
	'{C5331ACE-C5D5-11D2-8598-006097C68E81}' : '_dispFindEvents',
	'{22800963-2811-410D-BF87-A7808EAC977D}' : '_ProjectItemsEvents',
	'{9FF3DDCA-1795-4191-A5B1-02D1AE35D074}' : 'TextEditor',
	'{25968106-BAFB-11D2-8AD1-00C04F79E479}' : 'Breakpoints',
	'{9C5CEAAC-062F-4434-A2ED-78AB4D6134FE}' : 'BuildDependency',
	'{C34301A1-3EF1-41D8-932A-FEA4A8A8CE0C}' : 'StatusBar',
	'{4BC18A5B-DBB6-4AF5-A443-2E3F19365304}' : '_EnvironmentTaskList',
	'{9E66FE98-A1C6-421D-8C0C-6DA4E652E770}' : '_CommandBarControlEvents',
	'{0C763210-0FBB-11D3-B880-00C04F79E479}' : 'DebuggerEvents',
	'{EAD260EB-1E5B-450A-B628-4CFADA11B4A1}' : 'BuildDependencies',
	'{4CC8CCF5-A926-4646-B17F-B4940CAED472}' : 'Properties',
	'{0CFBC2B4-0D4E-11D3-8997-00C04F688DDE}' : 'CodeModel',
	'{B35CAA8C-77DE-4AB3-8E5A-F038E3FC6056}' : 'Solution',
	'{0CFBC2B6-0D4E-11D3-8997-00C04F688DDE}' : 'CodeElement',
	'{0CFBC2B7-0D4E-11D3-8997-00C04F688DDE}' : 'CodeType',
	'{0CFBC2B8-0D4E-11D3-8997-00C04F688DDE}' : 'CodeNamespace',
	'{0CFBC2B9-0D4E-11D3-8997-00C04F688DDE}' : 'CodeFunction',
	'{0CFBC2BA-0D4E-11D3-8997-00C04F688DDE}' : 'CodeVariable',
	'{0CFBC2BB-0D4E-11D3-8997-00C04F688DDE}' : 'CodeProperty',
	'{0CFBC2BC-0D4E-11D3-8997-00C04F688DDE}' : 'CodeTypeRef',
	'{0CFBC2BD-0D4E-11D3-8997-00C04F688DDE}' : 'CodeParameter',
	'{0CFBC2BE-0D4E-11D3-8997-00C04F688DDE}' : 'CodeAttribute',
	'{B6422E9C-9EFD-4F87-BDDC-C7FD8F2FD303}' : 'TextRanges',
	'{ED1A3F99-4477-11D3-89BF-00C04F688DDE}' : 'FileCodeModel',
	'{76ED1C48-ED86-4E9E-ACF8-A40E765DAF25}' : '_EnvironmentDocuments',
	'{FBD0D024-09CD-4D9F-9E2B-CACD628426A5}' : 'UIHierarchyItem',
	'{27ADC812-BB07-11D2-8AD1-00C04F79E479}' : 'Expression',
	'{C1FFE800-028B-4475-A907-14F51F19BB7D}' : 'EditPoint',
	'{F1DDC2C2-DF76-4EBB-9DE8-48AD2557062C}' : 'SourceControl',
	'{E914BBE1-03A4-11D1-BBCD-00A0C90F2744}' : 'IDTWizard',
	'{D4BB39FB-0F0E-11D3-B880-00C04F79E479}' : '_DebuggerEventsRoot',
}
VTablesToClassMap = {}
VTablesToPackageMap = {
	'{A3A80783-875F-435B-9639-E5CE888DF737}' : 'OutputGroup',
	'{DC5437F4-F114-11D2-AACF-00C04F688DDE}' : '_DocumentEventsRoot',
	'{63EB5C39-CA8F-498E-9A66-6DD4A27AC95B}' : 'Document',
	'{8D0AA9CC-8465-42F3-AD6E-DFDE28CCC75D}' : 'ObjectExtenders',
	'{8CC0CDE1-C16A-4749-99AF-6F7523C34A57}' : 'IVsProfferCommands',
	'{FC6A1A82-9C8A-47BB-A046-6E965DF5A99B}' : 'SolutionContext',
	'{DC6A118A-BBAB-11D2-8AD1-00C04F79E479}' : 'Programs',
	'{D4BB39FB-0F0E-11D3-B880-00C04F79E479}' : '_DebuggerEventsRoot',
	'{BDCAF240-2692-4713-902A-B110B1D0F100}' : 'IDTToolsOptionsPage',
	'{7EF39A3E-590D-4879-88D4-C9BE5BCFD92E}' : 'IDTCommandTarget',
	'{5943BD7E-D722-42DB-A251-FE2ADD8711EA}' : 'IVsTextEditPerLanguage',
	'{6CAA67CF-43AE-4184-AAAB-0200DDF6B240}' : 'SelectedItems',
	'{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}' : 'Window',
	'{0CFBC2B4-0D4E-11D3-8997-00C04F688DDE}' : 'CodeModel',
	'{90813589-FE21-4AA4-A2E5-053FD274E980}' : 'Configuration',
	'{26F6CC4B-7A48-4E4D-8AF5-9E960232E05F}' : '_Solution',
	'{8E2F1269-185E-43C7-8899-950AD2769CCF}' : 'ProjectItems',
	'{56FCD5AF-7F17-4C5C-AA8D-AE2BB2DDBF38}' : 'ToolBox',
	'{9043FDA1-345B-4364-900F-BC8598EB8E4F}' : 'ConfigurationManager',
	'{11C5114C-BB00-11D2-8AD1-00C04F79E479}' : 'Breakpoint',
	'{9E2CF3EA-140F-413E-BD4B-7D46740CD2F4}' : 'Documents',
	'{5C5A0070-F396-4E37-A82A-1B767E272DF9}' : 'Process',
	'{72A2A2EF-C209-408C-A377-76871774ADB7}' : 'UIHierarchy',
	'{6AA23FB4-BBA1-11D2-8AD1-00C04F79E479}' : 'Threads',
	'{F9FA748E-E302-44CF-891B-E263189D585E}' : 'OutputGroups',
	'{4B51103D-513C-4773-B56A-354D0928FD04}' : 'TaskItems',
	'{7B988E06-2581-485E-9322-04881E0600D0}' : 'Property',
	'{B02CF62A-9470-4308-A521-9675FBA395AB}' : 'OutputWindowPanes',
	'{0CFBC2B9-0D4E-11D3-8997-00C04F688DDE}' : 'CodeFunction',
	'{B1F42510-91CD-4D3A-8B25-A317D8032B24}' : 'CodeInterface',
	'{B1F42511-91CD-4D3A-8B25-A317D8032B24}' : 'CodeStruct',
	'{B1F42512-91CD-4D3A-8B25-A317D8032B24}' : 'CodeEnum',
	'{B1F42513-91CD-4D3A-8B25-A317D8032B24}' : 'CodeDelegate',
	'{B1F42514-91CD-4D3A-8B25-A317D8032B24}' : 'CodeClass',
	'{395C7DFB-F158-431C-8F43-DDA83B4EF54E}' : 'ToolBoxItems',
	'{23E78ED7-C9E1-462D-8BC6-366003486ED9}' : 'SolutionConfigurations',
	'{E5D17051-D6E5-4DA7-8B3A-CA888617A5E7}' : 'ColorableItems',
	'{F25AE7E6-1460-4BA4-8E5E-BBBE746DE353}' : 'FontsAndColorsItems',
	'{D5DBE57B-C074-4E95-B015-ABEEAA391693}' : 'ItemOperations',
	'{E57C510B-968B-4A3C-A467-EE4013157DC9}' : 'IExtenderSite',
	'{478F06D4-5D57-473F-9B74-5F8E88EFA5E7}' : '_EnvironmentProjectsAndSolution',
	'{F9F99155-6D4D-49B1-AD63-C78C3E8A5916}' : 'Macros',
	'{E68A3E0E-B435-4DDE-86B7-F5ADEFC19DF2}' : 'Globals',
	'{C1FFE800-028B-4475-A907-14F51F19BB7D}' : 'EditPoint',
	'{1342D0D8-BBA3-11D2-8AD1-00C04F79E479}' : 'StackFrame',
	'{E2CC506A-588B-4F65-A1F0-2244C060ABCB}' : 'IVsGlobalsCallback',
	'{F69B64A3-9017-4E48-9784-E152B51AA722}' : 'IExtenderProviderUnk',
	'{B3C38885-B288-44A8-B290-34FE63BF3C76}' : '_TextEditorEventsRoot',
	'{41D02413-8A67-4C28-A980-AD7539ED415D}' : 'WindowConfiguration',
	'{2E1BFD1C-5B26-4ACA-B97B-ED9D261BA3E7}' : 'IVsTextEditGeneral',
	'{338FB9A0-BAE5-11D2-8AD1-00C04F79E479}' : 'Debugger',
	'{866311E6-C887-4143-9833-645F5B93F6F1}' : 'Project',
	'{D8DEC44D-CAF2-4B39-A539-B91AE921BA92}' : 'UndoContext',
	'{0B48100A-473E-433C-AB8F-66B9739AB620}' : 'ProjectItem',
	'{72767524-E3B3-43D0-BB46-BBE1D556A9FF}' : 'TextRange',
	'{EB5BE8A7-E593-4DE6-A923-C2AFECB96336}' : 'IExtensibleObjectSite',
	'{DB8406B0-A916-449C-A277-BB04028F4394}' : 'UIHierarchyItems',
	'{049D2CDF-3731-4CB6-A233-BE97BCE922D3}' : 'SelectedItem',
	'{AEBDED64-A206-11D3-B8B5-00C04F79F802}' : '_EnvironmentHelp',
	'{53A87FA1-CE93-48BF-958B-C6DA793C5028}' : 'AddIn',
	'{CF177B52-4F2F-42A0-8DA3-CE78679A0D2D}' : 'ToolBoxTabs',
	'{A4F4246C-C131-11D2-8AD1-00C04F79E479}' : 'Languages',
	'{0A3BF283-05F8-4669-9BCB-A84B6423349A}' : 'TextPane',
	'{E3EC0ADD-31B3-461F-8303-8A5E6931257A}' : 'Projects',
	'{17D12026-BA99-403E-A359-71FD1E5A72CD}' : '_WindowEventsRoot',
	'{9FF3DDCA-1795-4191-A5B1-02D1AE35D074}' : 'TextEditor',
	'{F00EF34A-A654-4C1B-897A-585D5BCBB35A}' : 'LinkedWindows',
	'{0685B546-FB84-4917-AB98-98D40F892D61}' : 'SolutionContexts',
	'{B3CCFA68-C145-11D2-8AD1-00C04F79E479}' : 'Language',
	'{60AAAD75-CB8D-4C62-9959-24D6A6A50DE7}' : 'SolutionConfiguration',
	'{2294311A-B7BC-4789-B365-1C15FF2CD17C}' : 'Windows',
	'{46538D1B-4D81-4002-8BB4-DBDB65BABB23}' : 'ToolBoxItem',
	'{7F59E94E-4939-40D2-9F7F-B7651C25905D}' : 'TextPoint',
	'{4E4F0569-E16A-4DA1-92DE-10882A4DDD8C}' : 'TaskList',
	'{509B9955-7303-48C9-90D4-E165B974E6BA}' : 'CommandWindow',
	'{9C722678-490D-408F-98AE-B6B9A68AA45D}' : '_EnvironmentKeyboard',
	'{EAB0A63D-C3A8-496E-9ACF-A82CEF6A43B3}' : 'OutputWindow',
	'{9F379969-5EAC-4A54-B2BC-6946CFFB56EF}' : 'Processes',
	'{1FA0E135-399A-4D2C-A4FE-D21E2480F921}' : 'TextSelection',
	'{F47DC7E7-84B6-474F-BB91-631640AA0560}' : 'TextBuffer',
	'{04A72314-32E9-48E2-9B87-A63603454F3E}' : '_DTE',
	'{AADE1F59-6ACE-43D1-8FCA-42AF3A5C4F3C}' : 'IFilterProperties',
	'{3C536122-57B1-46DE-AB34-ACC524140093}' : 'IVsExtensibility',
	'{CB218890-1382-472B-9118-782700C88115}' : 'TextDocument',
	'{2FC54DC9-922B-44EB-8CC0-BA182584DC4B}' : 'TextWindow',
	'{D9013D31-3652-46B2-A25A-29A881B9F86B}' : 'TextPanes',
	'{FBD0D024-09CD-4D9F-9E2B-CACD628426A5}' : 'UIHierarchyItem',
	'{33C5EBB8-244E-449D-9CEE-FAD70A774E59}' : 'ContextAttributes',
	'{42320454-626C-4DD0-9ECB-357C4F1966D8}' : 'VirtualPoint',
	'{F6576203-FBCE-477E-A66B-EDA237BB68A7}' : 'HTMLWindow',
	'{6659ED14-2AB6-47F3-A890-00C8ABA43B84}' : 'ISupportVSProperties',
	'{E6B96CAC-B8C7-40AE-B705-5C81878C4A9E}' : 'Commands',
	'{CE2DEF9E-3387-4BF2-967B-A1F7F70DF325}' : 'ToolBoxTab',
	'{FFC9DFC4-61CA-4B0C-83C2-0703A24F5C16}' : 'OutputWindowPane',
	'{86C31347-5B52-4715-B454-A6E5FCAB975D}' : 'IExtensibleObject',
	'{134170F8-93B1-42DD-9F89-A2AC7010BA07}' : 'Events',
	'{1A6E2CB3-B897-42EB-96BE-FF0FDB65DB2F}' : 'ContextAttribute',
	'{40D4B9B6-739B-4965-8D65-692AEC692266}' : 'Find',
	'{192AC688-E7C6-4F9D-8180-4B37EFBF6F3A}' : 'IVsGlobals',
	'{AA6F4085-33B6-4629-B9EA-692101007CC2}' : '_OutputWindowEventsRoot',
	'{22800963-2811-410D-BF87-A7808EAC977D}' : '_ProjectItemsEvents',
	'{02273422-8DD4-4A9F-8A8B-D70443D510F4}' : 'SelectionContainer',
	'{0CFBC2BA-0D4E-11D3-8997-00C04F688DDE}' : 'CodeVariable',
	'{48E61D9C-8C8D-42D3-914B-46D70C8B7A40}' : '_EnvironmentGeneral',
	'{B6B4C8D6-4D27-43B9-B45C-52BD16B6BA38}' : 'Configurations',
	'{4DB06329-23F4-443B-9ABD-9CF611E8AE07}' : 'IExtenderProvider',
	'{50590801-D13E-4404-80C2-5CA30A4D0EE8}' : 'AddIns',
	'{9C5CEAAC-062F-4434-A2ED-78AB4D6134FE}' : 'BuildDependency',
	'{C34301A1-3EF1-41D8-932A-FEA4A8A8CE0C}' : 'StatusBar',
	'{4BC18A5B-DBB6-4AF5-A443-2E3F19365304}' : '_EnvironmentTaskList',
	'{E577442A-98E1-46C5-BD2E-D25807EC81CE}' : 'WindowConfigurations',
	'{76ED1C48-ED86-4E9E-ACF8-A40E765DAF25}' : '_EnvironmentDocuments',
	'{A3286B03-5AC6-44F0-8CC3-EBED7F1124E5}' : '_EnvironmentWebBrowser',
	'{6BC8C372-C6F0-4BE6-B255-827AC190BF71}' : '_TaskListEventsRoot',
	'{EAD260EB-1E5B-450A-B628-4CFADA11B4A1}' : 'BuildDependencies',
	'{4CC8CCF5-A926-4646-B17F-B4940CAED472}' : 'Properties',
	'{256068F6-1ADD-4F7B-BA76-571314C413AD}' : '_FontsAndColors',
	'{25968106-BAFB-11D2-8AD1-00C04F79E479}' : 'Breakpoints',
	'{0CFBC2B5-0D4E-11D3-8997-00C04F688DDE}' : 'CodeElements',
	'{0CFBC2B6-0D4E-11D3-8997-00C04F688DDE}' : 'CodeElement',
	'{0CFBC2B7-0D4E-11D3-8997-00C04F688DDE}' : 'CodeType',
	'{0CFBC2B8-0D4E-11D3-8997-00C04F688DDE}' : 'CodeNamespace',
	'{A3C1C40C-9218-4D4C-9DAA-075F64F6922C}' : 'SolutionBuild',
	'{9407F466-BBA1-11D2-8AD1-00C04F79E479}' : 'Thread',
	'{0CFBC2BB-0D4E-11D3-8997-00C04F688DDE}' : 'CodeProperty',
	'{0CFBC2BC-0D4E-11D3-8997-00C04F688DDE}' : 'CodeTypeRef',
	'{0CFBC2BD-0D4E-11D3-8997-00C04F688DDE}' : 'CodeParameter',
	'{0CFBC2BE-0D4E-11D3-8997-00C04F688DDE}' : 'CodeAttribute',
	'{B6422E9C-9EFD-4F87-BDDC-C7FD8F2FD303}' : 'TextRanges',
	'{ED1A3F99-4477-11D3-89BF-00C04F688DDE}' : 'FileCodeModel',
	'{7658B944-F37B-11D2-AACF-00C04F688DDE}' : '_MiscSlnFilesEventsRoot',
	'{5FE10FB0-91A1-4E55-BAAA-ECCAE5CCEB94}' : 'Command',
	'{2685337A-BB9E-11D2-8AD1-00C04F79E479}' : 'Expressions',
	'{27ADC812-BB07-11D2-8AD1-00C04F79E479}' : 'Expression',
	'{58E4D419-6B8C-4C63-92DE-70161CD95890}' : 'TaskItem',
	'{6A38D87C-BBA0-11D2-8AD1-00C04F79E479}' : 'Program',
	'{4ED85664-BBA2-11D2-8AD1-00C04F79E479}' : 'StackFrames',
	'{85451F83-B5CA-437F-A619-0CB705707420}' : '_ProjectsEvents',
	'{F809CAB6-2C9F-41F2-A5AF-E26FB80E62AD}' : '_EnvironmentFontsAndColors',
	'{F1DDC2C2-DF76-4EBB-9DE8-48AD2557062C}' : 'SourceControl',
	'{E914BBE1-03A4-11D1-BBCD-00A0C90F2744}' : 'IDTWizard',
	'{F39AB913-E6C9-4546-A265-1E43F8DE924C}' : 'IVsTextEditFonts',
}


NamesToIIDMap = {
	'Debugger' : '{338FB9A0-BAE5-11D2-8AD1-00C04F79E479}',
	'CodeElements' : '{0CFBC2B5-0D4E-11D3-8997-00C04F688DDE}',
	'CodeParameter' : '{0CFBC2BD-0D4E-11D3-8997-00C04F688DDE}',
	'_dispWindowEvents' : '{0D3A23A9-67BB-11D2-97C1-00C04FB6C6FF}',
	'OutputWindow' : '{EAB0A63D-C3A8-496E-9ACF-A82CEF6A43B3}',
	'Projects' : '{E3EC0ADD-31B3-461F-8303-8A5E6931257A}',
	'IExtensibleObjectSite' : '{EB5BE8A7-E593-4DE6-A923-C2AFECB96336}',
	'Configuration' : '{90813589-FE21-4AA4-A2E5-053FD274E980}',
	'_OutputWindowEventsRoot' : '{AA6F4085-33B6-4629-B9EA-692101007CC2}',
	'HTMLWindow' : '{F6576203-FBCE-477E-A66B-EDA237BB68A7}',
	'_WindowEvents' : '{0D3A23A8-67BB-11D2-97C1-00C04FB6C6FF}',
	'CodeModel' : '{0CFBC2B4-0D4E-11D3-8997-00C04F688DDE}',
	'BuildDependencies' : '{EAD260EB-1E5B-450A-B628-4CFADA11B4A1}',
	'IVsTextEditPerLanguage' : '{5943BD7E-D722-42DB-A251-FE2ADD8711EA}',
	'Breakpoints' : '{25968106-BAFB-11D2-8AD1-00C04F79E479}',
	'Configurations' : '{B6B4C8D6-4D27-43B9-B45C-52BD16B6BA38}',
	'_DocumentEventsRoot' : '{DC5437F4-F114-11D2-AACF-00C04F688DDE}',
	'_TextEditorEventsRoot' : '{B3C38885-B288-44A8-B290-34FE63BF3C76}',
	'StatusBar' : '{C34301A1-3EF1-41D8-932A-FEA4A8A8CE0C}',
	'_DTE' : '{04A72314-32E9-48E2-9B87-A63603454F3E}',
	'CodeDelegate' : '{B1F42513-91CD-4D3A-8B25-A317D8032B24}',
	'SolutionConfiguration' : '{60AAAD75-CB8D-4C62-9959-24D6A6A50DE7}',
	'Commands' : '{E6B96CAC-B8C7-40AE-B705-5C81878C4A9E}',
	'_EnvironmentHelp' : '{AEBDED64-A206-11D3-B8B5-00C04F79F802}',
	'FontsAndColorsItems' : '{F25AE7E6-1460-4BA4-8E5E-BBBE746DE353}',
	'Program' : '{6A38D87C-BBA0-11D2-8AD1-00C04F79E479}',
	'SolutionBuild' : '{A3C1C40C-9218-4D4C-9DAA-075F64F6922C}',
	'TextWindow' : '{2FC54DC9-922B-44EB-8CC0-BA182584DC4B}',
	'ISupportVSProperties' : '{6659ED14-2AB6-47F3-A890-00C8ABA43B84}',
	'_SelectionEvents' : '{EB6783DB-1819-496D-84A4-3CFF883010F6}',
	'IFilterProperties' : '{AADE1F59-6ACE-43D1-8FCA-42AF3A5C4F3C}',
	'UIHierarchy' : '{72A2A2EF-C209-408C-A377-76871774ADB7}',
	'WindowConfigurations' : '{E577442A-98E1-46C5-BD2E-D25807EC81CE}',
	'Processes' : '{9F379969-5EAC-4A54-B2BC-6946CFFB56EF}',
	'CodeNamespace' : '{0CFBC2B8-0D4E-11D3-8997-00C04F688DDE}',
	'_DebuggerEvents' : '{D4EAE958-0FBA-11D3-B880-00C04F79E479}',
	'_DebuggerEventsRoot' : '{D4BB39FB-0F0E-11D3-B880-00C04F79E479}',
	'ItemOperations' : '{D5DBE57B-C074-4E95-B015-ABEEAA391693}',
	'IExtenderSite' : '{E57C510B-968B-4A3C-A467-EE4013157DC9}',
	'_dispDTEEvents' : '{B50C9708-C909-4B87-A03D-AF6CC4BFB422}',
	'ToolBoxTabs' : '{CF177B52-4F2F-42A0-8DA3-CE78679A0D2D}',
	'ConfigurationManager' : '{9043FDA1-345B-4364-900F-BC8598EB8E4F}',
	'CodeClass' : '{B1F42514-91CD-4D3A-8B25-A317D8032B24}',
	'_EnvironmentKeyboard' : '{9C722678-490D-408F-98AE-B6B9A68AA45D}',
	'IDTToolsOptionsPage' : '{BDCAF240-2692-4713-902A-B110B1D0F100}',
	'Breakpoint' : '{11C5114C-BB00-11D2-8AD1-00C04F79E479}',
	'_dispOutputWindowEvents' : '{0D3A23AF-67BB-11D2-97C1-00C04FB6C6FF}',
	'Macros' : '{F9F99155-6D4D-49B1-AD63-C78C3E8A5916}',
	'CodeFunction' : '{0CFBC2B9-0D4E-11D3-8997-00C04F688DDE}',
	'_CommandBarControlEvents' : '{9E66FE98-A1C6-421D-8C0C-6DA4E652E770}',
	'TextSelection' : '{1FA0E135-399A-4D2C-A4FE-D21E2480F921}',
	'_dispFindEvents' : '{C5331ACE-C5D5-11D2-8598-006097C68E81}',
	'_EnvironmentGeneral' : '{48E61D9C-8C8D-42D3-914B-46D70C8B7A40}',
	'Expression' : '{27ADC812-BB07-11D2-8AD1-00C04F79E479}',
	'FileCodeModel' : '{ED1A3F99-4477-11D3-89BF-00C04F688DDE}',
	'Thread' : '{9407F466-BBA1-11D2-8AD1-00C04F79E479}',
	'ColorableItems' : '{E5D17051-D6E5-4DA7-8B3A-CA888617A5E7}',
	'ContextAttribute' : '{1A6E2CB3-B897-42EB-96BE-FF0FDB65DB2F}',
	'Globals' : '{E68A3E0E-B435-4DDE-86B7-F5ADEFC19DF2}',
	'CommandWindow' : '{509B9955-7303-48C9-90D4-E165B974E6BA}',
	'_dispProjectsEvents' : '{7F508D55-627F-4D7F-BE0B-9E3D829FF0ED}',
	'IVsTextEditFonts' : '{F39AB913-E6C9-4546-A265-1E43F8DE924C}',
	'EditPoint' : '{C1FFE800-028B-4475-A907-14F51F19BB7D}',
	'_BuildEvents' : '{794A2BA5-FFA6-4FC5-BF13-957B2C22EDD7}',
	'ToolBox' : '{56FCD5AF-7F17-4C5C-AA8D-AE2BB2DDBF38}',
	'OutputWindowPanes' : '{B02CF62A-9470-4308-A521-9675FBA395AB}',
	'ObjectExtenders' : '{8D0AA9CC-8465-42F3-AD6E-DFDE28CCC75D}',
	'SourceControl' : '{F1DDC2C2-DF76-4EBB-9DE8-48AD2557062C}',
	'CodeInterface' : '{B1F42510-91CD-4D3A-8B25-A317D8032B24}',
	'StackFrame' : '{1342D0D8-BBA3-11D2-8AD1-00C04F79E479}',
	'CodeAttribute' : '{0CFBC2BE-0D4E-11D3-8997-00C04F688DDE}',
	'SelectionContainer' : '{02273422-8DD4-4A9F-8A8B-D70443D510F4}',
	'Properties' : '{4CC8CCF5-A926-4646-B17F-B4940CAED472}',
	'TaskItems' : '{4B51103D-513C-4773-B56A-354D0928FD04}',
	'UIHierarchyItems' : '{DB8406B0-A916-449C-A277-BB04028F4394}',
	'_MiscSlnFilesEventsRoot' : '{7658B944-F37B-11D2-AACF-00C04F688DDE}',
	'CodeVariable' : '{0CFBC2BA-0D4E-11D3-8997-00C04F688DDE}',
	'TextBuffer' : '{F47DC7E7-84B6-474F-BB91-631640AA0560}',
	'Expressions' : '{2685337A-BB9E-11D2-8AD1-00C04F79E479}',
	'_ProjectsEvents' : '{85451F83-B5CA-437F-A619-0CB705707420}',
	'ProjectItems' : '{8E2F1269-185E-43C7-8899-950AD2769CCF}',
	'_WindowEventsRoot' : '{17D12026-BA99-403E-A359-71FD1E5A72CD}',
	'Project' : '{866311E6-C887-4143-9833-645F5B93F6F1}',
	'_dispCommandBarControlEvents' : '{987FB893-F96D-11D0-BBBB-00A0C90F2744}',
	'CodeType' : '{0CFBC2B7-0D4E-11D3-8997-00C04F688DDE}',
	'StackFrames' : '{4ED85664-BBA2-11D2-8AD1-00C04F79E479}',
	'IExtensibleObject' : '{86C31347-5B52-4715-B454-A6E5FCAB975D}',
	'TextPane' : '{0A3BF283-05F8-4669-9BCB-A84B6423349A}',
	'Process' : '{5C5A0070-F396-4E37-A82A-1B767E272DF9}',
	'OutputGroup' : '{A3A80783-875F-435B-9639-E5CE888DF737}',
	'Threads' : '{6AA23FB4-BBA1-11D2-8AD1-00C04F79E479}',
	'_FontsAndColors' : '{256068F6-1ADD-4F7B-BA76-571314C413AD}',
	'_OutputWindowEvents' : '{0A3546A8-6840-11D2-97C1-00C04FB6C6FF}',
	'_TextEditorEvents' : '{23B7A868-6C89-436A-94FA-25D755456A77}',
	'_ProjectItemsEvents' : '{22800963-2811-410D-BF87-A7808EAC977D}',
	'WindowConfiguration' : '{41D02413-8A67-4C28-A980-AD7539ED415D}',
	'TaskItem' : '{58E4D419-6B8C-4C63-92DE-70161CD95890}',
	'_Solution' : '{26F6CC4B-7A48-4E4D-8AF5-9E960232E05F}',
	'_dispSelectionEvents' : '{DEEB28B3-23E6-11D1-AE5C-00A0C90F26F4}',
	'SolutionContext' : '{FC6A1A82-9C8A-47BB-A046-6E965DF5A99B}',
	'_TaskListEventsRoot' : '{6BC8C372-C6F0-4BE6-B255-827AC190BF71}',
	'LinkedWindows' : '{F00EF34A-A654-4C1B-897A-585D5BCBB35A}',
	'OutputWindowPane' : '{FFC9DFC4-61CA-4B0C-83C2-0703A24F5C16}',
	'Language' : '{B3CCFA68-C145-11D2-8AD1-00C04F79E479}',
	'IVsExtensibility' : '{3C536122-57B1-46DE-AB34-ACC524140093}',
	'CodeProperty' : '{0CFBC2BB-0D4E-11D3-8997-00C04F688DDE}',
	'OutputGroups' : '{F9FA748E-E302-44CF-891B-E263189D585E}',
	'IVsGlobals' : '{192AC688-E7C6-4F9D-8180-4B37EFBF6F3A}',
	'ToolBoxItems' : '{395C7DFB-F158-431C-8F43-DDA83B4EF54E}',
	'AddIn' : '{53A87FA1-CE93-48BF-958B-C6DA793C5028}',
	'CodeEnum' : '{B1F42512-91CD-4D3A-8B25-A317D8032B24}',
	'Languages' : '{A4F4246C-C131-11D2-8AD1-00C04F79E479}',
	'_dispTextEditorEvents' : '{2699DD44-C507-4DA3-AA34-314A6C21DFE2}',
	'ToolBoxTab' : '{CE2DEF9E-3387-4BF2-967B-A1F7F70DF325}',
	'TaskList' : '{4E4F0569-E16A-4DA1-92DE-10882A4DDD8C}',
	'_FindEvents' : '{C5331ACD-C5D5-11D2-8598-006097C68E81}',
	'SelectedItem' : '{049D2CDF-3731-4CB6-A233-BE97BCE922D3}',
	'AddIns' : '{50590801-D13E-4404-80C2-5CA30A4D0EE8}',
	'TextRange' : '{72767524-E3B3-43D0-BB46-BBE1D556A9FF}',
	'IExtenderProvider' : '{4DB06329-23F4-443B-9ABD-9CF611E8AE07}',
	'IVsGlobalsCallback' : '{E2CC506A-588B-4F65-A1F0-2244C060ABCB}',
	'_TaskListEvents' : '{1125C422-49BD-11D2-8823-00C04FB6C6FF}',
	'Programs' : '{DC6A118A-BBAB-11D2-8AD1-00C04F79E479}',
	'Command' : '{5FE10FB0-91A1-4E55-BAAA-ECCAE5CCEB94}',
	'_EnvironmentDocuments' : '{76ED1C48-ED86-4E9E-ACF8-A40E765DAF25}',
	'ProjectItem' : '{0B48100A-473E-433C-AB8F-66B9739AB620}',
	'IDTWizard' : '{E914BBE1-03A4-11D1-BBCD-00A0C90F2744}',
	'Window' : '{0BEAB46B-4C07-4F94-A8D7-1626020E4E53}',
	'Documents' : '{9E2CF3EA-140F-413E-BD4B-7D46740CD2F4}',
	'TextEditor' : '{9FF3DDCA-1795-4191-A5B1-02D1AE35D074}',
	'SolutionConfigurations' : '{23E78ED7-C9E1-462D-8BC6-366003486ED9}',
	'CodeStruct' : '{B1F42511-91CD-4D3A-8B25-A317D8032B24}',
	'_EnvironmentFontsAndColors' : '{F809CAB6-2C9F-41F2-A5AF-E26FB80E62AD}',
	'CodeTypeRef' : '{0CFBC2BC-0D4E-11D3-8997-00C04F688DDE}',
	'_dispCommandEvents' : '{FF2D5C12-FEEA-11D0-BBC8-00A0C90F2744}',
	'_EnvironmentWebBrowser' : '{A3286B03-5AC6-44F0-8CC3-EBED7F1124E5}',
	'IDTCommandTarget' : '{7EF39A3E-590D-4879-88D4-C9BE5BCFD92E}',
	'_dispBuildEvents' : '{1926364E-6B90-46CB-A44D-8A80FB11ACD9}',
	'TextDocument' : '{CB218890-1382-472B-9118-782700C88115}',
	'TextPanes' : '{D9013D31-3652-46B2-A25A-29A881B9F86B}',
	'BuildDependency' : '{9C5CEAAC-062F-4434-A2ED-78AB4D6134FE}',
	'UIHierarchyItem' : '{FBD0D024-09CD-4D9F-9E2B-CACD628426A5}',
	'_dispTaskListEvents' : '{1125C423-49BD-11D2-8823-00C04FB6C6FF}',
	'_dispProjectItemsEvents' : '{6962753F-EFD5-41C5-B083-D70687166AEB}',
	'SelectedItems' : '{6CAA67CF-43AE-4184-AAAB-0200DDF6B240}',
	'Find' : '{40D4B9B6-739B-4965-8D65-692AEC692266}',
	'_EnvironmentTaskList' : '{4BC18A5B-DBB6-4AF5-A443-2E3F19365304}',
	'ToolBoxItem' : '{46538D1B-4D81-4002-8BB4-DBDB65BABB23}',
	'UndoContext' : '{D8DEC44D-CAF2-4B39-A539-B91AE921BA92}',
	'CodeElement' : '{0CFBC2B6-0D4E-11D3-8997-00C04F688DDE}',
	'TextRanges' : '{B6422E9C-9EFD-4F87-BDDC-C7FD8F2FD303}',
	'_DocumentEvents' : '{DC5437F5-F114-11D2-AACF-00C04F688DDE}',
	'_SolutionEvents' : '{BF8BBF37-5415-46A9-940D-594CAD9DEC26}',
	'VirtualPoint' : '{42320454-626C-4DD0-9ECB-357C4F1966D8}',
	'IExtenderProviderUnk' : '{F69B64A3-9017-4E48-9784-E152B51AA722}',
	'_EnvironmentProjectsAndSolution' : '{478F06D4-5D57-473F-9B74-5F8E88EFA5E7}',
	'Document' : '{63EB5C39-CA8F-498E-9A66-6DD4A27AC95B}',
	'SolutionContexts' : '{0685B546-FB84-4917-AB98-98D40F892D61}',
	'Property' : '{7B988E06-2581-485E-9322-04881E0600D0}',
	'TextPoint' : '{7F59E94E-4939-40D2-9F7F-B7651C25905D}',
	'ContextAttributes' : '{33C5EBB8-244E-449D-9CEE-FAD70A774E59}',
	'_DTEEvents' : '{FA1BB6D7-CA83-11D2-AAB2-00C04F688DDE}',
	'IVsProfferCommands' : '{8CC0CDE1-C16A-4749-99AF-6F7523C34A57}',
	'_CommandEvents' : '{A79FC678-0D0A-496A-B9DC-0D5B9E1CA9FC}',
	'_dispSolutionEvents' : '{FBCFF1C2-261C-11D1-AE5E-00A0C90F26F4}',
	'Events' : '{134170F8-93B1-42DD-9F89-A2AC7010BA07}',
	'_dispDocumentEvents' : '{DC5437F6-F114-11D2-AACF-00C04F688DDE}',
	'IVsTextEditGeneral' : '{2E1BFD1C-5B26-4ACA-B97B-ED9D261BA3E7}',
	'_dispDebuggerEvents' : '{46209330-0FBA-11D3-B880-00C04F79E479}',
	'Windows' : '{2294311A-B7BC-4789-B365-1C15FF2CD17C}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

