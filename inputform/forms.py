from django import forms

class InputForm(forms.Form):
    subject = forms.CharField(label='取り扱い会社種別', max_length=100)
    office = forms.CharField(label='Email', help_text='※ご確認の上、正しく入力してください。')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
    myself = forms.BooleanField(label='同じ内容を受け取る', required=False)
