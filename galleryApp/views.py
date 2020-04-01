from django.shortcuts import render
from django.http import HttpResponse
from galleryApp.models import Showroom, Brand, Bike

# Create your views here.
def index(request):
    showroom_list = Showroom.objects.all()
    # brand_list = Brand.objects.all()
    # brand_list.save()
    # bike_list = Bike.objects.all()
    # bike_list.save()
    showroom_dict={ "showroom_names": showroom_list}

    # bike_dict= {
    #             'brand_name':bike_list.brand, 'bike_name': bike_list.model,
    #             'bike_price':bike_list.price, 'bike_color': bike_list.color,
    #             'bike_cc': bike_list.cc,
    #             }

    return render(request,'galleryApp/gallery.html',context=showroom_dict)
