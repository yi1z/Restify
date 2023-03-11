# Only for testing purpose 
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getTest(request):
    test_urls  = [


        # This endpoint will give back an access token and refresh token. 
        # Delete Later: Reference: https://www.youtube.com/watch?v=xjMP0hspNLE
        '/api/token',
        # This endpoint will give back a new token based on the new refresh token we sent to the backend.
        # Delete Later: Reference: https://www.youtube.com/watch?v=xjMP0hspNLE
        '/api/token/refresh'

    ]
    return Response(test_urls)