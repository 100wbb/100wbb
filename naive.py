data = [ ['young','high','no','fair','no'],
['young','high','no','excellent','no'],
['old','low','yes','excellent','no'],
['middle','low','yes','excellent','yes'],
['young','medium','no','fair','no'],
['young','low','yes','fair','yes'],
['old','medium','yes','fair','yes'],
['young','medium','yes','excellent','yes'],
['middle','medium','no','excellent','yes'],
['middle','high','yes','fair','yes'],
['old','medium','no','excellent','no'],
['middle','medium','no','good','yes'],
['middle','high','yes','fair','yes'],
['old','medium','no','good','no']
]
number_data = 14

cmp_yes = 0
cmp_no = 0
for x in range(number_data): 
    if data[x][4] == 'yes':
       cmp_yes = cmp_yes + 1 
    else:
       cmp_no = cmp_no + 1 
Pcmp_yes = cmp_yes/number_data 
Pcmp_no = cmp_no/number_data
print("\nP(buys computer = 'yes'): ",(Pcmp_yes)) 
print("\nP(buys computer = 'no'): ",(Pcmp_no)) 
age = int(input("\nEnter Age: "))
income = input("\nEnter Category of Income: ") 
student = input("\nAre you a student?: ")
credit = input("\nEnter your Credit-Rating: ") 
if age<=30:
     age='young'
elif 31<=age<= 40: 
    age = 'middle'
else:
    age = 'old'
X = [age,income,student,credit] 
print("\nNew Tuple is") 
print(X)
Age_cmp_yes = 0
Age_cmp_no = 0

Inc_cmp_yes = 0
Inc_cmp_no = 0

Stud_cmp_yes = 0
Stud_cmp_no = 0

Cr_cmp_yes = 0
Cr_cmp_no = 0
for x in range(number_data):
  #age
  if data[x][0] == X[0] and data[x][4] == 'yes':
    Age_cmp_yes = Age_cmp_yes + 1
  if data[x][0] == X[0] and data[x][4] == 'no':
    Age_cmp_no = Age_cmp_no + 1
    #income
  if data[x][1] == X[1] and data[x][4] == 'yes':
    Inc_cmp_yes = Inc_cmp_yes + 1
  if data[x][1] == X[1] and data[x][4] == 'no':
    Inc_cmp_no = Inc_cmp_no + 1
    #stud
  if data[x][2] == X[2] and data[x][4] == 'yes':
    Stud_cmp_yes = Stud_cmp_yes + 1
  if data[x][2] == X[2] and data[x][4] == 'no':
    Stud_cmp_no = Stud_cmp_no + 1
    #credit
  if data[x][3] == X[3] and data[x][4] == 'yes':
    Cr_cmp_yes = Cr_cmp_yes + 1
  if data[x][3] == X[3] and data[x][4] == 'no': 
      Cr_cmp_no = Cr_cmp_no + 1
      
PAge_cmp_yes = Age_cmp_yes/cmp_yes 
PAge_cmp_no = Age_cmp_no/cmp_no 

PInc_cmp_yes = Inc_cmp_yes/cmp_yes 
PInc_cmp_no = Inc_cmp_no/cmp_no 

PStud_cmp_yes = Stud_cmp_yes/cmp_yes 
PStud_cmp_no = Stud_cmp_no/cmp_no

PCr_cmp_yes = Cr_cmp_yes/cmp_yes 
PCr_cmp_no = Cr_cmp_no/cmp_no

print("Probability that age is "+X[0]+" and buys computer is: ",(PAge_cmp_yes)) 
print("Probability that age is "+X[0]+" and does not buy computer is:",(PAge_cmp_no)) 
print("Probability that income is "+X[1]+" and buys computer is: ",(PInc_cmp_yes)) 
print("Probability that income is "+X[1]+" and does not buy computer is:",(PInc_cmp_no)) 
if(X[2] == 'yes'):
  print("Probability that person is a student and buys computer is: ",(PStud_cmp_yes))
  print("Probability that person is a student and does not buy computer is: ",(PStud_cmp_no))
else:
  print("Probability that person is not a student and buys computer is: ",(PStud_cmp_yes)) 
  print("Probability that person is not a student and does not buy computer is:",(PStud_cmp_no))
print("Probability that credit rating is "+X[3]+"and buys computer is: ",(PCr_cmp_yes))
print("Probability that credit rating is "+X[3]+"and does not buy computer is: ",(PCr_cmp_no))
P_Yes = PAge_cmp_yes*PInc_cmp_yes*PStud_cmp_yes*PCr_cmp_yes 
print("\nProbability that the person X buys a computer is: ",(P_Yes))
P_No = PAge_cmp_no*PInc_cmp_no*PStud_cmp_no*PCr_cmp_no 
print("\nProbability that the person X does not buy a computer is: ",(P_No))
CP_Yes = P_Yes*Pcmp_yes
print("\nConditional Probability that the person X buys a computer is: ",(CP_Yes))
CP_No = P_No*Pcmp_no
print("\nConditional Probability that the person X does not buy a computer is: ",(CP_No)) 
if(CP_Yes > CP_No):
  print("\nX belongs to class: buys computer(yes)") 
else:
  print("\nX belongs to class: buys computer(no)")