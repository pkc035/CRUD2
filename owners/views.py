import json

from django.views import View
from django.http import JsonResponse
from .models import Owner,Dog

class OwnerListView(View) :
    def post(self,request) :
        data = json.loads(request.body)

        Owner.objects.create(name=data['name'], email=data['email'], age=data['age'])

        return JsonResponse({'result':'SUCCESS'},status=200)


class DogListView(View):
    def post(self,request) :
        data = json.loads(request.body)
        data_owner = Owner.objects.filter(name=data['owner'])

        Dog.objects.create(name=data['name'], age=data['age'],owner=data_owner[0])

        return JsonResponse({'result':'SUCCESS'},status=200)

