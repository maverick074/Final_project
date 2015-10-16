import time
import random


#introduction & welcome messages
player_name = "Laura"
print "let's play baccarat,", player_name #move
time.sleep(4) 
player_buyin= 100
print "Here is your buy in money", player_buyin
time.sleep(2)
print "good luck!!!"
time.sleep(4)



player_bet = input("how much do you want to bet? ")
time.sleep(2)
#player_bet = 20
time.sleep(2)
print "you bet %d dollars, great!" % player_bet
time.sleep(2)

#drawing cards
player_1=random.choice(range(1,10))
player_2=random.choice(range(1,10))
player_3=random.choice(range(1,10))


banker_1= random.choice(range(1,10))
banker_2= random.choice(range(1,10))
banker_3=random.choice(range(1,10))

player_wins = True

	
	

def deal_cards(player_name, player_1, player_2, banker_1, banker_2):
	
	print "hi", player_name, "Your first card is ", player_1
	time.sleep(2)
	print "the banker's first card is ", banker_1
	
	time.sleep(2)
	print player_name, "your next hand is ", player_2
	time.sleep(2)
	print player_name, "your two cards are: ", player_1, "and", player_2
	time.sleep(2)
	
	print "the banker's next hand is ", banker_2
	time.sleep(2)
	print "the banker's two cards are: ", banker_1, "and", banker_2
	time.sleep(2)


def add_player_cards_together(player_1, player_2):
	player_total = player_1 + player_2
	print "your total is ", player_total
	time.sleep(2)
	return player_total

def add_banker_cards_together(banker_1, banker_2):
	time.sleep(2)
	banker_total = banker_1 + banker_2
	print "the banker's total is ", banker_total
	time.sleep(2)
	return banker_total


def is_nine(player_total, banker_total, player_wins):
	if player_total or banker_total == 9:
		if player_total == 9 and banker_total != 9:
			print "you win!",player_name
			player_wins = True
			return player_wins
			
		if banker_total == 9 and player_total != 9:
			print "banker wins! Sorry,", player_name
			player_wins = False
			return player_wins
			
		if banker_total and player_total == 9:
			print player_name, "and banker are tied"
			print "player wins money"
			player_wins = True
			return player_wins
	

		

def lessthan_nine(player_total, banker_total, player_wins):
	if banker_total > 5 and banker_total < 9 or player_total > 5 and player_total < 9:
	
		if player_total > 5 and player_total < 9:
			if player_total == banker_total:
				print player_name, "and banker are tied"
				print "player wins money"
				player_wins = True
				return player_wins
				
			
		if player_total >5 and player_total < 9: 
			if player_total > banker_total:
				player_wins = True
				print "you win!",player_name
				return player_wins
					
		
		if player_total > 5 and player_total <9:
			if player_total < banker_total:
				print "banker wins! Sorry,", player_name
				player_wins = False
				return player_wins
		
	
		
def lessthan_five(player_total, banker_total, player_wins):
	if player_total < 5: 
		player_total = player_total
		third_draw = player_3
		third_draw_total = player_3 + player_total
		
	if banker_total <5:
	 	banker_3 = banker_3
		banker_third_total = banker_total + banker_3

	if player_total < 5 and banker_total < 9:
		print "your total is less than 5, please draw again", player_name
		time.sleep(1)
		print "your have ", player_1 , "and", player_2
		print "your third card is", player_3
		time.sleep(1)
		print "the total of 3 cards is", third_draw_total
		
		if third_draw_total < banker_total:
			print "you lose"
			player_wins = False
			return player_wins
		
		
		if third_draw_total == banker_total:
			print "you tied!"
			print "you win money!"
			player_wins = True
			return player_wins
			
		
		if third_draw_total > banker_total:
			print "you win!"
			player_wins = True
			return player_wins
			
	
	if banker_total < 5 and player_total< 9 and player_total > 5:
		print "The Banker total is less than 5, Banker will draw again", banker_3
		time.sleep(1)
		print "The Banker has ", banker_1 , "and", banker_2
		print "The Banker's third card is", banker_3
		time.sleep(1)
		print "the total of 3 cards is", banker_third_total
	
		if banker_third_total < player_total:
			player_wins = True
			print "you win!"
			return player_wins
		
		if banker_third_total > player_total:
			print "banker wins"
			player_wins = False
			return player_wins
		
	if player_total < 5 and banker_total <5:	
		third_draw_total = player_3 + player_total
		if third_draw_total > banker_third_total and third_draw_total < 9:
			
			print "You win!"
			player_wins = True
			return player_wins
			
			
		if banker_third_total > third_draw_total  and banker_third_total < 9:
			print "You Lose!"
			player_wins = False
			return player_wins
			
		if banker_third_total == third_draw_total:
			print "You win!"
			player_wins = True
			return player_wins
		
	
		
	
def greaterthan_nine(player_total, banker_total, player_wins):
	
	if  player_total > 9 or banker_total > 9:
		if player_total > 9  and banker_total < 9:
			player_final = player_total - 10
		
			print "your total is greater than 9!"
			print "we need to drop the 1"
			print player_name, "your new total is", player_final
			
			if player_final < banker_total and banker_total < 9:
				print "you lose"
				print "you have", player_final, "and", "the banker has", banker_total
				player_wins = False
				return player_wins
				
				
			if player_final > banker_total and banker_total < 9:
				print "you win"
				print "you have", player_final, "and", "the banker has", banker_total
				player_wins = True
				return player_wins
				
			if player_final == banker_total:
				print "you tied, so you win!"
				print "you have", player_final, "and", "the banker has", banker_total
				player_wins = True
				return player_wins
				
		
		if  banker_total > 9 and player_total < 9:
			banker_final = banker_total - 10
			print "the banker's total is greater than 9!"
			print "we need to drop the 1"
			print "the banker's new total is", banker_final
		
			if banker_final > player_total:
				print "you have", player_total, "and", "the banker has", banker_final
				print "sorry ", player_name, "banker wins!!"
				player_wins = False
				return player_wins
					
				
			if banker_final < player_total:
				print "you have ", player_total, "and", "the banker has", banker_final
				print "you win"
				player_wins = True
				return player_wins
		
		if player_total > 9 and banker_total > 9:
			player_final = player_total - 10
			banker_final = banker_total - 10
			
			if player_final > banker_final and player_final <9:
				print "your final hand is:", player_final, "the banker's final hand is: ", banker_final
				print "you win"
				player_wins = True
				return player_wins
				
				
			if banker_final > player_final and banker_final < 9:
				print "your final hand is:", player_final, "the banker's final hand is: ", banker_final
				print "sorry ", player_name, "banker wins!!"
				player_wins = False
				return player_wins
	
				
			if  player_final == 9 and banker_final !=9:
				print "you win"
				print "you have a 9! You win"
				player_wins = True
				return player_wins
				
			
			if 	banker_final == 9 and player_final !=9:
				print "banker has 9"
				print "sorry ", player_name, "banker wins!!"
				player_wins = False
				return player_wins
		
			
			if player_final == banker_final:
				print player_name, "and banker are tied"
				print "player wins money"
				player_wins = True
				return player_wins
	
	
		
	
	
def money(player_buyin, player_wins):
	
	if player_wins == True:
		player_buyin = player_buyin + player_bet 
		return player_buyin

	if player_wins == False:
		player_buyin = player_buyin - player_bet
		return  player_buyin


	
def play_again(player_buyin, player_wins):
	
	player_buyin = money(player_buyin, player_wins)
	
	while player_buyin > 0:
		player_buyin = money(player_buyin, player_wins)
		print "you have", player_buyin, "dollars left"
		play_more = raw_input("do you want to play again? y/n ")
	
		if play_more == 'y':
			player_bet = input("how much do you want to bet? ")
			deal_cards(player_name, player_1, player_2, banker_1, banker_2)
			player_total = add_player_cards_together(player_1, player_2)
			banker_total = add_banker_cards_together(banker_1, banker_2)
			player_wins=is_nine(player_total,banker_total, player_wins)
			player_wins=lessthan_five(player_total,banker_total, player_wins)
			player_wins=greaterthan_nine(player_total,banker_total, player_wins)
			player_buyin = money(player_buyin, player_wins)
		
	

		if play_more == 'n':
		   print "you're going home with", player_buyin, "dollars"
		   print "come back soon!"
		   exit()

	else:
		print "you're broke."
		print "go home."
			
			

	
	
deal_cards(player_name, player_1, player_2, banker_1, banker_2)
player_total = add_player_cards_together(player_1, player_2)
banker_total = add_banker_cards_together(banker_1, banker_2)
is_nine(player_total,banker_total, player_wins)
lessthan_five(player_total,banker_total, player_wins)
greaterthan_nine(player_total,banker_total, player_wins)
money(player_wins, player_buyin)
play_again(player_buyin, player_wins)