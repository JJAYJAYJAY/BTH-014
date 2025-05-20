@echo off
setlocal enabledelayedexpansion

set envs=py36 py39 py311

set outdir=pickle_results
if not exist %outdir% mkdir %outdir%

for %%E in (%envs%) do (
    echo Activating %%E
    call conda activate %%E

    echo Running compare_pickle.py in %%E...
    python compare_pickle.py > %outdir%\result_%%E.txt

    echo Saved output to %outdir%\result_%%E.txt
    echo -------------------------
)

echo.
echo Comparing outputs:

fc %outdir%\result_py36_env.txt %outdir%\result_py39_env.txt > nul
if errorlevel 1 (
    echo [DIFFERENT] py36 vs py39
) else (
    echo [SAME] py36 vs py39
)

fc %outdir%\result_py39_env.txt %outdir%\result_py311_env.txt > nul
if errorlevel 1 (
    echo [DIFFERENT] py39 vs py311
) else (
    echo [SAME] py39 vs py311
)

endlocal
pause
