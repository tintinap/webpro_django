from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Poll, Question, Answer
from polls.forms import PollForm

# Create your views here.
def index(request):
    poll_list = Poll.objects.all()
    # poll_list = Poll.objects.annotate(question_count-Count('question')) #another method to do

    # print(poll_list.query)
    for poll in poll_list:
        question_count = Question.objects.filter(poll_id=poll.id).count()
        poll.question_count = question_count

    context = {
        'page_title': 'My Polls',
        'poll_list' : poll_list
    }

    return render(request, template_name='polls/index.html', context=context)

def detail(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        for question in poll.question_set.all():
            name = 'choice' + str(question.id)
            # choice_id = request.GET.get(name)
            choice_id = request.POST.get(name)

            if choice_id:
                try:
                    ans = Answer.objects.get(question_id=question.id)
                    ans.choice_id = choice_id
                    ans.save()
                except Answer.DoesNotExist:
                    Answer.objects.create(
                        choice_id = choice_id, #choice_id that we got fromGET
                        question_id = question.id
                    )
            
            print(choice_id)

    print(request.GET)

    return render(request, template_name="polls/detail.html", context={'poll': poll})

def create(request):
    
    #if this is a POST request we need to process the form data
    if request.method == "POST":
        form = PollForm(request.POST)

        if form.is_valid():
            poll = Poll.objects.create(
                title = form.cleaned_data.get('title'),
                start_date = form.cleaned_data.get('start_date'),
                end_date = form.cleaned_data.get('end_date')
            )

            for i in range(1, form.cleaned_data.get("no_questions")+1):
                Question.objects.create(
                    text="QQQQ"+str(i),
                    type='01',
                    poll=poll
                )

    #if a GET (or any other method) just query data from the database
    else:
        form = PollForm()

    context = {'form': form}
    return render(request, 'polls/create.html', context=context)
