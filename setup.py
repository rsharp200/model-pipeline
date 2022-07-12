import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="object_detection_model",
    version="0.0.23",
    author="Andrea Lowe",
    author_email="andrea.lowe@dominodatalab.com",
    description="Seabed-Object-Detection",
    long_description="Model to identify objects on seabed",
    long_description_content_type="text/markdown",
    url="https://github.com/andrealowe/cmodel-pipeline",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
