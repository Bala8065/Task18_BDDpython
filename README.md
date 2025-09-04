# Zenclass Behave + Allure Automation (Task-18)

## Overview
This project uses **Behave (BDD)** + **Selenium** with **Page Object Model (POM)** and generates **Allure** reports (JSON & HTML) for the Zen portal login/logout flows.

**Portal:** https://v2.zenclass.in/login
**Test user provided in task:** bala8065@gmail.com / Bala@8065

## Project Structure
```
zen_behave_allure/
├── features/
│   ├── login.feature
│   ├── environment.py
│   └── steps/
│       └── steps_login.py
├── pages/
│   └── login_page.py
├── requirements.txt
└── README.md
```

## Setup
1. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # mac/linux
   .venv\Scripts\activate     # windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure Chrome and matching chromedriver are installed and chromedriver is on PATH.

## Run tests and generate Allure results
1. Run behave with Allure formatter to generate results (JSON compatible):
   ```bash
   behave -f allure_behave.formatter:AllureFormatter -o ./allure-results features
   ```
2. Generate report HTML from results (requires Allure CLI installed):
   ```bash
   allure generate ./allure-results -o ./allure-report --clean
   allure open ./allure-report
   ```

## Notes
- The `pages/login_page.py` uses explicit waits and handles Selenium exceptions.
- Allure attachments are added for debugging on failures.
- The feature file contains scenarios for successful login, unsuccessful login, validating input fields, submit button, and logout functionality.

## Troubleshooting
- If tests fail due to driver issues, confirm chromedriver version matches Chrome.
- If running in CI, consider enabling headless mode in `features/environment.py` by uncommenting the headless option.
