import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="pygame_builder",
    version="0.1.4",
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