import setuptools
from glob import glob

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wiki_scrapper",
    version="0.0.1",
    author = "Evan Vandermate, Andrew Anderson, Jackson Schuiling, Kaylee Brinkman, Lemi Vargas Pagan",
    author_email="evanderm@mtu.edu, aanderso@mtu.edu, jjschuil@mtu.edu, cmbrinkm@mtu.edu, lvargasp@mtu.edu",
    description="A tool that allows people to easily pull information from the internet.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'numpy',
        'tk',
        'requests',
        'wikipedia-api',
        'customtkinter',
     ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    scripts=[
        'bin/webscraper_gui.py',
    ],
    include_package_data=True,
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9.6",
)
