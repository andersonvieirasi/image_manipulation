# image_manipulation/__init__.py

#Pacote de manipulação de imagens.

#from .utils import resize_image, apply_blur
from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    page_description=f.read()

with open("requirements.txt") as f:
    requirements=f.read().splitlines()


setup(
    name="image_manipulation",
    version="0.0.1",
    author="Anderson Vieira",
    author_email="andersonvieira.si@gmail.com",
    description="Desafio da DIO ",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andersonvieirasi/dio-me-python-basico",
    packages=find_packages(),
    install_required=requirements,
    python_requires='>=3.8',
)