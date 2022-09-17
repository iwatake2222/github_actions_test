"""setup script"""
from setuptools import setup, find_packages

setup(
    name="My Package",
    version='1.0',
    description='My Package',
    author='iwatake2222',
    author_email='abc@abc.com',
    license='Apache License 2.0',
    tests_require=['pytest'],
    packages=find_packages(),
    platforms=["linux", "unix"],
    python_requires=">3.7",
    entry_points="""
      [console_scripts]
      my_package_exe=my_package.main:main
    """,
)
