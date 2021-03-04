function [out, haspassed] = isdeidentified(filename, verbose)
%ISDEIDENTIFIED  Checks if an EDF file is deidentified
%
%   Usage:
%   Direct input:
%       [out, haspassed] = isdeidentified(filename, verbose)
%
%   Input:
%       filename: string - file name
%       verbose: logical - prints pass/fail for each record
%
%   Output:
%       out: logical - true if deidentified
%       haspassed: 1x3 logical - pass/fail for [Patient Info, Recording Info, Start Date]
%
%   Copyright 2021 Michael J. Prerau Laboratory. - http://www.sleepEEG.org
%   Author: Michael J. Prerau, Ph.D.
%
%   Last modified 03/03/2021
%% ********************************************************************
%Set verbose to true for default
if nargin<2
    verbose = true;
end

fid = fopen(filename); %Open file
fread(fid,8,'char'); %Read version

%Imporant fields
patient_info = deblank(char(fread(fid,80,'char')')); %Read patient info
recording_info = deblank(char(fread(fid,80,'char')')); %Read recording info
start_date = deblank(char(fread(fid,8,'char')')); %Read start data
fclose(fid); %Close file

%Check if de-identified
patient_ok = strcmpi(patient_info, 'X X X X');
info_ok = strcmpi(recording_info, 'Startdate X X X X');
date_ok = strcmpi(start_date, '01.01.01') || strcmpi(start_date, '00.00.00');

%See if all fields pass
out = patient_ok && info_ok && date_ok;

%Output vector
haspassed = [patient_ok  info_ok  date_ok];

%Output results to command line
if verbose
    disp(['Checking ' filename ' for de-identification using EDF+ standards:']);
    
    if ~patient_ok
        disp(['     Patient info: FAIL - ''' patient_info ''' must be changed to ''X X X X''']);
    else
        disp('     Patient info: PASS');
    end
    
    if ~info_ok
        disp(['     Recording info: FAIL - '''  recording_info  ''' must be changed to ''Startdate X X X X''']);
    else
        disp('     Recording info: PASS');
    end
    
    if ~date_ok
        disp(['     Recording info: FAIL - ''' start_date ''' must be changed to ''01.01.01''']);
    else
        disp('     Recording info: PASS');
    end
    disp(' ');
end