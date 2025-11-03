from app.calculator import Calculator


def main():
    calc = Calculator()
    commands = {
        "help": calc.help,
        "clear": calc.clear_history,
        "undo": calc.undo,
        "redo": calc.redo,
        "history": calc.show_history,
        "exit": exit,
    }

    while True:
        cmd = input("Enter command (help to list): ").strip().lower()
        if cmd in commands:
            commands[cmd]()
        elif cmd in ["add", "subtract", "multiply", "divide", "power", "root", "modulus"]:
            calc.perform_operation(cmd)
        else:
            print("Unknown command. Type 'help' for options.")


if __name__ == "__main__":
    main()
