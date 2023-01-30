# login-website-test
Testing website logging in via password

Version 2 of log in webpage. 

# Improvements and changes
1. Passwords are now stored in hash
2. Added usage of cookies in order to allow the user to bypass the login screen as long as the cookie has the correct password value.
3. Added a proper index page with a command line interface that one can type in.

# Changes in v2.1
1. Brute-force protection that will help slow down most brute-force attacks. Blocks user from logging in past the 10th attempt.
2. Added `remove_password()` command, an example of usage would be `remove_password("password")` with `password` of course being the password to be removed.

# Information
The passwords that you may use to log in are:
1. password
2. password2

Once you are logged in, snippets of code such as `print()` will work. You may use `add_password("pass")` to add a password, replacing `pass` with the password.

# I am aware of
1. The insecurity of using `in` whenever checking if the inputted password's hash is equivalent to the hash of accepted passwords. This was not designed for high-level security and is just a small project and that the issue creates a possible gap in security.
2. Brute-force is weak, however it should help slow down brute-force attacks.
