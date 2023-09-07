from django.shortcuts import render, redirect
from .models import Notes
from courses.models import Lecture
from tutors.views import tutor_required
from .forms import CreateNoteForm


# test displaying single note (download link)
def test_display_note(request):
    note = Notes.objects.get(pk=1)
    template = 'notes/test_display_note.html'
    context = {
        "note": note
    }
    return render(request, template, context)


#################################################
####  tutor create note
#################################################
@tutor_required
def tutor_create_note(request, lecture_id):

    template = 'notes/tutor_create_note.html'
    lecture = Lecture.objects.get(pk=lecture_id)

    if request.user != lecture.course.tutor:
        message = "Warning: You cannot upload notes to this lecture! (Not the instructor)"
        is_instructor = False
        context = {
            "is_instructor": is_instructor,
            "message": message
        }
        return render(request, template, context)
    else:
        message = f"Upload notes to {lecture}"
        is_instructor = True

        if request.method == "POST":
            form = CreateNoteForm(request.POST, request.FILES)
            print(request.FILES)
            if form.is_valid():
                note = Notes(
                    lecture=lecture,
                    title=form['title'].value(),
                    document=request.FILES["document"]
                )
                note.save()
                return redirect('tutor_lecture_detail', lecture.pk)
            else:
                error_message = "Upload Failed"
                context = {
                    "message": error_message,
                    "lecture_id": lecture.pk
                }
                return render(request, 'notes/note_upload_error.html', context)
        else:
            form = CreateNoteForm()
            context = {
                "is_instructor": is_instructor,
                "message": message,
                "form": form,
                "lecture_id": lecture.pk
            }
            return render(request, template, context)





#################################################
####  tutor delete note
#################################################
@tutor_required
def tutor_delete_note(request, note_id):
    
    template = 'notes/tutor_delete_note.html'
    note = Notes.objects.get(pk=note_id)
    lecture_id = note.lecture.pk

    if request.user != note.lecture.course.tutor:
        is_instructor = False
        message = 'You cannot delete this note. (Not the tutor of this course)'
        context = {
            "is_instructor": is_instructor,
            "message": message
        }
        return render(request, template, context)
    else:
        is_instructor = True
        message = f'Delete note: {note}'

        if request.method == 'POST':
            note.delete()
            return redirect('tutor_lecture_detail', lecture_id)
        
        context = {
            "is_instructor": is_instructor,
            "message": message,
            "lecture_id": lecture_id,
            "note": note
        }
        return render(request, template, context)