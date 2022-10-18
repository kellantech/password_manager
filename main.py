import json, getpass, secrets,traceback
from termcolor import colored
from kellanb_cryptography import aes,key
try: 
  mp = key.gen_key_from_password(getpass.getpass(prompt="password: "))
  with open('pass.json','r') as f:
    pwd_l = json.load(f)
  def add_pwd(new_pwd, enc_pwd, appname):
    global pwd_l
    d = aes.encrypt_aes(f"{appname} : {new_pwd}",enc_pwd)
    pwd_l.append(d)
    with open('pass.json', 'w') as fi:
      json.dump(pwd_l,fi)
  
  def get_pwd(enc_pwd):
    for i in pwd_l:
  
      try:
        a = aes.decrypt_aes(i,enc_pwd)
        print(a)

      except ValueError as e:
        if e.args[0] == "MAC check failed":
          t = ("bad password")
          print(colored(t,"white","on_red"))
  print('v: veiw all passwords \na: add a password\nq: quit\nr: add a random password')    
  def add_random_pass(enkey,appname):
    p = secrets.token_urlsafe(16)
    add_pwd(p,enkey,appname)
  while True:
    c = input('>')
    if c == 'q':
      break
    if c == 'v':
      get_pwd(mp)
    if c == 'a':
      add_pwd(getpass.getpass(prompt="what password would you like to add: "),mp,input("what website/app is this for? "))
    if c == 'r':
      add_random_pass(mp,input("what website/app is this for? "))
except Exception as er:
      txt = ("ERROR! please send the following information to kellanbutler52@gmail.com :\n")
      print(colored(txt,"white","on_red"))
      txt2 = f"{type(er)}:{er.args}:{traceback.format_exc()}"
      print(colored(txt2,"red"))      
