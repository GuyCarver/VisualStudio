#----------------------------------------------------------------------
# Copyright (c) 2013, Guy Carver
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.
#
#     * The name of Guy Carver may not be used to endorse or promote products # derived#
#       from # this software without specific prior written permission.#
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# FILE    VisualStudio.py
# BY      Guy Carver
# DATE    06/05/2013 09:06 PM
#----------------------------------------------------------------------

import sublime, sublime_plugin
import functools
import sys, os

packagepath = os.path.dirname(__file__)
#print(packagepath)
sys.path.append(packagepath + "/pywin32/win32")
sys.path.append(packagepath + "/pywin32/win32/lib")
sys.path.append(packagepath + "/pywin32")
import VisualStudio.pywin32.win32com.client as win32
import win32gui

dte_settings = None

StepPause = .2

def plugin_loaded(  ) :
  global dte_settings
  dte_settings = sublime.load_settings("VisualStudio.sublime-settings")

class MyDTE :
  def __init__( self, ExHandler = None ) :
    try:
      self.ex = ExHandler
      v = dte_settings.get("version", "11.0")
      objectName = "VisualStudio.DTE." + v
#      print "Getting DTE " + objectName
      #Might need to do this to ensure the com interface is generated.
      # win32.gencache.EnsureDispatch(objectName)
      self.dte = win32.GetActiveObject(objectName)
    except Exception as ve:
      if self.ex :
        self.ex(ve)
#      print ve
      self.dte = None

  def __enter__( self ) :
    return self.dte

  def __exit__( self, type, value, traceback ) :
    #If we had and exception pass to the handler.
    if value != None and self.ex != None :
      self.ex(value)
    return True

def GetAllBreakpoints(  ) :
  with MyDTE() as dte :
    return dte.Debugger.Breakpoints
  return [] #return an empty list.

def GetBreakpoints( aView, aOn ) :
  with MyDTE() as dte :
    deb = dte.Debugger
    if deb.BreakPoints :
      fname = aView.file_name()
      return [ brk
               for brk in deb.Breakpoints
               if ((fname == brk.File) and (brk.Enabled == aOn))
             ]
  return [] #return an empty list.

def ShowBreakpoints( aView, aList, aType, aColor ) :
  aView.erase_regions(aType)
  if aList :
    g = lambda line: aView.line(aView.text_point(line - 1, 0))
    regs = [ g(brk.FileLine) for brk in aList ]
    aView.add_regions(aType, regs, aColor, "dot", sublime.HIDDEN)

def UpdateBreakpoints( aView ) :
  if aView.file_name() and dte_settings.get("showbreakpoints") :
    bon = GetBreakpoints(aView, True)
    oncolor = dte_settings.get("bpointoncolor", "red")
    # print("On: " + str(len(bon)))
    ShowBreakpoints(aView, bon, "breakon", oncolor)
    boff = GetBreakpoints(aView, False)
    offcolor = dte_settings.get("bpointoffcolor", "gray")
    ShowBreakpoints(aView, boff, "breakoff", offcolor)

def SetFileAndLine( aDTE, aView ) :
  # print("filename " + aView.file_name())
  res = aDTE.ExecuteCommand("File.OpenFile", aView.file_name())
  if res == None :
    sel = aView.sel()[0]
    line, _ = aView.rowcol(sel.begin())
    line = line + 1
#    print "line %d" % (line)
    res = aDTE.ExecuteCommand("Edit.Goto", str(line))

  # print("res " + str(res))
  return res

class DteSelectBreakpointCommand( sublime_plugin.WindowCommand ) :
  def run( self ) :
    brks = GetAllBreakpoints()
    brkdata = [ b.File + ":" + str(b.FileLine) for b in brks ]
    self.window.show_quick_panel(brkdata, functools.partial(self.on_done, brkdata))

  def on_done( self, aBreaks, aIndex ) :
    if aIndex != -1 :
      path = aBreaks[aIndex]
      vw = self.window.open_file(path, sublime.ENCODED_POSITION)

class DteToggleBreakpointCommand( sublime_plugin.TextCommand ) :
  def run( self, edit ) :
    with MyDTE(lambda x : sublime.status_message("ToggleBreakPoint failed")) as dte :
      # print("Setting file and line.")
      res = SetFileAndLine(dte, self.view)
      if res == None :
        # print("ToggleBreakPoint")
        dte.ExecuteCommand("Debug.ToggleBreakPoint", "")
        # print("UpdatingBreakPoint")
        UpdateBreakpoints(self.view)

class DteSetFileLineCommand( sublime_plugin.TextCommand ) :
  def run( self, edit ) :
    with MyDTE(lambda x : sublime.status_message("SetFileAndLine failed")) as dte :
      # print("Setting fileandline")
      SetFileAndLine(dte, self.view)

class DteCommandCommand( sublime_plugin.TextCommand ) :
  def run( self, edit, command, syncfile = True, save = False ) :
    with MyDTE(lambda x : sublime.status_message(str(x))) as dte :
      if save and self.view.is_dirty():
        self.view.run_command("save")

      if syncfile :
        SetFileAndLine(dte, self.view)

      res = dte.ExecuteCommand(command, "")

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
    with MyDTE(lambda x : sublime.status_message("StepInto failed")) as dte :
      deb = dte.Debugger
      if deb.StepInto(False) == None :
        time.sleep(StepPause)
        SyncFileLine(dte, self.window)
#      print "res %d" % (res)

class DteStepOverCommand( sublime_plugin.WindowCommand ) :
  def run( self ) :
    with MyDTE(lambda x : sublime.status_message("StepOver failed")) as dte :
      deb = dte.Debugger
      if deb.StepOver(False) == None :
        time.sleep(StepPause)
        SyncFileLine(dte, self.window)
#      print "res %d" % (res)

class DteStepOutCommand( sublime_plugin.WindowCommand ) :
  def run( self ) :
    with MyDTE(lambda x : sublime.status_message("StepOut failed")) as dte :
      deb = dte.Debugger
      if deb.StepOut(False) == None :
        time.sleep(StepPause)
        SyncFileLine(dte, self.window)
#      print "res %d" % (res)

class DteSyncFileLineCommand( sublime_plugin.WindowCommand ) :
  def run( self ) :
    with MyDTE(lambda x : sublime.status_message("SyncFileLine failed")) as dte :
      SyncFileLine(dte, self.window)

class DteBreakUpdater(sublime_plugin.EventListener):
  def on_activated( self, view ) :
    UpdateBreakpoints(view)

class DtePickCmdCommand( sublime_plugin.WindowCommand ) :
  def run( self ) :
    #todo: Make a list of commands.
    def err( ex ) : sublime.status_message("PickCommand failed")
    with MyDTE(err) as dte :
      cmds = [ cmd.Name
               for cmd in dte.Commands
               if cmd.Name != ''
             ]
      print(cmds)
      #Show Selection
      self.window.show_quick_panel(cmds, functools.partial(self.on_done, cmds))

  def on_done( self, aCommands, aIndex ) :
    if aIndex != -1 :
      def err( ex ) : sublime.status_message(str(ex))
      with MyDTE(err) as dte :
        command = aCommands[aIndex]
        #Run command
        res = dte.ExecuteCommand(command, "")
        sublime.status_message(command + " returned " + str(res))
  #        print "%s" % aCommands[aIndex]

class FindWindowCommand(sublime_plugin.WindowCommand) :
  def run( self ) :
    self._handle = None
    wildcard = "80CC9F66-E7D8-4DDD-85B6-D9E6CD0E93E2x0x8x0"
#    wildcard = "Microsoft Visual Studio"
    win32gui.EnumWindows(self._window_enum_callback, wildcard)
    if self._handle != None:
      win32gui.BringWindowToTop(self._handle)

  def _window_enum_callback(self, hwnd, wildcard):
    if (win32gui.GetWindowText(hwnd) == wildcard) :
      self._handle = hwnd

class DteDirCommand( sublime_plugin.WindowCommand ) :
  def run( self ) :
    #todo: Make a list of commands.
    def err( ex ) : sublime.status_message("DteDirCommand failed")
    with MyDTE(err) as dte :
      print(dir(dte))

