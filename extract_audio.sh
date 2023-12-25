#!/bin/bash
# shellcheck source=/dev/null
source ~/Environments/personal1/bin/activate
python3 ~/Repos/tools/extract_audio.py "$1"
