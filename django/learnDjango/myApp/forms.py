from django import forms
from django.core import validators
# the classes which manage forms in django extends of django forms
class FormArticle(forms.Form):
    title = forms.CharField(
        label = "Title",
        max_length = 40,
        required = True, # This atribute disable the required field vallidation
        widget = forms.TextInput( 
            attrs = { # add some customization like classes
                'placeholder': 'Type the title',
                'class': 'Article_title'
            }
        ),
        validators = [
            validators.MinLengthValidator(4, 'The title is too short'),
            validators.RegexValidator('^[A-Za-z0-9 ]*$', 'The title has invalid format', 'invalid_title') # use ^ validatios *$ for indicate that this field can validate multiples values
        ]
    )
    content = forms.CharField(
        label = "Content",
        widget = forms.Textarea,
        validators = [
            validators.MaxLengthValidator(200,'The text is too long')
        ]
    )
    content.widget.attrs.update({
        'placeholder': 'Type the content here',
        'class': 'Article_content'
    })
    public_options = [
        (1,'Yes'),
        (0, 'No')
    ]
    public = forms.TypedChoiceField(
        label = "Public?",
        choices = public_options 
    )
