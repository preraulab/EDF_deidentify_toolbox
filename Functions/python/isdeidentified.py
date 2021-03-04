import os


def isdeidentified(filename, verbose=True):
    """ Checks if an EDF is deidentified

    Usage:
        result, haspassed = isdeidentified(filename)
        result, haspassed = isdeidentified(filename, verbose)

    :param filename: (str) file path to edf
    :param verbose: (bool) prints pass/fail for each variable that should be deidentified (default = True)

    :return: result: (bool) True if file is deidentified   /
             haspassed: = (list) List of 3 bools indicating pass/fail for [Patient Info, Recording Info, Start Date]

    Copyright 2021 Michael J. Prerau Laboratory. - http://www.sleepEEG.org
    Author: Michael J. Prerau, Ph.D., Thomas Possidente

    Last modified 03/04/2021
    """

    # Check if invalid file
    if not os.path.isfile(filename):
        raise Exception("Invalid file: " + filename)

    # Open file and try to read relevant info
    f = open(filename, "r", encoding="iso-8859-1")
    try:
        f.read(8)  # read version
        patient_info = str(f.read(80)).strip()  # get patient info
        recording_info = str(f.read(80)).strip()  # get recording info
        startdate = str(f.read(8)).strip()  # get startdate
    except UnicodeDecodeError:
        f.close()
        f = open(filename, "r", encoding="iso-8859-2")
        try:
            f.read(8)  # read version
            patient_info = str(f.read(80)).strip()  # get patient info
            recording_info = str(f.read(80)).strip()  # get recording info
            startdate = str(f.read(8)).strip()  # get startdate
        except UnicodeDecodeError:
            f.close()
            f = open(filename, "r+", encoding="utf-8")
            try:
                f.read(8)  # read version
                patient_info = str(f.read(80)).strip()  # get patient info
                recording_info = str(f.read(80)).strip()  # get recording info
                startdate = str(f.read(8)).strip()  # get startdate
                f.close()
            finally:
                raise Exception('No valid encoding format found')

    patient_info_pass = patient_info == "X X X X"
    recording_info_pass = recording_info == "Startdate X X X X"
    startdate_pass = (startdate == "01.01.01") | (startdate == "00.00.00") | (startdate == "99.99.99")

    result = patient_info_pass & recording_info_pass & startdate_pass
    haspassed = [patient_info_pass, recording_info_pass, startdate_pass]

    if verbose:
        print('Checking ' + filename + ' for de-identification using EDF+ standards:')

        if not patient_info_pass:
            print('     Patient info: FAIL - "' + patient_info + '" must be changed to "X X X X"')
        else:
            print('     Patient info: PASS')

        if not recording_info_pass:
            print('     Recording info: FAIL - "' + recording_info + '" must be changed to "Startdate X X X X"')
        else:
            print('     Recording info: PASS')

        if not startdate_pass:
            print('     Recording info: FAIL - "' + startdate + '" must be changed to "01.01.01"')
        else:
            print('     Recording info: PASS')

    return result, haspassed
