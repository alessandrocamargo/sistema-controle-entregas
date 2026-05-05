#!/bin/bash

echo "🚀 Configurando Sistema de Controle de Entregas..."
echo ""

echo "📦 Configurando Backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "✅ Backend configurado!"
echo ""

cd ..

echo "📦 Configurando Frontend..."
cd frontend
npm install
echo "✅ Frontend configurado!"
echo ""

cd ..
echo "🎉 Configuração concluída!"
echo ""
echo "Para iniciar o backend: cd backend && python run.py"
echo "Para iniciar o frontend: cd frontend && npm start"