from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
# Models import
from .models import *

def index(request):
    page = Statistic.objects.get(page_name='index')
    page.number_of_clicks+=1
    page.save()
    recent_articles = Article.objects.order_by("-article_date")[:5]
    return render(request, "educate/index.html", {"recent_articles": recent_articles,})

def courses(request):
    all_courses = Course.objects.all()
    return render(request, "educate/courses.html", {"all_courses":all_courses,})

def lists(request, course_id):
    all_articles_by_course = Article.objects.filter(course_id=course_id)
    return render(request, "educate/list.html", {"all_articles_by_course":all_articles_by_course,})

def article(request, article_id):
    exact_article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(comment_article=article_id)
    comments_number = Comment.objects.filter(comment_article=article_id).count()
    return render(request, "educate/article.html", {"exact_article":exact_article, 'comments':comments, 'comments_number':comments_number,})

def about_us(request):
    teacher_number = Author.objects.all().count()
    click_number = Statistic.objects.get(page_name='index').number_of_clicks
    article_number = Article.objects.all().count()
    course_number = Course.objects.all().count()
    return render(request, "educate/about_us.html", {'teacher_number':teacher_number, 'click_number':click_number, 'article_number':article_number, 'course_number':course_number,})

def faq(request):
    return render(request, "educate/faq.html", {})

## def search_page is not ready!
def search_page(request):
    return

def signup_page(request):
    return render(request, "educate/signup.html", {})


def register(request):
    if request.method == 'POST':
        new_user = User(username=request.POST['username'],
                        password=request.POST['psw'],
                        first_name=request.POST['firstname'],
                        last_name=request.POST['lastname'])
        temp_user = User.objects.filter(username=new_user.username)
        if temp_user:
            return render(request, 'educate/signup.html', {'is_used_username':True, 'is_registred':False, 'is_password_failed':False})
        else:
            val_num = None
            try:
                val_num = validate_password(password=new_user.password, user=new_user, password_validators=None)
                new_user.save()
                new_author = Author(user=new_user, DOR='2000-05-02', author_qualification="")
                new_author.save()
                __set_params__(new_user)
                return render(request, 'educate/signup.html', {'is_used_username':False, 'is_registred':True, 'is_password_failed':False})
            except ValidationError:
                return render(request, 'educate/signup.html', {'is_used_username':False, 'is_registred':False, 'is_password_failed':True})
            except:
                return render(request, 'educate/signup.html', {'is_used_username':False, 'is_registred':False, 'is_password_failed':False})

# hashing the password and adding to the group 'Teachers'
def __set_params__(author):
    group = Group.objects.get(name='Teachers')
    author.groups.add(group)
    author.password = make_password(author.password, salt=None, hasher='default')
    author.save()
    return

def signin_page(request):
    return render(request, "educate/login.html", {})

# incomplete
def auth_log(request):
    username = request.POST['username']
    password = request.POST['psw']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse(request.user.is_authenticated)
    else:
        return render(request, 'educate/login.html', {'errors':True})

    return


def log_out(request):
    logout(request)
    return

# incomplete
def comment(request, article_id):
    if request.method == "POST":
        author = request.POST['name']
        email = request.POST['email']
        if not author or email:
            return HttpResponse('Bad')
        else:
            text = request.POST['comment_text']
            com = Comment(comment_article=article_id,
                                comment_author=author,
                                comment_email=email,
                                comment_text=text)
            com.save()
            return HttpResponse('Good')
