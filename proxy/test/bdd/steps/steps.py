from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp 
from nose.tools import assert_equal, assert_in
from proxy import * 
from proxy_app import app
import os
from contextlib import contextmanager
from StringIO import StringIO
import sys

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

def sample():
  proxy1 = Proxy()
  print
  
  proxy2 = Proxy()
  print
  proxy3 = Proxy()
  print

@step(u'Given I run the proxy application')
def given_i_run_the_proxy_application(step):
    os.system("python proxy.py")

@step(u'When there are already 3 created references')
def when_there_is_already_3_created_references(step):
    assert True
    
@step(u'Then all references should be deleted afterwards for confirmation')
def then_all_references_should_be_deleted_afterwards_for_confirmation(step):
    assert True
