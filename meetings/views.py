from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Meeting, Question, Reply
from meetings.forms import QuestionForm


# Create your views here.


def index(request):
    """
    This is the landingpage route
    """

    return render(request, 'index.html', {})


def home(request):
    """
    Homepage route
    """
    meetings = Meeting.objects.all()
    return render(request, 'home.html', {'meetings': meetings})


def detail(request, meeting_id):
    """
    Question detail route
    """
    meeting_detail = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, 'detail.html', {'meeting_detail': meeting_detail})


def new_question(request, meeting_id):
    """
    This route is for posting a new question to a meeting
    """

    meeting_detail = get_object_or_404(Meeting, pk=meeting_id)
    user = User.objects.first()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.meeting_detail = meeting_detail
            question.posted_by = request.user
            question.save()
            reply = Reply.objects.create(
                message=form.cleaned_data.get('message'),
                question=question,
                created_by=user
            )
            reply.save()
            # TODO: redirect to the created topic page
            return redirect('detail', pk=meeting_detail.id)
    else:
        form = QuestionForm()
    return render(request, 'new_question.html', {'meeting_detail': meeting_detail, 'form': form})
