## Prerau Lab Matlab and Python functions for Deidentifying EDF files
---

<br/>

![alt text](https://prerau.bwh.harvard.edu/images/Splash-noversion.png)

<br/>

[European Data Format (EDF)](https://www.edfplus.info/) is one of the primary ways polysomnography and EEG data are stored. De-identification of EDF files is a necessary step for safe sharing of data, removing any identifying information from the file headers. Often EDF de-identification tools are part of some larger toolbox or software package, making distribution to clinical sites and personnel more difficult.

Here we provide functional source code in MATLAB and python to facilitate de-identification of EDF files.
The functions overwrite the following header data fields:  
```Patient Info:``` Overwrites with “X X X X”  
```Patient Recording Info:``` Overwrites with “Startdate X X X X”  
```Date:``` Overwrites with 01.01.01  
This format is designed to retain compliance with [EDF+ specification standards](https://www.edfplus.info/specs/edfplus.html).

<br/>
<br/>

Standalone GUI-based EDF de-identification programs for PC, Mac, and Linux are available on the Prerau Lab website - [http://sleepeeg.org/edf-de-identification-tool](http://sleepeeg.org/edf-de-identification-tool)
