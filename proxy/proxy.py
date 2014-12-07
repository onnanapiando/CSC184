from abc import ABCMeta, abstractmethod
import random

class AbstractSubject(object):
  """A common interface for the real and proxy objects."""

  __metaclass__ = ABCMeta

@abstractmethod
def sort(self, reverse=False):
  pass
