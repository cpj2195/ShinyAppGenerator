
# MithooCLI

This CLI helps you to scaffold a base shiny app on top of which you can develop. It lets' you create a template for an algorithm which consists a
function of the same name as the algorithm.After you are done developing the app or along the way, you can run the integrated sanity checker to see
if you are following the correct folder structure among other checks put in place.

## Setup 

## Setup pip.conf to download the pip packages from Elucidata's internal pip server.

Make a file pip.conf in $HOME/etc

Enter the following contents in that file:
```
[global]
extra-index-url = http://54.245.179.143/
[install]
trusted-host=54.245.179.143
```


## Ceate a virtual environment and activate it.

  $ pip install virtualenv 

  $ virtualenv .venv 

  $ source .venv/bin/activate 

## Now, install the demo application into the virtual environment.

  (.venv)$ pip install mithoocli 


# Usage


(.venv)$ mithoo makehiny {name_of_app} 

  Makes the shiny app in the current diretory you are in.

(.venv)$ mithoo makealgo {name_of_algo} 

  Makes a .R file in the algorithms folder with a function of the same name as the algorithm. Will work if you are anywhere in your
  shiny app directory.

(.venv)$ mithoo checkapp 

  Runs a sanity checker to see if the structure is followed among other things.Will work only if you are anywhere
  shiny app directory.


# Cleaning Up


Finally, when done, deactivate your virtual environment::

  (.venv)$ deactivate

# Author

Chander Prabh Jain <chanderprabh.jain@elucidata.io>


