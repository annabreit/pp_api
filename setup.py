from setuptools import setup

requirements = open('requirements.txt', 'r').read().split("\n")
requirements = [x for x in requirements if ((len(x) > 0)
                                            and (x[0] != '-')
                                            and ("+" not in x))]
requirements = [x.replace("python-", "python_") for x in requirements]
dependencies = ["https://github.com/semantic-web-company/nif/tarball/master#egg=nif"]

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='pp_api',
    version='0.1dev',
    description='Library for accessing PoolParty APIs',
    packages=['pp_api'],
    license='MIT',
    install_requires=requirements,
    dependency_links=dependencies
)
