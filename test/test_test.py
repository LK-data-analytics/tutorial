__author__ = 'tobias'

def test_empty_dictionary():
  x = dict()
  assert len(x) == 0

def test_put_item_into_dictionary():
  x = dict()
  x.update({"foo" : "bar"})
  assert x.get("foo") == "bar"

def test_some_math():
  a = 5
  b = 2
  assert a == b