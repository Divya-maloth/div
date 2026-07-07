# main.py
from test_case import TestCase
from executer import run_command
from logger import setup_logger

logger = setup_logger()

# Define one test case
test = TestCase("TC001", "Hello World", "python -c \"print('Hello World')\"", "Hello World")

# Run the command
out, err, code = run_command(test.command)
test.output = out if out else err

# Check result
if test.expected in test.output and code == 0:
    test.status = "PASS"
else:
    test.status = "FAIL"

# Log result
logger.info(f"Test {test.test_id} - {test.name} | Status: {test.status} | Output: {test.output}")

# Print mini report
print("====================================")
print("Mini Report")
print("====================================")
print(f"Test ID   : {test.test_id}")
print(f"Test Name : {test.name}")
print(f"Command   : {test.command}")
print(f"Status    : {test.status}")
print(f"Output    : {test.output}")
print("====================================")
