import random
#check
def check(n):
	f = [49,50,51,52,53,54]
	if(ord(n) in f):
		return True 			 
#batting
def user_bat(bob_first,bowling):
	options =[1,2,3,4,5,6]
	user_runs = 0
	user_number = 0
	random_number = 0
	s = True
	if bob_first == 0:
		while s:
			random_number = random.randint(1,6)
			print("\nEnter a number in between 1 to 6")
			user_number=input("\n\tEnter your runs: ")
			n = user_number
			if(check(n)):
				if int(random_number) == int(user_number):
					print("\nComputer Bowled: ",random_number)
					print("\nYou scored: ",user_number,"runs")
					print("\n\n YOU ARE OUT!")#out
					print("\n\t\t\t\t\t\t\t\t  YOUR TOTAL SCORE: ",user_runs)
					s = False
					break
				else:	
					print("\nComputer Bowled: ",random_number)
					print("\nYou scored: ",user_number,"runs")
					user_runs = int(user_runs)+int(user_number)
					print("\n\t\t\t\t\t\t\t\t  YOUR TOTAL SCORE: ",user_runs)
					continue
			else:
				print("Enter a number between 1 to 6!!!")					
	
	elif bob_first == 1:
		while s:
			random_number = random.randint(1,6)
			print("\nEnter a number in between 1 to 6")
			user_number= input("\n\tEnter your runs: ")
			n = user_number
			if(check(n)):
				if int(user_runs) > int( bowling):
					print("\n\t\tYou Won")
					s=False
					break
				if int(user_number) == int(random_number):
					print("\nComputer Bowled: ",random_number)
					print("\nYou scored: ",user_number,"runs")
					print("\n\n\t\t\t YOU ARE OUT!")#out
					print("\n\t\t\t\t\t\t\t\t  YOUR TOTAL SCORE: ",user_runs)
					if int(user_runs) < int(bowling):
						print("\n\t\tComputer won by",bowling - user_runs,"runs")
					elif int(user_runs) == int(bowling):
						print("\n\t\tThe match ended in draw....!!!")
					s=False
					break
				print("\nComputer Bowled: ",random_number)
				print("\nYou scored: ",user_number,"runs")
				user_runs = int(user_runs)+int(user_number)
				print("\n\t\t\t\t\t\t\t\t  YOUR TOTAL SCORE: ",user_runs)
				if int(user_runs) > int(bowling):
					print("\n\t\tYou Won")
					s=False
					break
				print("\nYou need ",(bowling+1)-user_runs,"runs to win\n\n")
				continue	
			else:
				print("\nEnter a number between 1 to 6")
		
	return user_runs

#bowling
def user_ball(bob_first,batting):
	options =[1,2,3,4,5,6]
	user_number = 0
	random_number = 0
	computer_runs = 0
	s = True
	if bob_first == 0:
		while s :
			random_number = random.randint(1,6)
			print("\nEnter a number in between 1 to 6")
			user_number= input("\n\tChoose your ball to ball: ")
			n=user_number
			if (check(n)):
				if int(computer_runs) > int(batting):
					print("\n\t\tComputer won")
					s = False
					break
				if int(user_number)== int(random_number):
					print("\nYou Bowled: ",user_number)
					print("\nComputer scored: ",random_number,"runs")
					print("\n\n\t\t\tCOMPUTER IS OUT!")#out
					print("\n\t\t\t\t\t\t\t\t  COMPUTER TOTAL SCORE: ",computer_runs)
					if int(computer_runs) < int(batting):
						print("\n\t\tYou won by",batting - computer_runs,"runs")
					elif int(computer_runs) == int(batting):
						print("\n\t\tThe match ended in draw...!!!")
					s = False
					break
				print("\nYou Bowled: ",user_number)
				print("\nComputer scored: ",random_number,"runs")
				computer_runs += int(random_number)
				print("\n\t\t\t\t\t\t\t\t  COMPUTER TOTAL SCORE: ",computer_runs)
				if int(computer_runs) > int(batting):
					print("\n\t\tComputer won")
					s = False
					break
				print("\nYou need ",(batting+1)-computer_runs,"runs to win\n\n")
				continue
			else:
				print("\nEnter a number between 1 to 6")	
				
	elif bob_first == 1:
		while s :
			random_number = random.randint(1,6)
			print("\nEnter a number in between 1 to 6")
			user_number= input("\n\tChoose your ball to ball: ")
			n = user_number
			if (check(n)):
				if int(user_number)== int(random_number):
					print("\nYou Bowled: ",user_number)
					print("\nComputer scored: ",random_number,"runs")
					print("\n\t\tCOMPUTER IS OUT!")#out
					print("\n\t\t\t\t\t\t\t\t  COMPUTER TOTAL SCORE: ",computer_runs)
					s=False
					break
				print("\nYou Bowled: ",user_number)
				print("\nComputer scored: ",random_number,"runs")
				computer_runs += int(random_number)
				print("\n\t\t\t\t\t\t\t\t  COMPUTER TOTAL SCORE: ",computer_runs)
				continue
			else:
				print("\nEnter a number between 1 to 6")
		
	return computer_runs
	
def play_again():		
	#tossing		
	print("\n\nTime for the toss :)")
	toss_play = random.randint(0,1)
	opt = ["h","t"]
	
	tossed =  opt[toss_play]
	toss = input("Enter h for HEADS or t for TAILS ").lower()

	while toss != "h" and toss != "t":
		print("enter h/t")
		toss = input("Enter h for HEADS or t for TAILS ").lower()
	s=True	
	while s:	
		if tossed == toss:
			print("you won the toss")
			
			while True:
				print("What do you choose?")
				bob = input("Bat or Bowl first:  ").lower()
				if bob == "bat":
					print("you choosed batting")
					bob_first = 0
					bowling = 0
					batting = user_bat(bob_first,bowling)
					print("\n\n\t\t\tComputer need ",batting+1,"runs to win")
					bowling = user_ball(bob_first,batting)
					s=False
					break
					
				elif bob == "bowl":
					print("you choosed bowling")
					bob_first = 1
					batting = 0
					bowling = user_ball(bob_first,batting)
					print("\n\n\t\t\tYou need ",bowling+1,"runs to win")
					batting = user_bat(bob_first,bowling)
					s=False
					break
		else:
			computer_toss =  random.randint(0,1)
			print("Computer won the toss")
			while True:
				if computer_toss== 0:
					print("Computer choose to bat first")
					bob_first = 1
					batting = 0
					bowling = user_ball(bob_first,batting)
					print("\n\n\t\t\tYou need ",bowling+1,"runs to win")
					batting = user_bat(bob_first,bowling)
					s=False
					break
				elif computer_toss== 1:
					print("Computer choose to bowl first")
					bob_first = 0
					bowling = 0
					batting = user_bat(bob_first,bowling)
					print("\n\n\t\t\tComputer need ",batting+1,"runs to win")
					bowling = user_ball(bob_first,batting)
					s=False
					break
				
	print("\n\nThanks for playing....")
	while True:
		print("Do you want to play again...")
		again = input("Enter 'y' to continue or enter any key to exit: ").lower()
		if again == "y":
			print("Come let's play!")
			play_again()
		else:
			print("See you next time.....")
			quit()
		
#introduction
def toss ():
	print("Welcome to IN OR OUT")
	while True:
		play = input("Do you want to continue....Enter y/n ").lower()

		if play == "n":
			print("See you next time...")
			quit()
			
		elif play == "y":
			print("Come let's play!")
			play_again()
			break
		
		else:
			print("Enter y/n")
			continue
toss()
