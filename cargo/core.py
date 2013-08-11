from cargo.dock import Dock

def get_default_dock(dock=Dock()):
  return dock


def build(path=None, dock=get_default_dock(), *args, **kw):
  raise NotImplementedError  


def start(container=None, *args, **kw):
  raise NotImplementedError  


def ps(dock=get_default_dock()):
  return dock.containers
