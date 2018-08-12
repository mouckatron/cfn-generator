import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cfngenerator",
    version="0.0.1",
    author="Graham Moucka",
    author_email="mouckatron@gmail.com",
    description="Library for generating AWS CloudFormation scripts from code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mouckatron/cfn-generator",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
