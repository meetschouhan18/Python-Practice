# Filter

Q1.) Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that only contains the strings from countries that begin with B.

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = filter(lambda k : k.startswith('B'), countries)

#filter function take 2 arguments
# 1st is a function which tells the condition
# 2nd is the list in which operation is to be done
# it works as -
# it tests whether the condition is true or not, if true element gets added, else neglected

# for ex in this case
# function checks whether string starts with b or not
# if it does, the string is added, else neglected

Q2.)Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each.

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
l3 = zip(l1, l2)
opposites = filter(lambda k : len(k[0]) > 3 and len(k[1]) > 3, l3)
