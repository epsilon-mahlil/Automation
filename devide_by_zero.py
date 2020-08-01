print("Give me two numbers, and I'll divide them")

while True:
    c=''
    print("Enter 'Q' to quit.")
    a=input("\nFirst Number :")
    if a=='q' :
        break
    b=input("\nSecond Number :")
    if b=='q' :
        break
    try :
       c =int(a)/int(b)
    except :
        print(" you can't devide by 0!")
    print(c)
