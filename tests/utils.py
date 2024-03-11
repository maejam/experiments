from contextlib import contextmanager


@contextmanager
def not_raises(exception):
  try:
    yield
  except e:
    raise pytest.fail(f"Exception raised {e}")
