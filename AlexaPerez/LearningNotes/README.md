## Learning Notes
  - based on: https://levelup.gitconnected.com/how-to-implement-login-logout-and-registration-with-djangos-user-model-59442164db73
  
  #### Login And Registration
  - based on :https://docs.djangoproject.com/en/3.0/ref/contrib/auth/
  https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
  # `django.contrib.auth`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django-contrib-auth)

This document provides API reference material for the components of Django’s authentication system. For more details on the usage of these components or how to customize authentication and authorization see the [authentication topic guide](https://docs.djangoproject.com/en/3.0/topics/auth/).



## `User` model[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#user-model)

- *class* `models.``User`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User)



### Fields[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#fields)

- *class* `models.``User`

  [`User`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User) objects have the following fields:`username`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.username)Required. 150 characters or fewer. Usernames may contain alphanumeric, `_`, `@`, `+`, `.` and `-` characters.The `max_length` should be sufficient for many use cases. If you need a longer length, please use a [custom user model](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-custom-user-model). If you use MySQL with the `utf8mb4` encoding (recommended for proper Unicode support), specify at most `max_length=191` because MySQL can only create unique indexes with 191 characters in that case by default.`first_name`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.first_name)Optional ([`blank=True`](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.Field.blank)). 30 characters or fewer.`last_name`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.last_name)Optional ([`blank=True`](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.Field.blank)). 150 characters or fewer.`email`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.email)Optional ([`blank=True`](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.Field.blank)). Email address.`password`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.password)Required. A hash of, and metadata about, the password. (Django doesn’t store the raw password.) Raw passwords can be arbitrarily long and can contain any character. See the [password documentation](https://docs.djangoproject.com/en/3.0/topics/auth/passwords/).`groups`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.groups)Many-to-many relationship to [`Group`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.Group)`user_permissions`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.user_permissions)Many-to-many relationship to [`Permission`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.Permission)`is_staff`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.is_staff)Boolean. Designates whether this user can access the admin site.`is_active`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.is_active)Boolean. Designates whether this user account should be considered active. We recommend that you set this flag to `False` instead of deleting accounts; that way, if your applications have any foreign keys to users, the foreign keys won’t break.This doesn’t necessarily control whether or not the user can log in. Authentication backends aren’t required to check for the `is_active` flag but the default backend ([`ModelBackend`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.backends.ModelBackend)) and the [`RemoteUserBackend`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.backends.RemoteUserBackend) do. You can use [`AllowAllUsersModelBackend`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.backends.AllowAllUsersModelBackend) or [`AllowAllUsersRemoteUserBackend`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.backends.AllowAllUsersRemoteUserBackend) if you want to allow inactive users to login. In this case, you’ll also want to customize the [`AuthenticationForm`](https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm) used by the [`LoginView`](https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.views.LoginView) as it rejects inactive users. Be aware that the permission-checking methods such as [`has_perm()`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.has_perm) and the authentication in the Django admin all return `False` for inactive users.`is_superuser`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.is_superuser)Boolean. Designates that this user has all permissions without explicitly assigning them.`last_login`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.last_login)A datetime of the user’s last login.`date_joined`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.date_joined)A datetime designating when the account was created. Is set to the current date/time by default when the account is created.



### Attributes[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#attributes)

- *class* `models.``User`

  `is_authenticated`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.is_authenticated)Read-only attribute which is always `True` (as opposed to `AnonymousUser.is_authenticated` which is always `False`). This is a way to tell if the user has been authenticated. This does not imply any permissions and doesn’t check if the user is active or has a valid session. Even though normally you will check this attribute on `request.user` to find out whether it has been populated by the [`AuthenticationMiddleware`](https://docs.djangoproject.com/en/3.0/ref/middleware/#django.contrib.auth.middleware.AuthenticationMiddleware) (representing the currently logged-in user), you should know this attribute is `True` for any [`User`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User) instance.`is_anonymous`[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.is_anonymous)Read-only attribute which is always `False`. This is a way of differentiating [`User`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User) and [`AnonymousUser`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.AnonymousUser) objects. Generally, you should prefer using [`is_authenticated`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.is_authenticated) to this attribute.



### Methods[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#methods)

- *class* `models.``User`

  `get_username`()[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.get_username)Returns the username for the user. Since the `User` model can be swapped out, you should use this method instead of referencing the username attribute directly.`get_full_name`()[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.get_full_name)Returns the [`first_name`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.first_name) plus the [`last_name`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.last_name), with a space in between.`get_short_name`()[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.get_short_name)Returns the [`first_name`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.first_name).`set_password`(*raw_password*)[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.set_password)Sets the user’s password to the given raw string, taking care of the password hashing. Doesn’t save the [`User`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User) object.When the `raw_password` is `None`, the password will be set to an unusable password, as if [`set_unusable_password()`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.set_unusable_password) were used.`check_password`(*raw_password*)[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.check_password)Returns `True` if the given raw string is the correct password for the user. (This takes care of the password hashing in making the comparison.)`set_unusable_password`()[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.set_unusable_password)Marks the user as having no password set. This isn’t the same as having a blank string for a password. [`check_password()`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.check_password) for this user will never return `True`. Doesn’t save the [`User`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User) object.You may need this if authentication for your application takes place against an existing external source such as an LDAP directory.`has_usable_password`()[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.has_usable_password)Returns `False` if [`set_unusable_password()`](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.set_unusable_password) has been called for this user.`get_user_permissions`(*obj=None*)[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.get_user_permissions)New in Django 3.0.Returns a set of permission strings that the user has directly.If `obj` is passed in, only returns the user permissions for this specific object.`get_group_permissions`(*obj=None*)[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.get_group_permissions)Returns a set of permission strings that the user has, through their groups.If `obj` is passed in, only returns the group permissions for this specific object.`get_all_permissions`(*obj=None*)[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.get_all_permissions)Returns a set of permission strings that the user has, both through group and user permissions.If `obj` is passed in, only returns the permissions for this specific object.`has_perm`(*perm*, *obj=None*)[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.has_perm)Returns `True` if the user has the specified permission, where perm is in the format `"<app label>.<permission codename>"`. (see documentation on [permissions](https://docs.djangoproject.com/en/3.0/topics/auth/default/#topic-authorization)). If the user is inactive, this method will always return `False`. For an active superuser, this method will always return `True`.If `obj` is passed in, this method won’t check for a permission for the model, but for this specific object.`has_perms`(*perm_list*, *obj=None*)[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.has_perms)Returns `True` if the user has each of the specified permissions, where each perm is in the format `"<app label>.<permission codename>"`. If the user is inactive, this method will always return `False`. For an active superuser, this method will always return `True`.If `obj` is passed in, this method won’t check for permissions for the model, but for the specific object.`has_module_perms`(*package_name*)[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.has_module_perms)Returns `True` if the user has any permissions in the given package (the Django app label). If the user is inactive, this method will always return `False`. For an active superuser, this method will always return `True`.`email_user`(*subject*, *message*, *from_email=None*, ***kwargs*)[¶](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.email_user)Sends an email to the user. If `from_email` is `None`, Django uses the [`DEFAULT_FROM_EMAIL`](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-DEFAULT_FROM_EMAIL). Any `**kwargs` are passed to the underlying [`send_mail()`](https://docs.djangoproject.com/en/3.0/topics/email/#django.core.mail.send_mail) call.

____________________________________________________________________

#### Extending the user model to Profile
- We create a profile model that extends from the user so that we can ask for more information from the user.

class UserForm(UserCreationForm):
class Meta:
    model = User
    fields = ['username', 'password1', 'password2']

def __init__(self, *args, **kwargs):
    super(UserForm, self).__init__(*args, **kwargs)
    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'form-control'


class ProfileForm(forms.ModelForm):
    email = forms.EmailField()

class Meta:
    model = Profile
    fields = ['firstname', 'lastname', 'phonenumber', 'email']

def __init__(self, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'form-control'

#### Showing form with two forms for registration
- To show one complete form that adds to the Users table and Profile tables

{% csrf_token %}
{{ user_form.as_p }}
{{ profile_form.as_p }}

{{ form.errors}}

#### Showing work diaries depending on user
- for all work diaries in work diary show their work diaries but only if the logged in user matches the user that created the work diary.

{% if all_workdiary %}
        <div class="list">
        {% for workdiary in all_workdiary %}
            {% if workdiary.userID == request.user %}
                <p class="list-item"><a href="/PyTraker/workdiary_detail/{{ workdiary.id }}">{{ workdiary.name }} | {{ workdiary.projectID.name }} | {{workdiary.date }}</a></p>
            {% endif %}
        {% endfor %}
        </div>
    {% else %}
        <p> No Work Diaries yet!</p>
{% endif %}


#### 