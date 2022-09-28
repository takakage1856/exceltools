#!/bin/bash
source ./set-path.sh
CURRENT=$(cd $(dirname "$0");pwd)
export PYTHONPATH="${CURRENT}/lib:$PYTHONPATH"
$PYTHON_INTERPRETER "${CURRENT}/grep.py" "$@"