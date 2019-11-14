from django. urls import path
from . import views
from accounts import views as account_views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', account_views.signup, name= 'signup' ),
    path('home/', views.home, name='home'),
    path('home/<int:meeting_id>/', views.detail, name='detail'),
    path('home/<int:meeting_id>/new/', views.new_question, name='new_question'),
]
