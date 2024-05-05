import rsa

def generate_keys():
  public_key, private_key = rsa.newkeys(1024)

  with open("public.pem","wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

  with open("private.pem","wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

def read_keys():
  with open("public.pem","rb") as f:
      public_key = rsa.PublicKey.load_pkcs1(f.read())


  with open("private.pem","rb") as f:
      private_key = rsa.PrivateKey.load_pkcs1(f.read())

  return public_key,private_key


def main():
  # generate_keys()
  public_key,private_key = read_keys()
  # print(f'public_key: {public_key}, private_key: {private_key}')
  message = "valzkai ae "
  emsg = rsa.encrypt(message.encode(),public_key)
  print(f"ecrypted msg: {emsg}")
  demsg = rsa.decrypt(emsg,private_key)
  print(f"decrypted msg: {demsg}")

if __name__ == "__main__":
  main()
