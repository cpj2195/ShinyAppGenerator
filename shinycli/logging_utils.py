#!/usr/bin/env python

import logging
logger = logging.getLogger('Shiny-Logger')
# create the console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


console_handler.setFormatter(formatter)