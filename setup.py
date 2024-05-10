from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="Anand",
      author_email="sonianand921@gmail.com",
      package=find_packages(),
      install_requires=["pandas","numpy","flask"]
     )