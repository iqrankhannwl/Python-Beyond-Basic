# Variables and Memory
a = 10
print(id(a))
print(a.__dir__())

# when two or more variable have same value that is less them 256 the memory address of all variable is same
a = 236
b = 256
print(id(a), id(b))
