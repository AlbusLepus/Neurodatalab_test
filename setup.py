from os import path
from setuptools import setup, find_packages

# for pip >= 10
try:
    from pip._internal.req import parse_requirements
# for pip <= 9.0.3
except ImportError:
    from pip.req import parse_requirements


install_reqs = parse_requirements(path.join(path.dirname(__file__), 'requirements.txt'), session='')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='neurodata_test',
    version='0.0.1',
    install_requires=reqs,
    packages=find_packages(),
    long_description=__doc__,
    include_package_data=True,
)
