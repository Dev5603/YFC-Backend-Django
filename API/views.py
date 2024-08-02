import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import User, Offer, Plan, Blog, Comment

# Create your views here.
@csrf_exempt
def users(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')

            newUser = User(
                name = name,
                email = email,
            )

            newUser.save()

            return JsonResponse({
                'message': 'User added successfully'
            }, status=201)

        except User.DoesNotExist():
            return JsonResponse({
                'message': 'Something went wrong'
            }, status=500)

def offers(request):
    try:
        offers = Offer.objects.all()
        offers = [offer.serialize() for offer in offers]

        return JsonResponse({
            'offers': offers
        }, status=200)
    except Offer.DoesNotExist():
        return JsonResponse({
            'message': 'Something went wrong'
        }, status=500)
    
def offer(request, name):
    try:
        offer = Offer.objects.get(name=name)
        offer = offer.serialize()

        return JsonResponse({
            'offer': offer
        }, status=200)
    except Offer.DoesNotExist():
        return JsonResponse({
            'message': 'Something went wrong'
        }, status=500)

def plans(request):
    try:
        plans = Plan.objects.all()
        plans = [plan.serialize() for plan in plans]

        return JsonResponse({
            'plans': plans
        }, status=200)
    except Plan.DoesNotExist():
        return JsonResponse({
            'message': 'Something went wrong'
        }, status=500)
    
def plan(request, name):
    try:
        plan = Plan.objects.get(name=name)
        plan = plan.serialize()

        return JsonResponse({
            'plan': plan
        }, status=200)
    except Plan.DoesNotExist():
        return JsonResponse({
            'message': 'Something went wrong'
        }, status=500)
    
def blogs(request):
    try:
        blogs = Blog.objects.all()
        blogs = [blog.serialize() for blog in blogs]

        return JsonResponse({
            'blogs': blogs
        }, status=200)
    except Blog.DoesNotExist():
        return JsonResponse({
            'message': 'Something went wrong'
        }, status=500)
    
def blog(request, title):
    try:
        blog = Blog.objects.get(title=title)
        blog = blog.serialize()

        return JsonResponse({
            'blog': blog
        }, status=200)
    except Blog.DoesNotExist():
        return JsonResponse({
            'message': 'Something went wrong'
        }, status=500)
    
@csrf_exempt
def addComment(request, id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            comment = data.get('comment')
            
            blog = Blog.objects.get(id=id)

            if not name or not comment:
                return JsonResponse({
                    'message': 'All fields are required'
                }, status=400)
            
            newComment = Comment(
                name = name,
                comment = comment,
                blog = blog
            )

            newComment.save()

            return JsonResponse({
                'message': 'Comment added successfully'
            }, status=201)
        except Comment.DoesNotExist():
            return JsonResponse({
                'message': 'Something went wrong'
            }, status=500)