from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import reverse
from .models import Links
from .forms import LinkForm
# Create your views here.
def index(request):
    link_data = Links.objects.all()
    links = {'links': link_data}
    # print(link_data)
    return render(request, 'links/index.html', links)

def link_redirect(request, root_link):
    specific_object = get_object_or_404(Links, slug = root_link)
    # print("############")
    specific_object.click()
    print(specific_object.url)
    return redirect(specific_object.url)

def create_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            print("FORM IS VALID")
            print(form.cleaned_data)
            form.save()

            return redirect(reverse("home"))
    else:
        form = LinkForm()
    context = {
        "form": form
    }
    return render(request, 'links/create.html', context)
    # post_data = request.POST
    # print(post_data.get('link'))
    # print("##########")
    # print("link")
