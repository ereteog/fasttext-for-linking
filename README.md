# fasttext-for-linking

# Introduction

This repository offer a REST API over the [fastText](https://github.com/facebookresearch/fastText) Python implementation. This app offers the possibility to compare two set of words in as much language as fastText can offer. The app has been design especially for doing entity linking.

# Python Packages and Requirements

* Python 2.7
* Pip
* gensim 2.0.0
* fastText 0.8.3
* numpy 1.12.1
* flask 0.12.1
* spacy 1.7.5

# Installation

Pip command line to install to be able to run the API:

```
pip install gensim fasttext flask spacy
```

# Usage

```
usage: fasttext_app [-h] -l LANGUAGE -m MODEL -p PORT [--version]

Webapp for entity linking using fastText in a given language

optional arguments:
  -h, --help            show this help message and exit
  -l LANGUAGE, --language LANGUAGE
                        Set the language
  -m MODEL, --model MODEL
                        Set the fastText model
  -p PORT, --port PORT  Set the port
  --version             show program's version number and exit
```

# Docker

Compile the English image:

```
docker build -t jplu/fasttext-en -f en/Dockerfile .
```

Run a container from the English image:

```
docker run -d -p 5000:5000 --name fasttest-english jplu/fasttext-en
```

# Opening an issue

If you find a bug, have trouble following the documentation or have a question about the project you can create an issue. Whatever issue you’re having, you’re likely not the only one, so others will find your issue helpful, too. To open an issue:

* Please, check before to see if not someone else has not already had the same issue.
* Be clear in detailing how to reproduce the bug.
* Include system details.
* In case it is an error, paste the error output.

# Team

Owner: Julien Plu (@jplu)

Maintainers and Collaborators:

* Julien Plu (main contact) ([@jplu](https://github.com/jplu))
* Giuseppe Rizzo ([@giusepperizzo](https://github.com/giusepperizzo))
* Raphaël Troncy ([@rtroncy](https://github.com/rtroncy))

# Licence

All the content of this repository is licensed under the terms of the Apache v2 license.
