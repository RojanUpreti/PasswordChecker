import hashlib
import sys

for h,count in hashes:
	if h==hash_to_check:
		return count
return 0

def pwned_api_check(password):
	sha1_password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	return sha1_password

def main(args):
	for password in args:
		count==pwned_api_check(password)
		if count:
			print(f'{password} was found {count} times..you should probably change it')
		else:
			print(f'{password} was NOT found')
	return 'done'

main(sys.argv[1:])

#python passwordchecker.py rojan88