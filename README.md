# ML-Challenge-Kosmos

## Activar API

Para probar el API es necesario  correr el archivo main.sh desde la carpeta principal con el siguiente commando

```console
./main.sh
```

## Enviar un request

Después se puede enviar un request con el siguiente comando:


```console
curl -X POST -H "Content-Type: application/json" -d '{ "oraciones": [ "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.", "San Francisco considera prohibir los robots de entrega en la acera." ] }' http://localhost:5000/ner
```

Es necesario cambiar las oraciones con aquellas que se quiera hacer la prueba.
