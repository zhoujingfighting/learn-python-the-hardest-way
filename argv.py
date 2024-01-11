from sys import argv

# Read the WYSS section from how to run this

[script, first, second, third] = argv

print("The script is called: ", script)
print("The first variable is: ", first)
print("the second variable is: ", second)
print("The third variable is: ", third)

'''
leran-python-the-hardest-way git:(master) ✗ python3 argv.py first second third
The script is called:  argv.py
The first variable is:  first
the second variable is:  second
The third variable is:  third
'''