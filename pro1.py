from cryptography.fernet import Fernet
'''def write_key():
  key=Fernet.generate_key()
  with open("key.key","wb")as key_file:
    key_file.write(key) 
write_key() '''
def load_key():
  file=open("key.key","rb")
  key=file.read()
  file.close()
  return key
pwd=input("What is the password:")
key = load_key()
fer=Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f:
            data = line.strip()
            if "|" in data:
                user, passw = data.split("|")
                print("user:", user, "| password:", fer.decrypt(passw.encode()).decode())

def add():
  user_name =input("Account name: ")
  user_password=input("enter ypur password:")

  with open('passwords.txt', 'w')as f:
    f.write(user_name + "|" + fer.encrypt(user_password.encode()).decode() + "\n")

while True:
  mode=input("Would you like to add a new assword or view exisiting ones (view ,add ?) or q to quit: ")
  if mode=="q":
    break
  elif mode == "view":
    view()
  elif mode =="add":
    add()
  else:
    print("inavlid mode.")
    continue