# emobon-dm-tools
collection of scripts and tricks that help automate collecting / formatting / checking  the data from the obervatories


List of tools

| code | name        | purpose                                                                                    |
|------|-------------|--------------------------------------------------------------------------------------------|
| gg   | google-get  | gets csv content from the managed google-documents                                         |
| ena  | ena         | creates / updates / gets info from objects in the ENA database                             | 


Usage of specific tools is explained in detail below

## google-get

``` bash
python -m pyedm.gg -g ../observatory-BPNS

```


## ena-sync 
``` bash
pythin -m pyedm.ena  -s ../sequencing-data/shipment/2022-07-14_samples.csv
```

