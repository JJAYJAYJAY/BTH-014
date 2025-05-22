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
    pytest .\diff_test\ > %outdir%\result_diff_test_%%E.txt
    echo Saved output to %outdir%\
    echo -------------------------
)

echo.

endlocal
