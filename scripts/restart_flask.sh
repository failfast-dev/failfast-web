#!/bin/bash
echo "🔁 Stopper Flask hvis den kjører..."
pkill -f app.py
sleep 1
echo "🚀 Starter Flask!"
python app.py
