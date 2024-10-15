print("WELCOME TO THE QUIZ BY GRACEY")
answer = input("Do you want to participate? yes/no:")
score = 0
totalquestion = 3

if answer.lower() == "yes":

    answer = input ("What is Gracey's favourite color?"":")
    if answer.lower() == "white":
      score += 1
      print ("you are correct!")
    else:
     print("hahahaha you are wrong!!!")

    answer = input ("What is Gracey's favourite food?"":")
    if answer.lower() == "momo":
      score += 1
      print ("you are correct!")
    else:
     print("hahahaha you are wrong!!!")
       
    answer = input ("What is Gracey's favourite place?"":")
    if answer.lower() == "beas":
      score += 1
      print ("you are correct!")
    else:
     print("hahahaha you are wrong!!!")

    print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
    mark= (score/totalquestion)*100
    print('Marks obtained:',mark)
    print("See ya!")




      
