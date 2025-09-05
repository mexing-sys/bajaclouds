from django.shortcuts import render
from .models import ComingSoonPage

def home_view(request):
    try:
        page_instance = ComingSoonPage.objects.filter(is_active=True).first()
        if not page_instance:
            # Crear datos por defecto si no existen
            page_instance = ComingSoonPage.objects.create(
                title="BAJA CLOUDS",
                subtitle="coming soon",
                on_air_text="ON AIR",
                logo="images/logo.png",
                
            )
        
        # Convertimos a dict
        page_data = {
            'title': page_instance.title,
            'subtitle': page_instance.subtitle,
            'on_air_text': page_instance.on_air_text,
            'background_image': page_instance.background_image.url if page_instance.background_image else None,
            'logo': page_instance.logo.url if page_instance.logo else None
        }
        
        # Separar palabras para BAJA y CLOUDS
        words = page_data['title'].split() if page_data.get('title') else ['BAJA', 'CLOUDS']
        page_data['baja_word'] = words[0] if len(words) > 0 else 'BAJA'
        page_data['clouds_word'] = words[1] if len(words) > 1 else 'CLOUDS'
    
    except Exception as e:
        # Datos de respaldo en caso de error
        print("Error en home_view:", e)
        page_data = {
            'title': 'BAJA CLOUDS',
            'subtitle': 'coming soon',
            'on_air_text': 'ON AIR',
            'background_image': None,
            'logo': None,
            'baja_word': 'BAJA',
            'clouds_word': 'CLOUDS'
        
        }

    return render(request, 'index.html', {'page_data': page_data})
