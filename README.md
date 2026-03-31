# 📝 Student Feedback Generator Agent

**AI-Powered Assessment Tool for Educators**

Built for Professor Fawzi BenMessaoud  
Luddy School of Informatics, Computing, and Engineering  
Indiana University Indianapolis

---

## What This Tool Does

This Streamlit application guides educators through a simple 5-step workflow to generate comprehensive, AI-powered feedback for student assignments — producing a downloadable Word document (.docx) with individualized critiques and a collective expert synthesis.

### Supported Assignment Types

| Template | Individual Feedback (Part A) | Collective Synthesis (Part B) |
|----------|:---:|:---:|
| 🔬 Hands-On Learning Activity | ✅ Section A1 (Artifact) + A2 (Reflection) | ✅ Expert Synthesis Masterclass |
| 📊 Current Events & Trend Reports | ✅ What Worked / Gaps / Recommendations | ✅ Expert Reflection & Masterclass |
| 💭 Reflection Activity | ✅ What Worked / Gaps / Recommendations | ✅ Collective Reflective Feedback |
| 💬 Discussion Question | ✅ What Worked / Gaps / Recommendations | ✅ Meta-Feedback Masterclass |

### Workflow

1. **Select** the assignment category
2. **Upload** a file with student submissions (`.docx` or `.txt`)
3. **Review** parsed students and toggle selections
4. **Generate** — AI produces individualized feedback per template
5. **Download** a formatted `.docx` document

### 💬 Chat with Agent

The app includes a built-in **Chat tab** that lets you or your TA have a conversation with the AI agent. The chat is context-aware — when a feedback session is active, the agent has access to:

- The assignment type, rubric, and context you provided
- All student names and submission excerpts
- Any feedback already generated (Part A and Part B)

**Use the Chat tab to:**
- Ask about patterns across student submissions
- Identify which students may need extra support
- Refine or adjust feedback language
- Draft class announcements or lecture talking points based on submissions
- Get help with rubric design, assignment prompts, or pedagogy

When no feedback session is active, the agent works in General Mode and can still help with assignment design, grading strategies, and educational questions.

---

## Quick Start (Local)

### Prerequisites

- Python 3.10 or higher
- An [Anthropic API key](https://console.anthropic.com/)

### Setup

```bash
# 1. Clone or unzip the project
cd feedback-generator-agent

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Set up your API key in secrets
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit .streamlit/secrets.toml and paste your Anthropic API key

# 5. Run the app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

> **Note:** If you skip step 4, you can enter your API key directly in the sidebar when the app loads.

---

## Preparing Student Submission Files

The tool expects a single file (`.docx` or `.txt`) containing all student submissions, separated by clear headers. The recommended format:

```
Student: Jane Doe
[Jane's complete submission text here — can be multiple paragraphs]

Student: John Smith
[John's complete submission text here — can be multiple paragraphs]

Student: Maria Garcia
[Maria's complete submission text here...]
```

### Supported Delimiters

The parser automatically detects these patterns:

- `Student: [Name]` — **recommended**
- `Name: [Name]`
- `Submission by: [Name]`
- `--- [Name] ---`
- `## [Name]`

### Tips for Preparing Files from Canvas

1. Open each student's submission in Canvas
2. Copy all submissions into a single Word document or text file
3. Add `Student: [First Last]` before each student's work
4. Save as `.docx` or `.txt`

---

## Deployment Options

### Option A: Streamlit Community Cloud (Free — Recommended)

This is the easiest way to share with your TA. No server setup required.

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR-USERNAME/feedback-generator.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repo
   - Set the main file path to `app.py`
   - Click "Deploy"

3. **Add Your API Key:**
   - In the deployed app, go to **Settings → Secrets**
   - Paste:
     ```toml
     ANTHROPIC_API_KEY = "sk-ant-api03-YOUR-KEY-HERE"
     ```
   - Save. The app will auto-reload with the key pre-filled.

4. **Share the URL** with your TA — they can use it immediately.

### Option B: Docker

```bash
# Build
docker build -t feedback-agent .

# Run (with API key as environment variable)
docker run -p 8501:8501 \
  -e ANTHROPIC_API_KEY="sk-ant-api03-YOUR-KEY" \
  feedback-agent
```

Access at `http://localhost:8501`.

### Option C: Railway / Render / Fly.io

These platforms auto-detect Dockerfiles or Python apps:

1. Push your repo to GitHub
2. Connect the repo on your chosen platform
3. Set the environment variable `ANTHROPIC_API_KEY`
4. Deploy — the platform handles the rest

---

## Chat with Agent Feature

The app includes a **Chat with Agent** tab alongside the Feedback Generator. This conversational AI assistant is context-aware — it can see your current assignment type, rubric, all student submissions, and all generated feedback.

**What you can ask:**
- Questions about specific students: "What patterns do you see in Maria's submission?"
- Feedback refinement: "Suggest a warmer phrasing for John's critical gaps section"
- Class-level insights: "What common misconceptions do you see across all submissions?"
- Teaching strategy: "What should I emphasize in next week's lecture based on these results?"
- General pedagogy: "How should I design a rubric that encourages deeper reflection?"

The chat preserves conversation history within a session and shows a context indicator ("Context-Aware Mode" vs "General Mode") depending on whether student data is loaded.

---

## Project Structure

```
feedback-generator-agent/
├── .streamlit/
│   ├── config.toml              # Streamlit theme and settings
│   └── secrets.toml.example     # Template for API key (copy to secrets.toml)
├── app.py                       # Main Streamlit application (UI + workflow)
├── templates.py                 # Four feedback template definitions with prompts
├── parser.py                    # Student submission file parser
├── doc_generator.py             # Word document (.docx) generator using python-docx
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Container deployment configuration
├── .gitignore                   # Git ignore rules (protects secrets)
└── README.md                    # This file
```

### Module Responsibilities

| File | Purpose |
|------|---------|
| `app.py` | Streamlit UI, workflow orchestration, API calls |
| `templates.py` | All four feedback template structures, system prompts, and prompt builders |
| `parser.py` | Parses uploaded files, extracts student names and submissions |
| `doc_generator.py` | Creates professional Word documents with python-docx |

---

## Configuration

### Anthropic API Key

The app needs an Anthropic API key to generate feedback. Three ways to provide it:

1. **Sidebar input** — Enter it manually each session
2. **Secrets file** — Create `.streamlit/secrets.toml` with `ANTHROPIC_API_KEY = "sk-..."`
3. **Streamlit Cloud** — Add it in Settings → Secrets (best for deployment)

### Theming

Edit `.streamlit/config.toml` to customize the color scheme:

```toml
[theme]
primaryColor = "#c06030"        # Accent color (buttons, links)
backgroundColor = "#faf9f7"     # Page background
secondaryBackgroundColor = "#f0ece6"  # Sidebar/card background
textColor = "#2c2c2c"           # Main text color
font = "serif"                  # Font family
```

---

## Customization

### Adding New Templates

To add a new assignment type, add an entry to `TEMPLATES` in `templates.py`:

```python
"new_type": {
    "label": "New Assignment Type",
    "icon": "🆕",
    "description": "Description of what this template covers...",
    "has_part_a": True,  # or False
    "part_a_label": "Individual Feedback",
    "part_b_label": "Collective Synthesis",
    "format_help": "Instructions for file formatting...",
    "system_prompt": "You are an expert in...",
    "build_part_a": lambda name, text, ctx: f"...",
    "build_part_b": lambda summaries, ctx: f"...",
}
```

The app will automatically pick up the new template — no changes to `app.py` needed.

### Changing the AI Model

In `app.py`, find the `call_anthropic` function and change the model parameter:

```python
model="claude-sonnet-4-20250514",  # Change to any supported model
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No student delimiters found" | Check that each submission starts with `Student: [Name]` on its own line |
| "Authentication Error" | Verify your API key is correct and has available credits |
| "Rate Limit" | Wait 60 seconds and retry. Consider processing fewer students at once |
| `.docx` upload not parsing | Ensure the file isn't password-protected. Try saving as `.txt` instead |
| Blank feedback generated | Add Assignment Context (the rubric/prompt) for better results |

---

## API Cost Estimate

Each student's individual feedback uses ~1 API call. The collective synthesis uses 1 additional call.

| Class Size | Estimated Calls | Approx. Cost (Sonnet) |
|-----------|:---------------:|:--------------------:|
| 15 students | 16 | ~$0.25 |
| 20 students | 21 | ~$0.35 |
| 30 students | 31 | ~$0.50 |

---

## License

This tool was built for educational use at Indiana University Indianapolis. Please consult with Professor BenMessaoud before redistributing.
