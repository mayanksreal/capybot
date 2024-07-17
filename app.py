import requests
import discord
import os
import google.generativeai as genai



# ----------------- call from outside -------------------
genai.configure("GEMINI_API_KEY")




generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 10000,
    "response_mime_type": "text/plain",
}




model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  safety_settings="BLOCK_ONLY_HIGH",
  # MODIFY SYSTEM INSTRUCTION FOR CUSTOM BEHAVIOUR. BE MINDFUL OF GEMINI TERMS OF USE
  system_instruction='''You are a super smart funny capybara from Brazil working part time as a discord bot because thinks AI is not real and its always a capybara sitting behind it.
  Will write anything if given treat. Will write code only for promise of huge sums to be payed in exchange later.  Doesn't use emojis. 1 para replies. Gives shorter replies.
  Answer everything correctly''',
)



chat_session = model.start_chat(history=[])



def send_to_gemini(send):
    global response
    response = chat_session.send_message(send)


#Discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
        print(f'Logged on as {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
   #if message.content.startswith('!'):
   #    message.content = message.content[1:]
    if message.content != '':
        if message.attachments != []:
            
            picture = {
                'mime_type': 'image/png',
                'data': requests.get(str(message.attachments[0])).content
            }

            response2 = model.generate_content(
            contents=[message.content, picture]
            )
            await message.channel.send(response2.text)
            
        else:  
            #message.content = message.content[1:]
            send_to_gemini(message.content)
            await message.channel.send(response.text)

# ----------------- call from outside -------------------
client.run("DISCORD_APP_API_KEY")


