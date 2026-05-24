# a215_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# minimum and maximum length of username and password
min_len = 8
max_len = 24

# validate length of username
username = ""
while (len(username) < min_len or len(username) > max_len):
   print("Usernames must be between 8 and 20 characters long.")
   username = input("Enter the username for the Restricted App: ")

# validated length of password and that it contains at least one digit and an alphabetic character
pw = ""
digit = False
alpha = False
while (not digit or not alpha or len(pw) < min_len or len(pw) > max_len):
   print("Passwords must be between 8 and 20 characters long and contain at least one letter and number.")
   pw = input("Enter the password for the Restricted App: ")
   digit = False
   alpha = False
   for c in pw:
      if c.isdigit():
         digit = True
      elif c.isalpha():
         alpha = True

# create a multi-factor interface to a restircted app
my_auth = mfg.MultiFactorAuth()

my_auth.set_authentication("administrator3","1StrongPassword4CSP")
# confirm authentication info
auth_info = my_auth.get_authentication_info()
print(auth_info)

# set the users multi-factor authentication information
question = "What is your favorite color?"
answer = "purple"
my_auth.set_multiFactorAuthentication(question, answer)

# start the GUI
my_auth.mainloop()
