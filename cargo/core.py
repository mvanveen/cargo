from cargo.container import Container
from cargo.dock import Dock

def get_default_dock(dock=Dock()):
  return dock


def build(path=None, dock=get_default_dock(), *args, **kw):
  raise NotImplementedError  


def start(container, *args, **kw):
  raise NotImplementedError  


def ps(dock=get_default_dock(), *args, **kw):
  _id = kw.get('id')
  if _id:
    del kw['id']

  containers = [Container(x) for x in dock._client.containers(*args, **kw)]
  if _id:
    return dict( 
     # make sure we got short form and long form of container id
     # note: this is expensive!
     [(x.container_id[:12], x) for x in containers] + 
     [(x.container_id, x) for x in containers]
    ).get(_id)
  return containers
