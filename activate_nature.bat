@echo off

REM Chemin absolu vers le dossier contenant votre environnement virtuel "nature"
set "env_path=C:\Users\levovo pro p50\Documents\informatique\IA\Projets jerem\musicreia\nature"

REM Activation de l'environnement virtuel "nature"
call "%env_path%\Scripts\activate"

REM Définition du chemin vers votre projet
cd /d "C:\Users\levovo pro p50\Documents\informatique\IA\Projets jerem\musicreia"

REM Afficher un message indiquant que l'environnement est activé et le chemin du projet
echo Environnement virtuel "nature" activé.
echo Chemin du projet : %cd%

REM Laisser la fenêtre ouverte pour que vous puissiez travailler dans l'environnement.
cmd /k