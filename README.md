# Libindic web

This is the web interface for libindic librarires, developed to provide an easy way to try out the features.

## Installation

Clone this repository, and prepare a virtual envirorment

```shell
python -m venv ENV_DIR
```

And activate it using

```shell
source ENV_DIR/bin/activate
```

Install all the required libraries

```shell
pip install -r requirements.txt
```

Run the webserver

```shell
flask run
```

### System Dependencies

For the script rendered module, there is a dependecy on some system libraries.
`Pango` and `cairo` can not be installed with pip and need to be installed
from your platform’s packages. `lxml` and `CFFI` can, but you’d still need
their own dependencies. This section lists system packages for lxml or
CFFI when available, the dependencies otherwise. lxml needs `libxml2`
and `libxslt`, CFFI needs `libffi`. On Debian, the package names with
development files are `libxml2-dev`, `libxslt1-dev` and `libffi-dev`.

#### Debian and Ubuntu

```shell
sudo apt-get install python-dev python-pip python-lxml libcairo2 \
     libpango1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

#### Fedora

```shell
sudo yum install python-devel python-pip python-lxml cairo pango gdk-pixbuf2\
   libffi-devel
```

#### Archlinux

```shell
sudo pacman -S python-pip python-lxml cairo pango gdk-pixbuf2
```

#### Mac OS X

##### With Macports

```shell
sudo port install py27-pip py27-lxml cairo pango gdk-pixbuf2 libffi
```

##### With Homebrew

```shell
brew install python cairo pango gdk-pixbuf libxml2 libxslt libffi
```

## Modules

The following modules are available for SILPA:

* [Soundex](https://github.com/Project-SILPA/soundex)
* [ApproxSearch](https://github.com/Project-SILPA/inexactsearch)
* [Transliteration](https://github.com/Project-SILPA/Transliteration)
* [Spellchecker](https://github.com/Project-SILPA/spellchecker)
* [Hyphenation](https://github.com/Project-SILPA/Hyphenation)
* [Chardetails](https://github.com/Project-SILPA/chardetails)
* [Payyans](https://github.com/Project-SILPA/payyans)
* [Text Similarity](https://github.com/Project-SILPA/text-similarity)
* [N Gram](https://github.com/Project-SILPA/indicgram)
* [Silpa Sort](https://github.com/Project-SILPA/ucasort)
* [Indic Stemmer](https://github.com/Project-SILPA/indicstemmer)
* [Katpayadi Numbers](https://github.com/Project-SILPA/Katapayadi)
* [shingling](https://github.com/Project-SILPA/shingling)
* [Indic-fortune](https://github.com/Project-SILPA/indicfortune) now renamed silpa-fortune
* [scriptrender](https://github.com/Project-SILPA/scriptrender)

Modules to be used with SILPA can be configured in the silpa.conf
file. Modules marked 'yes' should be installed before running SILPA
