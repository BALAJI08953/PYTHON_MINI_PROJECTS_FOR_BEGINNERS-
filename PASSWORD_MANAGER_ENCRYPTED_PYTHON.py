from cryptography.fernet import Fernet
def write_key():
    key =Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
def load_key():
    file= open("key.key","rb")
    key=file.read()
    file.close()
    return key
master_pwd=input("WHAT IS THE MASTER PASSWORD?:")
write_key()
key=load_key()
fer=Fernet(key)
def view():
    with open("PASSWORD.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("|")
            print("user:",user,"| password",(fer.decrypt(passw.encode())))
def add():
    name=input("ACCOUNT NAME: ")
    pwd=input("PASSWORD: ")
    with open("password.txt","a") as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode())
while True:
    mode=input("WOULD LIKE TO HAVE NEW PASSWORD OR VIEW EXISTING PASSWORD:(VIEW,ADD) AND PRESS Q QUIT ?:").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("INVALID MODE.")
        continue