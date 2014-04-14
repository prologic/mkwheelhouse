from setuptools import setup

setup(
    name='mkwheelhouse',
    version='0.1.0',
    author='Nikhil Benesch',
    author_email='benesch@whoop.com',
    py_modules=['mkwheelhouse'],
    url='https://github.com/WhoopInc/mkwheelhouse',
    description='Amazon S3 wheelhouse generator',
    install_requires=[
        "awscli >= 1.3.6",
        "yattag >= 0.9.2",
        "wheel >= 0.23.0"
    ],
)