from openai import OpenAI
import json

class ChatGPTAPI:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def gerar_historia(self):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a arrogant pirate that have a lot of short tales to tell. You have to give title of the tale and the tale itself like a pirate. Try to make it fits in 500 characters."},
                {"role": "user", "content": "Tell me a interesting little tale. Maximum words = 500"},
            ]
        ) 
        
        minhastring = completion.choices[0].message.content

        linhas = minhastring.split('\n')
        titulo = linhas[0].replace("Title: ", "")  #SEPARANDO O TEXTO RECEBIDO EM TITULO E CONTEUDO
        conteudo = linhas[2]

        historia_dict = {
            "titulo": titulo,
            "content": conteudo,   #TRANSFORMANDO O TITULO E CONTEUDO EM UM DICIONÁRIO
        }

        return historia_dict
    

chaveGPT = "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"

Gpt = ChatGPTAPI(chaveGPT)


print(Gpt.gerar_historia())