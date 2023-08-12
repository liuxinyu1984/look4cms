from django.db import models
from users.models import MyUser
from django.utils.timezone import datetime
from django.urls import reverse

##########################################################
class Term(models.Model):

    SEASON_CHOICES = [
        ('Fall', 'Fall'),
        ('Spring', 'Spring'),
        ('Summer_1', 'Summer_1'),
        ('Summer_2', 'Summer_2')
    ]
    year = models.CharField(
        max_length=4,
        help_text="Year of the term, e.g. 2023",
        blank=False,
        verbose_name='Year'
    )
    season = models.CharField(
        max_length=8,
        choices=SEASON_CHOICES,
        help_text="Season of the term, e.g. Fall.",
        blank=False,
        verbose_name='Season'
    )
    start_date = models.DateField(
        help_text="Start date of the term.",
        verbose_name='Start Date'
    )
    end_date = models.DateField(
        help_text="End date of the term.",
        verbose_name='End Date'
    )

    def __str__(self):
        return self.year + " " + self.season.capitalize()



################################################################
class Course(models.Model):

    SUBJECT_CHOICES = [
        ('APBI', 'APBI'),
        ('APSC', 'APSC'),
        ('BIOL', 'BIOL'),
        ('CHEM', 'CHEM'),
        ('COMM', 'COMM'),
        ('COMR', 'COMR'),
        ('CPEN', 'CPEN'),
        ('CPSC', 'CPSC'),
        ('DCSI', 'DCSI'),
        ('ECON', 'ECON'),
        ('ELEC', 'ELEC'),
        ('EOSC', 'EOSC'),
        ('MATH', 'MATH'),
        ('MFRE', 'MFRE'),
        ('PHIL', 'PHIL'),
        ('PHYS', 'PHYS'),
        ('PSYC', 'PSYC'),
        ('SCIE', 'SCIE'),
        ('STAT', 'STAT'),
        ('VANT', 'VANT'),
        ('WRDS', 'WRDS'),
    ]

    subject = models.CharField(
        max_length=4,
        choices=SUBJECT_CHOICES,
        help_text="Subject code, e.g. ECON.",
        blank=False,
        verbose_name='Subject'
    )
    course_number = models.CharField(
        max_length=3,
        help_text="3-digits course number, e.g. 101.",
        blank=False,
        verbose_name='Course Number'
    )
    section = models.CharField(
        max_length=20,
        help_text="Section number, e.g. 202 or professor name. <strong>Leave it blank</strong> if there is only one section.",
        blank=True,
        verbose_name='Section'
    )
    term = models.ForeignKey(
        Term,
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Term'
    )
    tutor = models.ForeignKey(
        MyUser,
        models.SET_NULL,
        limit_choices_to={'is_tutor': True},
        blank=True,
        null=True,
        verbose_name='Tutor'
    )
    # slug = models.SlugField()

    def is_active(self) -> bool:
        return datetime.today().date() >= self.term.start_date and datetime.today().date() <= self.term.end_date

    def get_short_title(self):
        return self.subject + self.course_number + self.section

    def get_long_title(self):
        return self.subject + self.course_number + self.section + "---" + self.term.__str__()

    def __str__(self):
        return self.subject + self.course_number + " - " + self.section + self.term.__str__()
    

########################################################################

class Lecture(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        help_text="Select the course.",
        verbose_name='Course'
    )
    title = models.CharField(
        max_length=300,
        default='',
        help_text='Enter the title of the lecture, e.g. Math101 Lecture 1.',
        verbose_name='Title'
    )
    week = models.PositiveIntegerField(
        blank=False,
        help_text='Enter the week number.',
        verbose_name='Week No.'
    )
    syllabus = models.TextField(
        blank=True,
        help_text="A short syllabus of this lecture."
    )
    is_midterm = models.BooleanField(
        default=False,
        help_text="Is this a midterm review lecture? (是否为期中冲刺)",
        verbose_name='Midterm Review?'
    )
    is_final = models.BooleanField(
        default=False,
        help_text="Is this a final review lecture? (是否为期末冲刺)",
        verbose_name="Final Review?"
    )
    is_public = models.BooleanField(
        default=False,
        help_text="Is this a free sample lecture? (是否为试听课)"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Create Time'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Update Time'
    )
    # slug = models.SlugField(
    #     default = "",
    #     null = True
    # )

    def get_short_title(self):
        return "Week" + str(self.week) + "---" + self.title

    def __str__(self):
        return str(self.course) + " Week" + str(self.week) + "---" + self.title

    def get_absolute_url(self):
        return reverse('tutor_lecture_detail', args=[str(self.id)])