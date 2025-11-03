import copy


class CalculatorMemento:
    """Stores a snapshot of the calculator state (such as history)."""
    def __init__(self, state=None):
        self.state = copy.deepcopy(state)


class Caretaker:
    """Manages undo and redo operations using mementos."""
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save(self, state):
        """Save a new state to the undo stack and clear redo history."""
        self.undo_stack.append(CalculatorMemento(state))
        self.redo_stack.clear()

    def undo(self, current_state=None):
        """Undo the last operation. Accepts optional current_state for tests."""
        if len(self.undo_stack) > 1:
            self.redo_stack.append(CalculatorMemento(current_state or self.undo_stack[-1].state))
            self.undo_stack.pop()
            return copy.deepcopy(self.undo_stack[-1].state)
        return None

    def redo(self, current_state=None):
        """Redo a previously undone operation. Accepts optional current_state for tests."""
        if self.redo_stack:
            memento = self.redo_stack.pop()
            self.undo_stack.append(CalculatorMemento(current_state or memento.state))
            return copy.deepcopy(memento.state)
        return None
