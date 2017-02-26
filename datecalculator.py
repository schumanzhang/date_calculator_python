def calculateDays(date1, date2):
    
    normalYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leapYear   = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    dd1 = int(date1[:2])
    mm1 = int(date1[3:-5])
    yyyy1 = int(date1[6:])
    dd2 = int(date2[:2])
    mm2 = int(date2[3:-5])
    yyyy2 = int(date2[6:])
    
    counter1 = mm1 - 1
    if yyyy1 % 4 == 0:
        daysnotpassed1 = 366 - (sum(leapYear[:counter1]) + dd1)
        dayspassed1 = sum(leapYear[:counter1]) + dd1
    else:
        daysnotpassed1 = 365 - (sum(normalYear[:counter1]) + dd1) 
        dayspassed1 = sum(normalYear[:counter1]) + dd1
  
    counter2 = mm2 - 1
    if yyyy2 % 4 == 0:
        dayspassed2 = sum(leapYear[:counter2]) + dd2 
    else:
        dayspassed2 = sum(normalYear[:counter2]) + dd2
        
    x = 0
    if yyyy1 != yyyy2:
        
        i = yyyy1 + 1
        while i < yyyy2:   
            
            if i % 4 == 0:
                x += 366
            else:
                x += 365

            i += 1
        days = x + daysnotpassed1 + dayspassed2 - 1
        
    else:    
        days = dayspassed2 - dayspassed1 - 1
    
    return days

#Make sure the end date is after the start date. If not, prompt user to re-enter
def checkDateOrder(date1, date2):
    
    correct = True
  
    dd1 = int(date1[:2])
    mm1 = int(date1[3:-5])
    yyyy1 = int(date1[6:])
    dd2 = int(date2[:2])
    mm2 = int(date2[3:-5])
    yyyy2 = int(date2[6:])
    
    if yyyy2 < yyyy1:
        correct = False
        
    if yyyy2 == yyyy1 and mm2 < mm1:
        correct = False     
          
    if yyyy2 == yyyy1 and mm2 == mm1 and dd2 <= dd1:
        correct = False    
    
    return correct

#Make sure the user input is in a valid date format DD/MM/YYYY. If not, prompt user to re-enter
def checkUserInput(date):
    
    notallowed = False
    incorrect = False
    allowedList = '1234567890/'
   
    for c in date:
        if c not in allowedList:
            notallowed = True
    
    if notallowed == True:
        incorrect = True
        
    else:   
        
        if len(date) != 10:
            incorrect = True
        else:  
            if date[2] and date[5] != '/': 
                incorrect = True     
            else: 
                dd = int(date[:2])
                mm = int(date[3:-5])
                yyyy = int(date[6:])

                if dd < 1 or dd > 31: 
                    incorrect = True

                if mm < 1 or mm > 12: 
                    incorrect = True

                if yyyy < 1901 or yyyy > 2999: 
                    incorrect = True
                    
                if yyyy % 4 != 0 and mm == 2 and dd > 28:
                    incorrect = True
                
                if yyyy % 4 == 0 and mm == 2 and dd > 29:
                    incorrect = True
                    
                if mm == 4 or mm == 6 or mm == 9 or mm == 11:
                    if dd > 30:
                        incorrect = True
        
    if incorrect == True: 
        print ("Date format incorrect")
        
    return incorrect

#Ask the user for the start date of the experiment
def askStartDate():
    
    userInput = raw_input("Please enter the start date of the experiment (DD/MM/YYYY) : ")
    
    checked = checkUserInput(userInput)
    
    if checked == False:
        global date1
        date1 = userInput
    else:
        askStartDate()
    
    return None

#Ask the user for the end date of the experiment
def askEndDate():
    
    userInput = raw_input("Please enter the end date of the experiment (DD/MM/YYYY) : ")
    
    checked = checkUserInput(userInput)
    
    if checked == False:
        global date2
        date2 = userInput
    else:
        askEndDate()
        
    return 

def main():
    
    askStartDate()
    askEndDate()

    print("Your entered dates are " + date1 + ", " + date2)

    inputsReady = checkDateOrder(date1, date2)

    if inputsReady == True:
        
        solution = calculateDays(date1, date2)
        print(str(solution) + " Day(s)")
        
        userInput = raw_input("Would you like to run another date calculation? [y/n] : ")
        
        if userInput == 'y':
            main()
        else:
            quit()
        
    else:
        print("The End Date Must be After the Start Date!")
        main()
        
    return None

######################################################################
print ("Welcome to the Date Calculator")

date1 = ''
date2 = ''

main()
   

















