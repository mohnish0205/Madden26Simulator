from madden_26_simulator.main import greet

def test_greet():
    print("Testing greet function...")
    assert greet("Test") == "Hello, Test!"