#!/usr/bin/env python

import os
from pathlib import Path

import shinycli.constants as cnst
import shinycli.helpers as hlp
from shinycli.logging_utils import logger


class CreateShinyAlgo:

    def __init__(self, algo_name):
        self.algo_name = algo_name

    def make_algo_file(self, shiny_path, algo_name):
        """
        Creates an algorithm file in the algorithms folder with the
        name of the file being the same as that of the algorithm provided by
        the user and also creates a function in the same file of the same name.

        Arguments:
            shiny_path {str} -- The path to your shiny app.
            algo_name {str} -- The name of the algorithm you want to add.

        """

        if not os.path.isfile(shiny_path + '/algorithms/' + algo_name + '.R'):
            Path(shiny_path + '/algorithms/' + algo_name + '.R').touch()
        else:
            logger.error(cnst.SAME_ALGORITHM_EXISTS)
            return
        algo_path = os.path.realpath(
            shiny_path + '/algorithms/' + algo_name + '.R')
        documentation_template = """
        #########################################################################
        #####                                                               #####
        #####   PLEASE WHEN IMPORTING ANYTHING, USE RELATIVE PATHS INSTEAD  #####
        #####                   OF ABSOLUTE PATHS.                          #####
        #####                                                               #####
        #########################################################################
        \n
        """
        function_template = """
        # Explain what the function does ...
        #' @param1 ....
        #' @param2 ...
        #'
        #' @return ...
        %s <- function(param1 , param2) { \n }""" % algo_name
        with open(algo_path, "r+") as file_pointer:
            file_pointer.write(documentation_template)
            file_pointer.write(function_template)

    def create_algo_template(self):
        """
        The entry point function to create an algorithm template
        after searching for the shiny state file and getiing the app_name
        and making the algorithm file in the required folder.
        """
        if (not self.algo_name):
            logger.error(cnst.GIVE_ALGORITHM_NAME)
        else:
            shiny_app_name, state_file_path = hlp.search_state_file(
                os.getcwd())
            if(shiny_app_name and state_file_path):
                shiny_app_dir = state_file_path.split(
                    shiny_app_name)[0] + shiny_app_name
                if not os.path.exists(shiny_app_dir + "/algorithms"):
                    logger.error(cnst.NO_ALGORITHMS_FOLDER)
                else:
                    self.make_algo_file(shiny_app_dir, self.algo_name)
            else:
                logger.error(cnst.NOT_IN_SHINY_APP)
