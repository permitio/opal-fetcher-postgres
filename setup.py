from setuptools import setup, find_packages

def get_requirements(env=""):
    if env:
        env = "-{}".format(env)
    with open("requirements{}.txt".format(env)) as fp:
        return [x.strip() for x in fp.read().split("\n") if not x.startswith("#")]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='opal-fetcher-postgres',
    version='0.0.1',
    author='Asaf Cohen',
    author_email="asaf@permit.io",
    description="An OPAL fetch provider to bring authorization state from Postgres DB.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/permitio/opal-fetcher-postgres",
    packages=find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    python_requires='>=3.7',
    install_requires=get_requirements(),
)