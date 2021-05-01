from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect
from .models import shop,Item,ItemPicture
from shopper.models import Shipping

# Create your views here.

def create_shop(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        logos =request.FILES.get("logo")
        s = shop()
        s.name = name
        s.description = description
        s.logo = logos
        s.user_id = request.user.id  
        s.save()
       
        # shop(name=name,description=description,logo=logos,user_id=request.user.id).save()
        return HttpResponseRedirect("/seller/")
    else:
        return render(request,"seller/create_shop.html")
        
def index(request):
    shops = shop.objects.filter(user_id=request.user.id)
    return render(request, "seller/index.html", {
        "shops": shops
    })
def add_item(request, shop_id):
    if request.method == "POST":


       
        Item(name=request.POST["name"], discription=request.POST["discription"], price=float(request.POST["price"]), shop_id=shop_id).save()

        item = Item.objects.filter(name=request.POST["name"], discription=request.POST["discription"], price=float(request.POST["price"]), shop_id=shop_id)[::-1][0]

        images = request.FILES.getlist('images')
        for i in images:
            
            img_file = i
            ItemPicture(item_id=item.item_id, img_url=img_file).save()

        return HttpResponseRedirect(f"/seller/shop/{shop_id}/items/{item.item_id}")
    else:
        return render(request, "seller/add_item.html")

def view_item(request, shop_id, item_id):
    shops = shop.objects.get(shop_id=shop_id)
    item = Item.objects.get(item_id=item_id)
    images = ItemPicture.objects.filter(item_id=item_id)

    return render(request, "seller/view.html", {
        "shop": shops,
        "item": item,
        #"image0": images[0],
        "imgs0": images[0],
        "imgs": images[1:]
    })
def view_shop(request, shop_id):
    items = Item.objects.filter(shop_id=shop_id)
    data = []

    
    items_data = []
    for item in items:
        img = ItemPicture.objects.filter(item_id=item.item_id)[0]
        items_data.append([item, img])

    return render(request, "seller/shop.html", {
        "data": data,
        "data_length": len(data),
        "items": items_data
    })
def vieworder(request,shop_id):

    order = Shipping.objects.filter(shop_id=shop_id)    
    #order_data=[]
    #for i in order:
        #pname = Item.objects.filter(item_id=i.item_id)
        #order_data.append([i,pname])
    return render(request, "seller/orders.html", {
        "orders": order
    })
    #print(order_data.pname)


