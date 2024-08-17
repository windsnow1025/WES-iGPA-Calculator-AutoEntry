from selenium.webdriver.remote.webdriver import WebDriver

from src.scraper import Scraper


class WESiGPA(Scraper):
    def __init__(self, driver: WebDriver):
        self.base_url = "https://applications.wes.org/igpa-calculator/igpa.asp"
        super().__init__(driver, self.base_url)

        # Define XPaths for the elements
        self.add_course_button_path = "//input[@value='Add Course']"
        self.title_input_path = lambda index: f"//input[@id='title{index}']"
        self.credit_input_path = lambda index: f"//input[@id='credit{index}']"
        self.grade_input_path = lambda index: f"//input[@id='grade{index}']"

    def add_course(self, index: int, title: str, credit: str, grade: str):
        """
        Adds a course to the WES iGPA Calculator.
        :param index: The index of the course (1-based).
        :param title: The course title.
        :param credit: The course credit.
        :param grade: The course grade.
        """
        # Fill in the course title
        title_input = self._wait_find(self.title_input_path(index))
        title_input.clear()
        title_input.send_keys(title)

        # Fill in the course credit
        credit_input = self._wait_find(self.credit_input_path(index))
        credit_input.clear()
        credit_input.send_keys(credit)

        # Fill in the course grade
        grade_input = self._wait_find(self.grade_input_path(index))
        grade_input.clear()
        grade_input.send_keys(grade)

        # Click the "Add Course" button
        self._wait_find(self.add_course_button_path).click()

    def add_courses_from_data(self, data: list[dict]):
        """
        Adds multiple courses to the WES iGPA Calculator.
        :param data: A list of dictionaries containing course data.
        """

        print("Waiting for up to 2 minutes to allow manual setup...")
        self._wait_find(self.add_course_button_path, timeout=120)

        for index, course in enumerate(data, start=1):
            self.add_course(index, course['title'], course['credit'], course['grade'])
