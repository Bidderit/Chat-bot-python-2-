#Abby
#9/10/21
#assignment 2

import random
user_response = ""
comment_list1 = ["Nice", "I'm going there too", "I just got off"]
comment_list2 = ["I am also going home", "I'm going to School right now"]


print("Where are you going today")
user_response = input()
if user_response == "School" or user_response == "school":
    print (random.choice(comment_list1))
elif user_response == "Home" or user_response == "home":
    print (random.choice(comment_list2))
else:
    print("Where is that?")
    
user_response = ""
comment_list3 = ["Nice", "Oh same", "you want to play together?"]
comment_list4 = ["I also play league","you want to play a game with me?"]


print("What games do you play")
user_response = input()
if user_response == "minecraft" or user_response == "Minecraft":
    print(random.choice(comment_list3))
elif user_response == "League of Legends" or user_response == "league":
    print(random.choice(comment_list4))
else:
    print("Ah I dont play that")
    
user_response = ""
comment_list5 = ["Chicken is my favourite", "I dont like chicken anymore"]
comment_list6 = ["I don't really like beef", "Beef is not my favourite"]
comment_list7 = ["I also like pork", "Pork is pretty tasty right?"]

print("What type of meat do you like? Chicken, beef, or pork")
user_response = input()
if user_response == "Chicken" or user_response == "chicken":
    print (random.choice(comment_list5))
elif user_response == "beef" or user_response == "Beef":
    print (random.choice(comment_list6))
elif user_response == "Pork" or user_response == "pork":
    print (random.choice(comment_list7))
else:
    print("What does that taste like?")