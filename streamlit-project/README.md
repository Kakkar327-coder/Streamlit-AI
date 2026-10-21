# 🔥 Smart AI Assistant

> 🚀 **Built during the Summer Bootcamp**

An interactive web application powered by **Streamlit** and the official **Google GenAI SDK**, allowing users to ask any question and receive AI-generated responses tailored to customizable personality styles and tones.

---

## ✨ Features

- **🎭 Multiple Response Styles**: Customize the AI's persona on the fly:
  - **Normal**: Direct, helpful, and balanced
  - **Funny**: Humorous, witty, and entertaining
  - **Strict Teacher**: Structured, academic, and disciplined
  - **Motivational**: Uplifting, energetic, and inspiring
- **⚡ Google Gemini Models**: Powered by Google's Gemini models (such as `gemini-2.5-flash` and `gemini-3.8-flash`).
- **⚙️ Flexible Configuration**:
  - Securely loads API keys from `.env` or system environment variables.
  - Interactive sidebar settings to enter API keys or switch Gemini models on the fly.
- **🛡️ Graceful Error Handling**: User-friendly alerts for missing questions, invalid keys, or API quota limits.

---

## 📁 Project Structure

```text
streamlit-project/
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── .env                # Local API key configuration (git-ignored)
├── .env.example        # Template for environment variables
├── .gitignore          # Git ignore rules for virtual environments & secrets
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites

- **Python 3.10+** (Python 3.11 – 3.13 recommended)
- A **Google Gemini API Key** from [Google AI Studio](https://aistudio.google.com/)

---

### 2. Setup Virtual Environment

Navigate to the project directory:

```bash
cd streamlit-project
```

#### Windows (PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### Windows (Command Prompt)
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

*(Packages installed: `streamlit`, `google-genai`, `python-dotenv`)*

---

### 4. Configure Your API Key

You can configure your Google Gemini API key in one of three easy ways:

#### Option A: `.env` File (Recommended)
Create a `.env` file in the `streamlit-project` directory (or copy from `.env.example`):

```bash
GEMINI_API_KEY=your_actual_api_key_here
```

#### Option B: Environment Variable
- **PowerShell**:
  ```powershell
  $env:GEMINI_API_KEY = "your_actual_api_key_here"
  ```
- **Bash / macOS**:
  ```bash
  export GEMINI_API_KEY="your_actual_api_key_here"
  ```

#### Option C: In-App Sidebar
Launch the app and enter your API key directly into the **Settings** sidebar.

---

### 5. Run the Application

```bash
streamlit run app.py
```

Once started, open your browser at:
👉 **`http://localhost:8501`**

---

## 💡 How It Works

1. **User Input**: Enter your prompt or question in the text input field.
2. **Style Selection**: Choose a response tone from the dropdown menu.
3. **Prompt Composition**: The app formats your question with the chosen tone guidance.
4. **API Generation**: `client.models.generate_content` is invoked with the selected Gemini model.
5. **Real-Time Display**: Streamlit renders the generated answer with clear status notifications.

---

## 🛠️ Troubleshooting

- **PowerShell Execution Policy Error**:
  If script activation is blocked, run:
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
  .\venv\Scripts\Activate.ps1
  ```
- **Invalid API Key**:
  Ensure your key from [Google AI Studio](https://aistudio.google.com/) is set correctly in `.env` without extra quotes or spaces.
- **503 / Resource Exhausted**:
  The Gemini API endpoint may be temporarily under high demand. Wait a moment and retry, or switch to another model in the sidebar.

---

## 📜 Acknowledgments

Created as part of the **Summer Bootcamp**.
