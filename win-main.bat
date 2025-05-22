@echo off
setlocal enabledelayedexpansion

set envs=py36 py39 py311
set os_name=windows
set outdir=test_results
if not exist %outdir% mkdir %outdir%

for %%E in (%envs%) do (
    echo Activating %%E
    call conda deactivate
    call conda activate %%E
    pip install pytest coverage
    echo Running ...
    coverage run -m pytest .\black_test\ .\fuzzing\ .\white_test\ .\boundary_value_test\ > %outdir%\result_%os_name%_%%E.txt
    coverage report >> %outdir%\result_%os_name%_%%E.txt
    echo -------------------------
)

echo.
echo Saved output to %outdir%\
endlocal
