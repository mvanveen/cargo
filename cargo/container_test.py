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

  #def test_container_ports(self):
  #  assert self.ex_container.ports == (49154, 8000)

