from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from .forms import FeedbackForm
from .models import Feedback


def add_feedback(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        form.save()
        paginator = Paginator(Feedback.objects.filter(to_publish=True), 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
        'form': form,
        'page_obj': page_obj,
        }
        return render(request, 'feedback/feedbacks.html', context)
    return redirect('feedback:feedbacks')


def feedbacks(request):
    paginator = Paginator(Feedback.objects.filter(to_publish=True), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'form': FeedbackForm(),
        'page_obj': page_obj,
    }
    return render(request, 'feedback/feedbacks.html', context)