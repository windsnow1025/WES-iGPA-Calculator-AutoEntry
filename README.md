# WES iGPA Calculator Automation

This project automates the process of entering course data into the GPA Calculator using Selenium. It reads course information from an Excel file and populates the calculator fields, saving you time and effort.

## Features

- **Automated Data Entry:** Reads course data (title, credit, grade) from an Excel file.
- **Selenium Integration:** Uses Selenium to interact with the WES iGPA Calculator website and Scholaro GPA Calculator.
- **Error Handling:** Includes basic error handling for file reading and data validation.

## Development

### Python uv

1. Install uv: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Install Python in uv: `uv python install 3.12`; upgrade Python in uv: `uv python upgrade 3.12`
3. Configure requirements:
  ```bash
  uv sync --refresh
  ```

### Pycharm

1. Add New Interpreter >> Add Local Interpreter
  - Environment: Select existing
  - Type: uv
2. Add New Configuration >> uv run >> Script: `main.py`

## Usage

1. **Prepare your data:**
   * Create an Excel file (e.g., `sign_score.xlsx`) with the following columns:
     * `title`: Course title
     * `credit`: Course credits
     * `grade`: Course grade (using the WES iGPA grading scale)
2. **Update the file path:**
   * In `main.py`, modify the `excel_file` variable to point to your Excel file:
     ```python
     excel_file = 'data/sign_score.xlsx'  # Replace with your Excel file path
     ```
3. **Run the script:**
   ```bash
   python main.py
   ```

## Example Data (sign_score.xlsx)

| title         | credit | grade |
|---------------|--------|-------|
| Math 101      | 3      | 88    |
| Physics 101   | 4      | 92    |
| Chemistry 101 | 3      | 95    |
| ...           | ...    | ...   |

## Note

* The script waits for up to 2 minutes to allow you to manually enter information on the webpage. You can adjust this timeout if needed.
