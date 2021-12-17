
import getpass, string, random

def passwordValidator():
    # display rules that a password must conform to
    print('\nYour password should: ')
    print('\t- Have a minimum length of 6;')
    print('\t- Have a maximum length of 12;')
    print('\t- Contain at least an uppercase letter or a lowercase letter')
    print('\t- Contain at least a number;')
    print('\t- Contain at least a special character (such as @,+,£,$,%,*^,etc);')
    print('\t- Not contain space(s).')

    userPassword = getpass.getpass('\nEnter a valid password: ').strip()

    if not(len(userPassword) >= 12):
        message = "Invalid Password... Your password should have a minimum. "
        message += "Minimum length required 12. "
        return message
    if ' ' in userPassword:
       message = 'Invalid Password... Your password shouldn\'t contain space(s). '
       return message
    if not any(i in string.ascii_letters for i in userPassword):
       message = 'Invalid Password..your password should contain at least. '
       message += 'an uppercase letter and a lowercase letter. '
       return message
    if not any(i in string.digits for i in userPassword):
        message = 'Invalid Password..your password should contain at least a number. '
        return message
    if not any(i in string.punctuation for i in userPassword): 
       message = 'Invalid Password..your password should contain at least a special character. '
       return message
    else:
        return "Valid Password!"

def checkPasswordStrength():
    password = passwordValidator()
    print(password)

def generateRandomPassword():
	alphabets = list(string.ascii_letters)
	digits = list(string.digits)
	special_characters = list("!@#$%^&*()")
	characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

	length = int(input("Enter password length: "))

	alphabets_count = int(input("Enter alphabets count in password: "))
	digits_count = int(input("Enter digits count in password: "))
	special_characters_count = int(input("Enter special characters count in password: "))

	characters_count = alphabets_count + digits_count + special_characters_count

	if characters_count > length:
		print("Characters total count is greater than the password length")
		return

	password = []
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))

	for i in range(digits_count):
		password.append(random.choice(digits))

	for i in range(special_characters_count):
		password.append(random.choice(special_characters))

	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))

	random.shuffle(password)
	print("".join(password))