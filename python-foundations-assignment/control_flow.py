##SECTION 3
#Age
age = int(input("enter your age: "))
if age < 13:
    print("child")
elif age < 20:
    print("teenager")
else:
    print("adult") 

password = input("enter password: ")
if len(password) >= 8:
    print("strong password")
else:
    print("weak password")

#gradeclass
score = int(input("enter your score: "))
if score >=80:
    print("grade A")
elif score >= 70:
    print("grade B")
elif score >= 60:
    print("grade C")
elif score >= 50:
    print("grade D")
else:
    print("fail")


#Mtable
number = int(input("enter a number: "))
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")


#Game
secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("guess the number: "))
if guess == secret_number:
    print("correct!")
else:
    print("try again")

#Countdown
for i in range(10,0,-1):
    print(i)
print("countdown complete!")

#ATM
balance = 1000
withdrawal = float(input("enter withdrawal amount: "))
if withdrawal <= balance:
    balance -= withdrawal
    print("withdrawal successful")
    print("remaining balance:", balance)
else:
    print("insufficient balance")

#login
username = input("enter username: ")
password = input("enter password: ")

if username == "admin" and password == "1234":
    print("login successful")
else:
    print("invalid username or password")

