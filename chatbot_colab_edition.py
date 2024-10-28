import google.generativeai as genai
from google.colab import userdata

// Adicione uma chave de api do Gemini (https://aistudio.google.com/apikey)
GOOGLE_GEMINI_API_KEY = userdata.get('GOOGLE_GEMINI_API_KEY')

// Aplicando a key
genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

// Escolhendo o modelo
model = genai.GenerativeModel("gemini-1.5-pro-latest")

// Defininindo um lista que servirá de histórico, para que o chatbot se lembre da pergunta anterior
chat = model.start_chat(history=[])

// Entrada/Saída e maneira de parar conversa com o chatbot
prompt = input("Esperando Prompt: ")
while prompt != "sair":
  response = chat.send_message(prompt)
  print(response.text)
  prompt = input("Esperando Prompt:")
