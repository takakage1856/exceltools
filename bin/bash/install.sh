#!/bin/bash
CURRENT=$(cd $(dirname "$0");pwd)
cd "$CURRENT"
source ./set-path.sh
PIP="${PYTHON_INTERPRETER} -m pip"

cd ../../
rm -rf lib

if [ ! -d "lib" ]; then
    mkdir "lib"
fi

$PIP install --upgrade pip
$PIP install -r ./requirements.txt -t ./lib