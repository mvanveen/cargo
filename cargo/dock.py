import docker

LOCAL_URL = 'http://localhost:4243'
DEFAULT_VERSION = "1.3"

class Dock(object):
  """Wrapper class for `docker-py` Client instances"""
  
  def __init__(self, *args, **kw):
    super(Dock, self).__init__()

    self._base_url = kw['base_url'] = kw.get('base_url') or LOCAL_URL
    self._version = kw['version'] = kw.get('version') or DEFAULT_VERSION
    
    self._client = docker.Client(*args, **kw)


  def __getattribute__(self, x):
    client = super(Dock, self).__getattribute__('_client')

    # return client attribute if not a magic method
    if hasattr(client, x) and not x.startswith('_'):
      return client.__getattribute__(x)

    return super(Dock, self).__getattribute__(x)

