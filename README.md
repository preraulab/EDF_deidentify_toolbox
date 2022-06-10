## Prerau Lab Matlab and Python functions for Deidentifying EDF files
---

<img class="alignnone size-full wp-image-1590" src="https://prerau.bwh.harvard.edu/wp-content/uploads/2021/02/Splash-noversion.png" alt="" width="960" height="342" />
<br/>


## Table of Contents
* [General Information](#general-information)
* [Standalone GUI Program](#deidentifier-standalone-program)
* [Functions](#deidentification-functions)
* [Installation Instructions](#installation-instructions)
* [GUI Usage Instructions](#gui-usage-instructions)
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

## Deidentifier Standalone Program

The python code used to create these standalone GUI programs is available in the "GUI" folder. Let us know if you use this code to compile a standalone GUI for an OS other than Mac, PC, or Linux, we would love to add it to what we have available.

Download standalone programs for:

<a href="#windows_install">

<button class="download"><img class="alignnone size-full wp-image-1513" src="https://prerau.bwh.harvard.edu/wp-content/uploads/2021/02/os-windows8-16.png" alt="" width="16" height="16" /> Windows

</button></a><a href="#mac_install"><button class="download"><img class="alignnone size-full wp-image-1512" src="https://prerau.bwh.harvard.edu/wp-content/uploads/2021/02/mac-os-16.png" alt="" width="16" height="16" /> Mac
  
</button></a><a href="https://prerau.bwh.harvard.edu/edf_deidentify/EDFdeidentify_linux_v2"><button class="download"><img class="alignnone size-full wp-image-1511" src="https://prerau.bwh.harvard.edu/wp-content/uploads/2021/02/linux-16.png" alt="" width="16" height="16" /> Linux</button></a>

<a href="#instructions">Click here for instructions on how to use EDF De-Identifier</a>
<a id="sourcecode"></a>

<br/>

## Deidentification Functions

The Matlab and Python implementations of the de-identification function are available in the "Functions" folder. For more information and example code visit the [matlab](https://github.com/preraulab/EDF_deidentify_toolbox/tree/master/Functions/matlab) or [python](https://github.com/preraulab/EDF_deidentify_toolbox/tree/master/Functions/python) subfolder.

Source code for EDF de-identification functions are available for direct download here:

<a href="https://prerau.bwh.harvard.edu/edf_deidentify/EDF_deidentify.m"><button class="download">Matlab Code
  
</button></a><a href="https://prerau.bwh.harvard.edu/edf_deidentify/EDFdeifentify_function.py"><button class="download">Python code
  
<br/>

## Installation Instructions
<a id="mac_install"></a>
<h3>Mac:</h3>
<a href="https://prerau.bwh.harvard.edu/edf_deidentify/EDF_deidentifier_Installer_mac.dmg">Download the .dmg file</a> and open it up. Drag the icon to the Applications folder shortcut:
<img class=" wp-image-1633 aligncenter" src="https://prerau.bwh.harvard.edu/wp-content/uploads/2021/02/Screen-Shot-2021-02-24-at-11.17.31-AM.png" alt="" width="429" height="431" />
<h4><strong>IMPORTANT: </strong>As this program is not hosted through the app store, <span style="color: #ff0000;"><strong>you must go to the applications folder and CONTROL-click the EDF De-Identifier application icon it the first time you open it. </strong> </span></h4>

<span style="color: #ff0000;"><span style="color: #000000;">If you see the following error:

<img class=" wp-image-1639 aligncenter" src="https://prerau.bwh.harvard.edu/wp-content/uploads/2021/02/Screen-Shot-2021-02-24-at-11.55.24-AM.png" alt="" width="290" height="315" /></span></span>

Select <strong>Cancel</strong>, navigate to the Applications folder, <strong>hold down control</strong>, then click on the <em>EDF De-Identifier</em> application icon.
After control-clicking on the app, you will then see the following window:

<img class=" wp-image-1634 aligncenter" src="https://prerau.bwh.harvard.edu/wp-content/uploads/2021/02/Screen-Shot-2021-02-24-at-11.16.58-AM.png" alt="" width="257" height="376" />

Click on <strong>Open</strong> and the application should open, with no further issue on subsequent use.
<a id="windows_install"></a>

<br/>
&nbsp;


<h3>Windows</h3>
Download the <a href="https://prerau.bwh.harvard.edu/edf_deidentify/EDF_deidentifier_installer_windows_v2.zip">installer</a> and open it, then this window will pop up. Select <strong>More info</strong>.

&nbsp;

<img class="wp-image-1706 size-medium aligncenter" src="https://prerau.bwh.harvard.edu/wp-content/uploads/2021/02/windowsw-300x279.png" alt="" width="300" height="279" />

Click <strong>Run anyway</strong>

<img class="size-medium wp-image-1682 aligncenter" src="https://prerau.bwh.harvard.edu/wp-content/uploads/2021/02/window2-300x280.png" alt="" width="300" height="280" />

Then select where you would like to place the .exe icon in the file dialogue window and the application will be installed there.
<a id="instructions"></a>

<br/>
&nbsp;

## GUI Usage Instructions
Upon running the application, the following window should appear:

<img class=" wp-image-1636 aligncenter" src="https://prerau.bwh.harvard.edu/wp-content/uploads/2021/02/Screen-Shot-2021-02-24-at-11.36.04-AM.png" alt="" width="589" height="252" />

Select <strong>Choose File(s)</strong> and a file dialog will pop up. Select all the file or files that you are interested in de-identifying.
Then the following window will appear:

<img class="wp-image-1637 aligncenter" src="https://prerau.bwh.harvard.edu/wp-content/uploads/2021/02/Screen-Shot-2021-02-24-at-11.39.41-AM.png" alt="" width="282" height="299" />

Selecting <strong>Yes</strong> will create a duplicate copies of your EDF files with the suffix '_deidentifed' added to the end. For example: <code>recording001.edf</code> will be renamed <code>recording001_deidentified.edf</code>.
Selecting <strong>No</strong> will directly overwrite the data in the files.

<br/>

## Status
All implementations are complete and functional but may receive updates occasionally 

<br/>

## Contact
For questions or suggestions please contact Thomas Possidente at tpossidente@bwh.harvard.edu 
