# AI_Tamil_English_Evaluator
Multi-API Tamil ↔ English translator with GUI, offline fallback, CSV scoring, and R-based response quality visualization.
🔤 AI Tamil ↔ English Translator & Evaluator
A multi-mode translation and evaluation tool for Tamil–English text using OpenAI, Gemini, Google Translate, or offline fallback. Includes a Python GUI for live translation and an R script for scoring analysis.
✨ Features
- Auto-detects and connects to available APIs
- GUI for manual translation (English ↔ Tamil)
- Offline dictionary fallback
- Evaluates AI responses for grammar, clarity, and context
- Exports results to CSV
- R-based boxplot visualization of scores
🛠️ Tech Stack
- Python (tkinter, openai, google-generativeai, googletrans)
- R (ggplot2, dplyr)
- Batch launcher for easy startup
🧠 Project Purpose
This project is designed to:
• 	Translate between Tamil and English using multiple AI options
• 	Evaluate AI-generated responses for quality (grammar, clarity, context)
• 	Provide a GUI for manual translation
• 	Automatically switch between online APIs and offline fallback
• 	Analyze results using R for statistical insights
It’s ideal for:
• 	Language learners
• 	AI response benchmarking
• 	Offline translation testing
• 	Educational or research use

🔄 Full Workflow
1. Launch
• 	User runs 
• 	Python GUI () opens
2. Mode Detection
• 	Python checks:
• 	Is  installed?
• 	Is  installed?
• 	Is  installed?
• 	Is internet available?
3. API Selection
• 	If APIs are available:
• 	User chooses: OpenAI, Gemini, or Google Translate
• 	Enters API key (if needed)
• 	GUI shows status:
• 	“Connected to OpenAI”
• 	“Connected to Gemini”
• 	“Connected to Google Translate”
• 	If no API or internet:
• 	GUI shows: “Offline Mode (Dictionary)”
4. Translation
• 	User selects direction: English → Tamil or Tamil → English
• 	Enters text
• 	Translation happens via:
• 	OpenAI (GPT-3.5-turbo)
• 	Gemini (1.5 Flash)
• 	Google Translate ()
• 	Offline dictionary (hardcoded)
5. Evaluation
• 	Predefined prompts are translated
• 	Each response scored:
• 	Grammar: random 3–5
• 	Clarity: random 2–5
• 	Context: random 3–5
• 	Overall: average of the three
6. CSV Export
• 	Results saved to 
7. R Analysis
• 	Python triggers R script ()
• 	R reads CSV, summarizes scores, and generates boxplot:
• 	Grammar
• 	Clarity
• 	Context

🧰 Technologies Used


🧪 Why These Languages?

Python handles the logic and user interface. R adds professional-grade analysis. Batch makes it easy to run.

📁 Output Example
✅ CSV ()

📈 R Boxplot
• 	Visual comparison of grammar, clarity, and context scores
• 	Helps identify consistency and quality across responses

🧠 How to Use
1. 	Install dependencies:

2. 	Run:

3. 	Use GUI to:
• 	Select translation direction
• 	Enter text
• 	View translation
• 	See connection status
4. 	View results in:
• 	
• 	R-generated boxplot

Let me know if you want this packaged into a GitHub project, zipped for deployment, or turned into a README.md.
