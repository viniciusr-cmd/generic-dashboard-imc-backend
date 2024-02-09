from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET", "POST"])
def person_list(request):
    if request.method == "GET":
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response({"person":serializer.data})
    elif request.method == "POST":
        person_data = PersonSerializer(data=request.data)
        if person_data.is_valid():
            person_data.save()
            return Response(person_data.data, status=status.HTTP_201_CREATED)
        return Response(person_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def person_detail(request, id):
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        return Response({"message": "The person does not exist!"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        person_serializer = PersonSerializer(person)
        return Response(person_serializer.data)
    elif request.method == "PUT":
        person_data = PersonSerializer(person, data=request.data)
        if person_data.is_valid():
            person_data.save()
            return Response(person_data.data)
        return Response(person_data.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        person.delete()
        return Response({"message": "Person was deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def peso_ideal(request, id):
    try:
        person = Person.objects.get(pk=id)
        sexo = person.sexo
    except Person.DoesNotExist:
        return Response({"message": "The person does not exist!"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        if sexo == "M":
            peso_ideal = (72.7 * person.altura) - 58
        elif sexo == "F":
            peso_ideal = (62.1 * person.altura) - 44.7
        # Return response format float with 2 decimal places
        return Response({"peso_ideal": float("{:.2f}".format(peso_ideal))})

@api_view(["GET"])
def healthCheck():
    return Response({"status": "ok"})

