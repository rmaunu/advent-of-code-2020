#!/usr/bin/env bash

set -e

eval "$(pyenv init -)"

python scripts/run_day.py $DAY $PART
