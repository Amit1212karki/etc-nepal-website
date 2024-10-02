from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string

from xhtml2pdf import pisa
from weasyprint import HTML
import pdfkit

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if pdf.err:
        return HttpResponse("Invalid PDF", status_code=400, content_type='text/plain')
    return HttpResponse(result.getvalue(), content_type='application/pdf')

def render_to_pdf_weasy(template_src, context_dict={}):
    html = render_to_string(template_src, context_dict)  # Use Django's template rendering
    pdf = HTML(string=html).write_pdf()
    return HttpResponse(pdf, content_type='application/pdf')



def render_to_pdf_pdfkit(template_src, context_dict={}):
    # Render the HTML template with the given context
    html = render_to_string(template_src, context_dict)

    # Set options for pdfkit with adjusted margins
    options = {
        'page-size': 'A4',  # Standard page size
        'dpi': 400,
        'orientation': 'Landscape',  # Ensure landscape orientation
        'margin-top': '10px',  # Set to 0px to maximize usable space
        'margin-right': '10px',  # Set a small positive margin instead of negative
        'margin-bottom': '0px',  # Set to 0px
        'margin-left': '10px',  # Set a small positive margin instead of negative
        'no-stop-slow-scripts': '',
        'enable-local-file-access': '',
    }
    
    # Generate the PDF from the rendered HTML
    pdf = pdfkit.from_string(html, False, options=options) 
    
    # Return the generated PDF as a HttpResponse
    return HttpResponse(pdf, content_type='application/pdf')