from distutils.core import setup

setup( name="datastream",
       version='0.1',
       py_modules=['datastream'],
       requires=['zmq>=15.0.0'],
       url="https://github.com/jheise/datastream",
       author="Jon Heise",
       author_email="j.heise@gmail.com",
       description="Library for streaming and analyzing data with zmq."
)
