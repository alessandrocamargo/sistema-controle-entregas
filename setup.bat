@echo off
echo 🚀 Configurando Sistema de Controle de Entregas...
echo.

echo 📦 Configurando Backend...
cd backend
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo ✅ Backend configurado!
echo.

cd ..

echo 📦 Configurando Frontend...
cd frontend
call npm install
echo ✅ Frontend configurado!
echo.

cd ..
echo 🎉 Configuração concluída!
echo.
echo Para iniciar o backend: cd backend && python run.py
echo Para iniciar o frontend: cd frontend && npm start
pause