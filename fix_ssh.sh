#!/bin/bash
# Script para limpiar VPS y dejar SSH listo para GitHub Actions
# Puerto de la aplicación: 1001

echo "🔹 Limpiando archivos de inicio del usuario..."

# Limpiar mensajes en bashrc y profile
if [ -f ~/.bashrc ]; then
  sed -i '/echo/d' ~/.bashrc
fi

if [ -f ~/.profile ]; then
  sed -i '/echo/d' ~/.profile
fi

if [ -f ~/.bash_profile ]; then
  sed -i '/echo/d' ~/.bash_profile
fi

echo "🔹 Desactivando mensajes MOTD..."
sudo chmod -x /etc/update-motd.d/* 2>/dev/null
sudo truncate -s 0 /etc/motd 2>/dev/null

echo "🔹 Reiniciando servicio SSH..."
sudo systemctl restart ssh

echo "✅ VPS listo para GitHub Actions"
echo "🔌 Puerto de aplicación: 1001"
