import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tradingbotinteractor",
    version="0.0.1",
    author="Justin Guese",
    author_email="guese.justin@gmail.com",
    description="Interacts with accounthandler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JustinGuese/tradingbot-crypto-interactor",
    project_urls={
        "Bug Tracker": "https://github.com/JustinGuese/tradingbot-crypto-interactor/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ["requests"],
    package_dir={"": "tradinghandler"},
    packages=setuptools.find_packages(where="tradinghandler"),
    python_requires=">=3.9",
)