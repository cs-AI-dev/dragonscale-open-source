import os
import blessed as gui

def executeSubroutine(name, *args):
	with open(__file__ + "system/subroutines/sr_" + name, "r") as f:
		exec(f.read())
	runSubroutine(*args)

