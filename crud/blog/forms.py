from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Title', 'Writer', 'Contents',)
        widgets = {
            'Title': forms.TextInput(attrs={'class': 'title', 'placeholder': '제목을 입력해주세요'}),
            'Writer': forms.TextInput(attrs={'class': 'writer'}),
            'Contents': forms.TextInput(attrs={'class': 'contents'})
        }
        # widget: modelForm의 각각의 form객체에 class,placeholder 등 속성부여
        labels = {
            'Title': '제목',
            'Writer': '글쓴이',
            'Contents': '본문'
        }
        # labeling : model 객체가 화면에 표시되는 이름

# comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('content',)
        widgets = {
            'content': forms.TextInput(attrs={'class': 'content', 'placeholder': '댓글을 달아주세요'}),
        }
        labels = {
            'content': '댓글',
        }

