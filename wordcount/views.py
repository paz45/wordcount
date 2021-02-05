from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    _dict_count_words = {}
    for word in word_list:
        if word not in _dict_count_words:
            _dict_count_words[word] = 1
        else:
            _dict_count_words[word] = _dict_count_words[word] + 1
    _dict_count_words = sorted(_dict_count_words.items())




    print(fulltext)
    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(word_list), 'word_counter':_dict_count_words})

def about(request):
    return render(request, 'about.html')