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

You may also run the same using gunicorn.

```shell
gunicorn libindic.web:app
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

The following modules are available under libindic:

* [Soundex](https://github.com/libindic/soundex)
* [ApproxSearch](https://github.com/libindic/inexactsearch)
* [Transliteration](https://github.com/libindic/Transliteration)
* [Spellchecker](https://github.com/libindic/spellchecker)
* [Hyphenation](https://github.com/libindic/Hyphenation)
* [Chardetails](https://github.com/libindic/chardetails)
* [Payyans](https://github.com/libindic/payyans)
* [Text Similarity](https://github.com/libindic/text-similarity)
* [N Gram](https://github.com/libindic/indicgram)
* [Sort](https://github.com/libindic/ucasort)
* [Indic Stemmer](https://github.com/libindic/indicstemmer)
* [Katpayadi Numbers](https://github.com/libindic/Katapayadi)
* [shingling](https://github.com/libindic/shingling)
* [Indic-fortune](https://github.com/libindic/indicfortune)
* [scriptrender](https://github.com/libindic/scriptrender)

Modules to be used with libindic can be configured in the app.conf
file. Modules marked 'yes' should be installed before running SILPA
