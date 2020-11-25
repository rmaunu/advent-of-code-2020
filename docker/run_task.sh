#!/usr/bin/env bash

set -e

eval "$(pyenv init -)"

python scripts/run_task.py $MY_TASK
