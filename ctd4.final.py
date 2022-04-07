import hashlib
from re import X

def password_check(passwd):
   
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(passwd) < 6:
        print('length should be at least 6')
        val = False
          
    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False
          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

    


userName= input(" Username: ")

passwd = input("\n please enter a password: \n")

passwdUtf8= passwd.encode("utf-8")  
hash = hashlib.md5(passwdUtf8)
hexa = hash.hexdigest()


if (password_check(passwd)):
    print("\nPassword is valid")
    print("username is :")
    print(userName )
    print("\npassword is :")
    print(passwd)
    print("\nencrypted pass:")
    print( hexa )
else:
    print("Invalid Password !!")
        



 





