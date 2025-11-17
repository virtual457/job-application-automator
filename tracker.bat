@echo off
echo ========================================
echo APPLICATION TRACKER COMMANDS
echo ========================================
echo.

if "%1"=="" goto help
if "%1"=="log" goto log
if "%1"=="view" goto view
if "%1"=="excel" goto excel
goto help

:log
echo.
echo Logging new application...
echo.
cd src
python quick_log.py
cd ..
goto end

:view
echo.
cd src
python view_tracker.py
cd ..
goto end

:excel
echo.
echo Exporting to Excel...
cd src
python view_tracker.py excel
cd ..
echo Opening Excel file...
start ..\data\applications.xlsx
goto end

:help
echo Commands:
echo   tracker log      - Log a new application interactively
echo   tracker view     - View all applications in table format
echo   tracker excel    - Export to Excel and open
echo.
echo Examples:
echo   tracker log
echo   tracker view
echo   tracker excel
goto end

:end
echo.
pause
