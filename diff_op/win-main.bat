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
    coverage run -m pytest .\black_test\ .\fuzzing\ .\white_test\ .\boundary_value_test\ > %outdir%\result_%osname%_%%E.txt
    coverage report >> %outdir%\result_%osname%_%%E.txt
    echo Saved output to %outdir%\result_%%E.txt
    echo -------------------------
)

echo.

endlocal
pause
