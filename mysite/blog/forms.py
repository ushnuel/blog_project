from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text')

        #CREATE WIDGETS DICTIONARY THAT WILL HELP YOU STYLE EACH INPUT
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'title of post'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','text')

        #CREATE WIDGETS DICTIONARY THAT WILL HELP YOU STYLE EACH INPUT IN THE COMMENT
        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
