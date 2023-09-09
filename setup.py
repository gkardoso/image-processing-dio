from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="kardoso_image_package",
    version="0.0.1",
    author="Guilherme Cardoso",
    author_email="gkardoso@hotmail.com  ",
    description="A test to learn manage packages",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gkardoso/image-processing-dio"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)