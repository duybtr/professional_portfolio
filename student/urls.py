from django.urls import path
from .views import (
    HomePageView, 
    AwardPageView,
    get_student_list,
    add_student,
    add_student_submit,
    add_student_cancel,
    edit_student,
    edit_student_submit,
    delete_student
)
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('get_student_list', get_student_list, name='get_student_list'),
    path('add_student', add_student, name='add_student'),
    path('add_student_submit', add_student_submit, name='add_student_submit'),
    path('add_student_cancel', add_student_cancel, name='add_student_cancel'),
    path('<int:student_pk>/delete_student', delete_student, name='delete_student'),
    path('<int:student_pk>/edit_student', edit_student, name='edit_student'),
    path('<int:student_pk>/edit_student_submit', edit_student_submit, name='edit_student_submit'),
    
]