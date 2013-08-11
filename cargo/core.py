from cargo.dock import dock

default_dock = Dock()

def build(path=None, dock=default_dock, *args, **kw):
  raise NotImplementedError  


def start(container=None, *args, **kw):
  raise NotImplementedError  


def ps(dock=default_dock):
  return dock.containers
