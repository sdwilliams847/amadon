from django.shortcuts import render, redirect
PRODUCTS = [
    {
        "id": 1,
        "name": "Dojo Tshirt",
        "price": "19.99",
    },
    {
        "id": 2,
        "name": "Dojo Sweater",
        "price": "29.99",        
    },
    {
        "id": 3,
        "name": "Dojo Cup",
        "price": "4.99",        
    },
    {
        "id": 4,
        "name": "Algorithm Book",
        "price": "49.99",        
    }
]


def index(request):

    return render(request, 'amadon_app/index.html', {'products':PRODUCTS})

def buy(request):
    request.session['POST'] = request.POST
    quantity = request.session['POST']['quantity']

    if 'total' not in request.session:
        request.session['total'] = 0
    if 'itemCount' not in request.session:
        request.session['itemCount'] = 0
    for element in PRODUCTS:
        if str(element['id']) == request.session['POST']['product_id']:
            request.session.cost = int(request.session['POST']['quantity']) * int(element['price'])
            request.session['total'] += request.session.cost
            request.session['itemCount'] += int(quantity)

            request.session['newDict'] = {
                'id' : element['id'],
                'name' : element['name'],
                'cost' : request.session.cost,
                'total' : request.session['total'],
                'quantity' : request.session['itemCount'],
            }
            
            print request.session['newDict']

    return redirect('/thankYou')


def thankYou(request):

    return render(request, 'amadon_app/thanks.html')
