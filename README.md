# Steve Jobs vs Elon Musk Debate Chatbot

This project simulates a live debate between two iconic tech leaders: **Steve Jobs** and **Elon Musk**. Using cutting-edge AI models from OpenAI and Groq, this chatbot mimics the ideologies and speaking styles of both individuals. The debate is hosted within a conversational interface powered by **Gradio**, and at the end, a **virtual judge** determines the winner based on the conversation.

---

## 💡 Objective

Create an interactive chatbot that:
- Simulates a debate between Steve Jobs and Elon Musk.
- Uses LLMs to generate dynamic, back-and-forth conversation.
- Judges and declares a winner based on the full debate transcript.

---

## ⚙️ Features

- 🤖 **Character Emulation**: 
  - Steve Jobs: Responds using OpenAI's `gpt-4o-mini`.
  - Elon Musk: Responds using Groq's `llama-3.2-90b-vision-preview`.

- 🧠 **Conversational Context**:
  - Maintains the chat history throughout the debate for coherent replies.

- 🧑‍⚖️ **Virtual Judging**:
  - A separate Groq model (`llama-3.3-70b-versatile`) reviews the debate and selects a winner.

- 🎨 **User Interface**:
  - Built using `Gradio` for an interactive and easy-to-use experience.
  - Includes a chat window and a textbox displaying the judge's final decision.

---

## 🛠️ Tech Stack

| Component           | Technology Used                   |
|---------------------|-----------------------------------|
| LLM for Jobs        | OpenAI `gpt-4o-mini`              |
| LLM for Musk        | Groq `llama-3.2-90b-vision-preview` |
| Judge Model         | Groq `llama-3.3-70b-versatile`    |
| Interface           | Gradio                            |
| Environment Config  | python-dotenv                     |

---

## 🚀 How It Works

1. The user clicks **Start** to initiate the debate.
2. Steve Jobs begins with a statement and a follow-up question.
3. Elon Musk responds and continues the thread with his counter and question.
4. This cycle continues for **10 turns**.
5. After the debate ends, a **virtual judge** reviews the entire conversation and summarizes + announces the **winner**.
6. The full conversation and judge’s decision are displayed.

---

## 🧪 Setup & Run

1. Clone the Repository

    ```bash
    git clone https://github.com/yourusername/debate-chatbot.git
    cd debate-chatbot

2. Install Dependencies

    ```bash
    pip install -r requirements.txt

3. Set Up API Keys
4. Run the application

### A Gradio interface will launch in your browser.

## Notes

- You can customize the debate topic or personas by modifying the system prompts.
- Each response is generated live using API calls, so ensure proper rate limits and key management.

---

## Contact

For questions or collaborations, feel free to reach out to nkarvindkumar@gmail.com.

