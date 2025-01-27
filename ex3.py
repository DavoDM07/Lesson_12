#Write a Python program to check whether a given string is number or
#not using Lambda.
#from curses.ascii import isdigit


is_number = lambda s: s.replace('.', '', 1).isdigit()
test_strings = ["123", "45", "abc", "12", "-789", "0"]
for s in test_strings:
    print(is_number(s))
