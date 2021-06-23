import parent
#print(locals())
print(parent.square(10))
print("I'm the child:",__name__)
print("My parent is:",parent.__name__)