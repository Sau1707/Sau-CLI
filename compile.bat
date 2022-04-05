xcopy "dist\sau\src\" "temp\" /E /Y
pyinstaller sau.py -y
xcopy "temp\" "dist\sau\src\" /E /Y
xcopy "src\" "dist\sau\src\" /E /EXCLUDE:exclude.bat.txt /Y