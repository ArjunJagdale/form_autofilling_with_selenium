from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === Configuration ===
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSezs9vfDnGxHrXsF52bxKXdrmlQHbHI0HsxrO6A9PGbC3K0Xw/viewform?usp=sf_link"
answers = [
    "Arjun Jagdale",              # Name
    "20",                       # Age
    "arjunxyz@gmail.com",   # Email
    "India",                    # Country
    "Pune",                  # City
    "Swargate"                 # Area
]

# === Setup Edge WebDriver ===
# If you added msedgedriver to PATH, you can just use webdriver.Edge() without the Service object.
driver = webdriver.Edge()
driver.implicitly_wait(10)  # Waits for elements to appear (more reliable than time.sleep)

def fill_form(driver, url, answers):
    try:
        driver.get(url)

        # Shorter, more reliable XPath: selects first 6 visible text inputs
        input_xpath = '(//input[@type="text"])[{index}]'

        for i, answer in enumerate(answers, start=1):
            try:
                input_box = driver.find_element(By.XPATH, input_xpath.format(index=i))
                input_box.send_keys(answer)
                time.sleep(0.5)  # Optional pause for visibility
            except Exception as e:
                print(f"⚠️ Couldn't fill field {i}: {e}")

        # Click the submit button
        submit_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Submit"]/ancestor::div[@role="button"]'))
        )
        submit_btn.click()
        print("✅ Form submitted successfully.")

    except Exception as e:
        print("❌ Error during form submission:", e)
    finally:
        time.sleep(2)  # Optional delay before closing
        driver.quit()

# === Run the form filler ===
fill_form(driver, form_url, answers)
