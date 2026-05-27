print("Hello\nWorld")
print("\tPython")

# rstrip() right space delete
# lstrip() left space delete
# strip() all space delete
favorite_language = "python "
print(favorite_language.rstrip())

# removeprefix()
url = "https://nostarch.com"
print(url.removeprefix("https://"))

# Numbers
universe_age = 14_000_000_000
print(universe_age)

# Constant
MAX_CONNECTIONS = 5000 

# 2-3. Personal Message: Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.
name = "ada loveless"
print(name.lower())
print(name.upper())
print(name.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, 
# “A person who never made a mistake never tried anything new.“
print('Albert Einstein once said, "A person who never made a mistake never tried anything new"')

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous
# person’s name using a variable called famous_person. Then compose your message 
# and represent it with a new variable called message. Print your message.
famous_person = "Albert Einstein"
print(f'{famous_person} once said, "A person who never made a mistake never tried anything new"')

# 2-8. File Extensions: Python has a removesuffix() method that works exactly
# like removeprefix(). Assign the value 'python_notes.txt' to a variable called
# filename. Then use the removesuffix() method to display the flename without
# the fle extension, like some fle browsers do.
filename = "python_note.txt"
print(filename.removesuffix(".txt"))

# 2-9. Number Eight: Write addition, subtraction, multiplication, and division
# operations that each result in the number 8. Be sure to enclose your operations
# in print() calls to see the results. You should create four lines that look like this:
# Exp: print(5+3)
# Your output should be four lines, with the number 8 appearing once on each line.
print(5 + 3)
print(10 - 2)
print(4 * 2)
print(16 / 2)

# 2-10. Favorite Number: Use a variable to represent your favorite number. Then,
# using that variable, create a message that reveals your favorite number. Print
# that message.
favortie_number = 1216
print(f"My favorite number is {favortie_number}.")

# 2-12. Zen of Python: Enter import this into a Python terminal session and skim
# through the additional principles.
import this

