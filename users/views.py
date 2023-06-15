from django.shortcuts import render, redirect
from .models import *
from .forms import UserInputForm


def dashboard(request):
    practice_areas = PracticeArea.objects.all()
    return render(request, 'users/dashboard.html', {'practice_areas': practice_areas})


def projects(request, practice_area_slug):
    practice_area = PracticeArea.objects.get(slug=practice_area_slug)
    practice_area_projects = Project.objects.filter(practice_area=practice_area)
    return render(request, 'users/projects.html', {'practice_area': practice_area, 'projects': practice_area_projects})


def user_input(request):
    selected_documents = request.POST.getlist('documents[]')

    if request.method == 'POST':
        placeholders = Placeholder.objects.filter(documents__in=selected_documents)
        form = UserInputForm(request.POST, placeholders=placeholders)
        if form.is_valid():
            form.save()
            return redirect('users:success')  # Redirect to a success page after form submission
    else:
        placeholders = Placeholder.objects.none()
        form = UserInputForm(placeholders=placeholders)

    return render(request, 'users/input.html', {'form': form})

