from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list":[
            {
                "restaurant_name":"Jabri",
                "food_type":"Mansaf"
            },
            {
                "restaurant_name":"firefly",
                "food_type":"wallstreet"
            },
            {
                "restaurant_name":"pizzhut",
                "food_type":"paparone pizza"
            }
        ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object":{
            "restaurant_name":"Jabri",
            "food_type":"Mansaf"
        }
    }
    return render(request, 'detail.html', context)
