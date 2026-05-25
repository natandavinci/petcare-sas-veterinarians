from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Consulta
from .tasks import transcribe_recording, ocr_and_markdown_file

@receiver(post_save, sender=Consulta)
def signals_gravacoes_transcricao_resumos(sender, instance, created, **kwargs):
    if created:
        transcribe_recording(instance.id)
        ocr_and_markdown_file(instance.id)