import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service = Service("FULL_geckodriver_FILE_ADDRESS_HERE")
# For example C:/PATH/TO/FILE/geckodriver.exe
options = Options()
options.binary_location = r"BROWSER_FILE_ADDRESS_HERE"
# For example C:/PATH/DIR/firefox.exe

driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get("https://www.instagram.com")
    time.sleep(7)
    with open("cookies.pkl", "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.refresh()
except FileNotFoundError:
    print("Cookies file not found. Logging in...", flush=True)

try:
    if driver.current_url == "https://www.instagram.com/accounts/login/":
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        user_name = 'USERNAME_HERE'
        username_input.send_keys(user_name')

        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys('PASSWORD_HERE')
        password_input.send_keys(Keys.ENTER)

        time.sleep(3)
        print("Login successfully...", flush=True)

        time.sleep(7)
        with open("cookies.pkl", "wb") as file:
            pickle.dump(driver.get_cookies(), file)

    print("Go To Profile Page...", flush=True)
    driver.get('https://www.instagram.com/' + user_name)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(@href, '/following/')]")
        )
    )

    print("Clicked on Following...", flush=True)

    following_button = driver.find_element(
        By.XPATH, "//a[contains(@href, '/following/')]"
    )
    following_button.click()

    print("Waiting For 15 sec...", flush=True)

    time.sleep(15)
    print("Clicking...", flush=True)

    while True:
        try:
            following_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[contains(text(), 'Following')]/ancestor::button")
                )
            )

            print("Clicking on the Following button...", flush=True)
            following_button.click()

            try:
                unfollow_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[text()='Unfollow']"))
                )
                print("Clicking on the Unfollow button...", flush=True)
                unfollow_button.click()

            except Exception:
                print(
                    "No confirmation dialog appeared, skipping to next user.",
                    flush=True,
                )

            print("Unfollowed the user successfully!", flush=True)
            time.sleep(10)

        except Exception as e:
            print(f"Error during the unfollowing process: {e}", flush=True)
            time.sleep(5)


except Exception as main_error:
    print(f"An error occurred: {main_error}", flush=True)
