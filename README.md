# 🤖 TalentScout Hiring Assistant Chatbot

An intelligent, AI-powered Hiring Assistant chatbot built with **Streamlit** and **LLaMA3**, designed to automate the initial screening process for tech candidates. The chatbot interacts conversationally with candidates, collects essential details, and generates relevant technical questions based on their declared tech stack.

---

## 🧠 Features

- 🔹 **Interactive Chat UI** using Streamlit
- 👋 **Greeting & Introduction** at session start
- 📝 **Information Gathering**: Full name, contact, location, experience, desired roles, tech stack
- 💻 **Tech Stack Declaration** with dynamic prompt handling
- ❓ **Automated Technical Question Generation** (3–5 tailored questions per tech/tool)
- 🧵 **Context Management**: Maintains smooth, relevant dialogue
- 🧯 **Fallback Handling** for unclear or irrelevant inputs
- ✅ **Secure Data Handling** using simulated/anonymized storage
- 🙋 **Conversation Exit** on specific keywords (e.g., “bye”, “exit”)
- 🌐 Optional: Cloud Deployment or Demo Recording

---

## 🛠 Tech Stack

| Component             | Tool/Library         |
|----------------------|----------------------|
| 💻 Frontend UI        | Streamlit             |
| 🧠 Language Model     | LLaMA3 (via API/integration) |
| 🔧 Backend Logic      | Python                |
| 🗃️ Data Storage        | Local (Simulated) |
| 📜 Prompt Design      | Custom Templates for GPT/LLaMA3 |

---

## ⚙️ Installation Instructions

1. **Clone the Repository**
    ```bash
    git clone https://github.com/chinmay1p/Hiring-Bot.git
    ```
2. Open the terminal
3. Start a python virtual environment using -
   ```
   python -m venv .venv
   ```
5. Run -
   ```
   .venv\Scripts\activate.ps1
   ```
6.Install dependencies -
   ``` 
  pip install -r req.txt
   ```
7.Set Environment Variables
Create a .env file and add your API key (for LLaMA3, Together.ai, etc.):
```
TOGETHER_API_KEY=your-api-key-here
```
8.Run the app
```
streamlit run app.py
```

---

## ✅ Future Improvements (Bonus)
- 🌍 Multilingual support
- 🧠 Memory-based personalization for returning users
- 🎨 Enhanced UI styling with custom themes
- 📈 Analytics dashboard for recruiters

---

## Working

Demo - https://www.loom.com/share/09d3030f7ace46f1ae6c72ab0442afca?sid=3847bf6c-8ad8-4d35-b7e2-6381e2f7316d

![image](https://github.com/user-attachments/assets/9d1e707c-c983-4c7b-ac16-cbf6563b46dc)


