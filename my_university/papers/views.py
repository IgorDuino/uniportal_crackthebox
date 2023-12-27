from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

import pdfkit
import io


@login_required
def papers(request):
    return render(request, "papers.html")


@login_required
def generate_paper(request):
    context = {
        "user": request.user,
    }
    rendered_template = render_to_string("application.html", context)
    optioins = {"encoding": "UTF-8", "enable-local-file-access": True}
    pdf = pdfkit.from_string(rendered_template, False, options=optioins)

    return HttpResponse(pdf, content_type="application/pdf")
