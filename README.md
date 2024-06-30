# Hospital-Management-Web-App-Testing
This project automates the testing of a Hospital Management Web App. The scripts are written in Python using Selenium.

## Prerequisites
Python 3.x
Selenium
Chrome WebDriver
Sample Dataset (Sample Dataset.csv)

## Setup Instructions
Clone the repository.
Install the required Python packages:

-pip install selenium
-pip install pytest
-pip install pandas

Place the Sample Dataset.csv file in the project directory.

## Running the Tests
Ensure the Chrome WebDriver is in your PATH or in the project directory.
Run the automated test script:

-python automated_test.py

## Automated Test Script Breakdown
Login Function: Automates the login process using provided credentials.
Navigate to Vitals Function: Navigates to the patient's vitals section.
Upload Data Function: Reads the sample dataset and populates the form fields with the data.
Logout Function: Logs out of the application.

## Notes
Adjust the time.sleep() duration as necessary based on your system's performance.
Ensure the IDs used in the script match those in the actual web application.

