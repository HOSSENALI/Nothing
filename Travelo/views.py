from django.shortcuts import render
from .models import Destination


# Create your views here.
def index(request):
    des1 = Destination()
    des1.name = "Dhaka"
    des1.des = "It is a populated city"
    des1.img = "destination_1.jpg"
    des1.price = "700"
    des1.offer = False

    des2 = Destination()
    des2.name = "Khunla"
    des2.des = "It is a beautiful city"
    des2.img = "destination_2.jpg"
    des2.price = "800"
    des2.offer = True
    des3 = Destination()
    des3.name = "Barishal"
    des3.des = "It is a beautiful city"
    des3.img = "destination_3.jpg"
    des3.price = "500"
    des3.offer = False

    dests = [des1, des2, des3]

    print(dests)

    return render(request, "index.html", {'destinations': dests})
