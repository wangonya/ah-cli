from setuptools import setup, find_packages

setup(
        name="ah-cli",
        version="0.1",
        py_modules=find_packages(),
        include_package_data=True,
        install_requires=[
            "Click",
            "requests",
            "halo",
            "pytest",
            "pytest-cov",
            "coveralls",
            ],
        entry_points="""
        [console_scripts]
        ah=app:cli
        """,
        )
