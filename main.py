from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

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
  res = generate_random_sentence_n(10)
  print(res)

if __name__ == "__main__":
  main()
