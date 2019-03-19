#!/usr/bin/env python
import os
from pathlib import Path

import shinycli.constants as cnst
import shinycli.helpers as hlp
from shinycli.logging_utils import logger


class CreateShinyApp:

    def __init__(self, app_name):
        self.app_name = app_name

    def make_folder_tree(self, root_folder, appname):
        """
        Creates a Folder Structure for the shiny app .
        Puts in place a ui.R and server.R files along with the algorithms 
        and tests folder.Also adds some documentation to the server.R and ui.R
        files.

        Arguments:
            root_folder {str} -- The path to your shiny app.
            appname {str} -- The name of your shiny app 

        """
        hlp.make_folder(appname, os.getcwd())
        Path(root_folder + "/ui.R").touch()
        Path(root_folder + "/Readme.md").touch()
        Path(root_folder + "/server.R").touch()
        hlp.make_folder("algorithms", root_folder)
        hlp.make_folder("tests", root_folder)
        hlp.make_folder("test_data", os.path.realpath(
            root_folder+cnst.TESTS_FOLDER))
        hlp.make_folder("data", os.path.realpath(
            root_folder+cnst.ALGORITHMS_FOLDER))
        self.write_ui_file(appname)
        self.write_server_file(appname)

    def write_ui_file(self, appname):
        """
        Adds some basic documentation to the server.R and ui.R files 
        which are placed in the root of the shiny app .

        Arguments:
            appname {str} -- The name of your shiny app.

        """
        documentation_template = """
            #########################################################################
            #####                                                               #####
            #####  PLEASE DO NOT IMPORT LIBRARIES WHICH ARE NOT NEEDED BY SHINY #####
            #####      SERVER TO FUNCTION in server.r AND ui.R                  #####
            #####                                                               #####
            #########################################################################
            \n

            library(shiny)

            # Define UI for application that plots random distributions 
            shinyUI(fluidPage(
            
            # Application title
            titlePanel("Hello Shiny!"),
            
            # Sidebar with a slider input for number of observations
            sidebarLayout(
                sidebarPanel(
                sliderInput("obs", 
                            "Number of observations:", 
                            min = 1, 
                            max = 1000, 
                            value = 500)
                ),
                
                # Show a plot of the generated distribution
                mainPanel(
                plotOutput("distPlot")
                )
            )
            ))"""
        file_name = 'ui.R'
        file_path = os.getcwd() + '/' + appname + '/' + file_name
        # using r+ mode so that if the file does not exist , it will create it.
        with open(file_path, "r+") as file_pointer:
            file_pointer.write(documentation_template)
    
    def write_server_file(self,appname):
        documentation_template = """
            #########################################################################
            #####                                                               #####
            #####  PLEASE DO NOT IMPORT LIBRARIES WHICH ARE NOT NEEDED BY SHINY #####
            #####      SERVER TO FUNCTION in server.r AND ui.R                  #####
            #####                                                               #####
            #########################################################################
            \n

            library(shiny)

            # Define server logic required to generate and plot a random distribution
            shinyServer(function(input, output) {
            
            # Expression that generates a plot of the distribution. The expression
            # is wrapped in a call to renderPlot to indicate that:
            #
            #  1) It is "reactive" and therefore should be automatically 
            #     re-executed when inputs change
            #  2) Its output type is a plot 
            #
            output$distPlot <- renderPlot({
                    
                # generate an rnorm distribution and plot it
                dist <- rnorm(input$obs)
                hist(dist)
            })
            
            }) """
        file_name = "server.R"
        file_path = os.getcwd() + '/' + appname + '/' + file_name
        # using r+ mode so that if the file does not exist , it will create it.
        with open(file_path, "r+") as file_pointer:
            file_pointer.write(documentation_template)



    def make_shiny_app(self):
        """
        The main function to cretae a shiny app which creates the folder structure after checking if
        .shiny folder exists and the .shiny-state file is in it.It does not let the use create a
        shiny app with the same name or a shiny app within a shiny app.

        """

        root_folder = os.path.realpath(os.getcwd() + '/' + self.app_name)
        name_app, state_path = hlp.search_state_file(os.getcwd())
        if (name_app and state_path):
            logger.error(cnst.ALREADY_IN_SHINY_APP)
            return
        if(os.path.exists(root_folder + cnst.SHINY_STATE_FOLDER) and os.path.exists(root_folder + cnst.SHINY_STATE_FILE)):
            data = hlp.load_from_json(root_folder + cnst.SHINY_STATE_FILE)
            if(self.app_name == data.get(cnst.NAME_OF_SHINY_APP)):
                logger.error(cnst.SAME_NAME_APP_EXISTS)
            else:
                data = {cnst.NAME_OF_SHINY_APP: self.app_name}
                hlp.write_to_json(data, root_folder+cnst.SHINY_STATE_FILE)
                self.make_folder_tree(root_folder, self.app_name)
        else:
            hlp.make_folder('.shiny', root_folder)
            data = {cnst.NAME_OF_SHINY_APP: self.app_name}
            hlp.write_to_json(data, root_folder+cnst.SHINY_STATE_FILE)
            self.make_folder_tree(root_folder, self.app_name)
