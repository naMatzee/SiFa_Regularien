@echo off
REM ──────────────────────────────────────────────────────────────────────────
REM  04_gb_aus_vorlage.bat – Windows-Starter für 04_gb_aus_vorlage.py
REM
REM  Voraussetzungen:
REM    - Python 3.x im PATH
REM    - lxml installiert: pip install lxml
REM    - stapcon_kern.py im gleichen Verzeichnis wie dieses Skript
REM
REM  Verwendung (Doppelklick oder Kommandozeile):
REM    04_gb_aus_vorlage.bat
REM      → öffnet Dateiauswahl-Dialog für JSON und verwendet Standard-Vorlage
REM
REM    04_gb_aus_vorlage.bat --template MeineVorlage.docx --json Daten.json
REM      → direkt mit Argumenten aufrufen
REM ──────────────────────────────────────────────────────────────────────────

setlocal

REM Verzeichnis dieser Batch-Datei als Arbeitsverzeichnis setzen
cd /d "%~dp0"

REM Python-Skript mit allen weitergegebenen Argumenten aufrufen
python 04_gb_aus_vorlage.py %*

REM Bei Fehler Pause anzeigen, damit die Fehlermeldung sichtbar bleibt
if errorlevel 1 (
    echo.
    echo [Fehler] Das Skript ist mit einem Fehler beendet worden.
    pause
)

endlocal
