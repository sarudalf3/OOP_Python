local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

if __name__ == "__main__":
    print("File is directly executed")
else:
    print(".The file has the name: ", __name__)

# in the same file, add the following below the User class
if __name__ == "__main__":
    print(square(5))
    user = User("Anna")
    print(user.name)
    print(user.say_hello())
    #print(locals())
    print("I'm the parent:",__name__)