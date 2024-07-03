from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                "placeholder": "Username",
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                "placeholder": "Password",
            }
        )
