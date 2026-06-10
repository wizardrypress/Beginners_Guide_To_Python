# Exercise 2: Scope and lifetime
# Ye example global variable aur local variable ka difference dikhata hai.

total = 0


def modify_global():
    global total
    total += 10


def use_local():
    total = 5
    print("Local total:", total)


print("Global total pehle:", total)

modify_global()
print("Global total baad me:", total)

use_local()
print("Final global total:", total)
