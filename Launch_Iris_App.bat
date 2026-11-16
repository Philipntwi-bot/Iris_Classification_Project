@echo off
title Iris Flower AI Classification Launcher
color 0B
echo ========================================================
echo   IRIS FLOWER AI CLASSIFICATION LAUNCHER
echo   Author: Philip Antwi - Pentecost University
echo ========================================================
echo.
echo Choose how you want to run the Iris Classification App:
echo.
echo   [1] Open Live Cloud App in Browser (Vercel)
echo   [2] Launch Local Interactive Web App (http://localhost:3000)
echo   [3] Launch Streamlit AI Dashboard (http://localhost:8501)
echo   [4] Open Online VS Code Web Editor (github.dev)
echo   [5] Exit
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo Opening live Vercel app...
    start https://iris-classification-project-rk73.vercel.app/
    goto end
)
if "%choice%"=="2" (
    echo Starting local web server on port 3000...
    start http://localhost:3000
    py -3 -m http.server 3000
    goto end
)
if "%choice%"=="3" (
    echo Launching Streamlit dashboard...
    py -3 -m streamlit run app.py
    goto end
)
if "%choice%"=="4" (
    echo Opening GitHub.dev online web editor...
    start https://github.dev/Philipntwi-bot/Iris_Classification_Project
    goto end
)

:end
