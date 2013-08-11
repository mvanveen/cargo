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


def test_repr():
  dock = Dock()
  assert dock.__repr__() == '<Dock [http://localhost:4243] (1.3)>'
 

def test_containers():
  #probably need pymox here
  dock = Dock()
