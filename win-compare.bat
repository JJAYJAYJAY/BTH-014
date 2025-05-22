@echo off
setlocal enabledelayedexpansion

set envs=py311
set os_name=windows
set outdir=test_results
if not exist %outdir% mkdir %outdir%

for %%E in (%envs%) do (
    echo Activating %%E
    call conda activate %%E
    pip install pytest
    echo Running compare_pickle.py in %%E...
    pytest .\diff_op\ > %outdir%\result_diffop_%%E.txt
    pytest .\diff_py\ > %outdir%\result_diffpy.txt
    echo Saved output to %outdir%\
    echo -------------------------
)

echo.

endlocal
