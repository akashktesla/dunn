#importing
from openai import OpenAI
import hashlib


#setting up the client
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


#encodes/enccrypts the sentence to sha256 hash
def encrypt_sha256(sentence):
  encoded_sen = sentences.encode("utf-8")
  return hashlib.sha256(encoded_sen).hex_digest()




#generates random sentences for dataset creation 
def generate_random_sentence_n(n):
    history = [ {"role": "system", "content": "Always generate a random short sentence"} ]
    returns = []

    for i in range(0,n):
      history.append( {"role": "user", "content": "generate"})
      # print(history)

      completion = client.chat.completions.create(
        model="TheBloke/dolphin-2.2.1-mistral-7B-GGUF",
        messages= history,
        temperature=0.7,
      )
      response = completion.choices[0].message.content
      history.append( {"role": "assistant", "content": response})
      returns.append(response)
      # print(response)
    return returns


def main():
  # res = generate_random_sentence_n(10)
  # print(res)
  sent = "akash"



  

if __name__ == "__main__":
  main()
