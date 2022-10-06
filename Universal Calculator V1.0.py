# Designed by Ferdinand
# Made on 01/09/2021

import time
import random

#r_p_c means registered perfomable calculations
r_p_c = ["convert measurements","mean average","area of a circle","circumference"] # in later versions i can add a big "equation triangles update"


searched_items = []  # i decided to come up with a list that stores what you search and the last item will always be "continue" so i will delete that item and read the second last item which will be what they searched last


global leave #i had to make this global because of scope issues, this is going to be what i make "true" when i want to exit the program
leave = False

time.sleep(3)
print("")
print("Welcome to the Universal Calculator V1.0")
print("")
time.sleep(4)
print("when presented with a question please answer yes or no (do not put a space after either)")
time.sleep(3)

while True:
    try:   
        Option = str(input("Would you like to search my database and see if i can perform your calculation? ")).lower()
        search = False 

        if Option == "yes":
            time.sleep(2)
            
            while True:
                print("")
                print("To exit the search feature type 'continue' ")
                time.sleep(1)
                wishlist = str(input("what you would like me to calculate (do not put a space at the end): ")).lower()
                time.sleep(1)
                
                if wishlist == "continue":
                    break
                
                confirmation = str(input("to confirm, did you say " + wishlist + "? ")).lower()  
                
                if confirmation == "yes":
                    if wishlist in r_p_c:  
                        print("yes i can do that ")
                        search = True
                        searched_items.append(wishlist)
                        time.sleep(3)

                    else:
                        print("no unfortunately i cannot currently do that ")
                        time.sleep(3)
                

                elif confirmation == "no": 
                    print("To exit the search feature type 'continue' ")
                    time.sleep(1)
                    wishlist = str(input("what you would like me to calculate (do not put a space at the end): ")).lower()     
                    time.sleep(1)
                    
                    if wishlist == "continue":
                        break              

                    confirmation = str(input("to confirm, " + wishlist + "? ")).lower()
                    
                    if confirmation == "yes":  
                        if wishlist in r_p_c:
                            print("yes i can do that ")
                            search = True
                            searched_items.append(wishlist)
                            time.sleep(3)

                        else:
                            print("no unfortunately i cannot currently do that ")
                            time.sleep(3)


                    else:   # if the user enters no or anything else for the 2nd time
                        print("")
                        print("I am ending the program, next time please enter your words correctly.")
                        print("")      
                        time.sleep(7)
                        leave = True #because i have now put this in a loop this break wont be good enough on its own
                        break

                else:  # if the user enters something other than yes or no
                    print("")
                    print("I am ending the program, next time please enter your words correctly.")
                    print("")      
                    time.sleep(7)
                    leave = True #because i have now put this in a loop this break wont be good enough on its own
                    break



        elif Option == "no":
            search = False
            # seen as they dont want to search i will make the search false and this will just ask what they want to calculate and then prceed with the calculations

        else:   # if the user enters something other than yes or no
            print("")
            print("I am ending the program, next time please enter your words correctly")
            print("")      
            time.sleep(7)
            break

        
        if leave == True:
            print("")
            break # this is to exit the program


        print("")
        print("")
        print("You are now in the calculation feature (the main part of the program)")
        print("")


        while True:
            if search == True:   # if the user has utilised the search function
                print("")
                print ("To exit the Universal Calculator type 'exit' ")

                actual_wishlist = searched_items[-1]

                search_calculate = str(input("Would you like me to calculate " + actual_wishlist + "? ")).lower() # this is just here to stop the user from having to repeat themselves
                print("")
                search = False # to stop it asking twice
                
                if search_calculate == "yes":
                    if actual_wishlist == "mean average":
                    
                        
                        count=0   #this is how many numbers have been added together
                        number=0  #this is the sum of all of the numbers you are adding up
                        print("")
                        print("This programme will work out the Mean Average of a series of numbers ")
                        time.sleep(2)
                        print("Only enter one number at a time ")
                        print("")
                        while True:
                            number = number + float(input("Please enter a number: ")) # in future versions it will be able to accept fractions and percentgages
                            count = count + 1
                            end = str(input("Type finish to calculate, type anything else to carry on: ")).lower()
                            if end == 'finish':
                                break
                        numbers = count 
                        answer = str( number/numbers)

                        time.sleep(2)
                        print("")
                        print("Your answer is " + answer)
                        time.sleep(1)
                        print("You're welcome :)")
                        print("")

 
                    elif actual_wishlist == "convert measurements":

                         while True:
                            num1 = float(input("Enter the value: "))
                            print("")
                            print("To exit type 'continue' ")
                            print("")
                            unit1 = str(input("Which unit do you want to convert from: ")).lower()
                            unit2 = str(input("Which unit do you want it converted to: ")).lower()

                            if unit1 == "cm" and unit2 == "m":
                                ans = float(num1)/100
                                print(ans)
                            elif unit1 == "mm" and unit2 == "cm":
                                ans = float(num1)/10
                                print(ans)
                            elif unit1 == "m" and unit2 == "cm":
                                ans = float(num1)*100
                                print(ans)
                            elif unit1 == "cm" and unit2 == "mm":
                                ans = float(num1)*10
                                print(ans)
                            elif unit1 == "mm" and unit2 == "m":
                                ans = float(num1)/1000
                                print(ans)
                            elif unit1 == "m" and unit2 == "mm":
                                ans = float(num1)*1000
                                print(ans)
                            elif unit1 == "km" and unit2 == "m":
                                ans = float(num1)*1000
                                print(ans)
                            elif unit1 == "m" and unit2 == "km":
                                ans = float(num1)/1000
                                print(ans)
                            elif unit1 == "mm" and unit2 == "km":
                                ans = float(num1)/1000000
                                print(ans)
                            elif unit1 == "ft" and unit2 == "cm":
                                ans = float(num1)*30.48
                                print(ans)
                            elif unit1 == "ft" and unit2 == "mm":
                                ans = float(num1)*304.8
                                print(ans)
                            elif unit1 == "ft" and unit2 == "inch":
                                ans = float(num1)*12
                                print(ans)
                            elif unit1 == "inch" and unit2 == "cm":
                                ans = float(num1)*2.54
                            elif unit1 == "inch" and unit2 == "mm":
                                ans = float(num1)*25.4
                            
                            elif unit1 or unit2 == "continue":
                                break

                            else:
                                print("i cannot currently do that")
                    
                    
                    elif actual_wishlist == "area of a circle":

                        print("")
                        print("This programme will work out the Area of a Circle")
                        time.sleep(1)
                        print("")
                        PI = 3.14159265359

                        while True:
                            Circle_Mode = input("Enter your prefered mode, Radius or Diameter: ").lower()
                            time.sleep(1)
                            Answer_Mode = input("Would you like your answer to be in terms of Pi? : ").lower()

                            if Circle_Mode == "diameter":
                                d = float(input("Enter the Diameter of the circle (just the number, no cm or mm): "))
                                d = d/2
                                
                                if Answer_Mode == "no":
                                    area = "The Area of your Circle = {0}"
                                    print("")
                                    print(area.format(PI * d * d))
                                    print("")
                                    break
                                elif Answer_Mode == "yes":
                                    area = "The Area of your Circle = {0} Pi"
                                    print("")
                                    print(area.format(2 * d))
                                    print("")       
                                    break
                                else:
                                    print("")
                                    print("i didnt understand that ")
                                    print("")

                            elif Circle_Mode == "radius":
                                r = float(input("Enter the Radius of the circle (just the number, no cm or mm): "))
                                
                                if Answer_Mode == "no":
                                    area = "The Area of your Circle = {0}"
                                    print("")
                                    print(area.format(PI * r * r))
                                    print("")
                                    break
                                elif Answer_Mode == "yes":
                                    area = "The Area of your Circle = {0} Pi"
                                    print("")
                                    print(area.format(r * 2 ))
                                    print("")
                                    break
                                else:
                                    print("")
                                    print("i didnt understand that ")
                                    print("")
                            else:
                                print("")
                                print("i didnt understand that ")
                                print("")




                    elif actual_wishlist == "circumference":
        
                        print("")
                        print("This programme will work out the Circumference of a Circle")
                        time.sleep(1)
                        print("")
                        PI = 3.14159265359

                        while True:
                            Circle_Mode = str(input("Enter your prefered mode, Radius or Diameter: ")).lower()
                            time.sleep(1)

                            if Circle_Mode == "diameter":
                                d = float(input("Enter the Diameter of the circle (just the number, no cm or mm): "))

                                area = "The Circumference of your Circle = {0}"
                                print("")
                                print(area.format(PI * d))
                                print("")
                                break


                            elif Circle_Mode == "radius":
                                r = float(input("Enter the Radius of the circle (just the number, no cm or mm): "))   

                                area = "The Circumference of your Circle = {0}"
                                print("")
                                print(area.format(PI * (2 * r)))
                                print("")
                                break

                            else:
                                print("")
                                print("i didnt understand that ")
                                print("")
                                            
                
                elif search_calculate == "no":
                    break
                
                
                elif search_calculate == "exit":
                        time.sleep(1)
                        print ("In the future you will be able to use the search feature more than once, ")
                        time.sleep(7)
                        print ("But currently, due to the way i am structured, it is only 1 time thing per run ")
                        time.sleep(7)
                        print ("ENDING PROGRAM ")
                        time.sleep(2)   
                else:
                    print("I cannot calculate that just yet however i may be able to in future updates")

            else:
                break
    
    
    

        while True:
            if search == False:
                print("")
                print ("To exit the Universal Calculator type 'exit' ")
                actual_calculation = str(input("What would you like me to calculate? ")).lower()
                print("")
                
                if actual_calculation == "mean average":

                    count=0   #this is how many numbers have been added together
                    number=0  #this is the sum of all of the numbers you are adding up
                    print("")
                    print("This programme will work out the Mean Average of a series of numbers ")
                    time.sleep(2)
                    print("Only enter one number at a time ")
                    print("")
                    while True:
                        number = number + float(input("Please enter a number: ")) # in future versions it will be able to accept fractions and percentgages
                        count = count + 1
                        end = str(input("Type finish to calculate, type anything else to carry on: ")).lower()
                        if end == 'finish':
                            break
                    numbers = count 
                    answer = str( number/numbers)

                    time.sleep(2)
                    print("")
                    print("Your answer is " + answer)
                    time.sleep(1)
                    print("You're welcome :)") 
                    print("")



                elif actual_calculation == "convert measurements":

                    while True:                        
                        num1 = float(input("Enter the value: "))
                        print("")
                        print("To exit type 'continue' ")
                        print("")
                        unit1 = str(input("Which unit do you want to convert from: ")).lower()
                        unit2 = str(input("Which unit do you want it converted to: ")).lower()

                        if unit1 == "cm" and unit2 == "m":
                            ans = float(num1)/100
                            print(ans)
                        elif unit1 == "mm" and unit2 == "cm":
                            ans = float(num1)/10
                            print(ans)
                        elif unit1 == "m" and unit2 == "cm":
                            ans = float(num1)*100
                            print(ans)
                        elif unit1 == "cm" and unit2 == "mm":
                            ans = float(num1)*10
                            print(ans)
                        elif unit1 == "mm" and unit2 == "m":
                            ans = float(num1)/1000
                            print(ans)
                        elif unit1 == "m" and unit2 == "mm":
                            ans = float(num1)*1000
                            print(ans)
                        elif unit1 == "km" and unit2 == "m":
                            ans = float(num1)*1000
                            print(ans)
                        elif unit1 == "m" and unit2 == "km":
                            ans = float(num1)/1000
                            print(ans)
                        elif unit1 == "mm" and unit2 == "km":
                            ans = float(num1)/1000000
                            print(ans)
                        elif unit1 == "ft" and unit2 == "cm":
                            ans = float(num1)*30.48
                            print(ans)
                        elif unit1 == "ft" and unit2 == "mm":
                            ans = float(num1)*304.8
                            print(ans)
                        elif unit1 == "ft" and unit2 == "inch":
                            ans = float(num1)*12
                            print(ans)
                        elif unit1 == "inch" and unit2 == "cm":
                            ans = float(num1)*2.54
                        elif unit1 == "inch" and unit2 == "mm":
                            ans = float(num1)*25.4
                        
                        elif unit1 or unit2 == "continue":
                            break

                        else:
                            print("i cannot currently do that")



                elif actual_calculation == "area of a circle":

                    print("")
                    print("This programme will work out the Area of a Circle")
                    time.sleep(1)
                    print("")
                    PI = 3.14159265359

                    while True:
                        Circle_Mode = input("Enter your prefered mode, Radius or Diameter: ").lower()
                        time.sleep(1)
                        Answer_Mode = input("Would you like your answer to be in terms of Pi? : ").lower()

                        if Circle_Mode == "diameter":
                            d = float(input("Enter the Diameter of the circle (just the number, no cm or mm): "))

                            if Answer_Mode == "no":
                                area = "The Area of your Circle = {0}"
                                print("")
                                print(area.format(PI * d))
                                print("")
                                break
                            elif Answer_Mode == "yes":
                                area = "The Area of your Circle = {0} Pi"
                                print("")
                                print(area.format(d))
                                print("")       
                                break
                            else:
                                print("")
                                print("i didnt understand that ")
                                print("")
                                time.sleep(1)

                        elif Circle_Mode == "radius":
                            r = float(input("Enter the Radius of the circle (just the number, no cm or mm): "))
                            
                            if Answer_Mode == "no":
                                area = "The Area of your Circle = {0}"
                                print("")
                                print(area.format(PI * r * r))
                                print("")
                                break
                            elif Answer_Mode == "yes":
                                area = "The Area of your Circle = {0} Pi"
                                print("")
                                print(area.format(r * 2 ))
                                print("")
                                break
                            else:
                                print("")
                                print("i didnt understand that ")
                                print("")
                                time.sleep(1)
                        else:
                            print("")
                            print("i didnt understand that ")
                            print("")
                            time.sleep(1)



                elif actual_calculation == "circumference":

                    print("")
                    print("This programme will work out the Circumference of a Circle")
                    time.sleep(1)
                    print("")
                    PI = 3.14159265359

                    while True:
                        Circle_Mode = str(input("Enter your prefered mode, Radius or Diameter: ")).lower()
                        time.sleep(1)

                        if Circle_Mode == "diameter":
                            d = float(input("Enter the Diameter of the circle (just the number, no cm or mm): "))

                            area = "The Circumference of your Circle = {0}"
                            print("")
                            print(area.format(PI * d))
                            print("")
                            break


                        elif Circle_Mode == "radius":
                            r = float(input("Enter the Radius of the circle (just the number, no cm or mm): "))   

                            area = "The Circumference of your Circle = {0}"
                            print("")
                            print(area.format(PI * (2 * r)))
                            print("")
                            break

                        else:
                            print("")
                            print("i didnt understand that ")
                            print("")
                            time.sleep(1)
                        

                elif actual_calculation == "exit":
                    time.sleep(1)
                    print ("In the future you will be able to use the search feature more than once, ")
                    time.sleep(7)
                    print ("But currently, due to the way i am structured, it is only 1 time thing per run ")
                    time.sleep(7)
                    print ("ENDING PROGRAM ")
                    time.sleep(2)   
                    break  
                else:
                    print("I cannot calculate that just yet however i may be able to in future updates")
                    time.sleep(1)

        break #this is here if the user wanted to exit the program in the block of code above, when they are using the actual calculations bit        
                
    except:
        print("")
        print("An error has occured")
        print("")
        print("Restarting Program")

# Designed by Ferdinand
