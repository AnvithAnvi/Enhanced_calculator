# 🧮 Enhanced Calculator – Command-Line Application

![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)

## 📖 Overview
The **Enhanced Calculator** is a command-line application built using **Python** that performs arithmetic operations, maintains calculation history, supports **undo/redo**, and implements software engineering design patterns such as:

- **Factory Pattern** – for operation creation  
- **Memento Pattern** – for undo/redo functionality  
- **Observer Pattern** – for logging and autosaving  

This project emphasizes **clean code architecture, modularity, testing, and CI/CD** integration through GitHub Actions.

---

## 🧩 Features

| Feature | Description |
|----------|-------------|
| 🧠 **Arithmetic Operations** | Add, Subtract, Multiply, Divide, Power, Root, Modulus |
| 🧾 **History Management** | Saves all calculations and can be exported to CSV |
| 🔁 **Undo/Redo (Memento Pattern)** | Revert or restore calculator state |
| 🪵 **Logging System** | Logs all user operations with timestamps |
| 💾 **Auto-Save Observer** | Automatically stores calculation history to CSV |
| 🧰 **Factory Pattern** | Dynamically selects operation logic |
| ✅ **Testing and CI/CD** | 26 unit tests passing via pytest & GitHub Actions |
| 🧱 **Environment Variables** | Uses `.env` for configurable paths and log settings |

---

## 🏗️ Project Structure

```
enhanced_calculator/
│
├── app/
│   ├── __init__.py
│   ├── calculation.py
│   ├── calculator.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── decorators.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── logger.py
│   ├── operations.py
│   └── repl.py
│
├── tests/
│   ├── test_calculator_basic.py
│   ├── test_calculator_memento.py
│   ├── test_edge_cases.py
│   ├── test_history.py
│   ├── test_logger.py
│   ├── test_main_entrypoint.py
│   ├── test_operations.py
│   └── test_repl_and_calculator_extra.py
│
├── .github/workflows/python-app.yml
├── .env
├── requirements.txt
├── README.md
└── pytest.ini
```

---

## ⚙️ Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/enhanced_calculator.git
   cd enhanced_calculator
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # (Mac/Linux)
   venv\Scripts\activate      # (Windows)
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**
   ```bash
   LOG_DIR=logs
   HISTORY_DIR=history
   LOG_FILE=calculator.log
   ```

---

## 💻 Usage

Run the calculator interactively:
```bash
python -m app.repl
```

Available commands:
```
add, subtract, multiply, divide, power, root, modulus
undo, redo, history, clear, help, exit
```

Example:
```
Enter first number: 5
Enter operation: add
Enter second number: 3
Result: 8.0
```

---

## 🧪 Testing Instructions

Run all unit tests:
```bash
pytest --disable-warnings -q
```

Run with coverage:
```bash
pytest --cov=app --cov-report=term-missing
```

✅ **All 26 tests passed successfully (90% coverage).**

---

## 🤖 CI/CD Integration (GitHub Actions)

A CI workflow (`.github/workflows/python-app.yml`) automatically:
1. Installs dependencies
2. Runs pytest with coverage
3. Ensures all tests pass before merging or deployment

View workflow status under the **Actions** tab on your GitHub repo.

---

## 🧱 Design Patterns Used

- **Factory Pattern:** Used in `operations.py` to dynamically instantiate the correct operation function.
- **Memento Pattern:** Implemented in `calculator_memento.py` to handle undo/redo.
- **Observer Pattern:** Implemented in `logger.py` via `LoggingObserver` and `AutoSaveObserver`.

---

## 🧩 Best Practices Implemented

- **DRY (Don't Repeat Yourself)** – Code reuse through modular components  
- **SOLID Principles** – Clear class responsibilities  
- **Comprehensive Logging** – Every operation is tracked  
- **Test-Driven Development (TDD)** – Full coverage with pytest  

---

## 📊 Example Output

```
Welcome to the Enhanced Calculator!
> add
Enter first number: 10
Enter second number: 5
Result: 15
> undo
Undo successful
> redo
Redo successful
> exit
Goodbye!
```

---
