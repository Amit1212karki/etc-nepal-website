from django import template
from django.utils.safestring import mark_safe
import nepali_datetime
import datetime

register = template.Library()



@register.filter(name='convert_to_nepali_date')
def convert_to_nepali_date(english_date):
    try:

        date_str = str(english_date)[:10]

        # Extract year, month, and day from the date_str
        year = int(date_str[:4])      # First 4 characters for the year
        month = int(date_str[5:7])    # Characters at position 5 and 6 for the month
        day = int(date_str[8:10])      # Characters at position 8 and 9 for the day

        # Create a datetime.date object
        date_obj = datetime.date(year, month, day)

        # Convert to Nepali date
        nepali_date = nepali_datetime.date.from_datetime_date(date_obj)

        return nepali_date

    except Exception as e:
        print(f"Conversion error: {e}")
        return english_date  # Return original date if conversion fails
