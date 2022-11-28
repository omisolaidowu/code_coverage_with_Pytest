
import coverage
cov = coverage.Coverage()
cov.start()
# Import the Pytest coverage plugin:


# Start code coverage before importing other modules:


# Main code to be covered----------:

import sys
sys.path.append(sys.path[0] + "/..")
from testscenario.test_scenarioRun import test_registration



registration = test_registration()
registration.it_should_register_user()

# Stop code coverage and save the output in a reports directory---------:
cov.stop()
cov.save()
cov.html_report(directory='coverage_reports')












