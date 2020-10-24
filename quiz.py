#Variables for algs
Ub_alg = "R2 U (R U R' U') R' U' (R' U R')"
Ua_alg = "(R U' R U) R U (R U' R' U') R2"
Z_alg = "(M2' U M2' U) (M' U2) (M2' U2 M') [U2]"
H_alg = "(M2' U M2') U2 (M2' U M2')"  
Aa_alg = "x (R' U R') D2 (R U' R') D2 R2 x'"
Ab_alg = "x R2' D2 (R U R') D2 (R U' R) x'"
E_alg = "x' (R U' R' D) (R U R' D') (R U R' D) (R U' R' D') x"
Ra_alg = "(R U' R' U') (R U R D) (R' U' R D') (R' U2 R') [U']"
Rb_alg = "(R' U2 R U2') R' F (R U R' U') R' F' R2 [U']"
Ja_alg = "(R' U L' U2) (R U' R' U2 R) L [U']"
Jb_alg = "(R U R' F') (R U R' U') R' F R2 U' R' [U']"
T_alg = "(R U R' U') (R' F R2 U') R' U' (R U R' F')"
F_alg = "(R' U' F')(R U R' U')(R' F R2 U')(R' U' R U)(R' U R)"
V_alg = "(R' U R' U') y (R' F' R2 U') (R' U R' F) R F"
Y_alg = "F (R U' R' U') (R U R' F') (R U R' U') (R' F R F')" 
Na_alg = "(RUR'U)(RUR'F')(RUR'U')(R'FR2U') R' U2 (RU'R')"
Nb_alg = "(R' U R U') (R' F' U' F) (R U R' F) R' F' (R U' R)"
Ga_alg = "R2 U (R' U R' U') (R U' R2) D U' (R' U R D') [U]"
Gb_alg = "(F' U' F) (R2 u R' U) (R U' R u') R2'"
Gc_alg = "R2 U' (R U' R U) (R' U R2 D') (U R U' R') D [U']"
Gd_alg = "D' (R U R' U') D (R2 U' R U') (R' U R' U) R2 [U]"
alg = "x x' y y' z' z"     

#Variables for quiz itself
points = 0

#Start of quiz
#Question 1 /////////////////////////////////////////////////////////////////////////
answer_1 = input("Q1) What is this PLL algorithm?" + Ub_alg + "a) Ub, b) Rb, c) Na")
if answer_1 == "a" or answer_1 == "a)":
  print("Correct!")
  points = points + 1
  print("Points: " + str(points))
elif answer_1 == "b" or answer_1 == "b)":
  print("Wrong, " + Ub_alg + " was Ub perm")
  print("Points: " + str(points))
elif answer_1 == "c" or answer_1 == "c)":
  print("Wrong, " + Ub_alg + " was Ub")
  print("Points: " + str(points))
#Question 2//////////////////////////////////////////////////////////////////////
answer_2 = input("Q2) What is this PLL algorithm?" + Y_alg + "a) H, b) Ga, c) Y")
if answer_2 == 'a' or answer_2 == 'a)': 
  print("Wrong, " + Y_alg + " was Y perm")
  print("Points: " + str(points))
elif answer_2 == 'b' or answer_2 == 'b)':
  print("Wrong, " + Y_alg + " was Y perm")
  print("Points: " + str(points))
elif answer_2 == 'c' or answer_2 == 'c)':
  print("Correct!")
  points = points + 1
  print("Points: " + str(points))
#Question 3/////////////////////////////////
answer_3 = input("Q3) Which of the following represents the Ja algorithm?" + "a) " + Ub_alg + " b) " + Ja_alg + " c) " + Aa_alg)
if answer_3 == 'a' or answer_3 == 'a)':
  print("Wrong, this algorithm is the Aa algorithm.")
  print("Points: " + str(points))
elif answer_3 == 'b' or answer_3 == 'b)':
  print("Correct!")
  points = points + 1
  print("Points: " + str(points))
elif answer_3 == 'c' or answer_3 == 'c)':
  print("Wrong, this algorithm was the Ja algorithm.")
  print("Points: " + str(points))
#Question 4///////////////////////////////////////////////////
answer_4 = input("Q4) How many G perms are there? a) 3 b) 6 c) 4")
if answer_4 == 'a' or answer_4 == 'a)':
  print("Wrong, there are 4 G perms in total.")
  print("Points: " + str(points))
elif answer_4 == 'b' or answer_4 == 'b)':
  print("Wrong, there are 4 G perms in total.")
  print("Points: " + str(points))
elif answer_4 == 'c' or answer_4 == 'c)':
  print("Correct!")
  points = points + 1
  print("Points: " + str(points))
#Question 5/////////////////////////////////////
answer_5 = input("Q5) How many moves are in the T perm? a) 15 b) 13 c) 18")
if answer_5 == 'a' or answer_5 == 'a)':
  print("Correct!")
  points = points + 1
  print("Points: " + str(points))
elif answer_5 == 'b' or answer_5 == 'b)':
  print("Wrong, the T perm has 15 moves")
  print("Points: " + str(points))
elif answer_5 == 'c' or answer_5 == 'c)':
  print("Wrong, the T perm has 15 moves")
  print("Points: " + str(points))
print("Well done! You have come to the end of the quiz!")
if points < 3:
  print("It's ok, you can do better next time!")
  print("Thank you for playing! I hope you are now more familiar with the PLL algorithms!")
else:
  print("Great job! You are a master!")
  print("Thank you for playing! I hope you are now more familiar with the PLL algorithms!")

        
  




  
  
  

