#!/bin/sh
# Script que permite la instalación de las aplicaciones necesarias para hacer correr la aplicación

echo 'Iniciando la instalación de aplicaciones python';
pip install -r requirements.txt;

exec su -c "

echo 'Iniciando la instalación de paquetes';
aptitude install python-pip python-reportlab python-psycopg2;
echo 'Iniciando la instalación de PIL';
aptitude install python-dev zlib1g-dev libjpeg62-dev libfreetype6-dev
wget http://effbot.org/downloads/Imaging-1.1.7.tar.gz;
tar xvzf Imaging-1.1.7.tar.gz;
python Imaging-1.1.7/setup.py install;
rm -r Imagin*;
"


