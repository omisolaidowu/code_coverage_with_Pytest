# Import the Pytest coverage plugin:
import coverage

# Start code coverage before importing other modules:
cov = coverage.Coverage()
cov.start()

# Main code to be covered----------:

import sys
sys.path.append(sys.path[0] + "/..")

from plain_tests.plain_tests import test_should_tweak_name


tweak_names = test_should_tweak_name("LambdaTest")

print(tweak_names.test_should_addNames("Grid"))

will_not_tweak_names = test_should_tweak_name("Not LambdaTest")

# print(tweak_names.test_should_changeName("LambdaTest Cloud Grid"))

print(will_not_tweak_names.test_should_addNames("Grid"))

   
# Stop code coverage and save the output in a reports directory---------:
cov.stop()
cov.save()
cov.html_report(directory='coverage_reports')