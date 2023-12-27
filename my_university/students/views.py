from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import Student


@login_required
def myaccount(request):
    user = request.user
    user: Student

    return render(
        request,
        "account.html",
        {
            "user": user,
        },
    )


@login_required
def myaccount_edit(request):
    user = request.user
    user: Student

    if request.method == "POST":
        user.name = request.POST["name"]
        user.surname = request.POST["surname"]
        user.email = request.POST["email"]
        user.save()

    return redirect("myaccount")
