from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Usuario, Producto

def index(request):
    return render(request, 'base.html')

# ========== VISTAS PARA USUARIOS ==========

def agregar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        tipo_usuario = request.POST.get('tipo_usuario')
        activo = request.POST.get('activo') == 'on'
        
        Usuario.objects.create(
            nombre=nombre,
            email=email,
            telefono=telefono,
            direccion=direccion,
            tipo_usuario=tipo_usuario,
            activo=activo
        )
        return redirect('ver_usuarios')
    
    return render(request, 'usuario/agregar_usuario.html')

def ver_usuarios(request):
    usuarios = Usuario.objects.all().order_by('-fecha_registro')
    return render(request, 'usuario/ver_usuarios.html', {'usuarios': usuarios})

def actualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST':
        usuario.nombre = request.POST.get('nombre')
        usuario.email = request.POST.get('email')
        usuario.telefono = request.POST.get('telefono')
        usuario.direccion = request.POST.get('direccion')
        usuario.tipo_usuario = request.POST.get('tipo_usuario')
        usuario.activo = request.POST.get('activo') == 'on'
        usuario.save()
        return redirect('ver_usuarios')
    
    return render(request, 'usuario/actualizar_usuario.html', {'usuario': usuario})

def borrar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST':
        usuario.delete()
        return redirect('ver_usuarios')
    
    return render(request, 'usuario/borrar_usuario.html', {'usuario': usuario})

# ========== VISTAS PARA PRODUCTOS ==========

def agregar_producto(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            precio = float(request.POST.get('precio'))
            categoria = request.POST.get('categoria')
            talla = request.POST.get('talla')
            color = request.POST.get('color')
            stock = int(request.POST.get('stock'))
            imagen_url = request.POST.get('imagen_url')
            disponible = request.POST.get('disponible') == 'on'
            
            Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                categoria=categoria,
                talla=talla,
                color=color,
                stock=stock,
                imagen_url=imagen_url,
                disponible=disponible
            )
            return redirect('ver_productos')
        except Exception as e:
            # En caso de error, mostrar la página de nuevo
            return render(request, 'producto/agregar_producto.html', {'error': str(e)})
    
    # GET request - mostrar el formulario
    return render(request, 'producto/agregar_producto.html')

def ver_productos(request):
    productos = Producto.objects.all().order_by('-fecha_agregado')
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        try:
            producto.nombre = request.POST.get('nombre')
            producto.descripcion = request.POST.get('descripcion')
            producto.precio = float(request.POST.get('precio'))
            producto.categoria = request.POST.get('categoria')
            producto.talla = request.POST.get('talla')
            producto.color = request.POST.get('color')
            producto.stock = int(request.POST.get('stock'))
            producto.imagen_url = request.POST.get('imagen_url')
            producto.disponible = request.POST.get('disponible') == 'on'
            producto.save()
            return redirect('ver_productos')
        except Exception as e:
            return render(request, 'producto/actualizar_producto.html', {'producto': producto, 'error': str(e)})
    
    return render(request, 'producto/actualizar_producto.html', {'producto': producto})

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    
    return render(request, 'producto/borrar_producto.html', {'producto': producto})