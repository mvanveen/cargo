import datetime
import json
import unittest

import docker

from cargo.container import Container


with open('example_payload.json', 'r') as file_obj:
  EXAMPLE_PAYLOAD = json.loads(file_obj.read())[0]

class TestContainer(unittest.TestCase):

  def __init__(self, *args, **kw):
    super(TestContainer, self).__init__(*args, **kw)

    client = docker.Client()
    self.paylod = client.containers or EXAMPLE_PAYLOAD
 
  def setUp(self):
    self.ex_container = Container(EXAMPLE_PAYLOAD)
 
  def test_container(self):
     # can the thing be instantiated and is it truthy?
     assert self.ex_container

  def test_container_status_type(self):
     with self.assertRaises(TypeError):
       container = Container('lolwhat')

  def test_container_status(self):
    container = Container(EXAMPLE_PAYLOAD)
    assert container.status == 'Up 6 hours'

  def test_container_created(self):
    assert self.ex_container.created == datetime.datetime.fromtimestamp(1376188514)

  def test_container_command(self):
    assert self.ex_container.command == 'python -m SimpleHTTPServer'

  def test_container_ports_list(self):
    assert isinstance(self.ex_container.ports, list)

  def test_container_ports_list_length(self):
    assert len(self.ex_container.ports) == 1

  def test_container_ports_inner_tuple(self):
    assert isinstance(self.ex_container.ports[0], tuple)

  # TODO: write mocks for this shit.
  #def test_container_ports_inner_forward_port_exterior(self):
  #  assert self.ex_container.ports[0][0] == 49155

  def test_container_ports_inner_forward_port_interior(self):
    assert self.ex_container.ports[0][1] == 8000

  def test_container_repr(self):
    assert self.ex_container.__repr__() == '<Container [b575c9ece1b9]>'

  #TODO(mvv): make a test payload that has more than one port forwarded
