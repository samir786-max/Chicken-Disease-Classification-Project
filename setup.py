import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version = '0.0.0'

REPO_NAME = "Chicken-Disease-Classification-Project"
AUTHOR_USER_NAME = "samir786-max"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "samirdanish55@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for Chicken Disease Classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)