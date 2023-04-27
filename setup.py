import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="snake-logger-DarthFener", # Ovviamente, metti il tuo nome ;)
    version="0.0.1",
    author="Francesco Cesare Giorgio Teseo Bosatra",
    author_email="francescocesare.bosatra@mail.polimi.it",
    description="Pacchetto per gestire log di programmi python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DarthFener/6sv-logger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)