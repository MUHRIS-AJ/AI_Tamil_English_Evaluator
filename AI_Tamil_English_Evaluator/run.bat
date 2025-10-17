@echo off
title AI Tamil-English Response Evaluator
echo ============================================
echo     AI Tamil-English Evaluator Launcher
echo ============================================
echo.

REM Activate your Python environment if needed
REM call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt >nul

echo.
echo Starting evaluator...
python ai_evaluator.py

echo.
echo ============================================
echo    Evaluation completed successfully!
echo    Output saved to labeled_results.csv
echo ============================================
pause
