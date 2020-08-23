import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

setuptools.setup(
    name="ytssubs",
    version = '0.0.2',
    description='A Script to download subs from yts',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kashish Srivastava',
    author_email = 'kash.pegasus@gmail.com',
    install_requires=requirements, #external packages as dependencies

    entry_points={
        'console_scripts': ['ytssubs = ytssubs:main']
    }
)