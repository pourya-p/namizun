from setuptools import setup

setup(name='namizun_core',
      version='1.3.8',
      description='namizun main functions',
      author='MalKeMit',
      url='https://github.com/pourya-p/namizun.git',
      setup_requires=['wheel'],
      install_requires=['psutil==5.9.4',
                        'redis==4.3.5',
                        'pytz==2022.6'],
      py_modules=["time", "ip", "database", "network", "udp", "log"],
      )
