from sys import argv
# close – Closes the file. Like File->Save.. in your editor.
# • read – Reads the contents of the file. You can assign the result to a variable.
# • readline – Reads just one line of a text file.
# • truncate – Empties the file. Watch out if you care about the file.
# • write('stuff') – Writes ”stuff” to the file.
# • seek(0) – Move the read/write location to the beginning of the file.
script, filename = argv

# txt = open(filename)

# print(f"Here's your file {filename}")
# try:
#   print(txt.read())
#   file_again = input("> ")
#   txt_again = open(file_again)
#   print(txt_again.read())
# except Exception as e:
#   print(str(e))
txt = open(filename, "")
