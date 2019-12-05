from django.urls import path, include
from . import views

# account закончить
# signup, register pages and views


app_name = 'educate'

urlpatterns = [
    path('index', views.index, name = 'index'),
    path('courses', views.courses, name = 'courses'),
    path('courses/<int:course_id>', views.lists, name = 'lists'),
    path('courses/course/<int:article_id>', views.article, name = 'article'),
    path('index/about_us', views.about_us, name='about_us'),
    path('index/faq', views.faq, name='faq'),
    path('index/search_page', views.search_page, name='search_page'),
    path('index/signin', views.signin_page, name='signin_page'),
    path('index/signup', views.signup_page, name="signup_page"),
    path('index/register', views.register, name="register"),
    path('index/auth_log', views.auth_log, name="auth_log"),
    path('index/log_out', views.log_out, name="log_out"),
    path('courses/course/<int:article_id>/comment', views.comment, name='comment'),

]
