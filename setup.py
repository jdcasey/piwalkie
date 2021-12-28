#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    zip_safe=True,
    name='piwalkie',
    version='0.0.1',
    long_description="Turn a Raspberry Pi into a walkie talkie with Telegram",
    classifiers=[
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: GNU General Public License (GPL)",
      "Programming Language :: Python :: 3",
    ],
    keywords='telegram rpi raspberry-pi',
    author='John Casey',
    author_email='jdcasey@commonjava.org',
    url='https://github.com/jdcasey/piwalkie',
    license='GPLv3+',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    install_requires=[
      "python-telegram-bot",
      "ruamel.yaml",
      "click",
      "pyaudio",
      'python-vlc',
      'ffmpy',
      'opencv-python',
      'imageio',
      'imutils',
      'pygifsicle'
    ],
    include_package_data=True,
    test_suite="tests",
    entry_points={
      'console_scripts': [
        'walkie = piwalkie:bot'
      ],
    }
)

