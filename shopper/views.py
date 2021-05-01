from django.shortcuts import render
from seller.models import Item,ItemPicture,shop
from .models import PageView,CartItem,Shipping

#import requests
#import xmltodict
import json
#from authentication.models import Profile
import datetime
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect,HttpResponse
import json

# Create your views here.
def sort_item(queryset):
    results = {}
    for i in queryset:
        try:
            results[i.item_id] = results[i.item_id] + 1
        except KeyError:
            results[i.item_id] = 1
    return results
def index(request):
    if request.GET.get("q") is not None:
        query = request.GET.get("q")
        results = []
        items = Item.objects.filter(name__contains=query) | \
                Item.objects.filter(discription__contains=query) | \
                Item.objects.filter(item_id__contains=query)

        for i in items:
            item_pic = ItemPicture.objects.filter(item_id=i.item_id)[0]
            results.append([item_pic, i])

        return render(request, "shopper/search.html", {
            "items": results,
            "q": query
        })
    
    else:
        current_hour = datetime.datetime.now().hour
        #slogo=shop()
        

        try:
            PageView.objects.filter(timestamp__hour=str(current_hour-1)).delete()
        except Exception as e:
            print(e)
            PageView.objects.filter(timestamp__hour=str(current_hour)).delete()

        popular_items = []
        result = sort_item(PageView.objects.filter())
        print(result)
        for i in result:
            item = Item.objects.get(item_id=i)
            pic = ItemPicture.objects.filter(item_id=item.item_id)[0]
            popular_items.append([item, result[i], pic])

        return render(request, "shopper/index.html", {
            "popular": popular_items,

            #"shops": slogo
             
        })    

def view_item(request,item_id):
    
    item = Item.objects.get(item_id=item_id)
    images = ItemPicture.objects.filter(item_id=item_id)
    
    PageView(item_id=item_id).save()
    print(images[1:])

    return render(request, "shopper/viewitem.html", {
        
        "item": item,
        #"image0": images[0],
        "imgs0": images[0],
        "imgs": images[1:]
    })  
@csrf_exempt
def add_cart(request):

    post_data = json.loads(request.body.decode("utf-8"))
    # https://stackoverflow.com/questions/61543829/django-taking-values-from-post-request-javascript-fetch-api

    item_id = post_data["item_id"]
    quantity = post_data["quantity"]
    user_id = request.user.id

    CartItem(item_id=item_id, user_id=user_id, quantity=quantity).save()

    return JsonResponse({"code": 200})


def cart(request):
    data = []
    items = CartItem.objects.filter(user_id=request.user.id)
    price = 0

    for i in items:
        item = Item.objects.get(item_id=i.item_id)
        pic = ItemPicture.objects.filter(item_id=i.item_id)[0]
        data.append([item, i, pic])
        print(i.quantity)
        price = (item.price * i.quantity)

    return render(request, "shopper/cart.html", {
        "data": data,
        "price": '%.2f' % round(price, 2)
    })

@csrf_exempt
def delete_cart(request):

    post_data = json.loads(request.body.decode("utf-8"))
    # https://stackoverflow.com/questions/61543829/django-taking-values-from-post-request-javascript-fetch-api

    item_id = post_data["item_id"]
    user_id = request.user.id

    CartItem.objects.get(item_id=item_id, user_id=user_id).delete()

    return JsonResponse({"code": 200})
@csrf_exempt
def modify_cart(request):

    post_data = json.loads(request.body.decode("utf-8"))
    item_id = post_data["item_id"]
    user_id = request.user.id
    quantity = post_data["quantity"]

    c = CartItem.objects.get(user_id=user_id, item_id=item_id)
    c.quantity = quantity
    c.save()

    return JsonResponse({"code": 200})

def checkout(request):
    if request.method == "POST":
        sfname = request.POST["sname"]
        slname =request.POST["slname"]
        smail =request.POST["mid"]
        sphone =request.POST["ph"]
        address = request.POST["adrs"]
        state = request.POST["state"]
        city =request.POST["city"]
        zip = request.POST["zip"]
        items = CartItem.objects.filter(user_id=request.user.id)
        
        for i in items:
            item = Item.objects.get(item_id=i.item_id)
            quantity = i.quantity
            print(item.item_id,"itemmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
            print(item.shop_id,"shopppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
            print(i.item_id,"iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii") 
            s=Shipping()
            s.firstname=sfname
            s.lastname=slname
            s.email=smail
            s.mobile=sphone
            
            s.address=address
            s.state=state
            s.city=city
            s.pincode=zip
            s.shop_id=item.shop_id
            s.item_id=i.item_id
            s.quantity=quantity
            s.save()
            
        
            

        
            
          
        
        return HttpResponse("order placed successfully seller will contact you shortly")
        print(item.item_id)
        print(quantity)    
    else:
        return render(request,"shopper/checkout.html")    
