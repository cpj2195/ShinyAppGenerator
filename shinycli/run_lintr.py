#!/usr/bin/env python

import os
import subprocess
from pathlib import Path

import shinycli.constants as cnst
import shinycli.helpers as hlp
from shinycli.logging_utils import logger


class RunRLintr:

    def __init__(self, file_name):
        self.file_name = file_name
  

    def run_R_lintr(self):
        commands = """
        R --no-save<<EOF
        library(lintr)
        lint("{}",,with_defaults(line_length_linter = line_length_linter(120),camel_case_linter = NULL))

        EOF""".format(self.file_name).encode()
        process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        out, err = process.communicate(commands)
        print(out.decode())
        print(err)

