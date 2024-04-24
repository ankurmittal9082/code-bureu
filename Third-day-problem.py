def checkArmstrong(n):
    #write your code here !!!!!!!!!
    temp=n

    sum=0
    while n>0:
        rem=n%10
        cube=rem**3
        sum=sum+cube
        n =  n //10
    return sum==temp    
    
    if checkArmstrong(n):
        print("true")
    else:
         print("false")            


    
