## Prerau Lab Matlab and Python functions for Deidentifying EDF files

[European Data Format](https://www.edfplus.info/) (EDF) is one of the primary ways polysomnography and EEG data are stored. De-identification of EDF files is a necessary step for safe sharing of data, removing any identifying information from the file headers. Often EDF de-identification tools are part of some larger toolbox or software package, making distribution to clinical sites and personnel more difficult. Here we provide a standalone program as well as code to facilitate de-identification of EDF files.

This code overwrite the following header data fields:  
Patient Info: overwrites with “DEIDENTIFIED”  
Patient Recording Info: overwrites with “DEIDENTIFIED”  
Date: overwrites with 01.01.01  
