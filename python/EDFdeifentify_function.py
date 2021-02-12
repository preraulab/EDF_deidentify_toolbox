import os
import shutil


def edf_deidentify(path, save_dir=None, overwrite=False):
    """ Deidentifies a given edf file (removes patient info and recording info)

    :param path: path to edf file to be deidentified
    :param save_dir: directory to save deidentified copy of edf (default is directory of edf file)
    :param overwrite: replace the edf file given with the deidentified file (default = False) (Note: if True, ignores
                      save_dir)

    :return: None
    """

    # If no save_dir provided, use dir of edf file
    if save_dir is None:
        save_dir = os.path.dirname(path)
    else:  # check if save_dir is valid
        if not os.path.isdir(save_dir):
            raise Exception("Invalid save_dir path: " + save_dir)

    # Check if invalid file
    if not os.path.isfile(path):
        raise Exception("Invalid file: " + path)

    # Copy file to new name
    if not overwrite:
        path_new = save_dir + '/' + os.path.basename(path)[0:-4] + '_deidentified.edf'
        shutil.copy(path, path_new)
        path = path_new

    # Open file(s) and deidentify
    f = open(path, "r+", encoding="iso-8859-1")  # 'r' = read
    try:
        f.write('%-8s' % "0")
        f.write('%-80s' % "DEIDENTIFIED")  # Remove patient info
        f.write('%-80s' % "DEIDENTIFIED")  # Remove recording info
        f.write('01.01.01')  # Set date as 01.01.01
    except UnicodeDecodeError:
        f.close()
        f = open(path, "r+", encoding="iso-8859-2")  # 'r' = read
        try:
            f.write('%-8s' % "0")
            f.write('%-80s' % "DEIDENTIFIED")  # Remove patient info
            f.write('%-80s' % "DEIDENTIFIED")  # Remove recording info
            f.write('01.01.01')  # Set date as 01.01.01
        except UnicodeDecodeError:
            f.close()
            f = open(path, "r+", encoding="utf-8")  # 'r' = read
            try:
                f.write('%-8s' % "0")
                f.write('%-80s' % "DEIDENTIFIED")  # Remove patient info
                f.write('%-80s' % "DEIDENTIFIED")  # Remove recording info
                f.write('01.01.01')  # Set date as 01.01.01
                f.close()
            finally:
                raise Exception('No valid encoding format found')

    return
