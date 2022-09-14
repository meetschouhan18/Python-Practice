original = input()
original = original.lower()
a = original.split()
new_original = "".join(a)
reverse = new_original[::-1]
if reverse == new_original:
    print("Palindorme")
else:
    print("Nope")