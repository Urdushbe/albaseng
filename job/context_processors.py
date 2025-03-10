from .models import Region  # Agar Region modelini ishlatmoqchi bo'lsangiz

def regions(request):
    return {'regions': Region.objects.all()}
