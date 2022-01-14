"""---------------------------------------------------------------------------------------------------------------------------- 
  Mini Quiz
  
     Program Execution :
     This Quiz conssists of 10 questions on Genral knowledge for students at kindergarten level. 
     Questions will appear on the screen one by one . for a correct answer, you get a score of 100 points. if the answer 
     is wrong then no score.lastly your Total score will display.
          
-------------------------------------------------------------------------------------------------------------------------------
"""
def getUser(userName):
    userName=input("Enter your name : ")
    if(userName==""):
        getUser(userName)
    return userName
   

questionsOptions=["A computer input device that is used to enter computer instructions and data into the computer*Floppy disk*Keyboard*Monitor*Flash drive*2",
           "An output device that shows images and text from the computer*Desktop*Modem*Monitor*Speaker*3",
           "Which two sites offer free emails?*Yahoo and google*Apple and ebay*Ebay and google*Amazon and hotmail*1",
           "Which of the following is a valid email address?*Johnbrown.com*Johnbrown@com*Johnbrowngmail.com*Johnbrown@gmail.com*4",
           "Which one of the following is a search engine?*Chrome*Altavista*Msn*Netscape*2",
           "Which of the following is a web browser?*Hotmail*Ms word*Internet*Chrome*4",
           "Another name for the address of a web page is*Its website*Its domain name*Its ULR*Its URL*4",
           "What do the letters CPU stand for?*Computer processing unit*Central puter unit*Computer personal unit*Central processing unit*4",
           "Web Camera is a____device*input*output*memory*Both 1 & 2*1",
           "Amazon is a ___Company*Airlines*Transport*Ecommerce*Dairy*3"]
""" In this method all the list elements in the question and options are split and added as list elements to options"""
def getQuestionsAndOptions():
    for questionOptions in questionsOptions:
        question_options.append(questionOptions.split("*"))
    return question_options

def QuestionAndOptions(score):
    i=1
    
    for qoption in question_options:
        q=qoption[0]
        opt1=qoption[1]
        opt2=qoption[2]
        opt3=qoption[3]
        opt4=qoption[4]
        ans=qoption[5]
        print()
        print("Q "+str(i)+". "+q)
        print()
        print("1. "+opt1)
        print("2. "+opt2)
        print("3. "+opt3)
        print("4. "+opt4)
        print()
        ans_input=input("Choose your option ")
        if(ans_input==ans):
            print()
            print("Correct Answer, You Scored 100 points for this Question")
            score=score + 100
        else:
            print("Wrong Answer, You Scored 0 points for this Question")
        i=i+1       
    print("*****************************************************************************************")
    print("**********************Congratulations",userName," your Score =",score,"**************************************")
    return score
                 
        
       
print("******************************************TECH QUIZ**************************************")
print("There are 10 MCQs in this Quiz. Each correct anwer would get 100 points. There are no negetive points for wrong answer.")

q=[]
score=0
userName=""
question_options=[]
getUser(userName)
getQuestionsAndOptions()
QuestionAndOptions(score)


