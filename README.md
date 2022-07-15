# emobon-dm-tools
collection of scripts and tricks that help automate collecting / formatting / checking  the data from the obervatories


List of tools

| code | name        | purpose                                                                                    |
|------|-------------|--------------------------------------------------------------------------------------------|
| gg   | google-get  | gets csv content from the managed google-documents                                         |
| ena  | ena         | creates / updates / gets info from objects in the ENA database                             | 


## install & dependencies

These tools have not been published yet so using them requires a local git checkout of the source, a virtualenv to work in, and then a straightforward install into that.

On windows we recommend having gitbash around to execute this. Gitbash is part of [git-scm](https://git-scm.com/downloads)

* open a bash terminal
* double check if you have python there:
```bash
$ python --version
```

* get the source code for the project - and enter the project

```bash
$ git clone git@github.com:emo-bon/emobon-dm-tools.git
$ cd emobon-dm-tools
```

* create a virtualenv and activate it

```bash
$ virtualenv venv -p python3
$ source ./${venv}/bin/activate
```

* install the tools and check

```bash
$ make init-dev
$ python -m pydem --help
```


## usage 

Usage of specific tools is explained in detail below

### google-get

``` bash
python -m pyedm.gg -g ../observatory-BPNS

```


### ena-sync 
``` bash
pythin -m pyedm.ena  -s ../sequencing-data/shipment/2022-07-14_samples.csv
```

