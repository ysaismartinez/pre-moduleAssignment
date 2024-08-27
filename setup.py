#Import my dependencies.
from setuptools import setup, find_packages

#This is the setup for my script
setup(
    name="my_cli_hw",
    version="0.1",
    packages=find_packages(),  # Ensure this correctly identifies 'my_cli_hw'
    include_package_data=True,
    install_requires=[
        "pandas",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "my_cli_hw=my_cli_hw.cli:main", #I make sure my entry point refers to the main method. 
        ],
    },
)

