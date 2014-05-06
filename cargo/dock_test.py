import re
import unittest

import docker

from cargo.dock import Dock



def test_get_attribute():
  import inspect
  dock = Dock()
  client = docker.Client()

  # source code equivalence ftw (refs will be different)
  assert inspect.getsource(dock.build) == inspect.getsource(client.build)

class DockTest(unittest.TestCase):
  """Test class for `Dock` objects.

  Not to be confused with `doctest`, of course ;-)
  """

  def setUp(self, *args, **kw):
    super(DockTest, self).setUp(*args, **kw)

    self._dock = Dock()
  
  def test_containers(self):
    #TODO(mvv): robably need pymox here
    assert self._dock

  def test_repr(self):
    assert re.match(
      '<Dock \[(.*)\] \((.*)\)>',
      self._dock.__repr__()
    )

  def test_dock_info(self):
    assert isinstance(self._dock.info, dict)

  def test_total_num_containers(self):
    assert isinstance(self._dock.total_num_containers, int)

  def test_total_num_images(self):
    assert isinstance(self._dock.total_num_images, int)

  def test_total_num_goroutines(self):
    assert isinstance(self._dock.total_num_goroutines, int)

  def test_memory_limit(self):
    assert isinstance(self._dock.memory_limit, int)

  def test_debug(self):
    assert isinstance(self._dock.debug, int)
