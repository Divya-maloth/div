# test_case.py
class TestCase:
    def __init__(self, test_id, name, command, expected):
        self.test_id = test_id
        self.name = name
        self.command = command
        self.expected = expected
        self.status = None
        self.output = None
