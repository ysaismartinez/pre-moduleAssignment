import unittest
from my_cli_hw.cli import main

class TestMyCliTool(unittest.TestCase):
    def test_main(self):
        # This is a simnple test case that will pass if things run successfully.
        try:
            main()
            self.assertTrue(True)  # If main() runs without error, the test passes.
            print("I passed the test because I run successfully")
        except Exception as e:
            self.fail("Command raised {e} unexpectedly") #This is an exception if things go south. 

if __name__ == "__main__":
    unittest.main()
