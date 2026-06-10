# Exercise 06: Comparison and logical operators

age = int(input("Apni age enter karein: "))

if age < 0:
    print("Age negative nahi ho sakti.")
elif age < 13:
    print("Aap child category mein hain.")
elif age >= 13 and age < 20:
    print("Aap teenager category mein hain.")
elif age >= 20 and age < 60:
    print("Aap adult category mein hain.")
else:
    print("Aap senior category mein hain.")
