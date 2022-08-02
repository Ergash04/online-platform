from django.urls import path
from django.contrib.auth.decorators import login_required

from courses.views import HomeView, AboutView, ContactView, CourseListView, CourseDetailView, LessonDetailView, \
    searchView, create_class, create_legend, create_teaching, ConfirmDeleteCourseView, DeleteCourseView

app_name = 'courses'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('courses/<int:id>', CourseListView, name='course_list'),
    path('courses/<slug>/', login_required(CourseDetailView.as_view()), name='course_detail'),
    path('courses/<course_slug>/<lesson_slug>/', login_required(LessonDetailView.as_view()), name='lesson_detail'),
    path('search/', searchView, name='search_course'),
    path('create/class', create_class, name='create_class'),
    path('create/legend', create_legend, name='create_legend'),
    path('create/teaching', create_teaching, name='create_teaching'),
    path('<int:courses_id>/courses/<int:course_id>/delete/confirm', ConfirmDeleteCourseView.as_view(),
         name="confirm_delete"),
    path('<int:courses_id>/courses/<int:course_id>/delete/', DeleteCourseView.as_view(), name="delete_courses")
]
