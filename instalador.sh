#!/bin/sh
# Script que permite la instalación de las aplicaciones necesarias para hacer correr la aplicación

exec su -c "

echo 'Iniciando la instalación de python pip';
aptitude install python-pip;

echo 'Iniciando la instalación y actualización de Django, visores de git, docutils, visores de progreso animado de git, psycopg2 para soporte a postgres, motor de base de datos PostgreSQL';
pip install django; pip install --upgrade django django-extensions; aptitude install gitk tig gource python-psycopg2 postgresql python-docutils;
"
