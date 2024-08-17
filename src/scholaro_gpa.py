from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from src.scraper import Scraper

class ScholaroGPA(Scraper):
    def __init__(self, driver: WebDriver):
        self.base_url = "https://www.scholaro.com/gpa-calculator/"
        super().__init__(driver, self.base_url)

        # Define XPaths for the elements
        self.table_xpath = "//table[@class='FrontPage pastetable']"
        self.row_xpath = lambda index: f"//table[@class='FrontPage pastetable']//tbody/tr[{index}]"
        self.course_input_xpath = lambda index: f"//table[@class='FrontPage pastetable']//tbody/tr[{index}]/td[2]//input"
        self.credit_input_xpath = lambda index: f"//table[@class='FrontPage pastetable']//tbody/tr[{index}]/td[3]//input"
        self.grade_input_xpath = lambda index: f"//table[@class='FrontPage pastetable']//tbody/tr[{index}]/td[4]//input"

    def add_course(self, index: int, title: str, credit: str, grade: str):
        """
        Adds a course to the Scholaro GPA Calculator.
        :param index: The index of the course (1-based).
        :param title: The course title.
        :param credit: The course credit.
        :param grade: The course grade.
        """
        # Fill in the course title
        course_input = self._wait_find(self.course_input_xpath(index))
        course_input.clear()
        course_input.send_keys(title)

        # Fill in the course credit
        credit_input = self._wait_find(self.credit_input_xpath(index))
        credit_input.clear()
        credit_input.send_keys(credit)

        # Fill in the course grade
        grade_input = self._wait_find(self.grade_input_xpath(index))
        grade_input.clear()
        grade_input.send_keys(grade)

    def add_courses_from_data(self, data: list[dict]):
        """
        Adds multiple courses to the Scholaro GPA Calculator.
        :param data: A list of dictionaries containing course data.
        """

        print("Waiting for up to 2 minutes to allow manual setup...")
        self._wait_for_condition(
            lambda driver: len(driver.find_elements(By.XPATH, f"{self.table_xpath}//tbody/tr")) > len(data) + 1,
            timeout=120
        )

        for index, course in enumerate(data, start=2):  # Start from the second row
            self.add_course(index, course['title'], course['credit'], course['grade'])