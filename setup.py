import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pymitt",
    version="1.0.0",
    description="Minimal Python wrapper for Keymitt webhooks",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/fedus/pymitt",
    author="Federico Gentile",
    author_email="gentfede+github@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["pymitt"],
    include_package_data=True,
    install_requires=["asyncio", "aiohttp[speedups]"]
)
