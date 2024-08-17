from selenium import webdriver

from src.scholaro_gpa import ScholaroGPA
from src.wes_igpa import WESiGPA
from excel_reader import read_excel_data

excel_file = 'data/sign_score.xlsx'  # Replace with your Excel file path

try:
    course_data = read_excel_data(excel_file)

    driver = webdriver.Chrome()

    # Create an instance of WESiGPA / ScholaroGPA Scraper
    scraper = WESiGPA(driver)
    # scraper = ScholaroGPA(driver)

    scraper.add_courses_from_data(course_data)

    input("Press Enter to close the browser...")

    driver.quit()

except Exception as e:
    print(f"An error occurred: {e}")