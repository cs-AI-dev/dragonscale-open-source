import os
from blessed import Terminal

def listtostring(l):
	o = ""
	for x in l:
		o = o + x
	return o

def runSubroutine():
	print("Subroutine run")

def executeSubroutine(name, *args):
	with open(__file__[:-10] + "system/subroutines/sr_" + name + ".py", "r") as f:
		exec(f.read())
	runSubroutine(*args)

def getSystemInfo(name):
	o = ""
	with open(__file__[:-10] + "system/" + name + ".syin", "r") as f:
		o = f.read()
	return o

# System subroutines
class subroutine:
	def createNewUser(username, password, permissions="Default"):
		fdir = __file__.split("/subroutines/sr_newuser.py")[0] + "/users/" + username + ".user", "x"
		with open(fdir, "x") as f:
			pass
		with open(fdir, "w") as f:
			encryptedPass = executeSubroutine("nkc", password)
			f.write(f"username:{username};password:{encryptedPass};permissions:{permissions}")

	def nkc(raw):
		cipherBase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "\\", "|", ";", ":", "\'", "\"", ",", "<", ".", ">", "/", "?", "`", "~"]

		newCipher = []
		for chara in list(raw):
			if not chara in newCipher:
			  newCipher.append(chara)

		for chara in cipherBase:
			if not chara in newCipher:
				newCipher.append(chara)

		step1 = ""
		for chara in list(raw):
			for x in range(len(cipherBase)):
				if chara == cipherBase[x]:
					step1 = step1 + newCipher[x]

		step2 = ""
		for x in range(len(list(step1))):
			if x < 3:
				step2 = step2 + list(step1)[x]
			elif x % 2 == 0:
				step2 = step2 + list(step1)[x - 3]
			else:
				step2 = step2 + list(step1)[x]

		encrypted = ""
		for x in list(step2):
			encrypted = encrypted + format(
				(int(str(ord(x)), 16) ^ int(len(raw))) * int(hex(len(raw)), 16), "x"
				)

		return encrypted

term = Terminal()

username = None
password = None

print(term.clear())
[print(" ") for x in range(int(term.height / 2) - 5)]
print(term.black_on_lime(term.center(getSystemInfo("systemName").strip())))
with term.location(int(term.width / 2) - 20, int(term.height / 2) - 2):
	username = input("Username: ")
if not username.lower() == "guest":
	with term.location(int(term.width / 2) - 20, int(term.height / 2) - 2):
		print("Password: " + listtostring(" " for x in range(len(username))))
	with term.location(int(term.width / 2) - 20, int(term.height / 2) - 2):
		password = input("Password: ")

	all_users = []
	for filedir in os.listdir(__file__[:-10] + "/system/users"):
		with open(__file__[:-10] + "system/users/" + filedir, "r") as f:
			data = f.read().split(";")

else:
	print(term.clear())
	print(term.black_on_lime(term.center("SIGNED IN AS GUEST")))
