import time
from abc import ABCMeta, abstractmethod
import datetime

class Subject(object):
  def __init__(self):
    self.observers = []
    self.cur_time = None

  def register_observer(self, observer):
    if observer in self.observers:
      print observer, 'already in subscribed observers'
    else:
      self.observers.append(observer)

  def unregister_observer(self, observer):
    try:
      self.observers.remove(observer)
    except ValueError:
      print 'No such observer in subject'

  def notify_observers(self):
    self.cur_time = time.time()
    for observer in self.observers:
      observer.notify(self.cur_time)


class Observer(object):
  """Abstract class for observers, provides notify method as interface for subjects."""

  __metaclass__ = ABCMeta

  @abstractmethod
  def notify(self, unix_timestamp):
    pass

class USATimeObserver(Observer):
  def __init__(self, name):
    self.name = name
  
  def notify(self, unix_timestamp):
    time = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d %I:%M:%S%p') print 'Observer', self.name, 'says:', time

