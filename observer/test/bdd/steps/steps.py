from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp 
from nose.tools import assert_equal, assert_in
from observer import * 
from observer_app import app
import os

@step(u'Given I run the observer application')
def given_i_run_the_observer_application(step):
    os.system("python proxy.py")

@step(u'When the time is already recorded in 12-hr and 24-hr format')
def when_the_time_is_already_recorded_in_12_hr_and_24_hr_format(step):
    assert True

@step(u'Then there should be a record like this')
def then_there_should_be_a_record_like_this(step):
    f = open('time', 'r')
    for row in step.hashes: 
        time_ref = f.readline().splitlines()
        str1 = ''.join(time_ref)
        assert_equal(str1, str(row['time_format']))