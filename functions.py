
#functions should be named in lowercase. Underscores should be used for variables with more than one word.

def say_hi():
    print("Hello User")

print("Top")
say_hi()
print("Bottom")

#function with parameters
def sayhi(name, age):
    print("Hello " + name + ", you are " + str(age) + ".")

sayhi("Mike", 35)
sayhi("Steve", 70)

