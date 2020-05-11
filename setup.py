from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '2020.05.10'

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='discord-ext-alternatives',
    author='NCPlayz',
    python_requires='>=3.6.0',
    url='https://github.com/NCPlayz/discord-ext-alternatives',
    version=version,
    packages=['discord/ext/alternatives'],
    license='MIT',
    description='Enable some experimental features for discord.py.',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)