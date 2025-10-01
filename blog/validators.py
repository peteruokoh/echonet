# myapp/validators.py
from django.core.exceptions import ValidationError

def validate_image_size(value):
    max_size_mb = 1
    if value.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Image file too large ( > {max_size_mb}MB ).")

def validate_video_size(value):
    max_size_mb = 10
    if value.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Video file too large ( > {max_size_mb}MB ).")

