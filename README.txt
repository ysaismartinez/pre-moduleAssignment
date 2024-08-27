This is the READ ME file

Requirements:

This script runs from the command line and it reads a CSV file.
There is also a unit test that lets you know that the test ran successfully. The unit test is as simple as simple can be. It was just added to the script to satisfy the assignment's rubric. 

Please check out the repositoty running tnis command: git clone https://github.com/ysaismartinez/pre-moduleAssignment.git 

Then browse to the folder my_cli_hw
And from terminal run: my_cli_hw 
When you try to run that command (my_cli_hw) you will get a "command not found" error message. This is because we have to complete some steps. 

From terminal run the following commands in order:
1. python3 -m venv myenv
2. source myenv/bin/activate (On a Windows system run this instead: myenv\Scripts\activate)
3. pip install .

Then you should see an output like this (lines 21-38 of this README file):

(myenv) ysais.a.martinez@AMAQ91CJPGXMM my_cli_hw % pip install .
Processing /Users/ysais.a.martinez/Documents/my_cli_hw
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: pandas in ./my_cli_hw/myenv/lib/python3.12/site-packages (from my_cli_hw==0.1) (2.2.2)
Requirement already satisfied: numpy in ./my_cli_hw/myenv/lib/python3.12/site-packages (from my_cli_hw==0.1) (2.1.0)
Requirement already satisfied: python-dateutil>=2.8.2 in ./my_cli_hw/myenv/lib/python3.12/site-packages (from pandas->my_cli_hw==0.1) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in ./my_cli_hw/myenv/lib/python3.12/site-packages (from pandas->my_cli_hw==0.1) (2024.1)
Requirement already satisfied: tzdata>=2022.7 in ./my_cli_hw/myenv/lib/python3.12/site-packages (from pandas->my_cli_hw==0.1) (2024.1)
Requirement already satisfied: six>=1.5 in ./my_cli_hw/myenv/lib/python3.12/site-packages (from python-dateutil>=2.8.2->pandas->my_cli_hw==0.1) (1.16.0)
Building wheels for collected packages: my_cli_hw
  Building wheel for my_cli_hw (pyproject.toml) ... done
  Created wheel for my_cli_hw: filename=my_cli_hw-0.1-py3-none-any.whl size=1701 sha256=c44f075fe1f25a57ec320cecabf95ca3289bb0aec78f90cef743b5ce8f6252a6
  Stored in directory: /private/var/folders/mn/cprx3km57zd71wfpwv5y93340000gn/T/pip-ephem-wheel-cache-it4ycy_u/wheels/b5/4d/df/26c33ccbb4fe7d856d950809e0bf16b01d34211353267a1fec
Successfully built my_cli_hw
Installing collected packages: my_cli_hw
Successfully installed my_cli_hw-0.1

4. Run my_cli_hw 

And the command should run and output the CSV file contents and the output of the method describe()

If you want to run a unittest from terminal run this:
python -m unittest discover tests 

I added a sceenshot of the output (ScreenshotOfSuccessfulRun.docx). My unit test is simple. 

