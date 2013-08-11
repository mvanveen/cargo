import cargo

def test_ps():
  # TODO: pymox yo

  # assert that container ids are the same for both `cargo.ps` and 
  # `dock.containers` (interfaces should be identical)

  assert [x.container_id == y.container_id for x, y in 
     zip(cargo.ps(), cargo.get_default_dock().containers
  )]
