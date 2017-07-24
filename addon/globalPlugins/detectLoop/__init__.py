#Window utility scripts for NVDA

# For LoopDetector
# Created by Hritik Gupta

# Select a line in your code and press NVDA+h
# NVDA speaks out whether its a for/while loop

import globalPluginHandler
import ui
import versionInfo
import api
import textInfos
import speech
import globalVars
import re
from NVDAObjects import NVDAObject, NVDAObjectTextInfo
from NVDAObjects.IAccessible import IAccessible
from NVDAObjects.window.scintilla import Scintilla

class randClass(IAccessible):
	def script_detect(self, gesture):
		obj=api.getFocusObject()
		try:
			info=obj.makeTextInfo(textInfos.POSITION_SELECTION)
		except (RuntimeError, NotImplementedError):
			info=None
		if not info or info.isCollapsed:
			speech.speakMessage(_("No selection"))
		else:
			selected = info.text
			k = info.text.split(" ")
			countIndent = 0
			ctr = 0
			for i in range(0, len(k)):
				if k[i] == "for":
					for j in range(i, len(k)):
						if k[j] == "in":
							flag = 1
							countIndent = re.search('\S', selected).start()
							ui.message("For loop starts")
				elif k[i] == "while":
					ui.message("While loop starts")

	__gestures = {
		"kb:NVDA+h":"detect"
	}



class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def chooseNVDAObjectOverlayClasses(self,obj,clsList):
		if obj.windowClassName == u'Scintilla' and obj.windowControlID == 0:
			clsList.insert(0, randClass)


