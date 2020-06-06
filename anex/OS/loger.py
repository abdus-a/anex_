def log__(file, log_text):
	with open(file, 'a') as f:
		f.write(log_text)
		f.close()


