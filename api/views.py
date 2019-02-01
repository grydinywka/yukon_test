from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
import json
import base64

from blog.models import BlogPost


class BlogPostView(View):
    def get(self, request):
        user = get_user(request)
        if not user:
            return JsonResponse({"error": "not valid auth"}, safe=False)
        blogpost_list = list(BlogPost.objects.values())
        return JsonResponse(blogpost_list, safe=False)

    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            # print(request.META)
            user = get_user(request)
            if not user:
                return JsonResponse({"error": "not valid auth"}, safe=False)
            new_blogpost = BlogPost(name=data["name"], text=data["text"], created_by_id=user.id)
            new_blogpost.save()
            return JsonResponse({"created": data}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)


class BlogPostItemView(View):
    def get(self, request, pk):
        user = get_user(request)
        if not user:
            return JsonResponse({"error": "not valid auth"}, safe=False)
        blogpost = list(BlogPost.objects.filter(pk=pk).values())
        return JsonResponse(blogpost, safe=False)

    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def put(self, request, pk):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            user = get_user(request)
            if not user:
                return JsonResponse({"error": "not valid auth"}, safe=False)
            blogpost_item = BlogPost.objects.get(pk=pk)
            if user.id != blogpost_item.created_by_id:
                return JsonResponse({"error": "You don't have access to the object!"}, safe=False)

            changed = False
            for key in data:
                if key == 'name':
                    blogpost_item.name = data[key]
                    changed = True
                if key == 'text':
                    blogpost_item.text = data[key]
                    changed = True
            if changed == True:
                blogpost_item.save()
                return JsonResponse({"updated": data}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)

    def delete(self, request, pk):
        try:
            blogpost_item = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return JsonResponse({"error": "Object with specified id does not exist!"}, safe=False)
        user = get_user(request)
        if not user:
            return JsonResponse({"error": "not valid auth"}, safe=False)
        if user.id != blogpost_item.created_by_id:
            return JsonResponse({"error": "You don't have access to the object!"}, safe=False)
        blogpost_item.delete()
        return JsonResponse({"deleted": True, "pk_obj": pk}, safe=False)


def get_user(request):
    auth_header = request.META['HTTP_AUTHORIZATION']
    encoded_credentials = auth_header.split(' ')[1]  # Removes "Basic " to isolate credentials
    decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
    username = decoded_credentials[0]
    password = decoded_credentials[1]
    return authenticate(username=username, password=password)

def check_none_user(user):
    if not user:
        return JsonResponse({"error": "not valid auth"}, safe=False)