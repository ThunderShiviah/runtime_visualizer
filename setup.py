#!/usr/bin/env python

from distutils.core import setup

setup(name='Runtime_visualizer',
    version='0.1',
    description='Visualize the time complexity of functions',
    author='Thunder Shiviah',
    author_email='thunder.shiviah+rtviz@gmail.com',
    license='MIT',
classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
],    
    keywords='runtime visualization',
    install_requires=['matplotlib'],
    url='https://github.com/ThunderShiviah/runtime_visualizer',
     )
