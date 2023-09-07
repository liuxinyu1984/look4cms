from django.urls import path
from .views import test_display_note, tutor_create_note, tutor_delete_note


urlpatterns = [
    path('', test_display_note),
    path('tutor_create_note/<int:lecture_id>', tutor_create_note, name='tutor_create_note'),
    path('tutor_delete_note/<int:note_id>', tutor_delete_note, name='tutor_delete_note'),
]
