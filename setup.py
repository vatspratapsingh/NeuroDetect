from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="neurodetect",
    version="1.0.0",
    author="Vats Pratap Singh",
    author_email="vatspratapsingh@gmail.com",
    description="Machine Learning project for Parkinson's Disease detection using voice analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vatspratapsingh/NeuroDetect",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    keywords="machine-learning, healthcare, parkinsons-disease, voice-analysis, medical-diagnosis, neurodetect",
    project_urls={
        "Bug Reports": "https://github.com/vatspratapsingh/NeuroDetect/issues",
        "Source": "https://github.com/vatspratapsingh/NeuroDetect",
        "Documentation": "https://github.com/vatspratapsingh/NeuroDetect#readme",
    },
)
