@echo off
echo ====================================
echo   TIERING APP - BUILD SCRIPT
echo ====================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python no está instalado o no está en el PATH
    echo    Descargue Python desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python detectado

REM Crear entorno virtual si no existe
if not exist "venv" (
    echo 📦 Creando entorno virtual...
    python -m venv venv
)

REM Activar entorno virtual
echo 🔄 Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instalar dependencias
echo 📚 Instalando dependencias...
pip install -r requirements.txt

REM Crear ejecutable con PyInstaller
echo 🔨 Generando ejecutable...
pyinstaller --onefile ^
    --windowed ^
    --name "TieringApp-Bancolombia" ^
    --add-data "templates;templates" ^
    --add-data "static;static" ^
    --hidden-import=flask ^
    --hidden-import=werkzeug ^
    --hidden-import=jinja2 ^
    --hidden-import=markupsafe ^
    --hidden-import=itsdangerous ^
    --hidden-import=click ^
    --hidden-import=blinker ^
    --distpath=dist ^
    --workpath=build ^
    --specpath=. ^
    app.py

if errorlevel 1 (
    echo ❌ Error al generar el ejecutable
    pause
    exit /b 1
)

echo.
echo ✅ ¡Ejecutable generado exitosamente!
echo 📁 Ubicación: dist\TieringApp-Bancolombia.exe
echo.
echo 💡 Instrucciones de uso:
echo    1. Copie el archivo .exe a cualquier ubicación
echo    2. Ejecute el archivo .exe
echo    3. Se abrirá automáticamente en su navegador
echo    4. Para cerrar, presione Ctrl+C en la ventana de consola
echo.
pause
