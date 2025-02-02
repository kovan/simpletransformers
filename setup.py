from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="simpletransformers",
    version="0.64.5",
    author="Thilina Rajapakse",
    author_email="chaturangarajapakshe@gmail.com",
    description="An easy-to-use wrapper library for the Transformers library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThilinaRajapakse/simpletransformers/",
    packages=find_packages(),
    scripts=["bin/simple-viewer"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "requests",
        "tqdm>=4.47.0",
        "regex",
        "transformers>=4.31.0",
        "datasets",
        "scipy",
        "scikit-learn",
        "seqeval",
        "tensorboard",
        "tensorboardx",
        "pandas",
        "tokenizers",
        "wandb>=0.10.32",
        "streamlit",
        "sentencepiece",
        "torch-directml"
    ],
)
