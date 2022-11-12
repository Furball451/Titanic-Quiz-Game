# Developer: Zachery S Obendorf
# Date Nov 12 2022
# Project: Quiz game based on the RMS Titanic

question_1 = input("Who was Titanic's wealthist passenger?")

question_2 = input("Where are many of Titanic's victims buried?")

question_3 = input("""What was the last ship that Titanic 
                    had contact with before it 
                    struck the iceberg? 
                    a: SS New Yorker, 
                    b: SS Chicago, 
                    c: SS Californian""")
question_4 = input("""What the last port Titanic docked
                     before sailing for New York? a: South Hampton, b: Queenstown, c: Sherbort""")

question_5 = input("""T/F: It is speculated that the last song 
                    Titanic's band played was 'My God To Thee'""")

if question_1.capitalize == "John Jacob Astor ":
    print("Correct!")
else:
    print("Wrong")
    print("Correct answer was John Jacob Astor")
if question_2.capitalize == "Halifax, Nova Scotia":
    print("Correct!")
else:
    print("Wrong!")
    print("Correct answer was Halifax, Nova Scotia")

if question_3.capitalize == "c":
    print("Correct!")
else:
    print("Wrong!")
    print("Correct answer was c")
if question_4.capitalize == "b":
    print("Correct")

if question_5.capitalize == "t":
    print("Correct")
