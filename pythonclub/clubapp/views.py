from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getresources(request):
    resource_list=Resource.objects.all()
    return render(request, 'clubapp/resources.html' , {'resource_list' : resource_list})

def getmeetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'clubapp/meetings.html', {'meetings_list': meetings_list})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={
        'meeting' : meet
    }
    return render(request, 'clubapp/meetingdetails.html', context=context)

def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
      form=MeetingForm(request.POST)
      if form.is_valid():
        post=form.save(commit=True)
        post.save()
        form=MeetingForm()
    else:
      form=MeetingForm()
    return render(request, 'clubapp/newmeeting.html', {'form': form})
