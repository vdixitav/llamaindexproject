from setuptools import find_packages, setup

setup(
    name="llamaindexproject",
    version="0.0.1",
    author="Dixita",
    packages=find_packages(),
    install_requires=["llama-index","python-dotenv","html2text","llama-index-readers-web"]
)
    