
def login(username, password):
	try:
		user_file = open('/etc/users.txt')
		user_buf = user_file.read()
		users = [line.split("|") for line in user_buf.split("\n")]
		if [username, password] in users:
			return True
		else:
			return False
	except Exception as e:
		print("I can't authenticate you.")
		return False
