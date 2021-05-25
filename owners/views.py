import json

from django.views import View
from django.http import JsonResponse
from .models import Owner,Dog

class OwnerListView(View) :
    def post(self,request) :
        data = json.loads(request.body)

        Owner.objects.create(name=data['name'], email=data['email'], age=data['age'])

        return JsonResponse({'result':'SUCCESS'},status=200)

    def get(self,request) :

        owners = Owner.objects.all()
        
        result = []
        

        for owner in owners :
            name = owner.name
            email = owner.email
            age = owner.age

            dog_list = []
            dogs_info = owner.dog_set.all()

            for dog_info in dogs_info :
                if owner.id == dog_info.owner_id :
                    dog_name = dog_info.name
                    dog_age = dog_info.age

                    dog_dic = {"name" : dog_name, "age" : dog_age}
                    dog_list.append(dog_dic)

            text = {"name" : name, "email" : email, "age" : str(age), "Dog" : dog_list}

            result.append(text)

        return JsonResponse({'result':result}, status=200)


class DogListView(View):
    def post(self,request) :
        data = json.loads(request.body)
        data_owner = Owner.objects.filter(name=data['owner'])

        Dog.objects.create(name=data['name'], age=data['age'],owner=data_owner[0])

        return JsonResponse({'result':'SUCCESS'},status=200)

    
    def get(self,request) :

        dogs = Dog.objects.all()

        result = []

        for dog in dogs :
            name = dog.name
            age = dog.age
            owner = dog.owner.name

            text = {"name":name,"age":str(age),"owner":owner}

            result.append(text)
            

        return JsonResponse({'result':result}, status=200)

