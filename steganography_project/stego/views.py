import os
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .utils import decode_lsb

def index(request):
    return render(request, 'stego/index.html')

def decode(request):
    image_path = settings.BASE_DIR / 'stego' / 'static' / 'stego' / 'encoded_image.png'
    if image_path.exists():
        try:
            message = decode_lsb(str(image_path))
            return JsonResponse({'status': 'success', 'message': message})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Image not found'})
