#!/bin/bash
python backend/src/bot.py &
uvicorn backend.src.app:app --host 0.0.0.0 --port 8000