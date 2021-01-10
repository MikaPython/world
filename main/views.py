from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CountryForm, ImageForm
from .models import *


def index(request):
    return render(request, 'index.html')

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    countries = Country.objects.filter(category_id=slug)
    return render(request, 'category-detail.html', locals())

def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    image = country.get_image
    images = country.images.exclude(id=image.id)
    return render(request, 'country-detail.html', locals())

def add_country(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5)
    if request.method == 'POST':
        country_form = CountryForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if country_form.is_valid() and formset.is_valid():
            country = country_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                Image.objects.create(image=image, country=country)
            return redirect(country.get_absolute_url())
        else:
            country_form = CountryForm()
            formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'add-country.html', locals())


def update_country(request, pk):
    pass
