from django import forms

class LogInForm(forms.Form):
    css_class={"username":"block w-full px-4 py-2 mt-2 text-gray-700 bg-white border rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40",
    "password":"block w-full px-4 py-2 mt-2 text-gray-700 bg-white border rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40"}
    username=forms.CharField(label='Username')
    password=forms.CharField(widget=forms.PasswordInput,label='Password')
    username.widget.attrs.update({'class':css_class['username']})
    password.widget.attrs.update({'class':css_class['password']})