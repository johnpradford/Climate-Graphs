@echo off
start cmd /k "cd frontend && npm install && npm run dev"
start cmd /k "cd backend && pip install -r requirements.txt && uvicorn api.main:app --reload"
pause
