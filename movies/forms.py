from django import forms



class ReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    rating = forms.DecimalField(max_value=10,
                                min_value=1,
                                max_digits=3,
                                decimal_places=1,
                                step_size=0.5)
    author = forms.CharField(max_length=50)
