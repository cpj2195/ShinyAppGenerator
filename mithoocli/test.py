import subprocess
commands = '''
R --no-save<<EOF
library(lintr)
lint('/home/chander/get_KSEA_input.R',with_defaults(line_length_linter = line_length_linter(120),camel_case_linter = NULL))

EOF'''
process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, err = process.communicate(commands)
