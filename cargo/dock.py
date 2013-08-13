import docker

from cargo.container import Container
from cargo.image import Image

LOCAL_URL = 'http://localhost:4243'
DEFAULT_VERSION = "1.3"

# this is a hack to get `__getattribute__` working for a few reserved properties
RESERVED_METHODS = ['containers', '_client', 'images', 'info', 'start', 'stop']

class Dock(object):
  """Wrapper class for `docker-py` Client instances"""
  
  def __init__(self, *args, **kw):
    super(Dock, self).__init__()

    self._base_url = kw['base_url'] = kw.get('base_url') or LOCAL_URL
    self._version = kw['version'] = kw.get('version') or DEFAULT_VERSION
    
    self._client = docker.Client(*args, **kw)

  def __repr__(self):
    return '<Dock [%s] (%s)>' % (self._base_url, self._version)

  def __getattribute__(self, x):
    client = super(Dock, self).__getattribute__('_client')


    # return client attribute if not a magic method or reserved attr
    legal = not x.startswith('_') and not(x in RESERVED_METHODS)

    if hasattr(client, x) and legal:
      return client.__getattribute__(x)

    return super(Dock, self).__getattribute__(x)

  @property
  def containers(self, *args, **kw):
    return [Container(x) for x in self._client.containers(*args, **kw)]

  @property
  def _containers(self, *args, **kw):
    return [x for x in self._client.containers(*args, **kw)]

  @property
  def images(self, *args, **kw):
    return [Image(x) for x in self._client.images(*args, **kw)]

  @property
  def _images(self, *args, **kw):
    return [x for x in self._client.images(*args, **kw)]

  @property
  def info(self):
    return self._client.info()

  @property
  def total_num_containers(self):
    info = self.info
    return int(info.get('Containers'))

  @property
  def total_num_images(self):
    info = self.info
    return int(info.get('Images'))

  @property
  def total_num_goroutines(self):
    info = self.info
    return int(info.get('NGoroutines'))

  @property
  def memory_limit(self):
    info = self.info
    return info.get('MemoryLimit')

  @property
  def debug(self):
    info = self.info
    return info.get('Debug')

  def running(self, container):
    """Returns True if dock is running container, else False

    Accepts container id's and Container objects
    """
    container_ids = [x.container_id for x in self.containers]
    if isinstance(container, Container):
      return container.container_id in containder_ids
    elif isinstance(container, basestring):
      return container in container_ids

    raise TypeError('expected container id as string or Container object.')


  def start(self, container, *args, **kw):
    if isinstance(container, Container):
      cid = container.container_id
    elif isinstance(container, basestring):
      cid = container
    
    return self._client.start(cid, *args, **kw)

  def stop(self, container, *args, **kw):
    if isinstance(container, Container):
      cid = container.container_id
    elif isinstance(container, basestring):
      cid = container
    
    return self._client.stop(cid, *args, **kw)
