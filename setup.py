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
            "pytest"
            ],
        entry_points="""
        [console_scripts]
        ah=app:main
        """,
        )
