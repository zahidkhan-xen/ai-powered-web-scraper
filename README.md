# Python AI Web Scraper

A simple web scraper that uses AI to extract information from any website. You just tell it what you want in plain English — no need to write complex scraping rules.

## What It Does

Give it a URL and a question like _"What is the purpose of this website?"_ and it returns the answer. It uses an AI model (Llama 3.1 via Groq) to read the page and extract exactly what you ask for.

## Quick Setup

### Step 1 — Clone and enter the project

```bash
git clone <repo-url>
cd python-scrapper
```

### Step 2 — Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

> On Windows use: `venv\Scripts\activate`

### Step 3 — Install dependencies

```bash
pip install scrapegraphai
playwright install
```

### Step 4 — Add your API key

Get a free API key from [console.groq.com](https://console.groq.com), then open [main.py](main.py) and replace the `api_key` value:

```python
"api_key": "paste-your-key-here",
```

### Step 5 — Run it

```bash
python main.py
```

You should see the scraper fetch the page and print the result.

## Changing the Target

Open [main.py](main.py) and edit these two lines:

```python
prompt="What do you want to extract?",
source="https://the-website-you-want-to-scrape.com/",
```

That's it. The AI handles the rest.
