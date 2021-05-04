from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='webnews',
    version='1.0',
    description='Web news',
    license='MIT',
    author='Francois Colombo',
    author_email='francoiscolombo@protonmail.com',
    url='https://github.com/francoiscolombo/webnews-v2',
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: Other/Proprietary License',
        'Operating System :: Unix',
    ],
    entry_points='''
        [console_scripts]
        webnews=webnews.__main__:cli
    ''',
    python_requires='>=3.8',
)
