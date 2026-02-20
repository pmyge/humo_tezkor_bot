@echo off
set TOKEN=8354261773:AAFcVFIYIHRZ-9koTGSXaAtDo6zr-e-H3HI

echo --- Terminating sessions ---
curl.exe -s -X POST "https://api.telegram.org/bot%TOKEN%/close"
echo.
curl.exe -s -X POST "https://api.telegram.org/bot%TOKEN%/logOut"
echo.
curl.exe -s -X POST "https://api.telegram.org/bot%TOKEN%/deleteWebhook?drop_pending_updates=true"
echo.
echo --- Draining updates ---
curl.exe -s "https://api.telegram.org/bot%TOKEN%/getUpdates?offset=-1"
echo.
echo --- Done ---
