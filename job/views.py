from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import JobCreateForm
from .models import Job, City, Region
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse #Region City ni tanlashda ishlatiladigan JavaScript uchun
from datetime import date, datetime
from django.conf import settings


class LangView():
    """Barcha `CreateView` lar uchun `.lang` ma’lumotini qo‘shuvchi sinf"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lang"] = settings.GLOBAL_LANG  # `.lang` fayldan ma’lumot olish
        return context


class HomeView(LangView, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.order_by('-id')[:15]

        # Buguni bilan joylangan ishlar sonini hisoblash

        datetime = date.today()
        job_count_today = Job.objects.filter(date__gte=datetime.today()).count()
        context['job_count_today'] = job_count_today

        job_count_all = Job.objects.filter().count()
        context['job_count_all'] = job_count_all




        return context

class MyJobListView(ListView):
    model = Job
    template_name = 'user_job_list.html'
    context_object_name = 'userposts'

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_user_model().objects.get(username=username)
        return self.model.objects.filter(author=user)

class RegionListView(ListView):
    model = Region
    template_name = 'region_list.html'
    context_object_name = 'regions'
    paginate_by = 10

class RegionDetailView(DetailView):
    model = Region
    template_name = 'region_detail.html'
    context_object_name = 'region'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jobs = Job.objects.filter(region=self.object).order_by('-id')
        paginator = Paginator(jobs, 10)  # Har sahifada 10 ta ish
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['jobs'] = page_obj

        datetime = date.today()
        job_count_today = Job.objects.filter(region_id=self.object.id, date__gte=datetime.today()).count()
        context['job_count_today'] = job_count_today


        return context



class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'
    context_object_name = 'jobs'
    paginate_by = 10 #pogination test1


class JobDetailView(DetailView):
    model = Job
    template_name = 'job_detail.html'

class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = ('name', 'description', 'start_time', 'end_time', 'phone_number', 'salary', 'salary_period', 'address', 'region', 'city')
    template_name = 'job_edit.html'


    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser

class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    template_name = 'job_delete.html'

    def get_success_url(self):
        user_pk = self.object.author
        return reverse_lazy('user_job_list', args=[user_pk])

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_superuser

class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    template_name = 'job_new.html'
    form_class = JobCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user

        # Quyidagi satr kiritilgan postlarni tekshirish uchun
        # formni ishlatamiz
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        region = form.cleaned_data['region']
        city = form.cleaned_data['city']


        # Bu postlardan biri borligini tekshiramiz
        # Misol uchun, ismni va matnni o'zgartiring
        existing_post = Job.objects.filter(name=name, description=description, region=region, city=city).exists()

        if existing_post:
            # Agar bir xil post topilsa, o'tkazib yuborishni to'xtatamiz
            return render(self.request, 'job_new.html', {'error_message': 'Bu post allaqachon mavjud!'}) # Xato sahifasiga yo'nalish

        return super().form_valid(form)  # Agar bir xil post topilmasa, saqlashni davom ettiramiz



def get_cities(request, region_id):
        cities = City.objects.filter(region_id=region_id).values('id', 'name')
        return JsonResponse(list(cities), safe=False)









