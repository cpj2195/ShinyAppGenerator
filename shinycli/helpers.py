#!/usr/bin/env python

import errno
import glob
import json
import os

import shinycli.constants as cnst


def recursive_search(directory_path):
    """
    This function seraches for the file glob which matches to that of
    the shiny state file.

    Arguments:
    directory_path {str} -- The directory in which you want to search the
                                state file recursively.
    Return:
    file_exists {bool} -- If the state file exists or not.

    state_path {str} -- the path to your state file
    """
    file_exists = False
    state_path = ""
    state_file_glob = directory_path + '/.shiny' + '/.shiny-state'
    for filepath in glob.iglob(state_file_glob):
        if filepath:
            state_path = filepath
            file_exists = True
            return file_exists, state_path
    return file_exists, state_path


def search_state_file(present_directory):
    """
    This function splits the input directory from the
    end with '/' and paases that path to the recursive_search function.

    Arguments:
    present_directory {str} -- The directory in which you want to search the
                                state file recursively.
    Return:
    app_name {str} -- the name of your shiny app

    state_path {str} -- the path to your state file

    """
    app_name = ""
    state_path = ""
    for i in range(5):
        file_exists, state_path = recursive_search(present_directory)
        present_directory = present_directory.rpartition('/')[0]
        if(file_exists):
            break
    if(file_exists and state_path):
        data = load_from_json(state_path)
        app_name = data.get(cnst.NAME_OF_SHINY_APP)
    return app_name, state_path


def make_folder(folder_name, folder_path):
    """
    This function makes a folder in the given
    directory.

    Arguments:
    folder_name {str} -- The name of the folder which you want
                         to create.

    folder_path {str} -- The path in which you want to create the folder.
    """
    try:
        os.makedirs(folder_path + '/' + folder_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def load_from_json(json_file_path):
    """
    This function loads data from a json File

    Arguments:
    folder_name {str} -- The path to your json file.
    """
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data


def write_to_json(data, json_file_path):
    """
    This function writes data to a json file.

    Arguments:
    data {JSON} -- Data which you want to write to the file.

    json_file_path{str} -- The path to your json file.
    """
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)
