from observer import *


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
  subject = Subject()

  print 'Adding usa_time_observer'
  observer1 = USATimeObserver('usa_time_observer')
  subject.register_observer(observer1)
  subject.notify_observers()
  
  time.sleep(2)
  print 'Adding eu_time_observer'
  observer2 = EUTimeObserver('eu_time_observer')
  subject.register_observer(observer2)
  subject.notify_observers()
  
  time.sleep(2)
  print 'Removing usa_time_observer'
  subject.unregister_observer(observer1)
  subject.notify_observers()


def test_sample():
  with open ("time.txt", "r") as myfile:
    data=myfile.read()
  with captured_output() as (out, err):
        sample()
        # This can go inside or outside the `with` block
        output = out.getvalue().strip()
        assert_equal(output, data)


