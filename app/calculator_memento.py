class CalculatorMemento:
    def __init__(self, state):
        self.state = state

class Caretaker:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save(self, state):
        self.undo_stack.append(CalculatorMemento(state.copy()))
        self.redo_stack.clear()

    def undo(self, current_state):
        if not self.undo_stack:
            print("Nothing to undo.")
            return current_state
        memento = self.undo_stack.pop()
        self.redo_stack.append(CalculatorMemento(current_state.copy()))
        return memento.state

    def redo(self, current_state):
        if not self.redo_stack:
            print("Nothing to redo.")
            return current_state
        memento = self.redo_stack.pop()
        self.undo_stack.append(CalculatorMemento(current_state.copy()))
        return memento.state
