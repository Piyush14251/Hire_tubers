from django.shortcuts import get_object_or_404, render
from .models import Youtubers
# Create your views here.



def youtubers(request):
    Tubers = Youtubers.objects.order_by('-created_date')
    data = {
        'Tubers': Tubers
    }
    return render(request, 'youtubers/youtubers.html', data)




def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtubers, pk=id)
    data = {
        'tuber': tuber
    }
    return render(request, 'youtubers/youtuber_detail.html', data)


def search(request):
    Tubers = Youtubers.objects.order_by('-created_date')
    city_search = Youtubers.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtubers.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtubers.objects.values_list('category', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
          Tubers = Tubers.filter(description__icontains=keyword)  

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            Tubers = Tubers.filter(city__iexact=city)  

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            Tubers = Tubers.filter(camera_type__iexact=camera_type)       

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            Tubers = Tubers.filter(category__iexact=category)       

    data = {
        'Tubers': Tubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'category_search': category_search
        


    }

   
    return render(request, 'youtubers/search.html', data)