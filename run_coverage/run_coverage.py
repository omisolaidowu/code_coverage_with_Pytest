import coverage
cov = coverage.Coverage()

cov.start()

import unittest

import sys
sys.path.append(sys.path[0] + "/..")

from plain_tests.plain_tests import test_should_tweak_name

from testscenario.scenarioRun import test_registration


registration = test_registration()

registration.test_should_register_user()






tweak_names = test_should_tweak_name("Idowu")

print(tweak_names.test_should_addNames("Omisola"))
print(tweak_names.test_should_changeName("Paul"))
    
    


cov.stop()
cov.save()
cov.html_report(directory='coverage_reports')







