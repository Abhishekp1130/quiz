print("WELCOME TO THE QUIZ !")
name = input("what is your'e name?")
print(f"hello {name}")
playing= input("Are you ready to play? ")
if playing.lower()!="yes":
    quit()
print("ok! let's Begin")
score=0
answer = input("1. What year did the Titanic sink in the Atlantic Ocean on 15 April, on its maiden voyage from Southampton? a.1915  b.1913  c.1918  d.1912  ").lower()
if answer =="1912":
    print("your'e right")
    score+=1

else:
    print("oops!your'e wrong")
answer = input("2. When was God Father released ? a.1972  b.1954 c.1988  d.1979  ").lower()
if answer =="1972":
    print("your'e right")
    score+=1
    print(f"your score = {score}")
else:
    print("oops!your'e wrong")
    