from setuptools import setup

setup(name='namizun_menu',
      version='1.0.0',
      description='namizun menu',
      author='MalKeMit',
      url='https://github.com/pourya-p/namizun.git',
      setup_requires=['wheel'],
      install_requires=['colored~=1.4.4',
                        'pyfiglet>=1.0.4,<2',
                        'prettytable~=3.5.0'],
      py_modules=["monitor", "udp_submenu", "network_submenu", "display", "main_menu"],
      )
