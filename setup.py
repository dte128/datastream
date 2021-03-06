from distutils.core import setup

setup( name="datastream",
       version='0.1',
       packages=['datastream'],
       requires=['pyzmq(>=15.0.0)'],
       install_requires=['pyzmq>=15.0.0'],
       url="https://github.com/jheise/datastream",
       author="Jon Heise",
       author_email="j.heise@gmail.com",
       description="Library for streaming and analyzing data with zmq."
)
