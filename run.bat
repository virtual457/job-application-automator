@echo off
REM Quick commands for Job Application Automator

echo ========================================
echo Job Application Automator
echo ========================================
echo.

if "%1"=="" goto help
if "%1"=="install" goto install
if "%1"=="init" goto init
if "%1"=="test" goto test
if "%1"=="generate" goto generate
if "%1"=="batch" goto batch
if "%1"=="stats" goto stats
if "%1"=="roles" goto roles
goto help

:install
echo Installing dependencies...
pip install -r requirements.txt
goto end

:init
echo Initializing project...
cd src
python main.py init
cd ..
goto end

:test
echo Running tests...
python tests\test_resume_generator.py
goto end

:generate
if "%2"=="" (
    echo Error: Company name required
    echo Usage: run.bat generate CompanyName [role_type]
    goto end
)
set ROLE=%3
if "%3"=="" set ROLE=backend
cd src
python main.py generate-resume --company %2 --role %ROLE%
cd ..
goto end

:batch
if "%2"=="" (
    echo Error: Batch file required
    echo Usage: run.bat batch config\week1_applications.yaml
    goto end
)
cd src
python main.py batch-generate %2
cd ..
goto end

:stats
cd src
python main.py stats
cd ..
goto end

:roles
cd src
python main.py list-roles
cd ..
goto end

:help
echo Usage: run.bat [command] [options]
echo.
echo Commands:
echo   install              Install dependencies
echo   init                 Initialize project structure
echo   test                 Run tests
echo   generate COMPANY     Generate resume for company (default: backend role)
echo   generate COMPANY ml  Generate ML role resume
echo   batch FILE           Generate batch resumes from YAML file
echo   stats                Show generation statistics
echo   roles                List available role types
echo.
echo Examples:
echo   run.bat install
echo   run.bat generate Salesforce
echo   run.bat generate ByteDance ml
echo   run.bat batch config\week1_applications.yaml
echo   run.bat stats
goto end

:end
echo.
