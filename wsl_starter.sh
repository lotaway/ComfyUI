#!/bin/bash
# Nedd to create python venv manuallys
mamba run -n python3.12 python main.py --listen --lowvram --reserve-vram=3.8 --enable-cors-header="*"
#deactivate