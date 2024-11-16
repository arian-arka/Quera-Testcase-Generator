# A test case generator for quera

    This program uses zip and unzip command, u need to have them installed on your linux or wsl

**Introduction**

You can use it to generate testcases for students 


## How it works
First you need to develop your code 
Then every program has its own inputs and prints (inputs-stdin-... and prints-stdout-... are abstracts, it can be any executable file or interpreter programming language)
This program creates 2 temp file for each test case. one for input and one for out put and runs your executable with the command written below
for example for a python program
````bash
python3 main.py < tempIn.txt > tempOut.txt
````
after that all testcases are generated, all temp files are removed and test cases will be zipped to a file

## Config file
confs.json
````json
{
  "execute": "python3",
  "executable_file": "path-to-your-executable/main.py",
  "destination": "path-to-generate-test-cases",
  "zip_name": "name-of-the-zip-file",
  "test_cases": [
    "testcase1-input1\ntestcase1-input2",
    "testcase2-input1\ntestcase2-input2",
    "testcase3-input1\ntestcase3-input2",
    "testcase4-input1\ntestcase4-input2"
  ],
  "extract": 1
}
````
- for example if you are using gcc, you can set the execute attribute to
  - ````bash
    gcc main.c -o executable
    ````
  - and the executable_file to 
    - ````bash
      ./main
      ````
- test_cases
  - each line represent a test case
  - for example consider the following python code
    - ````python
      inp1 = input('input1 : ')
      inp2 = input('input2 : ')
      print('input1 is',inp1)
      print('input2 is',inp2)
      ````
    - in the above confs.json file,the first value of test_cases array is
      - "testcase1-input1\ntestcase1-input2",
      - which you can see inputs are seperated with \n, which is newline