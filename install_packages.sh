#!/usr/bin/env bash

pkg1=${1}
pkg2=${2}

[ -z ${pkg} ] && help

REXEC=$(which R)

if [ -z ${REXEC} ]; then
  echo "R not found, please ensure R is available and try again."
  exit 1
fi

echo "install.packages(c(\"${pkg1}\",\"${pkg2}\"), repos=\"https://cran.rstudio.com\")" | sudo R --no-save