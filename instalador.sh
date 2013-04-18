#!/bin/sh
# Script que permite la instalación de las aplicaciones necesarias para hacer correr la aplicación

exec su -c "

echo 'Iniciando la instalación de paquetes';
aptitude install python-pip gitk tig gource postgresql;

echo 'Iniciando la instalación de aplicaciones python';
pip install -r requirements.txt
"
