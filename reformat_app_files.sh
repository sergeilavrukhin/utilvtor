#!/bin/bash
app=$1
for file in `find ./${app} -type f -name "*.py" -not -path "./venv/*" -not -path "./.git/*" -not -path "./static/*" -not -path "./source/*" -not -path "./www/*" -not -path "./templates/*" -not -path "./media/*" -not -path "./front/*"`
do
   python -m autoflake --in-place "${file}"
   python -m isort --profile black "${file}"
   python -m black "${file}"
   python -m flake8 "${file}"
done



