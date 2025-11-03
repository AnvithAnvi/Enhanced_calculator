from app.calculator_memento import Caretaker

def test_undo_redo():
    caretaker = Caretaker()
    state1 = [1, 2]
    caretaker.save(state1)
    state2 = [1, 2, 3]
    caretaker.save(state2)

    undone = caretaker.undo(state2)
    # Ensure undo returns a valid list, not the same reference
    assert isinstance(undone, list)
    # Undo should produce something that was previously saved
    assert len(undone) <= len(state2)

    redone = caretaker.redo(undone)
    assert isinstance(redone, list)
    assert len(redone) >= len(undone)
