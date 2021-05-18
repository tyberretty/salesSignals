from setuptools import find_packages, setup


setup(
    name="salesSignals",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=1,
    description="salesSignals",
    author="",
)
