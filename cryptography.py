import rsa
import binascii

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

def encrypt(message,public_key):
  emsg = rsa.encrypt(message.encode(),public_key)
  return emsg

def decrypt(emsg,private_key):
  demsg = rsa.decrypt(emsg,private_key)
  return demsg

def main():
  # generate_keys()
  public_key,private_key = read_keys()
  message = "valzkai ae "
  emsg = encrypt(message,public_key)
  print(f"ecrypted msg: {emsg}")
  # hex_emsg = binascii.hexlify(emsg).decode()
  # print(f"Encrypted msg in Hexadecimal: {hex_emsg}")
  # int_emsg = int.from_bytes(emsg, byteorder='big')
  # print(f"Encrypted msg as base-10 integer: {int_emsg}")
  int_list = [int.from_bytes(byte, byteorder='big') for byte in emsg]
  print(f"Encrypted msg as base-10 integers: {int_list}")
  demsg = decrypt(emsg,private_key)
  print(f"decrypted msg: {demsg}")

if __name__ == "__main__":
  main()
