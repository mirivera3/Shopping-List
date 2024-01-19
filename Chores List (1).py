#list
#


#Functions 

def simpleCalculator():
   while True:
      print("Your to do list!")
      print("Please choose an option:(Type in a number between 1-5)")
      print("1.Display \n2.Add item \n3.Remove Item \n4.Mark a Task as Done \n5.Exit \n.6 clear list \n.7 sort alphabetically \n.8 print how many items are on the list")
      myList = ["Vacuum", "Homework", "Nails", "Hair", "Read", "Dust", "Make Bed"]
      option = int(input("Option: "))
      if option == 1: print(myList)
      if option == 2:
         x= input("What do you want to add: ")
         myList.insert(7,x)
         print(myList)
      if option == 3:
         y = input("What do you want to remove: ")
         myList.remove(y)
         print(myList)
      if option == 4:
         z =input("what task will be marked as done:")
         a=myList.index(z)
         myList[a]= z +"[X]"
         print(myList)
      if option == 5: 
         print("Goodbye!")
         break
      if option == 6:
         myList.clear()
         print (myList)
      if option == 7:
         myList.sort()
         print(myList)
      if option == 8:
         print(len(myList))
      
      
   
   #Main 
simpleCalculator()