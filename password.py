import random
import string
def password(len):
	if len<4:
		return "password must be 4 letter.."
	ch=string.ascii_letters+string.digits+string.punctuation
	pas=''.join(random.choice(ch)  for _ in range(len) )
	return pas
try:
	len=int(input("Enter to password length:"))
	pas=password(len)
	print("Generated password:",pas)
except ValueError:
	print("Please enter a valid number..")