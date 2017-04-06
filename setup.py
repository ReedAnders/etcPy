from setuptools import setup

setup(name='etcdPy',
      version='0.1',
      description='Queue update with Python etcd Raft wrapper ',
      url='http://github.com/ReedAnders/etcdPy',
      author='Reed Anderson',
      author_email='reed.anderson@colorado.edu',
      license='MIT',
      packages=['etcdPy'],
      entry_points={
        'console_scripts':
            ['etcdPy = etcdPy.__main__:main']
            },
      zip_safe=False)
