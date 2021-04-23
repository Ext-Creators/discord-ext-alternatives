import re
import setuptools


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

with open("requirements.txt") as stream:
    install_requires = stream.read().splitlines()

packages = [
    "discord.ext.alternatives",
]

project_urls = {
    "Issue Tracker": "https://github.com/Ext-Creators/discord-ext-alternatives/issues",
    "Source": "https://github.com/Ext-Creators/discord-ext-alternatives",
}

_version_regex = r"^version = ('|\")((?:[0-9]+\.)*[0-9]+(?:\.?([a-z]+)(?:\.?[0-9])?)?)\1$"

with open("discord/ext/alternatives/__init__.py") as stream:
    match = re.search(_version_regex, stream.read(), re.MULTILINE)

version = match.group(2)

if match.group(3) is not None:
    try:
        import subprocess

        process = subprocess.Popen(["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += out.decode("utf-8").strip()

        process = subprocess.Popen(["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE)
        out, _ = process.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except (Exception) as e:
        pass

setuptools.setup(
    author="Ext-Creators",
    classifiers=classifiers,
    description="A discord.py extension with additional and alternative features.",
    install_requires=install_requires,
    license="Apache Software License",
    name="discord-ext-alternatives",
    packages=packages,
    project_urls=project_urls,
    url="https://github.com/Ext-Creators/discord-ext-alternatives",
    version=version,
)
