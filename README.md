# login-website-test
Testing website logging in via password

Version 2 of log in webpage. 

# Improvements-and-changes
1. Passwords are now stored in hash
2. Added usage of cookies in order to allow the user to bypass the login screen as long as the cookie has the correct password value.
3. Added a proper index page with a command line interface that one can type in.

# Information
The passwords that you may use to log in are:
1. password
2. password2

Once you are logged in, snippets of code such as `print()` will work. You may use `add_password("pass")` to add a password, replacing `pass` with the password.

# I-am-aware-of
1. The insecurity of using `in` whenever checking if the inputted password's hash is equivalent to the hash of accepted passwords. This was not designed for high-level security and is just a small project and that the issue creates a possible gap in security.
