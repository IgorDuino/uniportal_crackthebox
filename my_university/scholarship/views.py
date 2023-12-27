from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import Student


@login_required
def scholarship(request):
    user = request.user
    user: Student

    bmin = 3000
    bmax = 10000
    srac = 3000
    gpa = user.gpa if user.gpa else 4.2

    s = bmin + (bmax - bmin) * ((gpa - 2) / 3) ** 2.5 - srac

    return render(
        request,
        "scholarship.html",
        {
            "scholarship": int(s),
        },
    )
