from django.shortcuts import render, get_object_or_404
from .models import Restaurant
from django.core.serializers import serialize
from .forms import RestaurantFilterForm
from  django.db.models import Q 


# Create your views here.
def search_page(request):
    return render(request, 'restaurants/search.html')



def home(request):
    return render(request, 'restaurants/home.html')

def map_restaurants(request):

    form = RestaurantFilterForm(request.GET)
    if form.is_valid():
        cuisine_type = form.cleaned_data.get('cuisine_type')
        min_rating = form.cleaned_data.get('min_rating')

        if cuisine_type:
            restaurants = Restaurant.filter(cuisine_type__icontains=cuisine_type)
        if min_rating:
            restaurants = Restaurant.filter(rating_gte=min_rating)
    
    restaurants = Restaurant.objects.filter(is_24_hours=True)
    restaurants_geojson = serialize('geojson', restaurants, geometry_field='location', fields=('name', 'cuisine_type', 'rating'))

    return render(request, 'restaurants/map.html', {'restaurants': restaurants_geojson, 'form': form})

    print(type(restaurants_geojson)) 


def search_results(request):

    query = request.GET.get('query', '')
    results = None 
    if query:
        results = Restaurant.objects.filter(
            Q(name__icontains=query) | Q(cuisine_type__icontains=query) | Q(location__icontains=query)
        )
    return render(request, "restaurants/search_results.html",  {"query": query, "results": results})



#FOR Nearby Restaurants Endpoint
from django.http import JsonResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.http import JsonResponse

def nearby_restaurants(request):
    try:
        user_lat = float(request.GET.get('lat', 0))
        user_lng = float(request.GET.get('lng', 0))

        if user_lat == 0 or user_lng == 0:
            return JsonResponse({'error': 'Invalid or missing coordinates'}, status=400)
        
        user_location = Point(user_lng, user_lat, srid=4326)

        print(f"User location: {user_location}")

        restaurants = Restaurant.objects.filter(
            location__distance_lte=(user_location, D(km=5))
        ).annotate(distance=Distance('location', user_location)).order_by('distance')


        print(f"Nearby restaurants: {nearby_restaurants}")

        data = {
            'restaurants': [
                {
                    'name': restaurants.name,
                    'description': restaurants.description,
                    'rating': restaurants.rating,
                    'distance_km': round(restaurants.distance.km, 2),
                    'latitude': restaurants.location.y,
                    'longitude': restaurants.location.x, 
                } 
                for  restaurant in nearby_restaurants
            ]
        }

        print(f"Serialized data: {data}")

        return JsonResponse({'restaurants': data}, status=200)
    
    except ValueError as e:
        #Debug login error
        print(f"Error: {e}")
        return JsonResponse({'error': 'Coordinates must be valid numbers'}, status=400)


def restaurant_detail(request, pk):
    restaurants = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurants})



from django.http import JsonResponse
import json

#Ensure only valid  restaurants are passed to the template 
def map_restaurants(request):
    restaurants = Restaurant.objects.exclude(id__isnull=True)

    #Serialize the data JSON-compatible format 
    serialized_restaurants = json.loads(serialize('json', restaurants, fields=('name', 'address', 'cuisine_type', 'rating', 'location')))

    return render(request, 'restaurants/map.html', {'restaurants': serialized_restaurants})


