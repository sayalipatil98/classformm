from django import forms

class Studentform(forms.Form):
    sid=forms.IntegerField()
    snm=forms.CharField(max_length=100)
    sem=forms.EmailField()
