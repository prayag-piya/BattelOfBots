import os
import json
from OpenAI.Chatgpt import ChatGPT, chatgpt
from LLAMA.GroqBase import LLamaGroq, llama



if __name__ == "__main__":
    for file in os.listdir("Problem"):
        with open("Problem\\"+file, "r") as f:
            resp = llama.create_chats(f.read())
            llama.save(file, resp)

    if json.load(open("OpenAI\\config.json", 'r'))["api_key"] != "change_me":
        for file in os.listdir("Problem"):
            with open("Problem\\"+file, "r") as f:
                resp = chatgpt.create_chats(f.read())
                chatgpt.save(file, resp)  
    else: 
        print("ITs still the same")