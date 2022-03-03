from django import forms
from .models import Category, Listing, User, Bid, Comment
from django.contrib.auth.forms import UserCreationForm

class CreateListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'image', 'starting_price']
    
    categories = forms.CharField(max_length=150, required=False)
    


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

class CreateCategoryForm(forms.Form):
    class Meta:
        model = Category
        fields = ['name']


class CreateBidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user