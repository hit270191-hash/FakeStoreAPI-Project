@echo off
:: ====================================================
:: [Constants / Paths]
:: ====================================================
set ALLURE_RESULTS=reports\allure-results
set ALLURE_HTML=reports\allure-html
set PYTEST_HTML=reports\report.html

:: ====================================================
:: Step 1: Create virtual environment
:: ====================================================
echo Creating Virtual Environment...
python -m venv venv

:: ====================================================
:: Step 2: Activate the virtual environment
:: ====================================================
echo Activating Virtual Environment...
call venv\Scripts\activate.bat

:: ====================================================
:: Step 3: Install required Python packages
:: ====================================================
echo Installing/updating required packages...
pip install -r requirements.txt

:: ====================================================
:: Step 4: Clean up previous test reports
:: ====================================================
echo Cleaning previous test reports...
if exist %ALLURE_RESULTS% rmdir /s /q %ALLURE_RESULTS%
if exist %ALLURE_HTML% rmdir /s /q %ALLURE_HTML%
if exist %PYTEST_HTML% del %PYTEST_HTML%

:: ====================================================
:: Step 5: Re-create required directories (IMPORTANT)
:: ====================================================
echo Creating report directories...
mkdir %ALLURE_RESULTS%
mkdir %ALLURE_HTML%

:: ====================================================
:: Step 6: Run Pytest tests
:: ====================================================
echo Running tests...
pytest -s -v ^
--reruns=2 --reruns-delay=2 ^
--alluredir=%ALLURE_RESULTS% ^
--html=%PYTEST_HTML% --self-contained-html ^
testCases/

:: ====================================================
:: Step 7: Generate Allure report
:: ====================================================
echo Generating Allure report...
allure generate %ALLURE_RESULTS% -o %ALLURE_HTML% --clean
