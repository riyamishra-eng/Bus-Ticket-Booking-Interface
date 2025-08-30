female=40
man=80
mf=120
print("||..Welcome to MSRTC Bus terminal..||")

while True:

    print("1.ticket for yavatmal to nag.")
    print("2.ticket for yavatmal to wardha.")
    print("5.ticket for nag to yvtml.")
    print("8.ticket for nag. to wardha.")
    ticket=int(input("choose a destination :"))
    if ticket in [1,2,5,8]:
        print("a.for female ")
        print("b.for male ")
        print("ab. for male and female both ")
        choose=input("Enter your choice:")
    if choose in ['a','b','ab']:
        numbers=int(input("enter the no. of people="))
    if (ticket==1 and choose=='a'):
        print("your amount of ticket is Rs",female*numbers)
    elif (ticket==1 and choose=='b'):
        print("your fair prize is",man*numbers)
    elif (ticket==2 and choose=='ab'):
        print("your prize for this fair is",(mf*numbers)//2)
    elif (ticket==1 and choose=='ab'):
        print("your fair prize is",mf*numbers) 
    elif (ticket==2 and choose=='b'):
        print("your fair prize is",(man*numbers)//2)
    elif (ticket==2 and choose=='a'):
        print("your fair prize is",(female*numbers)//2)
   
    else:
        print("invalid input")

    print("if you want to continue press 1 and if not then press 0")
    user =int(input("enter your choice= "))
    if user==1:
        continue
    elif user==0:
        break
print("...Thank you for using MSRTC terminal...")
