@echo off
set FilePath=%1
set ProgramFile=%~dp0\atlasJsonGenerator.py
python %ProgramFile% %FilePath%
pause