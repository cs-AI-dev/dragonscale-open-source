def executeSubroutine(username, password, permissions="Default"):
	fdir = __file__.split("/subroutines/sr_newuser.py")[0] + "/users/" + username + ".user", "x"
	with open(fdir, "x") as f:
		pass
	with open(fdir, "w") as f:
		encryptedPass = executeSubroutine("nkc", password)
		f.write(f"username:{username};password:{encryptedPass};permissions:{permissions}")
