@echo off
echo Switch to mamba ai environment(Nedd manually install condaforge and create env)
call mamba activate ai

echo Running main.py with torch-directml...
python main.py --directml --lowvram --disable-xformers --use-quad-cross-attention --reserve-vram=3.8

echo.
echo Script execution finished.
pause