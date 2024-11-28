from groq import Groq
import os
from dotenv import load_dotenv


class LLamaGroq:
    def __init__(self, model) -> None:
        load_dotenv()
        self.client = Groq(api_key=os.getenv("api"))
        self.model = model
        self.path = "LLAMA\\Response\\"

    def create_chats(self, message):
        self.conversation_history = [{"role": "system", "content": "You are an expert python coder. Respond with only optimal code and best solution with no explanations."}] 
        self.conversation_history.append({"role": "user", "content": message})

        self.completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        all_responses = []

        for chunk in self.completion:
            content = chunk.choices[0].delta.content or "" 
            if content:
                self.conversation_history.append({"role": "assistant", "content": content})
                all_responses.append(content)

        resp = "".join(all_responses)
        return resp.strip("`")


    def save(self, task_name, resp):
        with open(self.path + task_name+".py", "w") as file:
            file.write(resp)

    def __len__(self):
        return len(self.conversation_history)

    def __repr__(self) -> str:
        return f"Agent - {self.model}"
        
    
llama = LLamaGroq("llama3-8b-8192")
        