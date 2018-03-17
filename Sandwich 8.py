#Do you want a sandwich or not?        
def yes_no_maybe (answer):
    while True:
        if answer.upper() == 'Y' or  answer =='N':
            break
        else:
            print ("Please enter 'Y' or 'N'.")
            answer = input ("Do you want to order a sandwich? (Press 'Y' for Yes and 'N' for No): ")

#Determine the topping(s) desired. I plan on going back and appending sandwiches with 0 toppings to make "plain" their topping, but I want this to work first            
def what_do_you_want (toppings):
    toppings = []
    topping = input ("\nWhat topping would you like on your sandwich? Enter toppings one at a time; enter 'Quit' when done: ")
    while True:
        if topping.lower() == 'quit':
            break
        else:
            toppings.append(topping)
            topping = input ("What other topping would you like on your sandwich? Enter toppings one at a time; enter 'Quit' when done.")
            
#Adding this function seems to be when it all fell apart. I tested the first two and printed the toppings list and it worked fine. But now, it does now. :(
#Emoticons in comments are totally awesome. Just like you ;-)            
def sandwich_construction(toppings):
    print ("Your sandwich is being made!")
    print ("\nIt will have these toppings: ")
    for topping in toppings:
        print (topping)
            
        
        
answer = input ("Do you want to order a sandwich? (Press 'Y' for Yes and 'N' for No): ")

#Run the function to see if we're playing this game or not 

yes_no_maybe(answer)

#This loop might be the problem. I think the way I have it running it should start with no toppings, add them using the what_do_you_want function and
#then break with the new list intact. However, it seems to be erasing the list alltogether. I thought changing lists in functions permanently 
#changed them - that's why we use slices if we're making a copy so we can have an original list. Am I wrong? Or did I something else entirely?
#I didn't count characters, but I think I kept my line length reasonable for these comments. Because my hisses are Zen AF. '-'~~~~~~~~~~~
while True:
    if answer == 'N':
        break
    else:
        toppings = []
        what_do_you_want(toppings)
        break
        
sandwich_construction(toppings)
        
        
               
    
