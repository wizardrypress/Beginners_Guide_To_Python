# Exercise 2: Scope and Lifetime

total = 0

def modify_global():
    global total
    total += 10

def use_local():
    total = 5
    print("Local total:", total)
