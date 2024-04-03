str = "!!!Jitendriya Meher!!!"
print(str)

print(len(str))

print(str.upper())
print(str.lower())

print(str.strip("!"))
print(str.rstrip("!"))
print(str.strip("!").rstrip("!"))

print(str.replace("ten","eleven"))

print(str.split(" "))

blog = "jiten tO AmIt"
print(blog.capitalize())

print(str.center(50))

print(str.count("e"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

print(str1.find("Daniel"))

print(str1.index("Dan"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())

print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())