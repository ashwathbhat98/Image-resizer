from setuptools import setup
import sys

setup(name = 'image-resizer',
      description = 'Python tool to resize a bunch of images quickly.',
      long_description=open('README.rst').read(),
      version = '0.1.1',
      install_requires = [
        r for r in open('requirements.txt', 'r').read().split('\n') if r],
      author = 'Ashwath Bhat',
      author_email = 'ashwathbhat02@gmail.com',
      packages = ['image-resizer'],

      entry_points = {
          'console_scripts': ['image-resize=image_resize:console_main'],
      },
      url = 'https://github.com/ashwathbhat98/image-resizer/',
      download_url = 'https://github.com/ashwathbhat98/image-resizer/tarball/v0.1.0',
      keywords = ['image', 'resize', 'utility', 'compress'],
      classifiers = [
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities'
      ],
      )
