import random

def choose():
	words = ['scheme','lisp','perl','pascal','java','python','html','php','fortran','cobol','ruby','javascript','c++','ada','amos','basic','c sharp','comtron','jython']
	pick = random.choice(words)
	return pick


def jumble(word):
	jumbled = "".join(random.sample(word,len(word)))
	return jumbled


def thank(pn1,pn2,p1,p2):
	print(pn1,"Your Score is :- ",p1)
	print(pn2,"Your Score is :- ",p2)
	if p1 > p2:
		print("Thus  ",pn1," Wins the game..")
	elif p2> p1:
		print("Thus  ",pn2," Wins the game..")
	else:
		print("Thus match is tied ..")
	print("Thanks for playing , have a nice day.")

	
def play():
	p1n = input("Player 1 enter your name :- ")
	p2n = input("Player 2 enter your name :- ")
	pp1 = 0
	pp2 = 0
	turn = 0
	
	while(1):
		picked_word = choose()
		qn = jumble(picked_word)
		print(qn)
		
		if turn%2 == 0:
			print(p1n," its your turn.")
			ans = input("What is on my mind?  :- ")
			if ans == picked_word:
				pp1 = pp1 + 1
				print("Correct ..")
				#print("Your Score is :- ",pp1)
			else:
				print("Wrong .. Answer was :- ", picked_word)
		
		else:
			print(p2n," its your turn.")
			ans = input("What is on my mind?  :- ")
			if ans == picked_word:
				pp2 = pp2 + 1
				print("Correct ..")
				#print("Your Score is :- ",pp2)
			else:
				print("Wrong .. Answer was :- ", picked_word)
		
		turn = turn + 1
		c = int(input("Press 0 to quit or any other number to continue :- "))
		
		if c == 0:
			thank(p1n,p2n,pp1,pp2)
			break

			
print("Lets play a game ...")
print("Game is simple , i.e. there are 2 players and a jumbled word would be given to the 1st player and ")
print("if player 1 rearranges it correctly then he/she will score a point and the same goes for player 2")
print("Both players can quit whenever they want")
print("#HINT   Word given will be a programming language...")
play()
