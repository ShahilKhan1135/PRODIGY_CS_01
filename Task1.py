print("This is Ciepher Case Project")
print("1.Encryption")
print("2.Decryption")
print("3.Exit")
def cieher(value):
    special = r"`~!@#$%^&*()-_=+[]{};:'\",|.<>/?"
    if value==1:
        message=input("Enter Your Meassage: ")
        num=int(input("Enter the shift value: "))
        newmessage=""  
        for i in message:
            if i.isupper():
                i=ord(i)-ord('A')
                i=(i+num)%26
                i=chr(i+ord('A'))
                newmessage+=i
            elif i.islower():
                i=ord(i)-ord('a')
                i=(i+num)%26
                i=chr(i+ord('a'))
                newmessage+=i
            elif i.isdigit():
                i=int(i)
                i=(i+num)%10
                i=str(i)
                newmessage+=i
            elif i in special:
                i=special.index(i)
                i=(i+num)%len(special)
                i=special[i]
                newmessage+=i
            else:
                newmessage+=i
        print("Your Message after Caesor Cipher is:",newmessage)
    elif value==2:
        message=input("Enter Your Meassage: ")
        num=int(input("Enter the shift value: "))
        newmessage=""
        for i in message:
            if i.isupper():
                i=ord(i)-ord('A')
                i=(i-num)%26
                i=chr(i+ord('A'))
                newmessage+=i
            elif i.islower():
                i=ord(i)-ord('a')
                i=(i-num)%26
                i=chr(i+ord('a'))
                newmessage+=i
            elif i.isdigit():
                i=int(i)
                i=(i-num)%10
                i=str(i)
                newmessage+=i
            elif i in special:
                i=special.index(i)
                i=(i-num)%len(special)
                i=special[i]
                newmessage+=i
            else:
                newmessage+=i
        print("Your Message after Caesor Cipher is:",newmessage)
    else:
        print("Please enter proper number.")
while True:
    value=int(input("Enter your choice: "))
    if value==3:
        break
    cieher(value)