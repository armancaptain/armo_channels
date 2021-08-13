from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from . import models
from django.contrib.auth.decorators import login_required
from . import forms
import articles

# Create your views here.
def article_detail(request, slug):
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)
    comments = models.Comment.objects.all().filter(post = article)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = models.Article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = forms.CommentForm()

                                           
    return render(request, 'articles/article_detail.html',{'article':article,
                                                        'comments': comments,
                                                        'new_comment': new_comment,
                                                        'comment_form': comment_form,})

@login_required(login_url = "/accounts/login")
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid:
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('list')
    else:
        form = forms.CreateArticle()
    return render(request , 'articles/create_article.html',{'form':form})

    

