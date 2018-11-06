from setuptools import setup, find_packages


with open('requirements.txt', 'r') as rf:
    requirements = rf.readlines()
    requirements = [x.replace('\n', '').replace('\r', '')
                    for x in requirements]
setup(
    name='presign',
    version='0.1',
    author="Matthew Griffiths",
    author_email="matthew.griffiths2@gmail.com",
    description="A command line tool for creating presigned AWS S3 links",
    packages=find_packages(),
    install_requires=[requirements],
    license="MIT",
    entry_points={
        'console_scripts': [
            'presign = presign.__main__:main',
        ],
    }
)
