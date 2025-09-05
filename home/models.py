from django.db import models

class ComingSoonPage(models.Model):
    title = models.CharField(max_length=200, default="BAJA CLOUDS")
    subtitle = models.CharField(max_length=200, default="coming soon")
    on_air_text = models.CharField(max_length=50, default="ON AIR")
    background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    logo = models.ImageField(upload_to='static/images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Coming Soon Page"
        verbose_name_plural = "Coming Soon Pages"

    def __str__(self):
        return f"{self.title} - {'Active' if self.is_active else 'Inactive'}"