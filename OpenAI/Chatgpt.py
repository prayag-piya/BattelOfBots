import os
import json

from openai import OpenAI

class ChatGPT:
    def __init__(self, model: str) -> None:
        #loading API for the agent
        with open("OpenAI/config.json", "r") as file:
            self.api_key = json.loads(file.read())["api_key"]
        self.path = "OpenAI\\Response\\"
        self.model = model
        self.client = OpenAI(api_key=self.api_key)
        self.conversation_history = [{"role": "system", "content": "You are an expert python coder. Respond with only code and no explanations."}]
        

    def create_chats(self, message):
        self.conversation_history.append({"role": "user", "content": message})

        completion = self.client.chat.completions.create(
            model=self.model,
            messages= self.conversation_history,
            max_tokens=150
        )

        reply = completion.choices[0].message['content']
        self.conversation_history.append({"role": "assistant", "content": reply})

        return reply.strip("`")

    
    def save(self, task_name, resp):
        with open(self.path + task_name+".py", "w") as file:
            file.write(resp)

    def __len__(self):
        return len(self.conversation_history)

    def __repr__(self):
        return f"Agent Model - {self.model}"
    

chatgpt = ChatGPT("gpt-3.5-turbo")