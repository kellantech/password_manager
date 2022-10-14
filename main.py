import json, getpass
from kellanb_cryptography import aes,key
mp = key.gen_key_from_password(getpass.getpass(prompt="password: "))
with open('pass.json','r') as f:
  pwd_l = json.load(f)
def add_pwd(new_pwd, enc_pwd):
  global pwd_l
  d = aes.encrypt_aes(new_pwd,enc_pwd)
  pwd_l.append(d)
  with open('pass.json', 'w') as fi:
    json.dump(pwd_l,fi)

def get_pwd(enc_pwd):
  for i in pwd_l:
    a = aes.decrypt_aes(i,enc_pwd)
    print(a)
print('v: veiw all passwords \na:add a password\nq:quit\n')    
while True:
  c = input('>')
  if c == 'q':
    break
  if c == 'v':
    get_pwd(mp)
  if c == 'a':
    add_pwd(getpass.getpass(prompt="what password would you like to add: "),mp)
