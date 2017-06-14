from django import forms
from .models import BlogPost, Comment

class PostForm(forms.ModelForm):

	class Meta:
		model = BlogPost
		fields = ('title', 'body',)

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('author', 'text',)