from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import User, Estudiante, Profesor, Administrador

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        # Si el usuario es superusuario, no crear perfil de estudiante/profesor/admin
        if instance.is_superuser:
            return
        if hasattr(instance, 'rol'):
            if instance.rol == 'estudiante':
                # Generar una matrícula única usando el username y el id del usuario
                matricula = f"{instance.username}_{instance.id}"
                Estudiante.objects.get_or_create(user=instance, defaults={'matricula': matricula})
            elif instance.rol == 'profesor':
                Profesor.objects.get_or_create(user=instance)
            elif instance.rol == 'admin':
                Administrador.objects.get_or_create(user=instance)
        # Puedes agregar más roles si es necesario
