# Sublime Text VisualStudio Plugin

## Install

GitHub location

    $ https://github.com/GuyCarver/VisualStudio

## Instructions

### Settings:
* version = "9.0". "10.0" or "11.0" etc.  As of this writing VS2012 still uses "11.0"
* "showbreakpoints" - Since this queries vs every time a view gains focus it may be a bit slow.
* "detect_slow_plugins" = false by default because the interface to EnvDTE is often slow enough to trigger this. If "showbreakpoints" is false this may also be false.
* "bponcolor" = "red".  This is a colorscheme context.  The default "red" value does not exist in most schemes.  See below for instructions on adding it.
* "bpoffcolor" = "gray". Like the on color this default color does not exist in most schemes.

### ColorScheme customization:
* Edit whichever color scheme you use, find the <dict> entries near the end for Comment, String or Storage and add the following anywhere within this group.

###
	<dict>
		<key>name</key>
		<string>Red</string>
		<key>scope</key>
		<string>red</string>
		<key>settings</key>
		<dict>
			<key>foreground</key>
			<string>#FF0000</string>
		</dict>
	</dict>
	<dict>
		<key>name</key>
		<string>Gray</string>
		<key>scope</key>
		<string>gray</string>
		<key>settings</key>
		<dict>
			<key>foreground</key>
			<string>#808080</string>
		</dict>
	</dict>

### Sending Visual Studio Commands:
* The "dte_command" takes a "command" argument string which may be any command in Visual studio that can be bound to a key.  To find a list of these command edit the key bindings in visual studio and browse your options for the commands.  The most useful commands are under "Build." and "Debug."

### Stepping:
* I have step in, over and out commands.  They attempt to keep the view synchronized but since I have no way of determining when the step command has finished I don't know when it is time to update the view.  I have a default delay of .2 seconds which is still not sufficient, but any longer of a wait is annoying.

### dte_pick_cmd:
* This shows a quick panel with a list of commands to select from.  Collection the command list is extremely slow so I do not suggest using this except to browse available commands for sending to "dte_command".
