#!/bin/bash
# Nedd to create python venv manuallys
source venv/bin/activate
python main.py --listen --lowvram --reserve-vram=3.8
#deactivate