
# ShinyCLI

This CLI helps you to scaffold a base shiny app on top of which you can develop. It lets' you create a template for an algorithm which consists a
function of the same name as the algorithm.After you are done developing the app or along the way, you can run the integrated sanity checker to see
if you are following the correct folder structure among other checks put in place.

## Prerequisites

1. You should have Python3.6 installed on your system
2. You should have R 3.5.1 installed
3. Make sure you have virtualenv pip package
4. Install R packages using the `install_packages.sh` using the command `sudo sh install_packages.sh lintr shiny`


## Ceate a virtual environment and activate it.

  $ pip install virtualenv 

  $ virtualenv -p python3.6 .venv 

  $ source .venv/bin/activate 

## Now, install the demo application into the virtual environment.

  (.venv)$ Clone the Repo 
  (.venv)$ Change the directory and run `python setup.py install`




# Usage


(.venv)$ shiny makeshiny {name_of_app} 

  Makes the shiny app in the current diretory you are in.

(.venv)$ shiny makealgo {name_of_algo} 

  Makes a .R file in the algorithms folder with a function of the same name as the algorithm. Will work if you are anywhere in your
  shiny app directory.

(.venv)$ shiny checkapp 

  Runs a sanity checker to see if the structure is followed among other things.Will work only if you are anywhere
  shiny app directory.

(.venv)$ shiny runapp 

  Runs the shiny app locally on the default URL for the user to test.Will work only if you are anywhere
  shiny app directory.

(.venv)$ shiny runlintr {R_file_path}

  Runs the R lintr on the specified R files to see if you are following standard R linting .Here, Camel Case functions are allowed and
  default line length can be 120 charcters instaed of 89.


(.venv)$ shiny --help
  To see the list of available shinycli commands and their basic usage 



# Cleaning Up


Finally, when done, deactivate your virtual environment::

  (.venv)$ deactivate


# Motivation for the CLI

When I was working at a startup , I witnessed that code handover from data science to engineering team was not standardised. It did not follow a standard process
given that the data science team at the organisation was developing shiny app because they found it easy to devlop and and for demoing the same to external users. This CLI is a small effort to bridge the gap between the two teams such that the engineering can being those apps to production with the least intervention from the data science team.


# Author

Chander Prabh Jain <chanderprabhjain95@gmail.com>


