from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp 
from nose.tools import assert_equal, assert_in
from facade import * 
from facade_app import app

import httplib2
import os
import re
import threading
import urllib
from urlparse import urlparse, urljoin
from BeautifulSoup import BeautifulSoup

@step(u'Given I run the facade application') 
def given_i_run_the_facade_application(step):
    os.system("python facade.py")

@step(u'When I visit the site "([^"]*)"')
def when_i_visit_the_site_group1(step, website):
    url = website_url(website)
    assert_equal(url.website, website)

@step(u'Then I see that there is a cached data')
def then_i_see_that_there_is_a_cached_data(step):
    path = os.path.isfile("myfile")
    if path == True:
      pass
    else:
      assert False

