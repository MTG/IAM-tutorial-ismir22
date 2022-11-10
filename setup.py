from setuptools import setup, find_packages

with open("README.md") as f:
    README = f.read()

with open("requirements.txt") as f:
    REQUIREMENTS = f.readlines()

setup(
    name="common",
    version="0.1.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Topic :: Multimedia",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Editors",
        "Topic :: Software Development :: Libraries",
    ],
    description="Tutorial webbook to get started with the computational analysis of Indian Art Music",
    long_description=README,
    long_description_content_type="text/markdown",
    author_email=["genis.plaja@upf.edu", "thomas.nuttall@upf.edu"],
    license="GNU GENERAL PUBLIC LICENSE",
    packages=find_packages(),
    keywords=["indian art music", "computational musicology"],
    install_requires=[
        REQUIREMENTS
    ],
)