set /p build=<version
set /a build=build+1
echo %build% > version
git add .
git commit -m 'asdf'
git push