import re
import setuptools


with open("README.rst", "r") as stream:
    long_description = stream.read()

with open("requirements.txt") as stream:
    install_requires = stream.read().splitlines()

with open("discord/ext/alternatives/__init__.py") as stream:
    version = re.search(r"^__version__\s*=\s*[\'\"]([^\'\"]*)[\'\"]", stream.read(), re.MULTILINE).group(1)

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

project_urls = {
    "Issue Tracker": "https://github.com/Ext-Creators/discord-ext-alternatives/issues",
    "Source": "https://github.com/Ext-Creators/discord-ext-alternatives",
}

setuptools.setup(
    author="Ext-Creators",
    classifiers=classifiers,
    description="A discord.py extension with additional and alternative features. Use with caution.",
    install_requires=install_requires,
    license="Apache Software License",
    name="discord-ext-alternatives",
    packages=["discord.ext.alternatives"],
    project_urls=project_urls,
    python_requires=">=3.5.3",
    url="https://github.com/Ext-Creators/discord-ext-alternatives",
    version=version,
)
