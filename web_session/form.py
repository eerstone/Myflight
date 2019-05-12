from django.forms import ModelForm, TextInput, PasswordInput
from web_session.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', ]  # 只显示 model 中指定的字段
        # 指定呈现样式字段、指定 CSS 样式
        widgets = {
            'username': TextInput(attrs={'class': 'text',
                                         'value': 'monkey'}),
            'password': PasswordInput(attrs={'value': '13245678', })
        }
