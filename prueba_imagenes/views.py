# views.py
from django.shortcuts import render
from .models import Producto
from django.conf import settings
from django.http import JsonResponse

import os
def lista_productos(request):
    productos = Producto.objects.all()
    print(productos)
    for producto in productos:
        # Extraer solo el nombre del archivo de la imagen
        nombre_archivo = os.path.basename(producto.imagen)
        producto.imagen = f"images/{nombre_archivo}"  # Ruta relativa a /static/
    return render(request, 'inicio.html', {
        'productos': productos})


def cargar_productos_desde_static(request):
    # Ruta de la carpeta de imágenes (relativa a 'static/')
    ruta_estatica = os.path.join(settings.BASE_DIR, 'prueba_imagenes', 'static', 'images')

    # Verificar si la carpeta existe
    if not os.path.exists(ruta_estatica):
        return JsonResponse({'error': f'No existe la carpeta: {ruta_estatica}'}, status=404)

    creados = []
    
    # Listar los archivos en la carpeta de imágenes
    for nombre_archivo in os.listdir(ruta_estatica):
        if nombre_archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Construir la ruta relativa que Django usará para acceder al archivo estático
            
            # Crear el producto si no existe
            ruta_relativa = f'prueba_imagenes\static\images\{nombre_archivo}'  # Esta es la ruta que usarás en los templates
            producto, creado = Producto.objects.get_or_create(
                nombre=os.path.splitext(nombre_archivo)[0],  # El nombre será el nombre del archivo sin extensión
                imagen=ruta_relativa  # Guardar la ruta relativa en el campo imagen
            )
            
            # Si se creó el producto, agregarlo a la lista de creados
            if creado:
                creados.append(producto.nombre)

    # Responder con los productos creados
    return JsonResponse({'productos_creados': creados})

def eliminar_imagenes(request):
    # Aquí obtenemos todos los productos con imágenes
    productos = Producto.objects.all()
    eliminados = []

    for producto in productos:
        # Verificamos si el producto tiene una imagen
        if producto.imagen:
            # Construimos la ruta completa del archivo en el sistema de archivos
            archivo_imagen = os.path.join(settings.BASE_DIR, 'prueba_images', 'static', producto.imagen)
            
            # Verificamos si el archivo existe y lo eliminamos
            if os.path.exists(archivo_imagen):
                os.remove(archivo_imagen)
                producto.imagen = None  # Limpiamos la referencia de la imagen en la base de datos
                producto.save()  # Guardamos el cambio en la base de datos
                eliminados.append(producto.nombre)

    return JsonResponse({'imagenes_eliminadas': eliminados})