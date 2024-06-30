from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Load sample dataset
sample_data = pd.read_csv('Sample Dataset.csv')

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the website
driver.get("https://staging-scweb.arcapps.org/")

# Function to log in
def login():
    driver.find_element(By.ID, "username").send_keys("tester")
    driver.find_element(By.ID, "password").send_keys("tester2023!")
    driver.find_element(By.ID, "province").send_keys("Lusaka")
    driver.find_element(By.ID, "district").send_keys("Lusaka")
    driver.find_element(By.ID, "facility").send_keys("Dr Watson Dental Clinic")
    driver.find_element(By.ID, "loginButton").click()

# Function to navigate to the patient's vitals section
def navigate_to_vitals():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "NRC")))
    driver.find_element(By.ID, "NRC").send_keys("111111111")
    driver.find_element(By.ID, "attendButton").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "addVitalButton")))
    driver.find_element(By.ID, "addVitalButton").click()

# Function to upload dataset and populate form fields
def upload_data():
    for index, row in sample_data.iterrows():
        driver.find_element(By.ID, "vitalField1").send_keys(row['Field1'])
        driver.find_element(By.ID, "vitalField2").send_keys(row['Field2'])
        # Continue for other fields as necessary
        driver.find_element(By.ID, "saveButton").click()
        time.sleep(1)  # Adjust sleep time as necessary
        driver.find_element(By.ID, "addVitalButton").click()

# Function to log out
def logout():
    driver.find_element(By.ID, "logoutButton").click()

# Main function to run all tasks
def main():
    try:
        login()
        navigate_to_vitals()
        upload_data()
    finally:
        time.sleep(5)  # Allow time to observe the final state
        driver.quit()

if __name__ == "__main__":
    main()
