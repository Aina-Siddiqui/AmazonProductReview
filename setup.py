import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()
__version__="0.0.0"
REPO_NAME="AmazonProductReview"
AUTHOR_USER_NAME="Aina-Siddiqui"
SRC_REPO="reviewClassifier"
AUTHOR_EMAIL="ainasiddiqui1235@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for classifying Amazon product reviews",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src" },
    packages=setuptools.find_packages(where="src")
)
    