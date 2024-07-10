#!/usr/bin/env bash

find app -type d -name 'migrations' -exec sudo chown -R $(whoami):$(whoami) {} +
