import re
# | 
r = re.compile(r'Hello|World')
# | is used in between and it prints which ever strings of the strings mentioned and leaves the rest
# in this case in or string - s Hello comes before World .thus Hello is printed leaving the second string(world)
s = "Hello World"
print(r.search(s).group())

# ?
r = re.compile(r'bas(ket)?ball')
# string present in paranthesis in front of ? is optional
s = 'I love basball'
q = 'basketball'
print(r.search(s).group())
print(r.search(q).group())

#range
vowel = re.compile(r'[aeiouAEIOU]')
s = 'Today I dont feel ## LIKE @@@ d...oing anything'
print(vowel.findall(s))                 #prints all characters present in vowel and in s
r = re.compile(r'[a-zA-Z0-9]')    #here we set range i.e. a to z ,A to Z and 0 to 9
print(r.findall(s))                        #prints everything in range

# ^,$
r = re.compile(r'^Hello')                   #^ means start with i.e. it stores Hello only if the string begins with Hello
print(r.search('Hello World').group())      #Prints Hello
#print(r.search('world Hello').group())    #Error since string does not start with Hello
r = re.compile(r'\d$')           #$ means ends with i.e. in this case it stores integer only if string end with integer
print(r.search('No. of apples are 4').group())
#print(r.search('No. of apples are 4.').group())   #Error since string ends with . ,not 4

# .
r = re.compile(r'.ad')     #it will store words(3 aplhabets including 'a','d') ending with ad
print(r.findall('Bad Sad Glad Mad had cat'))

#split
string = 'Twelve:12 Eighty nine:89..'
pattern = '\d+'     #\d means integer , it means spliting should be done when integer occurs
result = re.split(pattern,string)  #it means keeping pattern in mind string will be splitted
print(result)

#sub, subn
string = 'abc12\
de 23   \n    f45  6'
print(string)
pattern = '\s+'  #\s means whitespace
r = '$'
new = re.sub(pattern, r, string)  #it means find pattern(space) in string and replace it with r
print(new)     #every space in string is replaced by $
new = re.subn(pattern, r, string) #it creates a tuple with 2 elements i.e. 1st our result and 2nd no. of time replacing is done
print(new)