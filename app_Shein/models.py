from django.db import models

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('cliente', 'Cliente'),
        ('vendedor', 'Vendedor'),
        ('administrador', 'Administrador'),
    ]
    
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='cliente')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.email})"

class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('ropa', 'Ropa'),
        ('accesorios', 'Accesorios'),
        ('zapatos', 'Zapatos'),
        ('belleza', 'Belleza'),
        ('hogar', 'Hogar'),
    ]
    
    TALLA_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('Única', 'Única'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    talla = models.CharField(max_length=10, choices=TALLA_CHOICES, blank=True, null=True)
    color = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    imagen_url = models.URLField(blank=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"