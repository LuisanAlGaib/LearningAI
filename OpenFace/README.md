# OpenFace setup del proyecto

## Descarga
Descargar el paquete preparado desde:
https://drive.google.com/file/d/198gIxRcvLogj-kToS8mV5iFV3lctnFmk/view?usp=drive_link

## Contenido
El ZIP incluye OpenFace para Windows con modelos ya agregados.

## Pasos
1. Descargar el ZIP
2. Extraer la carpeta
3. Abrir PowerShell dentro de la carpeta de OpenFace
4. Ejecutar para una persona:

   .\FeatureExtraction.exe -device 0 -out_dir ".\salidas\webcam_single" -of "single_live" -vis-track -vis-hog -vis-align -vis-aus

6. Ejecutar para grupo:

   .\FaceLandmarkVidMulti.exe -device 0 -out_dir ".\salidas\grupo_webcam" -of "grupo_live"

## Archivos de salida

Los resultados se guardarán en la carpeta `salidas` e incluye archivos como:

- `.csv` → datos numéricos por frame
- `.avi` → video procesado
- `.hog` → características HOG
- `.txt` → resumen de configuración y salida

## Notas
- Usar `Ctrl + C` para detener la ejecución
