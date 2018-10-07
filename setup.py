from distutils.core import setup

setup(
    name="panoply_typeform",
    version="1.0.0",
    description="Panoply Data Source for the Typeform API",
    author="Alon Weissfeld",
    author_email="alon.weissfeld@panoply.io",
    url="http://panoply.io",
    package_dir={"panoply": ""},
    install_requires=[
        "panoply-python-sdk==1.5.0",
        "requests==2.3.0",
        "backoff==1.4.3",
    ],
    extras_require={
        "test": [
            "pycodestyle==2.4.0",
            "coverage==4.3.4",
            "mock==2.0.0"
        ]
    },
    packages=["panoply.typeform"]
)
