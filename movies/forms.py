from django.forms import ModelForm

from movies.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('username', 'email', 'text')
