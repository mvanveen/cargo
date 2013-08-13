import datetime

import cargo

class Container(object):
  """Python wrapper class encapsulating the metadata for a Docker Container"""

  def __init__(self, *args, **kw):
    super(Container, self).__init__()

    # if the first argument is the `docker-py` response dict, we want to 
    # leverage that
    if len(args) and isinstance(args[0], dict):
      config = args[0]
      config.update(kw)

    elif len(args) and not isinstance(args[0], dict):
      raise TypeError('expected container dictionary as first parameter') 
    else:
     config = kw

    # response dict  from `docker-py` preserves caps.  we want 
    # lowercase to correspond with keyword attrs
    self._config = config = dict([(x.lower(), y) for x, y in config.iteritems()])

  @property
  def status(self):
    return self._config.get('status')

  @property
  def created(self):
    return datetime.datetime.fromtimestamp(int(self._config.get('created')))

  @property
  def image(self):
     return self._config.get('image')

  @property
  def ports(self):
     split = lambda payload: [tuple([int(port) for port in x.split('->')]) for x in payload.split(', ')]
     return split(self._config.get('ports'))

  @property
  def command(self):
     return self._config.get('command')

  @property
  def container_id(self):
    return self._config.get('id')

  @property
  def image(self):
    return self._config.get('image')
  
  def __repr__(self):
    return '<Container [%s]>' % (self.container_id[:12],)

  @property
  def logs(self, dock=None):
    #TODO(mvv): unit test this!!!
    if not dock:
      dock = cargo.get_default_dock()
    return dock._client.logs(self.container_id) 

  @property
  def top(self, dock=None):
    #TODO(mvv): unit test this!!!
    if not dock:
      dock = cargo.get_default_dock()
    return dock._client.top(self.container_id) 
