from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('student/', views.students, name='students'),
    path('student/<int:id>/', views.student, name='student')
]