@echo off

:: Install dependencies
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies
    exit /b %errorlevel%
)

:: Apply database migrations
python manage.py makemigrations
if %errorlevel% neq 0 (
    echo Failed to make migrations
    exit /b %errorlevel%
)
python manage.py migrate
if %errorlevel% neq 0 (
    echo Failed to apply migrations
    exit /b %errorlevel%
)

:: Collect static files
python manage.py collectstatic --noinput
if %errorlevel% neq 0 (
    echo Failed to collect static files
    exit /b %errorlevel%
)
