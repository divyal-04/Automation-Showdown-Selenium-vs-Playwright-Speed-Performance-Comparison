# 🔧 Automation Showdown: Selenium vs Playwright – Speed & Performance Comparison

🚀 Curious which web automation tool is faster? In this project, we pit **Selenium** against **Playwright** in a head-to-head speed test to find out which automation tool performs better for real-world tasks.

---

## 📌 What’s Inside

| Feature                        | Selenium                    | Playwright                  |
|-------------------------------|-----------------------------|-----------------------------|
| Language Support              | Python, Java, C#, JS        | Python, JS, TS, C#          |
| Speed                         | Slower                      | ⚡ Blazing Fast              |
| Browser Support               | Chrome, Firefox, Edge, etc. | Chromium, Firefox, WebKit   |
| Auto-waiting Mechanism        | Manual waits needed         | Built-in auto-waiting       |
| Installation Complexity       | Simple                      | Simple                      |

---

## 🧪 Test Cases

We ran both tools to automate the same task on **[Books to Scrape](http://books.toscrape.com/)**:

- Open the homepage of the site
- Scrape the **first book's information**
- Run the script in **headless=False** mode
- Measure the time taken for the automation

📂 Files:

- `selenium_test.py`: Selenium-based automation
- `playwright_test.py`: Playwright-based automation

---

## 📊 Benchmark Results

- **Selenium**: ~7.13 seconds  
- **Playwright**: ~3.47 seconds  

➡️ *Playwright clearly wins in terms of speed and performance for this task!*

---

## ⚙️ Requirements

```bash
pip install -r requirements.txt
