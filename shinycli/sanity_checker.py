#!/usr/bin/env python

import glob
import os
import pathlib
import re
from pathlib import Path

import constants as cnst
import helpers as hlp
from logging_utils import logger
from tree import DisplayablePath


class SanityChecker:

    def __init__(self):
        self.shiny_app_name, self.state_path = hlp.search_state_file(
            os.getcwd())
        if(not self.state_path):
            self.shiny_app_dir, self.algos_folder = "", ""
            logger.error(cnst.NOT_IN_SHINY_APP_OR_NO_STATE_FILE)
        elif(self.shiny_app_name and self.state_path):
            self.shiny_app_dir = self.state_path.split(self.shiny_app_name)[
                0] + self.shiny_app_name
            self.algos_folder = self.shiny_app_dir + cnst.ALGORITHMS_FOLDER

    def check_folder_structure(self):
        """
        This function checks if the folder and files exists or not.
        for eg, it checks if the algorithms folder,tests folder exists.

        """
        if(self.shiny_app_dir and self.algos_folder):
            shiny_app = pathlib.Path(self.shiny_app_dir)
            algos = pathlib.Path(self.algos_folder)
            data_folder = pathlib.Path(self.shiny_app_dir + cnst.DATA_FOLDER)
            readme_file = pathlib.Path(self.shiny_app_dir + '/Readme.md')
            server_file = pathlib.Path(self.shiny_app_dir + '/server.R')
            ui_file = pathlib.Path(self.shiny_app_dir + '/ui.R')
            tests_folder = pathlib.Path(self.shiny_app_dir + '/tests')
            folder_file_list = [shiny_app, algos, data_folder,
                                readme_file, server_file, ui_file, tests_folder]
            for file_folder in folder_file_list:
                if not file_folder.exists():
                    logger.warn(
                        '%s does not exists.Please first create it', file_folder)

    def check_directory_structure(self):
        """
        This function checks if the "CORRECT" folder structure is follwed in
        the shiny app.

        """

        if(self.shiny_app_dir and self.algos_folder):
            correct_shiny_directory = [
                'algorithms', 'ui.R', 'server.R', 'Readme.md', 'tests', '.shiny']
            actual_directory = os.listdir(self.shiny_app_dir)
            state_file_glob = self.shiny_app_dir + cnst.SHINY_STATE_FILE
            for filepath in glob.iglob(state_file_glob):
                if not filepath:
                    logger.error(cnst.NO_SHINY_STATE_FILE)
            if set(actual_directory) != set(correct_shiny_directory):
                logger.warn(cnst.INCORRECT_FOLDER_STRUCTURE)

    def check_algos_folder(self):
        """
        This function checks if the algorithms folder has only .R files
        and the data folder has no .R files in it.
        """
        if self.shiny_app_dir and self.algos_folder:
            data_folder = self.shiny_app_dir + cnst.DATA_FOLDER
            if(os.path.exists(self.algos_folder)):
                for file in os.listdir(self.algos_folder):
                    if os.path.isfile(file) and not file.endswith(".R"):
                        logger.warn(cnst.INCLUDE_R_FILES_IN_ALGORITHMS)

            if(os.path.exists(data_folder)):
                for file in os.listdir(data_folder):
                    if file.endswith(".R"):
                        logger.warn(cnst.NO_R_FILES_IN_DATA_FOLDER)

    def tell_exposed_algonames(self):
        """
        This function will tell what algorithms will be exposed as an endpoint
        finally when deployed. Also it checks if the algorithm scripts do not
        have any imports of ui.R and server.R
        """
        if self.shiny_app_dir and self.algos_folder:
            for file in os.listdir(self.algos_folder):
                if file.endswith(".R"):
                    file_name = file.split('.')[0]
                    my_regex = re.compile(
                        file_name + r'[ ]+(<-)[ ]+(function)')
                    ui_regex = re.compile(r'ui.R')
                    server_regex = re.compile(r'server.R')
                    with open(self.algos_folder + '/' + file, 'r') as myfile:
                        r_code = myfile.read()
                        result = re.search(my_regex, r_code)
                        ui_result = re.search(ui_regex, r_code)
                        server_result = re.search(server_regex, r_code)
                        if(result is not None):
                            logger.info(
                                "%s will be exposed finally as an Algorithm\n", file_name)
                        else:
                            logger.info(
                                "%s will not be exposed as an Algorithm \n", file_name)
                        if(ui_result or server_result):
                            logger.error(
                                "%s has server.R or ui.R imported. Please remove it and resolve the dependency \n", file_name)

    def print_current_structure(self, directory):
        """
        Prints the directory structure of the input parameter
        directory.Similar to tree command in linux.
        Arguments:
            directory {str} -- The path for which you want to print the
                                directory tree.
        """
        paths = DisplayablePath.make_tree(Path(directory))
        if(self.state_path):
            logger.info("Your current Folder Structure looks like \n")
            for path in paths:
                print(path.displayable())


def run_checker():
    """
    Entry point function the sanity checker which will make a Sanity
    checker object and call all the methods.
    """
    sanity_object = SanityChecker()
    sanity_object.check_folder_structure()
    sanity_object.check_directory_structure()
    sanity_object.check_algos_folder()
    sanity_object.tell_exposed_algonames()
    sanity_object.print_current_structure(sanity_object.shiny_app_dir)
