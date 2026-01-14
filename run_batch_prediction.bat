@echo off
echo ================================
echo Running Batch Prediction Script
echo ================================

REM Activate virtual environment
call env\Scripts\activate

REM Run batch prediction
python -m src.batch_predict

echo.
echo ================================
echo Batch Prediction Finished
echo ================================
pause
