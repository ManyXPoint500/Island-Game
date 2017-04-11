import time

#next lines describe item objects and lists


#Today's TO DO LIST:
#Finish seperate paths for "Set up camp"
#Finish seperate paths for "Look for Food"
#Finish seperate paths for "Panic"
#Finish seperate paths for "Think about Last Night"


cls = lambda: print('\n'*300)
item_1 = "Tent (2 person)"
item_2 = "Pocket Knife"
item_3 = "200 ft paracord"
item_4 = "Iron Sheets"
item_5 = "Multi-Tool"
item_6 = "Bleach (for cleaning cloths)"
item_7 = "Inflatable Boat"
item_8 = "Skittles"
item_9 = "Matches"
item_10 = "iPhone 7"
item_11 = "Swim Trunks"
item_12 = "Flint and Steel"
item_13 = "Computer"
item_14 = "Watch"
item_15 = "10 days worth of food"
items_all = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12, item_13, item_14, item_15]
tools = []

q_1 = input(str(items_all) + "What's 1/5 items do you want to bring to this island? (enter item # (organized by order, 1-15))(You are supplied with a backpack automatically)(you can bring multiple items...)")
q_2 = input("2nd item")
q_3 = input("3rd item")
q_4 = input("4th item")
q_5 = input("Last item!")

#next lines describe all the functions/choices

def item1():
    tools.append(items_all[int(q_1) - 1])
    
def item2():
    tools.append(items_all[int(q_2) - 1])
  
def item3():
    tools.append(items_all[int(q_3) - 1])
    
def item4():
    tools.append(items_all[int(q_4) - 1])
    
def item5():
    tools.append(items_all[int(q_5) - 1])
    
def option1():
    print ("Hello")

def note():
  cls()
  print ("This game registers your answers using numbers. To pick your option, type the option's number in order from left to right.")
  time.sleep(5)
  print ("")
  print ("example: What's better: Ice cream or Cake?")
  time.sleep(3)
  print ("")
  print ("If you wanted Ice cream for your answer, then you would type '1'. If you wanted cake, then you would type '2'")
  time.sleep(5)
  print ("")
  print ("If you type in anything besides a number (unless otherwise specified), you will get an error and will have to start the game all over, so be carful what you type...")
  time.sleep(7)
  print ("Thanks!")
  time.sleep(1.5)
  cls()
  time.sleep(5)
  
def mdialogue1():
  cls()
  print ("Hello")
  time.sleep(2)
  print ("                                                            Where am I?")
  time.sleep(2)
  print ("You are on an island but I don't know what it's called...")
  time.sleep(3)
  print ("                                                  What am I doing here?")
  time.sleep(2)
  print("You were ship wrecked and brought in by the sea. I saw your ship sink to the ground...")
  time.sleep(4)
  print("                                                            Who are you?")
  time.sleep(2)
  print (".")
  time.sleep(1)
  print (".")
  time.sleep(1)
  print (".")
  time.sleep(2)
  print ("No Response...")
  time.sleep(3)
  cls()
  
def dialogue1():
  time.sleep(3)
  print ("Uh, what a horrible headache! What on earth happened!")
  time.sleep(2)
  print ("  *You begin to recall what happened the night before...")
  time.sleep(3)
  print ("Oh.")
  time.sleep(1)
  print ("Well... Im stuck on an island... So...")
  time.sleep(4)
  print ("Now what?")
  time.sleep(1)
  
def choice1():
  c1 = input("Set up camp, look for food, panic, or think about what hapened last night?")
  if c1 == 1:
    path1()
  elif c1 == 2:
    path2()
  elif c1 == 3:
    path3()
  elif c1 == 4:
    path4()
    
def path1():
  print("You decide to set up camp")
  time.sleep(3)
  p1 = input("What would you like to setup first? Campfire, Shelter, or Chapel?")
  if p1 == 1:
    print("Incomplete Section")
  if p1 == 2:
    print("Incomplete Section 2")
  if p1 == 3:
    print("Incomplete Seection 3")
    
def path2():
  print ("Path 2")
  
def path3():
  print ("Path 3")
  
def path4():
  print ("Path 4")

#start game here!

item1()
item2()
item3()
item4()
item5()
print (tools)
time.sleep(5)
print ("These are the items you are bringing!")
time.sleep(5)
note()
mdialogue1()
dialogue1()
choice1()
