import webbrowser , sys
# webbrowser allow us to browse and sys is used in order to specify the arguments 

#we are taking address and showing it on google maps

#address = ' '.join(sys.argv[1:])
#above code simply takes address while opening our file in command prompt
#for ex we write in command prompt - Web.py India where Web.py is file name and India is our address
#join is used to add the argument specified by the user in the command itself
#join joins the command with empty string and in join we mentioned sys.argv which stands for multiple arguments
#we use slicing in argv because while joining command is printed prior to our reqired address
#and we only need address . thus we remove command and take proper address to the last
#Or Simply Just do as done below


address = input("Enter address :- ")
webbrowser.open('https://www.google.com/maps/place/' + address)