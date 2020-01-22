#monte carlo simulation used to test the 
#monte carol is used for
#the first task is
import random 
import matplotlib.pyplot as plt

lower_bust = 31.24
#we want to have bust rate less than 31.24
higher_profit = 63.208
#we want to have profit percent higher than or equal to 63.4



def rollDice():
	#notes we commmented the print functions since we used them initialy to debug the function
	#after we have emphasised that the function works well we can simply comment them
	roll = random.randint(1,100)

	if roll <=50:
		#print(f"{roll} roll is 100 you loss what are the odds! play again")
		return False	

	elif  roll>50:
		#print(f"{roll} roll was 51-100 you win pretty light flash")
		return True
	#now come an create simple bettor


def simple_bettor(funds,initial_wager,wager_count):
	value = funds
	wager = initial_wager
	#now we ate going to plot wagers and values
	global broke_count
	global simple_profits
	global simple_bust
	wx = []
	vy = []


	#the two above lists are used to store some data

	currentWager = 0
	status = None
	while currentWager < wager_count :
		
		wx.append(currentWager)
		vy.append(value)

		if rollDice():
			value += wager
			status = wager
			#if we roll the dice and we won then we add the wager to our fund
		else :
			value -= wager
			status = -wager

		currentWager +=1
		#we add wager so we increment the number of wagers we encountered
		#print(f"funds: {value} and you get {status}")
	if value< 0:
		#so we solve the debt issue
		simple_bust += 1
		value = 'broke'

	plt.plot(wx,vy,'k')
	if value>startingFunds:
		simple_profits += 1
	#black color

	print(f"funds: {value} and you get {status}")



#build double wager which has some strategy if he losses he is going to double the wager
# if he wins he is going to go back with the same old wager


def doubler_bettor(funds,initial_wager,wager_count):
#video 6

	value = funds
	wager = initial_wager
	#now we ate going to plot wagers and values

	wx = []
	vy = []

	#the two above lists are used to store some data

	currentWager = 1
	status = None
	global broke_count
	global doubler_busts
	global doubler_profits

	previous_wager = 'win'
	previous_wager_amount = initial_wager

	while currentWager <= wager_count:
		if previous_wager=='win':
			print("we win hte last wager. great")
			if rollDice():
				value += wager
				print (value)
				wx.append(currentWager)
				vy.append(value)
			else :
				value -= wager
				previous_wager = 'loss'
				print(value)
				previous_wager_amount = wager
				wx.append(currentWager)
				vy.append(value)

				if value < 0:
					print(f"we went broke again after {currentWager} rolls")
					doubler_busts += 1
					
					
					break
		
		elif previous_wager=='loss':
			print('we los the last one so we will be smart and double the wager')
			#v.9
			#we want to solve the debt issue until v.8 
			#so in the cass previous_wager was loss then we
			#make sure that the value we have left is larger than the wager
			if rollDice():
				wager = previous_wager_amount*2
				print(f"we won with {wager}")
				if value - wager < 0 :
					wager = value
					#note we donot want to endup with debt so we make the last wager equals the value
				value += wager
				print(value)
				wager = initial_wager
				previous_wager = 'win'
				wx.append(currentWager)
				vy.append(value)

			else:
				wager = previous_wager_amount*2
				print (f"we lost {wager}")
				if value - wager <0:
					wager = value
				value -= wager
				if value<=0:
					print(f"we went broke after {currentWager} rolls")
					doubler_busts += 1
					
					break
				print(value)
				previous_wager = 'loss'

				previous_wager_amount = wager
				wx.append(currentWager)
				vy.append(value)

		currentWager +=1
	print (value)
	plt.plot(wx,vy,'c')
	if value> startingFunds:
		doubler_profits +=1
	#cin color is faint blue



def multiple_bettor(funds, initial_wager,wager_count):
	#the goal of the alogrithm is to define the best percents to wagers with
	global multiple_busts
	global multiple_profit

	value = funds
	wager = initial_wager
	wx = []
	vy = []
	currentWager = 1
	previous_wager = 'win'

	previous_wager_amount = initial_wager

	while currentWager <= wager_count:
		if previous_wager=='win':
			#print("we win hte last wager. great")
			if rollDice():
				value += wager
			#	print (value)
				wx.append(currentWager)
				vy.append(value)
			else :
				value -= wager
				previous_wager = 'loss'
			#	print(value)
				previous_wager_amount = wager
				wx.append(currentWager)
				vy.append(value)

				if value < 0:
			#		print(f"we went broke again after {currentWager} rolls")
					multiple_busts += 1
					
					
					break
		
		elif previous_wager=='loss':
			#print('we los the last one so we will be smart and double the wager')
			#v.9
			#we want to solve the debt issue until v.8 
			#so in the cass previous_wager was loss then we
			#make sure that the value we have left is larger than the wager
			if rollDice():
				wager = previous_wager_amount*random_multiple

			#	print(f"we won with {wager}")
				if value - wager < 0 :
					wager = value
					#note we donot want to endup with debt so we make the last wager equals the value
				value += wager
			#	print(value)
				wager = initial_wager
				previous_wager = 'win'
				wx.append(currentWager)
				vy.append(value)

			else:
				wager = previous_wager_amount*random_multiple
			#	print (f"we lost {wager}")
				if value - wager <0:
					wager = value
				value -= wager
				if value<=0:
			#		print(f"we went broke after {currentWager} rolls")
					multiple_busts += 1
					
					break
			#	print(value)
				previous_wager = 'loss'

				previous_wager_amount = wager
				wx.append(currentWager)
				vy.append(value)

		currentWager +=1
	
	#print (value)
	#plt.plot(wx,vy,'c')
	if value> funds:
		multiple_profit +=1
	#cin color is faint blue





#commented at the start of vi.15
# this is part of vi.14 dalmbert



def dAlemert (funds,initial_wager,wager_count):
		global da_busts
		global da_profits

		global Ret
		value = funds
		wager = initial_wager
		currentWager = 1
		previous_wager = 'win'
		previous_wager_amount = initial_wager
		#hte amount of money we are wagering
		while currentWager <= wager_count:
			if previous_wager == 'win':
				if wager == initial_wager:
					pass
				else :
					wager -= initial_wager
				
				#print(f"current wager {wager} value {value}")
				
				if rollDice():
					value += wager
					previous_wager_amount = wager
					#print(f"we won current value: {value}")
				else :
					value -= wager
					previous_wager = 'loss'
					#print(f"we lost current value {value}")
					previous_wager_amount = wager
					if value <= 0:
						da_busts += 1
						break
			elif previous_wager == 'loss':
				wager = previous_wager_amount+initial_wager
				if (value - wager ) <= 0:
					wager = 0
				#print(f"we lost the last wager {wager} ")
					#we donont want ot enter the debt
				if rollDice():
					value += wager
					previous_wager = 'win'
					previous_wager_amount = wager
				else :
					value -= wager
					previous_wager_amount = wager

					if value <= 0:
						da_busts +=1
						break
						# we get in debt we donot want to play any more
		
			currentWager +=1
		if value > funds:
			da_profits += 1
		Ret += value







samplesize = 100
startingFunds = 100000

while True:
		
	wagersize = random.uniform(1.0,1000.00)
	#the amount we are wagering
	wagercount = random.uniform(10,100000)
	#the target number of wagers

	wagercount = 100


	da_profits = 0
	da_busts = 0
	Ret = 0
	#of the people who profit how much they make profit
	#out of the people who loss how much did they loss
	#out of the people who

	x = 0
	while x< samplesize:

		dAlemert (startingFunds,wagersize,wagercount)
		x += 1

	ROI = Ret - samplesize*startingFunds
	print(f"total invested is {samplesize*startingFunds}")
	print(f"total return {Ret}")
	print(f"the total return of investment is{ROI}")
	print(f"bust rate is {da_busts/samplesize*100.00}")
	print(f"profit rate is {da_profits/samplesize*100.00}")

	print("############################################")
	print(f"number of people make money is {da_profits}")
	print("############################################")


