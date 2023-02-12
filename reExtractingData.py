#Extracting phone numbers from string

import re        #re - regex or regular expression
no = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#inside compile func. we specify format of the phone number(\d represents integer and r stands for regular) 
num = "My Phone Number is 333-555-4444 ."
match = no.search(num)
#search func. search number in the given string in the format mentioned in compile func.
print(match)
print('Found a phone number :- ' , match.group())
#group func. is used to remove additional details and simply print out the number
string = '''In this string
we have a phone number
which is 333-333-3333
and we have another phone number 
which is 4444-444-4444 (which is in wrong format)'''
match = no.search(string)
print("Correct Number is :- " , match.group())
halfno = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')     #we simply divided phone number in 2 sections
match = halfno.search("My Phone Number is 333-555-4444 .")
print(match.group(1))      #prints 1st section i.e. 333
print(match.group(2))     #prints 2nd section i.e. 555-4444
print(match.group())       #prints all sections
code,number = match.groups()    #groups functions simply calls every section
#1st section is stored in code and 2nd section is stored in number
print("Code :- " , code , "\nPhone Number :- " , number)


#Extracting E-mails from string of another file

#import re     #already done above
file = open('email.txt','r')
text = file.read()            #storing emails in text variable by reading
match = re.findall(r'[\w.-]+@[\w.-]+.com',text)
print(match)
#selecting correct emails , findall func. is used to serch/store multiple lines or every match possible
#while search func. searches/stores only first match
#inside findall r - regular \w represents string ,which is read till @ comes then again a string and at last .com
#all strings which follows the above conditions are stored