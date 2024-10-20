from django import template
from nepali_unicode_converter.convert import Converter
from django.utils.safestring import mark_safe

register = template.Library()

# Initialize the Nepali Unicode Converter
converter = Converter()

@register.filter(name='convert_to_nepali_unicode')
def convert_to_nepali_unicode(text):
    try:
        # Convert the text to Nepali Unicode
        converted_text = converter.convert(text)
        return mark_safe(converted_text)
    except Exception as e:
        print(f"Conversion error: {e}")
        return text  # Return original text if conversion fails
