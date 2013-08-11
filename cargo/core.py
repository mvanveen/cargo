from cargo.dock import dock

default_dock = Dock()

def build(path=None, dock=default_dock, *args, **kw):
  # catch an actual cargo type here
  if len(args) and isinstance(args[0], Image):
    # TODO: build image
    image = args[0]
    args = args[1:]
    pass

  return dock.build(*args, **kw)


def start(container=None, *args, **kw):
  return docker.start


def ps(dock=default_dock):
  return dock.containers
