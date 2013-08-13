import datetime
import json
import unittest

import docker

from cargo.image import Image

with open('example_image_payload.json', 'r') as file_obj:
  EXAMPLE_PAYLOAD = json.loads(file_obj.read())[0]

class TestImage(unittest.TestCase):
  def __init__(self, *args, **kw):
    super(TestImage, self).__init__(*args, **kw)
    client = docker.Client()

    self.payload = client.images or EXAMPLE_PAYLOAD


  def setUp(self):
    self.ex_image = Image(EXAMPLE_PAYLOAD) 

  def test_image(self):
    assert self.ex_image

  def test_image_created(self):
    assert self.ex_image.created == datetime.datetime.fromtimestamp(1364084963)

  def test_image_repository(self):
    assert self.ex_image.repository == 'busybox'

  def test_image_tag(self):
    assert self.ex_image.tag == 'latest'

  def test_image_vsize(self):
    assert self.ex_image.vsize == 6824592

  def test_image_size(self):
    assert self.ex_image.size == 6824592
