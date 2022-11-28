# Import the Pytest coverage plugin:
import coverage

# Start code coverage before importing other modules:
cov = coverage.Coverage()
cov.start()

# Main code to be covered----------:

import sys
sys.path.append(sys.path[0] + "/..")
from testscenario.test_scenarioRun import test_registration

registration = test_registration()
registration.test_should_register_user()
    
# Stop code coverage and save the output in a reports directory---------:
cov.stop()
cov.save()
cov.html_report(directory='coverage_reports')












