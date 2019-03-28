#!/usr/bin/env python

import os
import subprocess
from pathlib import Path

import shinycli.constants as cnst
import shinycli.helpers as hlp
from shinycli.logging_utils import logger


class RunShinyApp:

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
    

    def run_shiny_app(self):
        commands = '''
        R --no-save<<EOF
        library(shiny)
        runApp("{}")

        EOF'''.format(self.shiny_app_dir).encode()
        print(commands)
        logger.warn("in function -----")

        process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        logger.warn("after function -----")

        out, err = process.communicate(commands)
        print(out.decode())
        # print(err)
        # logger.warn("out")

