from django import forms
from .models import Job

class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('name', 'description', 'salary', 'salary_period', 'start_time', 'end_time', 'phone_number', 'address', 'region', 'city')


    def clean_salary(self):
        salary = self.cleaned_data.get('salary')

        def format_number(salary):
            # Sonni ifodalash uchun `,` belgisini qo'shamiz
            formatted_number = "{:,.0f}".format(float(salary.replace(' ', '').replace(',', '')))
            return formatted_number

        try:
            # Sonni raqamga o'tkazamiz va to'g'ri formatlash uchun format_number funksiyasini ishlatamiz
            salary = format_number(salary)
        except ValueError:
            # Sonni raqamga o'girib bo'lmagan holda qolgan belgilarni olib tashlaymiz
            salary = ''.join([c for c in salary if c.isdigit()])

        return salary

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser
