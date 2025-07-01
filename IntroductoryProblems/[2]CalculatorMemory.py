value=0 #this is value of stored result
MR=0  #Memory is currently 0
def Calculator(first,operator,second):
    if operator=='+':
        value=first+second
        return value
    elif operator=='-':
        value=first-second
        return value
    elif operator=='*':
        value=first*second
        return value
    elif operator=='%':
        value=first%second
        return value
    elif operator=='/':
        value=first/second
        return value
    else:
        print("invalid operator")
        return 0
while True:  
        #this will continously ask user to perform further till not exit by user
        print("YOUR CALCULATOR IS READY TO ASSIST YOU")
        one=input("enter first number or if you want to use Memory simply type MR")
        if(one.upper()=='MR'):
          first=MR
        else:
          first=int(one)


        operator=input("enter operator")
        second=int(input("enter second number"))
        result=Calculator(first,operator,second)
        print("RESULT :", result)
        MR=result
        # Memory is updated
        print("Calculation done")
        print("enter 1 to perform further or 2 for exist")
        dual=int(input("enter your choice"))
        if dual==2:
            print("exiting")
        elif dual!=1:
            print("Invalid number,exiting")
            break



