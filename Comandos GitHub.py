    
-----------------------Consola-----------------------
mkdir: Crear carpeta
ls -la: Mostrar que hay en la carpeta 
cd: Volver



--------------------Nueva carpeta--------------------

1)  Copiar link de la carpeta
2)  Abrir el terminal de ubuntu.
3)  cd computacion/
4)  git clone <<pegar el link>>
5)  Ingresar usuario: Facundo-Guarnier
6)  Ingresar token: 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 -> Settings/Developer_settings/Personal_access_tokens y hay que crear uno si ya se venció el que tenia 
7)  "warning: Pareces haber clonado un repositorio sin contenido." tiene que salir en la terminal.
8)  En la crpeta tiene que estar el .git
9)  Abrir VS y abrir la terminal en la carpera.
10) Copiar los .py a la carpeta
11) git status, deberia salir en rojos lo .py


------------Subir y/o actualizar archivos------------

1) git add "Nombre del archivo"         #Subir/actualizar archivo nuevo, falta confirmar con el 3).
1.2) git add .                          #Sube/actualiza TODOS los archivos.
2) git commit -m "texto"                #Una expliacion a toda la ultima tanda de archivos subida.
3) git push                             #Confirma/actualiza todo lo anterior y sube los archivo de git add

git status                              #Ver el status



-------------------Info sobre tags-------------------
https://juncotic.com/tag-en-git/

Crear con el ultimo commit:
1) git tag -a <Nombre> -m "<Descripcion>"
2) git push origin <Nombre>

Eliminar un tag:
1) git push origin --delete <Nombre>
2) git tag -d args

