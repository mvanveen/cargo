import datetime

from cargo.base import CargoBase, lowercase, make_id_dict

class Container(CargoBase):
  """Python wrapper class encapsulating the metadata for a Docker Container"""

  def __init__(self, *args, **kw):
    super(Container, self).__init__(*args, **kw)
 
  def __repr__(self):
    return '<Container [%s]>' % (self.container_id[:12],)

  @property
  def config(self):
    # make a dictionary {container_id: <container> \forall containers in 
    # `self._dock.containers` and try to key into the current container id
    container = make_id_dict(self._dock._containers).get(self._config.get('id'))
    if container:
      self._config = lowercase(container)
    return self._config

  @property
  def status(self):
    return self.config.get('status')

  @property
  def created(self):
    return datetime.datetime.fromtimestamp(int(self.config.get('created')))

  @property
  def image(self):
     return self.config.get('image')

  @property
  def ports(self):
     split = lambda payload: [tuple([int(port) for port in x.split('->')]) for x in payload.split(', ')]

     payload = self.config.get('ports')

     if self.running:
       return split(payload)
     else:
       # no host ports are exposed if container isn't running
       # TODO: unit test this case
       payload = self._config.get('ports')
       return payload and [(None, y) for _, y in split(payload)] or None

  @property
  def command(self):
     return self.config.get('command')

  @property
  def container_id(self):
    return self.config.get('id')

  @property
  def image(self):
    return self.config.get('image')
 
  @property
  def logs(self):
    #TODO(mvv): unit test this!!!
    return self._dock._client.logs(self.container_id) 

  @property
  def running(self):
    #TODO(mvv): unit test this!!!
    return self._dock.running(self.container_id)

  @property
  def top(self, dock=None):
    #TODO(mvv): unit test this!!!
    return self._dock._client.top(self.container_id) 

  def start(self, *args, **kw):
    #TODO(mvv): unit test this!!!
    self._dock.start(self.container_id, *args, **kw)

  def stop(self, *args, **kw):
    #TODO(mvv): unit test this!!!
    self._dock.stop(self.container_id, *args, **kw)

