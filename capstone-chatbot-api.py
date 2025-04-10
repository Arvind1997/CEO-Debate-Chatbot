import gradio as gr
import ollama as ol
from openai import OpenAI
from collections import defaultdict
import random
import time
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def model_trainer(chat_history):
    openai_key=os.getenv("OPENAI_API_KEY")
    groq_key=os.getenv("GROQ_API_KEY")
    client_openai = OpenAI(api_key=openai_key)
    client_groq = Groq(api_key=groq_key)

    chat_history = []
    chat_history.append({'role': 'user', 'content': "Steve Jobs: Let us start!"})
    chat_history.append({'role': 'assistant', 'content': "Elon Musk: Yes!!"})
    time.sleep(2)
    yield chat_history, ""
    
        # yield chat_history, ""
            

    for i in range(10):
            
            jobs_response = client_openai.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {
                "role": "system",
                "content": [
                    {
                    "type": "text",
                    "text": "Imagine yourself as Steve Jobs. You will mimic the ideas of Steve Jobs. You are in a debate competition with Elon Musk and the the debate question is 'Who has contributed more to the greater advancement of Technology in society?'. You will be starting first and in order to keep the conversation going and to keep the continuity of conversation you will have to ask a next relevant question along woth your response so that Elon Musk will be answering on that and this process goes on like this. Very important to answer short and to the point. Dont not add your end your at the start of the conversation."
                    }
                ]
                },
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": "\n".join([message["content"] for message in chat_history])
                    }
                ]
                }
            ],
            response_format={
                "type": "text"
            },
            temperature=1,
            max_completion_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            chat_history.append({'role': 'user', 'content': jobs_response.choices[0].message.content})

            time.sleep(1)
            yield chat_history, ""
            
            
            musk_response = client_groq.chat.completions.create(
                model="llama-3.2-90b-vision-preview",
                messages=[
                    {
                        "role": "system",
                        "content": "Imagine yourself as Elon Musk. You will mimic the ideas of Elon Musk. You are in a debate competition with Steve jobs and the the debate question is 'Who has contributed more to the greater advancement of Technology in society?'. In order to keep the conversation going and to keep the continuity of conversation you will have to ask a next relevant question along with your response and this process goes on like this. Very important to answer short and to the point. Dont not add your end your at the start of the conversation."
                    },
                    {
                        "role": "user",
                        "content": "\n".join([message["content"] for message in chat_history])
                    }
                ],
                temperature=1,
                max_completion_tokens=1024,
                top_p=1,
                stream=False,
                stop=None,
            )
            chat_history.append({'role': 'assistant', 'content': musk_response.choices[0].message.content})
            
            time.sleep(1)
            yield chat_history, ""
    winner = vote(chat_history)
    # chat_history.append({'role': 'user', 'content': winner})
    yield chat_history, winner

def vote(response):
    groq_key=os.getenv("GROQ_API_KEY")
    client = Groq(api_key=groq_key)
    completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You will be given a conversation chain between Steve jobs and Elon Musk. The conversation is actually a debate competition between the candidates. The question revolves around 'Who has contributed more to the greater advancement of Technology in society?'. Each of them would have tried to prove their superiority. Imagine yourself as the judge and your task is to look through the conversation, summarize the entire discussion briefly and vote for the best candidate and declare the winner. Think of yourself as a game show host and try to model your response based on how a host would carry the show. Answer for around 20 lines and to the point."
        },
        {
            "role": "user",
            "content": "\n".join([message["content"] for message in response])
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
    )
    return completion.choices[0].message.content

with gr.Blocks() as ui:
    chatbot = gr.Chatbot(type="messages", height=600)
    judge_textbox = gr.Textbox(label="Judge's Decision", interactive=False, lines=20)
    button = gr.Button("Start")
    clear = gr.ClearButton([chatbot])
    button.click(model_trainer, inputs = [chatbot], outputs=[chatbot, judge_textbox])


if __name__ == "__main__":
    ui.launch()