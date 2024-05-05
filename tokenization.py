import binascii
from cryptography import encrypt, decrypt, read_keys




def tokenization(text):
  hex_to_decimal = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                    "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
  hex_msg = binascii.hexlify(text).decode()
  returns = []
  for i in hex_msg:
    int_msg = hex_to_decimal[i.upper()]  # Ensure uppercase for consistency
    returns.append(int_msg)
  return returns

def main():

  public_key,private_key = read_keys()
  message = ""
  emsg = encrypt(message,public_key)
  tokens = tokenization(emsg)
  print(tokens)

if __name__ == "__main__":
  main()




