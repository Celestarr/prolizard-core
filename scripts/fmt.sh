#!/usr/bin/env bash

sort -o requirements.txt requirements.txt
black .
isort --atomic .
