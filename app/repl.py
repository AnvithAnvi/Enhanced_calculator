from app.calculator import Calculator

def main():
    calc = Calculator()
    print("Enhanced Calculator — type 'help' to see commands.")
    while True:
        cmd = input(">>> ").strip().lower()
        if cmd in calc.commands:
            calc.commands[cmd]()
        else:
            print("Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()
