@echo off
echo =========================================
echo    Starting AI Resume Analyzer App...
echo =========================================
echo.

echo Installing required dependencies (if any)...
pip install -r requirements.txt
echo.

echo Launching Streamlit...
streamlit run app.py

pause
