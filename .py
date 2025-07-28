import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
    messages = [{"role": "system", "content": "Você é um assistente de atendimento ao cliente."}]
    print("Inicie a conversa com o bot (digite 'sair' para encerrar).")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Bot: Até logo!")
            break
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    chatbot()
