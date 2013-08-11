import docker

from cargo.container import Container

LOCAL_URL = 'http://localhost:4243'
DEFAULT_VERSION = "1.3"

# this is a hack to get `__getattribute__` working for a few reserved properties
RESERVED_METHODS = ['containers', '_client', 'info']

class Dock(object):
  """Wrapper class for `docker-py` Client instances"""
  
  def __init__(self, *args, **kw):
    super(Dock, self).__init__()

    self._base_url = kw['base_url'] = kw.get('base_url') or LOCAL_URL
    self._version = kw['version'] = kw.get('version') or DEFAULT_VERSION
    
    self._client = docker.Client(*args, **kw)

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

  def __repr__(self):
    return '<Dock [%s] (%s)>' % (self._base_url, self._version)
