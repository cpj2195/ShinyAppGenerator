#!/usr/bin/env python

from cliff.command import Command
from create_app import CreateShinyApp
from create_algo import CreateShinyAlgo
from sanity_checker import run_checker
from runshiny_app import RunShinyApp


class Makeshiny(Command):
    "Command to scaffold a base shiny app with a set structure."

    def get_parser(self, prog_name):
        parser = super(Makeshiny, self).get_parser(prog_name)
        parser.add_argument('app', nargs='?', default="myshinyapp")
        return parser

    def take_action(self, parsed_args):
        shiny_app_obj = CreateShinyApp(parsed_args.app)
        shiny_app_obj.make_shiny_app()


class MakeAlgo(Command):
    """Command to create an algorithm file and a function in that file
    of the same name as the algorithm"""

    def get_parser(self, prog_name):
        parser = super(MakeAlgo, self).get_parser(prog_name)
        parser.add_argument('algo', nargs='?')
        return parser

    def take_action(self, parsed_args):
        shiny_algo_obj = CreateShinyAlgo(parsed_args.algo)
        shiny_algo_obj.create_algo_template()
        

class SanityCheck(Command):
    """Command which checks the sanity of your shiny app among other things 
     like if your are follwoing the correct folder strcuture."""

    def take_action(self, parsed_args):
        run_checker()
        

class RunShiny(Command):
    """Command which runs the Shiny Appp"""

    def take_action(self, parsed_args):
        app_obj = RunShinyApp()
        app_obj.run_shiny_app()
        