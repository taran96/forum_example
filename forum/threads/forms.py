from django.forms import ModelForm

from threads.models import Thread, Comment


class ThreadForm(ModelForm):
    '''Form for threads'''

    class Meta:
        model = Thread
        fields = ('title', 'text')


class CommentForm(ModelForm):
    '''Form for comments'''

    class Meta:
        model = Comment
        fields = ('text',)
