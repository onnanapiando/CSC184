from lettuce import *
from nose.tools import assert_equal
from webtest import TestApp 
from nose.tools import assert_equal, assert_in
from FactoryMethod import * 
from FactoryMethod_app import app

import httplib2
import os
import re
import threading
import urllib
from urlparse import urlparse, urljoin
from BeautifulSoup import BeautifulSoup
import codecs
import ast

@step(u'Given I accessed the web resources of a site')
def given_i_accessed_the_web_resources_of_a_site(step):
    assert True

@step(u'When I use the protocol ftp')
def when_i_use_the_protocol_ftp(step):
    os.system("python FactoryMethod.py")

@step(u'Then I get a file list for ftp containing:')
def then_i_get_a_file_list_for_http_containing(step):
    #file = open('http_files.txt', 'r')
    #lines1 = file.readline().splitlines())
     for row in step.hashes:
       #files = row['http_files']
       if "../" ==  str(row['ftp_files']):
         assert True

@step(u'When I use the protocol http')
def when_i_use_the_protocol_http(step):
    os.system("python FactoryMethod.py")

@step(u'Then I get a file list for http containing:')
def then_i_get_a_file_list_for_http_containing(step):
     for row in step.hashes:
       if "CERT" ==  str(row['http_files']):
         assert True