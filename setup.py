from distutils.core import setup

setup(
    name="panoply_typeform",
    version="1.1.0",
    description="Panoply Data Source for the Typeform API",
    author="Alon Weissfeld",
    author_email="alon.weissfeld@panoply.io",
    url="http://panoply.io",
    package_dir={"panoply": ""},
    install_requires=[
        "panoply-python-sdk==1.5.0",
        "requests==2.20.1",
        "backoff==1.7.1",
        "ratelimit==2.2.0"
    ],
    extras_require={
        "test": [
            "pycodestyle==2.4.0",
            "coverage==4.5.2",
            "mock==2.0.0"
        ]
    },
    packages=["panoply.typeform"]
)
