import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygame-builder",
    version="0.0.1",
    author="Aaryan Dehade",
    author_email="aaryandehade@adehade.tech",
    description="A package to build games with ease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dehadeaaryan/pygame-builder",
    project_urls={
        "Bug Tracker": "https://github.com/dehadeaaryan/pygame-builder/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)