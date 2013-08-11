import docker

from cargo.dock import Dock


def test_make_dock():
  dock = Dock()

def test_get_attribute():
  import inspect
  dock = Dock()
  client = docker.Client()

  # source code equivalence ftw (refs will be different)
  assert inspect.getsource(dock.build) == inspect.getsource(client.build)


