from django.db import models

class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=120)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='empleados/', blank=True, null=True)
    departamento = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, related_name='empleados'
    )

    def __str__(self):
        return self.nombre