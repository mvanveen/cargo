import cargo

def test_ps():
  # TODO: pymox yo

  # assert that container ids are the same for both `cargo.ps` and 
  # `dock.containers` (interfaces should be identical)
  dock = cargo.get_default_dock()
  assert [x.container_id == y.container_id for x, y in 
     zip(cargo.ps(), dock.containers)
  ] or not (len(cargo.ps()) and len(dock.containers))

def test_ps_all():
  # passing in all=True both works and returns Container objects
  assert all([isinstance(x, cargo.Container) for x in cargo.ps(all=True)])
