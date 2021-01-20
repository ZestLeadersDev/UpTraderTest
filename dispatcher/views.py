from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", {})


def feedback_view(request, *args, **kwargs):
    return render(request, "pages/feedback.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "pages/about.html", {})


def profile_view(request, *args, **kwargs):
    return render(request, "pages/profile.html", {})


def settings_view(request, *args, **kwargs):
    return render(request, "pages/settings.html", {})
