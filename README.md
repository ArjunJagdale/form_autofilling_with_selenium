# 📝 Google Form Auto-Filler using Selenium

This Python script uses **Selenium** to automatically fill out and submit a **Google Form**. It's useful for automating repetitive form submissions for testing or demo purposes.

---

## 📌 Features

- Auto-fills multiple fields in a Google Form
- Clicks the submit button automatically
- Clean and modular Python code
- Uses Selenium with Microsoft Edge WebDriver
- Easily adaptable for different forms

---

## 🚀 Getting Started

### ✅ Prerequisites

- **Python 3.8+** installed
- **Selenium** installed  

pip install selenium

* **Microsoft Edge installed**
* **Matching Edge WebDriver** downloaded from:
  [Edge WebDriver Downloads](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

> Make sure the WebDriver version matches your Microsoft Edge browser version (check `Settings > About Edge`).

---

### 📁 Project Structure

```
form_filler.py
README.md
```

---

### 🛠 Setup

#### 1. Install Selenium

```bash
pip install selenium
```

#### 2. Download Edge WebDriver

* Visit: [Edge WebDriver Downloads](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
* Download the version that matches your browser
* Extract the `msedgedriver.exe` file

#### 3. Add WebDriver to System PATH (Optional but Recommended)

* Place `msedgedriver.exe` in `C:\WebDriver\`
* Add that folder to your Environment Variables → `Path`

---

## 🧪 How to Run

1. Save the script as `form_filler.py`
2. Open a terminal in that directory
3. Run the script:

```bash
python form_filler.py
```

---

## 🖥 Example Google Form Used

📎 [Sample Google Form](https://docs.google.com/forms/d/e/1FAIpQLSezs9vfDnGxHrXsF52bxKXdrmlQHbHI0HsxrO6A9PGbC3K0Xw/viewform?usp=sf_link)

---

## ⚙️ Customization

To modify for another form:

* Update the `form_url` variable in the script
* Adjust the number of `answers`
* If needed, inspect the form fields and update XPath selectors

---

## 📷 Screenshots (Optional)

*Add screenshots or screen recordings of the script in action here.*

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

Feel free to reach out for questions, collaboration, or issues:

* GitHub: [YourUsername](https://github.com/ArjunJagdale)
