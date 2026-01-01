import json
from todo import complete_task

def test_complete_task():
    tasks = [{"title": "Task 1", "done": False}, {"title": "Task 2", "done": False}]
    
    # Test that the task is marked as completed when index is valid
    complete_task(1)
    assert tasks[0]["done"] == True
    assert tasks[1]["done"] == False
    
    # Test that the task is not modified if index is invalid
    complete_task(3)
    assert tasks[0]["done"] == True
    assert tasks[1]["done"] == False
    
    # Test that an error is raised if index is out of range
    with pytest.raises(ValueError):
        complete_task(-1)
        complete_task(3)

