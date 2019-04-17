from django.contrib import admin

# Register your models here.
from polls.models import Poll, Question, Choice


class QuestionInline(admin.StackedInline): #normal Inline
    model = Question
    extra = 1 #normally Django will add 3 extra for admin in case that admin want to add something new

class PollAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'del_flag']
    list_per_page = 10

    list_filter = ['start_date', 'end_date', 'del_flag']
    search_fields = ['title']

    # fields = [''] #choose field
    # exclude = ['']#like except
    fieldsets = [
        (None, {'fields':['title', 'del_flag']}),
        ("Active Duration", {'fields': ['start_date', 'end_date'], 'classes': ['collapse']})
    ]

    inlines = [QuestionInline]

admin.site.register(Poll, PollAdmin)

#====================================================================================================================================================
class ChoiceInline(admin.TabularInline): # this is table inline
    model = Choice
    extra = 1  # normally Django will add 3 extra for admin in case that admin want to add something new

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'text']
    list_per_page = 15

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
#====================================================================================================================================================

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'text', 'value']
    list_per_page = 15

admin.site.register(Choice, ChoiceAdmin)
#====================================================================================================================================================
