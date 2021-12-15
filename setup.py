from setuptools import setup

packages = []
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(
    name="app",
    version="1.0",
    description="example api for testing aws lambda",
    url="http://github.com/siavrez/fastapi-aws-lambda-second",
    author="siavrez",
    author_email="siavash.rezazadeh@gmail.com",
    license="MIT",
    include_package_data=True,
    install_requires=requirements,
    packages=packages,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
)
