¨¨¨
Goal of this tool:


for all the observatories
  - for all the material-samples in there
     - we need to check if we already have a ena-accession-nr to it
     - if not create ena-sample object to represent it (XML and curl)
     - get the created accession-nr
     - keep known relations between samples and assension-numbers on file


this assumes new files in the sequencing-data repository to work on

  mapping/observatory_ena_proj.csv
  * assession-numbers (ERP-----) for every observatory   --> observatory_ena_proj.csv (2 columns at least) 

  shipment/YYYYMMDD_samples.csv 
  * package-shipment-lists --> files listing the sample-ids included --> 1 col will do

  mapping/material_sample_ena_sample.csv
  * a file managed (mainly by script) linking samples to their accession number (ERS----)   --> material_sample_ena_sample.csv


we are going to apply some templating to generate the XML

we need API descriptions of the services we need to call at ENA

we will assume all needed repositories are available locally and are in sync with github
  (we can later create scripts that help assure that / even do it on the fly)


we postpone thinking about ena-run objects
-- assume genoscope creates those
-- we might need to think about updating them later though


also: check if py libs exist to interact with ena
--> https://pypi.org/project/ena-upload-cli/
--> https://github.com/phe-bioinformatics/ena_submission


the docs for doing the submission are at
https://ena-docs.readthedocs.io/en/latest/submit/general-guide/programmatic.html
https://ena-docs.readthedocs.io/en/latest/submit/samples/programmatic.html

todo -- check if there is some test-environment to try out stuff first
¨¨¨
