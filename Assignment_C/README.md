# Assignment C: Python Expressions & Unit Tests &nbsp; (16 Pts)

This assignment demonstrates Python's powerful (*"one-liner"*) expressions.

### Challenges
- [Challenge 1:](#1-challenge-create-new-project) Create New Project
- [Challenge 2:](#2-challenge-run-code) Run Code
- [Challenge 3:](#3-challenge-run-unit-tests) Run Unit Tests
- [Challenge 4:](#4-challenge-write-expressions) Write Expressions
- [Challenge 5:](#5-challenge-final-test) Final Test

Points: [1, 2, 3, 0, 10]


&nbsp;
### 1.) Challenge: Create New Project
Create a Python project, e.g. named `C_expressions`, and
[pull files](https://gitlab.bht-berlin.de/sgraupner/ds_cs4bd_2324/-/tree/main/C_expressions)
from GitLab (above).

Inspect files and figure out their purpose. Write 1-2 sentenses what each file means
and purpose is:

 - [__init __.py](https://gitlab.bht-berlin.de/sgraupner/ds_cs4bd_2324/-/blob/main/C_expressions/__init__.py)
    : `_____________________________________`
 
     - What does the init-file contain?
     - When and how often is this file executed?

 - [expressions.py](https://gitlab.bht-berlin.de/sgraupner/ds_cs4bd_2324/-/blob/main/C_expressions/expressions.py)
    : `__________________________________`

 - [test_expressions.py](https://gitlab.bht-berlin.de/sgraupner/ds_cs4bd_2324/-/blob/main/C_expressions/test_expressions.py)
    : `______________________________`

(1 Pt)


&nbsp;
### 2.) Challenge: Run Code
Run file `expressions.py` in your IDE:
```
numbers: [4, 12, 3, 8, 17, 12, 1, 8, 7]
#
a) number of numbers: 9
b) first three numbers: []
c) last three numbers: []
d) last three numbers reverse: []
e) odd numbers: []
f) number of odd numbers: 0
g) sum of odd numbers: 0
h) duplicate numbers removed: []
i) number of duplicate numbers: 0
j) ascending, de-dup (n^2) numbers: []
k) length: NEITHER

[Done] exited with code=0 in 0.126 seconds
```
(1 Pt)

Run file `expressions.py` in terminal:
```sh
cd <project>                # cd into project directory
pwd                         # print working directory
/c/.../workspaces/ds_cs4bd_2324/C_expressions

python expressions.py       # run program
-->
numbers: [4, 12, 3, 8, 17, 12, 1, 8, 7]
#
a) number of numbers: 9
b) first three numbers: [4, 12, 3]
c) last three numbers: [1, 8, 7]
d) last three numbers reverse: [7, 8, 1]
e) odd numbers: [3, 17, 1, 7]
f) number of odd numbers: 4
g) sum of odd numbers: 28
h) duplicate numbers removed: [1, 3, 4, 7, 8, 12, 17]
i) number of duplicate numbers: 2
j) ascending, de-dup (n^2) numbers: [1, 9, 16, 49, 64, 144, 289]
k) length: ODD_LIST
```
(1 Pt)


&nbsp;
### 3.) Challenge: Run Unit Tests
Unit Tests are used to *"test-a-unit"* of code in isolation. This unit can be
a function, a file, a class, a module.

In contrast to running code regularly, Unit Tests execute under the
supervision of a `test runner` that:

 - looks for (discovers) tested units,

 - executes them with test data, collects test results regardless
    whether a test succeeded or failed and

 - reports test results at the and.

Read *"A Beginner’s Guide to Unit Tests in Python"*,
[link](https://www.dataquest.io/blog/unit-tests-python/),
and answer questions:

 - How are tests discovered? Which feature makes the test runner to collect
    something as a test?

 - What is an
    [assert](https://docs.python.org/3/library/unittest.html#assert-methods)
    statement? What happens when a test (assert) passes and fails?

 - Where is the test runner started in given files?

(1 Pt)

Run tests in a terminal. Currently, only one test runs and passes:
*TestCase_a_number_of_numbers* :
```sh
python test_expressions.py      # run tests directly from file calling the
                                # test runner in __main__
```

Output:

```
test_a_number_of_numbers (C_expressions.test_expressions.TestCase_a_number_of_nu
mbers.test_a_number_of_numbers) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
<unittest.runner.TextTestResult run=1 errors=0 failures=0>
```
Result: 1 test was performed that passed.

Alternatively, run tests with test discovery. Run the unit test module that
starts the test runner, which in turn discovers tests that are then executed:

```sh
python -m unittest              # let test runner discover tests
```
Output is the same as above.

(1 Pt)

Configure your IDE so it runs Unit Tests (you can use other IDE than VS Code
that is used here as example).

VSCode discovers unit tests under the test glass icon (red circled).

The figure shows one unit test that has been discovered passing. Unit tests are
structured as *"TestCase - Classes"*, which are classes that inherit from class:
[unittest.TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase),
in the example indirectly through class `Test_case_a`.

VSCode shows discovered test classes in the left panel and their execution result
with a green check mark when passed or a red cross when failed.

![](../markup/img/C_unit_tests_1.png)

Uncomment tests: *"Test_case_b"* and *"Test_case_c"* in `test_expressions.py`
above and re-run tests.
Both tests should fail because expressions they test have not been implemented:

![](../markup/img/C_unit_tests_2.png)

Re-run unit tests with the two tests failing in the terminal:

```sh
python -m unittest              # let test runner discover tests
```

Output shows one passing and two failed tests:

```
======================================================================
FAIL: test_b_first_three_numbers (test_expressions.TestCase_b_first_three_number
s.test_b_first_three_numbers)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Sven1\svgr\workspaces\ds_cs4bd_2324\C_expressions\test_expressions.py
", line 103, in test_b_first_three_numbers
    self.assertEqual(self.ut1.b, [4, 12, 3])
AssertionError: Lists differ: [] != [4, 12, 3]

Second list contains 3 additional elements.
First extra element 0:
4

- []
+ [4, 12, 3]

======================================================================
FAIL: test_c_last_three_numbers (test_expressions.TestCase_c_last_three_numbers.
test_c_last_three_numbers)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Sven1\svgr\workspaces\ds_cs4bd_2324\C_expressions\test_expressions.py
", line 117, in test_c_last_three_numbers
    td.assertEqual(td.ut1.c, [1, 8, 7])
AssertionError: Lists differ: [] != [1, 8, 7]

Second list contains 3 additional elements.
First extra element 0:
1

- []
+ [1, 8, 7]

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=2)
```
Output says: `Ran 3 tests`, `FAILED (failures=2)`.

When tests fail, the test report tells which tests have failed and why:

  - *test_b_first_three_numbers* failed in line: 103. The test expected
    result: `[4, 12, 3]`, but an empty list `[]` was found in the tested
    expression: `self.b` in file `expressions.py`.

  - *test_c_last_three_numbers* failed in line: 117 where the test expected
    result: `[1, 8, 7]`, but an empty list `[]` was found in: `self.c`

Tests refer to the `self.numbers` list: `[4, 12, 3, 8, 17, 12, 1, 8, 7]`.

(1 Pt)


&nbsp;
### 4.) Challenge: Write Expressions

In order to let tests pass, write expressions in
[expressions.py](https://gitlab.bht-berlin.de/sgraupner/ds_cs4bd_2324/-/blob/main/C_expressions/expressions.py)
for variables `self.b` .. `self.k` according to specification, e.g. write an
expression for `self.b` that extracts the first three numbers from `self.numbers`.

Use <b>one-line expressions</b> only.
Python's [built-in functions](https://docs.python.org/3/library/functions.html)
are allowed, but not own functions.

Tests exercise expressions with various lists. Initialization with constants
(`self.b = [4, 12, 3]`) will hence not work.

Write expression incrementally, one after the other - not all at once. Some
expressions require thinking and reading.

Once you have written an expression, uncomment the corresponding test case in 
[test_expressions.py](https://gitlab.bht-berlin.de/sgraupner/ds_cs4bd_2324/-/blob/main/C_expressions/test_expressions.py):
and re-run the test. See if it is passing or figure out why it is failing
from the test report.

![](../markup/img/C_unit_tests_3.png)

Test cases a), b) and c) are now passing.

Continue until all tests pass.

![](../markup/img/C_unit_tests_4.png)


&nbsp;
### 5.) Challenge: Final Test

Pull latest Unit-test file from GitLab and re-run tests:
```sh
wget https://gitlab.bht-berlin.de/sgraupner/ds_cs4bd_2324/-/blob/main/C_express
ions/test_expressions.py

python test_expressions.py --tests=all
```

Result:

```
...........
----------------------------------------------------------------------
Ran 11 tests in 0.002s

OK
<unittest.runner.TextTestResult run=11 errors=0 failures=0>
```
(10 Pts, 1 Pt for each test passing)
