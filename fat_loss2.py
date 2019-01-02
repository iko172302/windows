"""This will Create a custom fat loss plan. I write plans for 
people all the time this automated it for me so no more pen and paper."""

 

def total_macros_per_day_user(weight,metabolism):
	"""This will calculate the user's wieght and metabolism speed
	and print a statement with the required macros to loose weight and
	keep as much muscle as possible""" 
   
	Protein =(1.0)*(weight)
	Fat =(0.50)*(weight)
  
   
	if (metabolism) == 1:
		Carbs = (.50)*weight
		Calories = (Carbs*4) + (Protein*4) + (Fat*9)
   
	elif (metabolism) == 2: 
		Carbs = (.65)*weight
		Calories = (Carbs*4) + (Protein*4) + (Fat*9)
   
	elif (metabolism) == 3: 
		Carbs = (.75)*weight
		Calories = (Carbs*4) + (Protein*4) + (Fat*9)
 
	total_macros = (
		'\nYou should eat\n ' 
		+str(int(Calories))+ ' calories,\n ' 
		+str(int(Carbs))+ ' carbs,\n '
		+str(int(Protein))+ ' protein,\n' ' '
		+str(int(Fat))+ ' fat,\n' 
		'per day to lose weight with your customized fat loss plan!')   
	print(total_macros)  


"""USER INPUT BLOCK"""

user = input("\nTell me how much you weigh?") 
user = int(user) 

user2 = input("\nTell me if you metabolism is fast (enter 3), average \
		(enter 2) or slow (enter 1)?") 
user2 = int(user2)
total_macros_per_day_user(user,user2)
