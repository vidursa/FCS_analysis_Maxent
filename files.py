import os
import glob
import re

def _only(file_list, keyword):
    """Helper function to returns files from list of files that match the
    items in the keyword.

    Parameters
    ----------
    file_list : list
        List with paths to different files that needs to be filtered.

    keyword : str
        Keyword that is to be used for the filtering criteria.

    Returns
    -------
    list_ : list
        This is the list which has all the elements of file_list after
        filtering with keyword.
    """
    list_ = [_ for _ in file_list if all(key in _ for key in keyword)]
    return sorted(list_)

def _endswith(file_list, keyword):
    """Helper function to returns files from list of files that match the
    items in the keyword.

    Parameters
    ----------
    file_list : list
        List with paths to different files that needs to be filtered.

    keyword : str
        Keyword that is to be used for the filtering criteria.

    Returns
    -------
    list_ : list
        This is the list which has all the elements of file_list after
        filtering with keyword.
    """
    list_ = [_ for _ in file_list if _.endswith(keyword)]
    return list_

def _skip(file_list, keyword):
    """Helper function to returns files from list of files that does not match
    the items in the keyword.

    Parameters
    ----------
    file_list : list
        List with paths to differnt files that needs to be filtered.

    keyword : str
        Keyword that is to be used for the filtering criteria.

    Returns
    -------
    list_ : list
        This is the list which has all the elements of file_list after
        filtering with keyword.
    """
    list_ = [_ for _ in file_list if all(key not in _ for key in keyword)]
    return sorted(list_)


def unique_dirs(list1):
    
    unique_list = [] 
    wbname = []  
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x) 
    for x in unique_list: 
        wbname.append(x)
    return wbname


def get_files(keyword="./", only=None, skip=None):
    """Returns the path to all the files in a path as specified in the
    keyword. If a "*" is detected in the keyword, the file list returned
    makes use of glob to run the search.

    Parameters
    ----------
    keyword : str, optional
        Keyword that specifies the path to images.

    only : list, optional
        List of secondary keywords to filter file names. Only filenames with
        these keywords will be returned.

    skip : list, optional
        List of secondary keywords to filter file names. Only filenames that
        do not have these keywords will be returned.

    Returns
    -------
    file_list : list
        List of files that match the keyword, and the only and skip criteria.
    """
    if "*" in keyword:
        return sorted(glob.glob(keyword))

    file_list = []
    for paths, subdirs, files in os.walk(keyword):
        for name in files:
            file_list.append(os.path.join(paths, name))

    if only is not None:
        file_list = _only(file_list, only)

    if skip is not None:
        file_list = _skip(file_list, skip)

    return sorted(file_list)

def grouping(file_list):
    folder_iter = []
    a = []
    for i in iter(file_list):
        a.append(i.rsplit('\\',3)[1])
    genotype = unique_dirs(a)
    for _ in range(len(genotype)):
        regex=re.compile(".*("+genotype[_]+").*")
        folder = [m.group(0) for l in file_list for m in [regex.search(l)] if m ]
        folder_iter.append(folder)
    return folder_iter

def mkdir(path):
    """Function to make a directory.

    Parameters
    ----------
    path : str
        The path for which the function checks if the folder exists, and makes
        a directory if it does not.
    """

    if not os.path.exists(path):
        os.makedirs(path)
    return
