# code_coverage_with_Pytest
This mock test measures the amount of code the test covers using Pytest's coverage.py plugin. It simultaneously runs the test on a cloud grid.
## Test Structure
```
Coverage_demo
├─ .gitignore
├─ locators
│  ├─ locator.py
│  
├─ plain_tests
│  ├─ plain_tests.py
│  
├─ run_coverage
|  ├─ name_tweak_coverage.py
│  ├─ run_coverage.py
|  ├─ coverage_reports
|  ├─ .env
├─ setup
│  ├─ setup.py
│
└─ testscenario
|   ├─ test_scenarioRun.py
├─ requirements.txt
```
## To Run this Test Coverage:
`cd run_coverage`

Then run:

`run_coverage.py`
