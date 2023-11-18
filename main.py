# Student number: 2804535

# Term 1
print("# # # Term 1 # # #")
AES1 = int(input("Please tell me your Term 1 AES score: "))
Maths1 = int(input("Please tell me your Term 1 Maths 1 score: "))
Physics1 = int(input("Please tell me your Term 1 Physics 1 score: "))
Computerprogramming1 = int(input("Please tell me your Term 1 Computer Programming 1 score: "))

if AES1<0 or AES1>100 or Maths1<0 or Maths1>100 or Physics1<0 or Physics1>100 or Computerprogramming1<0 or Computerprogramming1>100:
    print("That is not a valid input. Goodbye.")
    quit()
else:
    print("Thank you, Term 1 is inputted.")

# Term 2
print("# # # Term 2 # # #")
AES2 = int(input("Please tell me your Term 2 AES score: "))
Maths2 = int(input("Please tell me your Term 2 Maths 2 score: "))
Physics2 = int(input("Please tell me your Term 2 Physics 2 score: "))
Computerprogramming2 = int(input("Please tell me your Term 2 Computer Programming 2 score: "))

if AES2<0 or AES2>100 or Maths2<0 or Maths2>100 or Physics2<0 or Physics2>100 or Computerprogramming2<0 or Computerprogramming2>100:
    print("That is not a valid input. Goodbye.")
    quit()
else:
    print("Thank you, Term 2 is inputted.")

# Term 3
print("# # # Term 3 # # #")
AES3 = int(input("Please tell me your Term 3 AES score: "))
Maths3 = int(input("Please tell me your Term 3 Maths 3 score: "))
Physics3 = int(input("Please tell me your Term 3 Physics 3 score: "))
Creativedesign = int(input("Please tell me your Term 3 Creative Design score: "))

if AES3<0 or AES3>100 or Maths3<0 or Maths3>100 or Physics3<0 or Physics3>100 or Creativedesign<0 or Creativedesign>100:
    print("This is not a valid input. Goodbye.")
    quit()
else:
    print("Thank you, Term 3 is inputted.")

Overall = (AES1 + Maths1 + Physics1 + Computerprogramming1 + AES2 + Maths2 + Physics2 + Computerprogramming2 + AES3 + Maths3 + Physics3 + Creativedesign) / 12

AvgMath2Math3 = (Maths2+Maths3) / 2

if AES1>=40 and Maths1>=40 and Physics1>=40 and Computerprogramming1>=40 and AES2>=40 and Maths2>=40 and Physics2>=40 and Computerprogramming2>=40 and AES3>=40 and Maths3>=40 and Physics3>=40 and Creativedesign>=40:
    if Overall >= 60:
        if AvgMath2Math3 >= 65:
            if AES3 >= 60 and AES3 != 100:
                print("Well done :) YOU PROGRESS!!!")
            elif Overall == 100:
                print("Well done :) YOU PROGRESS!!!")
                print("Wow you are so smart! 100 in everything!!")
            else:
                print("Sorry, you do not progress because you must have at least 60% in AES Term 3.")
        else:
            print("Sorry, you do not progress because you must have at least 65% in Math 2 and Math 3.")
    else:
        print("Sorry, you do not progress because you must have at least an average of 60% overall.")
else:
    print("Sorry, you do not progress because you must have at least 40% in all subjects.")

quit()