import sublime, sublime_plugin
import comtypes, functools
#import time
import comtypes.client as cc

dte_id = comtypes.GUID("{80cc9f66-e7d8-4ddd-85b6-d9e6cd0e93e2}")

dte_settings = sublime.load_settings("VisualStudio.sublime-settings")

#I don't know why this still uses V8 but no other version # works.
cc.GetModule((dte_id, 8, 0))

import comtypes.gen.EnvDTE
StepPause = .2

def GetDTE(  ) :
  try:
    v = dte_settings.get("version", "11.0")
    objectName = "VisualStudio.DTE." + v
    return cc.GetActiveObject(objectName)
  except:
    return None

def GetBreakpoints( aView, aOn ) :
  dte = GetDTE()
  if dte :
    deb = dte.Debugger
    if deb.BreakPoints :
      return [ brk.FileLine
               for brk in deb.Breakpoints
               if ((aView.file_name() == brk.File) and (brk.Enabled == aOn))
             ]
  return [] #return an empty list.

def ShowBreakpoints( aView, aList, aType, aColor ) :
  aView.erase_regions(aType)
  if aList :
    g = lambda line: aView.line(aView.text_point(line - 1, 0))
    regs = [ g(line) for line in aList ]
    aView.add_regions(aType, regs, aColor, "dot", sublime.HIDDEN)

def UpdateBreakpoints( aView ) :
  if aView.file_name() and dte_settings.get("showbreakpoints") :
    bon = GetBreakpoints(aView, True)
    oncolor = dte_settings.get("bponcolor", "red")
    ShowBreakpoints(aView, bon, "breakon", oncolor)
    boff = GetBreakpoints(aView, False)
    offcolor = dte_settings.get("bpoffcolor", "gray")
    ShowBreakpoints(aView, boff, "breakoff", offcolor)

def SetFileAndLine( aDTE, aView ) :
  res = aDTE.ExecuteCommand("File.OpenFile", aView.file_name())
  if res == 0 :
    sel = aView.sel()[0]
    line, _ = aView.rowcol(sel.begin())
    line = line + 1
#    print "line %d" % (line)
    res = aDTE.ExecuteCommand("Edit.Goto", str(line))

#  print "res %d" % (res)
  return res

class PrintFileCommand( sublime_plugin.TextCommand ) :
  def run( self, edit ) :
    try:
      dte = GetDTE()
      if dte :
        res = SetFileAndLine(dte, self.view)
        if res == 0 :
          ad = dte.ActiveDocument
          #TODO: Make sure active document is the one we want to
          # print before sending the print command.
          if (ad and (ad.FullName == self.view.file_name())) :
            ad.PrintOut()
    except:
      sublime.status_message("PrintFile failed")

class DteToggleBreakpointCommand( sublime_plugin.TextCommand ) :
  def run( self, edit ) :
    try:
      dte = GetDTE()
      if dte :
        res = SetFileAndLine(dte, self.view)
        if res == 0 :
          dte.ExecuteCommand("Debug.ToggleBreakPoint", "")
          UpdateBreakpoints(self.view)
    except:
      sublime.status_message("ToggleBreakPoint failed")

class DteSetFileLineCommand( sublime_plugin.TextCommand ) :
  def run( self, edit ) :
    try:
      dte = GetDTE()
      if dte :
        SetFileAndLine(dte, self.view)
    except:
      sublime.status_message("SetFileAndLine failed")

class DteCommandCommand( sublime_plugin.TextCommand ) :
  def run( self, edit, command ) :
    try:
      dte = GetDTE()
      if dte :
        SetFileAndLine(dte, self.view)
        res = dte.ExecuteCommand(command, "")
    except Exception, ex:
      sublime.error_message(str(ex))

def SyncFileLine( aDTE, aWindow ) :
  doc = aDTE.ActiveDocument
  if doc :
    textDoc = doc.Object("TextDocument")
    sel = textDoc.Selection
    tp = sel.TopPoint
    line = tp.Line
    path = doc.FullName + ":" + str(line)
    vw = aWindow.open_file(path, sublime.ENCODED_POSITION)
    # This doesn't currently work.
    # if vw:
    #   while (vw.is_loading()) :
    #     pass
    #   UpdateBreakpoints(vw)

class DteStepIntoCommand( sublime_plugin.WindowCommand ) :
  def run( self ) :
    try:
      dte = GetDTE()
      if dte :
        deb = dte.Debugger
        if deb.StepInto(False) == 0 :
          time.sleep(StepPause)
          SyncFileLine(dte, self.window)
#        print "res %d" % (res)
    except:
      sublime.status_message("StepInto failed")

class DteStepOverCommand( sublime_plugin.WindowCommand ) :
  def run( self ) :
    try:
      dte = GetDTE()
      if dte :
        deb = dte.Debugger
        if deb.StepOver(False) == 0 :
          time.sleep(StepPause)
          SyncFileLine(dte, self.window)
#        print "res %d" % (res)
    except:
      sublime.status_message("StepOver failed")

class DteStepOutCommand( sublime_plugin.WindowCommand ) :
  def run( self ) :
    try:
      dte = GetDTE()
      if dte :
        deb = dte.Debugger
        if deb.StepOut(False) == 0 :
          time.sleep(StepPause)
          SyncFileLine(dte, self.window)
#        print "res %d" % (res)
    except:
      sublime.status_message("StepOut failed")

class DteSyncFileLineCommand( sublime_plugin.WindowCommand ) :
  def run( self ) :
    try:
      dte = GetDTE()
      if dte :
        SyncFileLine(dte, self.window)
    except:
      sublime.status_message("SyncFileLine failed")

class DteBreakUpdater(sublime_plugin.EventListener):
  def on_activated( self, view ) :
    UpdateBreakpoints(view)

class DtePickCmdCommand( sublime_plugin.WindowCommand ) :
  def run( self ) :
    #todo: Make a list of commands.
    try:
      dte = GetDTE()
      if dte :
        cmds = [ cmd.Name
                 for cmd in dte.Commands
                 if cmd != ""
               ]
        #Show Selection
        self.window.show_quick_panel(cmds, functools.partial(self.on_done, cmds))
    except:
      sublime.status_message("PickCommand failed")

  def on_done( self, aCommands, aIndex ) :
    if aIndex != -1 :
      try:
        dte = GetDTE()
        if dte :
          command = aCommands[aIndex]
          #Run command
          res = dte.ExecuteCommand(command, "")
          sublime.status_message(command + " returned " + str(res))
  #        print "%s" % aCommands[aIndex]
      except Exception, ex:
        sublime.error_message(str(ex))

