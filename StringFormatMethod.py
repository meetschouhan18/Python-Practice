# s – strings
# d – decimal integers (base-10)
# f – floating point display
# c – character
# b – binary
# o – octal
# x – hexadecimal with lowercase letters after 9
# X – hexadecimal with uppercase letters after 9
# e – exponent notation

# <   :  left-align text in the field
# ^   :  center text in the field
# >   :  right-align text in the field


# ex1
name = "Meet"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
#or
print("Your lucky number is {num}, {name}.".format(name = name , num = number))


#ex2 - formatting expression #decimal
price = 7.5
with_tax = price * 1.09
print("Base price: {:.2f}. With Tax: {:.2f}".format(price , with_tax))


# ex3 - number conversion - decimal to binary,octal & hexa
print("decimal to every form :- ")
print("The binary of 100 is {:b}".format(100))
print("The octal of 100 is {:o}".format(100))
print("The hexa(in lower case) of 1000 is {:x}".format(1000))
print("The hexa(in upper case) of 1000 is {:X}".format(1000))


# ex4 - alignment of text
print("Sam has {:<4} red {:^16}! so he is {:>6}".format(5 , "balloons", "happy"))
# 5 is printed then 3 spaces (in <4)
# balloons is printed in middle of 16 digits(in ^16)
# in 6 digits place 5 places are taken by happy and the last left place is printed by space in left(in >6)
print("Sam has {:*<4} red {:$^16}! so he is {:&>6}".format(5 , "balloons", "happy"))
#given characters are printed in place of space


# ex5 - alignment of numbers 
#same as aligning text just use d
for i in range(3,11):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))
#first colums is given 3 places to print
#second column is given 4 places to print
#similarly third column is given 5 places to print