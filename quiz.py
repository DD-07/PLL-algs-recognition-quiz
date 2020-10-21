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

answer_1 = input("Q1) What is this PLL algorithm?")

#Start of quiz
print("What is this PLL algorithm?")
print(Ub_alg)
print("a) Ub")
print("b) Rb")
print("c) Na")

if answer_1 == "a" or answer_1 == "a)":
  print("Correct!")
  print("Points: " + str(points += 1))
elif answer_1 == "a" or answer_1 == "b)":
  print("Wrong, " + Ub_alg + " was Ub")
  print("Points: " + str(points))
elif answer_1 == "c" or answer_1 == "c)":
  
  
  

