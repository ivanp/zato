# -*- coding: utf-8 -*-

"""
Copyright (C) 2013 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

# flake8: noqa
import os
from json import loads
from setuptools import setup, find_packages

curdir = os.path.dirname(os.path.abspath(__file__))
release_info_dir = os.path.join(curdir, '..', 'release-info')
release = open(os.path.join(release_info_dir, 'release.json')).read()
release = loads(release)
revision = open(os.path.join(release_info_dir, 'revision.txt')).read()[:8]

version = '{}.{}.{}.rev-{}'.format(release['major'], release['minor'], release['micro'], revision)

long_description = description = 'Convenience Python client for Zato ESB and app server (https://zato.io)'

setup(
      name = 'zato-client',
      version = version,

      author = 'Zato Developers',
      author_email = 'info@zato.io',
      url = 'https://zato.io',
      license = 'GNU Lesser General Public License v3 (LGPLv3)',
      platforms = 'OS Independent',
      description = description,
      long_description = description,

      package_dir = {'':'src'},
      packages = find_packages('src'),
      namespace_packages = ['zato'],
      
      install_requires=[
          'anyjson==0.3.3',
          'bunch==1.0.1',
          'lxml==3.3.5',
          'requests==2.3.0'
          ],
      
      keywords=('soa eai esb middleware messaging queueing asynchronous integration performance http zeromq framework events agile broker messaging server jms enterprise python middleware clustering amqp nosql websphere mq wmq mqseries ibm amqp zmq'),
      classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Framework :: Buildout',
          'Intended Audience :: Customer Service',
          'Intended Audience :: Developers',
          'Intended Audience :: Financial and Insurance Industry',
          'Intended Audience :: Healthcare Industry',
          'Intended Audience :: Information Technology',
          'Intended Audience :: Telecommunications Industry',
          'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: C',
          'Programming Language :: Python :: 2 :: Only',
          'Programming Language :: Python :: 2.7',
          'Operating System :: POSIX :: Linux',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Communications',
          'Topic :: Database',
          'Topic :: Internet',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
          'Topic :: Internet :: File Transfer Protocol (FTP)',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: Object Brokering',
          ],

      zip_safe = False,
)
