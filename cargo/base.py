#from cargo.core import get_default_dock
import cargo

def make_id_dict(_list):
  return dict([(x.get('Id'), x) for x in _list])

def lowercase(config):
  return dict([(x.lower(), y) for x, y in config.iteritems()])

class CargoBase(object):
  """Base class for Cargo `Container` and `Image` classes"""

  def __init__(self, *args, **kw):
    super(CargoBase, self).__init__()

    # if the first argument is the `docker-py` response dict, we want to 
    # leverage that
    if len(args) and isinstance(args[0], dict):
      config = args[0]
      config.update(kw)

    elif len(args) and not isinstance(args[0], dict):
      raise TypeError('expected container dictionary as first parameter') 
    else:
     config = kw

    dock = kw.get('dock')
    if dock and not isinstance(dock, cargo.Dock):
      raise TypeError('expected dock parameter to be Dock object')

    self._dock = dock or cargo.get_default_dock()

    # response dict  from `docker-py` preserves caps.  we want 
    # lowercase to correspond with keyword attrs
    self._config = config = lowercase(config)

  @property
  def config(self):
     raise NotImplementedError
