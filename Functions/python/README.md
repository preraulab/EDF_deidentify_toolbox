## Prerau Lab Python functions for Deidentifying EDF files
---

<img class="alignnone size-full wp-image-1590" src="https://prerau.bwh.harvard.edu/wp-content/uploads/2021/02/Splash-noversion.png" alt="" width="960" height="342" />
<br/>


## Table of Contents
* [General Information](#general-information)
* [Usage](#usage)
* [Example](#example)
* [Status](#status)
* [Contact](#contact)

<br/>


## General Information
<a href="https://www.edfplus.info/" target="_blank" rel="noopener">European Data Format (EDF)</a> is one of the primary ways polysomnography and EEG data are stored. De-identification of EDF files is a necessary step for safe sharing of data, removing any identifying information from the file headers. Often EDF de-identification tools are part of some larger toolbox or software package, making distribution to clinical sites and personnel more difficult.

Here we provide [standalone GUI-based programs](#deidentifier-standalone-program) for PC, Mac, and Linux as well as [functional source code](#deidentification-functions) in MATLAB and python to facilitate de-identification of EDF files.
The program overwrites the following header data fields:

<code>Patient Info</code>: Overwrites with "X X X X"

<code>Patient Recording Info</code>: Overwrites with "Startdate X X X X"

<code>Date</code>: Overwrites with 01.01.01

Note: There is currently no standard for de-identification of the StartDate field under EDF/EDF+ specifications. We have chosen to use 01.01.01 since it will not return an error for readers or viewers that verify date validity. 

This format is designed to retain compliance with <a href="https://www.edfplus.info/specs/edfplus.html">EDF+ specification standards</a>.

<br/>

## Usage

```
edf_deidentfy(path)
edf_deidentfy(path, save_dir)
edf_deidentfy(path, save_dir, overwrite)
```

<br/>

## Example

```
# Import edf_deidentify and isdeidentified functions
from EDFdeidentify_function import edf_deidentify
from isdeidentified import isdeidentified

# Import os for path name transformation
import os 

path = '../../test.edf'  # path test.edf in main repo directory
save_dir = '.' # directory to current directory
overwrite = False  # Don't overwrite original file

# Check if .edf is deidentified
isdeidentified(path)

# Deidentify
edf_deidentify(path, save_dir, overwrite)

# Check deidentified file to make sure it is deidentified
isdeidentified(save_dir + '/' + os.path.basename(path)[0:-4] + '_deidentified.edf')

```

<br/>

## Status
All implementations are complete and functional but may receive updates occasionally 

<br/>

## Contact
For questions or suggestions please contact Thomas Possidente at tpossidente@bwh.harvard.edu 
