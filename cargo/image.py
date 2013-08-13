from cargo.base import CargoBase, lowercase, make_id_dict


class Image(CargoBase):
  """Python wrapper class encapsulating the metadata for a Docker Image"""

  def __init__(self, *args, **kw):
    super(Image, self).__init__(*args, **kw)

  @property
  def config(self, *args , **kw):
    image = make_id_dict(self._dock._images).get(self._config.get('id'))
    if image:
      self._config = lowercase(image)
    return self._config

  @property
  def image(self):
    return self.config.get('image')

  @property
  def size(self):
    return self.config.get('size')

  @property
  def vsize(self):
    return self.config.get('virtualsize')

  @property
  def image_id(self):
    return self.config.get('id')

  @property
  def repository(self):
    return self.config.get('repository')

  @property
  def tag(self):
    return self.config.get('tag')

  def __repr__(self):
    if self.repository:
      return '<Image [%s:%s]>' % (self.repository, self.image_id[:12])
    return '<Image [%s]>' % (self.image_id[:12],)
