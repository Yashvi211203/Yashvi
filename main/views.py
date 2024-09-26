from django.shortcuts import render,redirect
from datetime import datetime
import random
from.models import Query

def home(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Example of random quotes
    quotes = [
        "If you can dream it, you can do it.",
        "Keep Going !!",
        "Tiny steps still count as progress.",
        "Everything is hard before it is esay.",
        "Success does'nt come to you, you go to it."
    ]
    random_quote = random.choice(quotes)

    return render(request, 'index.html', {
        'current_time': current_time,
        'random_quote': random_quote
    })


def Query_Form(request):
    return render(request, 'Query_Form.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query_text = request.POST.get('query')

        # Save to database
        query = Query(name=name, email=email, query=query_text)
        query.save()

        return render(request, 'submit.html', {
            'name': name,
            'email': email,
            'query': query_text,
        })
    return redirect('Query_Form')



def about(request):
    return render(request, 'about.html')

