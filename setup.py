from distutils.core import setup

setup(
  name='cargo',
  version='.01',
  description='Docker Containers for Humans',
  author='Michael Van Veen',
  author_email='michael@codebrow.se',
  url='http://github.com/mvanveen/cargo',
  packages=['cargo'],
  install_requires=['docker-py']
)
