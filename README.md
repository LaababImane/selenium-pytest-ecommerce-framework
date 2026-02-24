# Demoblaze E-Commerce Test Automation Framework

A professional Selenium-based test automation framework built with Python, following the Page Object Model (POM) design pattern, with CI/CD integration via GitHub Actions.

## 🛠️ Tech Stack

- **Python 3.11**
- **Selenium 4** — browser automation
- **Pytest** — test framework
- **Allure Report** — test reporting
- **GitHub Actions** — CI/CD pipeline
- **Page Object Model** — design pattern

## 📁 Project Structure
```
├── .github/
│   └── workflows/
│       └── selenium-tests.yml   # CI/CD pipeline
├── config/
│   └── config.json              # local credentials (gitignored)
├── pages/
│   ├── base_page.py             # shared methods for all pages
│   ├── home_page.py             # home page interactions
│   ├── login_page.py            # login modal interactions
│   ├── product_page.py          # product page interactions
│   └── cart_page.py             # cart page interactions
├── tests/
│   ├── conftest.py              # driver setup and hooks
│   ├── test_login.py            # login test cases
│   ├── test_navigation.py       # navigation test cases
│   └── test_cart.py             # cart and checkout test cases
├── utils/
│   └── config_reader.py         # reads config from file or env vars
├── reports/                     # generated test reports
├── conftest.py                  # root conftest for import resolution
├── pytest.ini                   # pytest configuration
├── .gitignore
└── requirements.txt
```

## ✅ Test Coverage

| Module | Test Cases |
|--------|-----------|
| Login | Valid login, invalid credentials, empty fields |
| Navigation | Home page loads, category filtering, cart navigation |
| Cart | Add product, verify total, delete item, full checkout |

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Google Chrome or Brave Browser
- Java JDK (required for Allure reporting)

### Installation

1. Clone the repository
```bash
git clone https://github.com/LaababImane/selenium-pytest-ecommerce-framework.git
cd selenium-pytest-ecommerce-framework
```

2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create your config file
```bash
mkdir config
```

Create `config/config.json` with your Demoblaze credentials:
```json
{
    "base_url": "https://www.demoblaze.com",
    "valid_user": {
        "username": "your_username",
        "password": "your_password"
    },
    "invalid_user": {
        "username": "wrong_user",
        "password": "wrong_pass"
    }
}
```

> Register a free account at [demoblaze.com](https://www.demoblaze.com) to get your credentials.

### Running Tests

Run all tests:
```bash
pytest tests/ -v
```

Run a specific test file:
```bash
pytest tests/test_login.py -v
pytest tests/test_cart.py -v
```

Run a specific test:
```bash
pytest tests/test_login.py::test_login_valid -v
```

### Generating Reports
```bash
# Run tests and generate Allure results
pytest tests/ -v

# Open Allure report in browser
allure serve reports/allure-results
```

## ⚙️ CI/CD Pipeline

The project uses GitHub Actions to automatically run all tests on every push to the `main` branch. Test results are uploaded as artifacts and can be downloaded from the Actions tab.

Required GitHub Secrets:
- `VALID_USERNAME` — your Demoblaze username
- `VALID_PASSWORD` — your Demoblaze password

## 🎯 Design Patterns

- **Page Object Model (POM)** — each page has its own class containing locators and interactions, keeping tests clean and maintainable
- **Fixtures** — shared browser setup and teardown via pytest fixtures
- **External config** — credentials and URLs stored outside test code, supporting both local and CI environments