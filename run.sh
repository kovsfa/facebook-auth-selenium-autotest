#!/bin/bash

source .venv/Scripts/activate
find . -iname "*.test.py" | xargs -I {} python {}
