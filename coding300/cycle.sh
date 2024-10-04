
# Usar un bucle para extraer archivos de nivel
for i in {1..49};  # Comienza desde 1 para procesar lvl1.png
do
    j=$((i + 1))
    
    # Usar el nombre del archivo correctamente y llamar al script de Python
    echo "Procesando lvl${i}.png"
    password=$(python coding300.py "lvl${i}.png")
    
    # Asegúrate de que el archivo ZIP existe antes de intentar extraerlo
    if [[ -f "lvl${j}.zip" ]]; then
        7z x -p"$password" "lvl${j}.zip"
    else
        echo "No se encontró lvl${j}.zip, terminando el proceso."
        break
    fi
done
