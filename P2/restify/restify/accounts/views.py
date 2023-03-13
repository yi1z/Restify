from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from . serializers import ThisUserSerializer, ThisUserUpdateSerializer, ListReservationSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView,ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ThisUser, Reserve

# Create your views here.

class UserCreate(CreateAPIView):
    serializer_class = ThisUserSerializer

class UserEdit(UpdateAPIView):
    serializer_class = ThisUserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(ThisUser, id=self.kwargs['pk'])


# List all of reservations
class ListReservation(ListAPIView):
    serializer_class = ListReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # A queryset of all user's reservations as client
        client_queryset = Reserve.objects.filter(user=self.request.user)

        # A querset of all user's reservations as host
        # reference: https://docs.djangoproject.com/en/4.1/topics/db/queries/#following-relationships-backward
        host_queryset = Reserve.objects.all().filter(property__owner=self.request.user)
        # A queryset of all user's 
        # reference: https://docs.djangoproject.com/en/4.1/ref/models/querysets/#or
        all_query = client_queryset | host_queryset
        print('here')
        return all_query
    

class ListReservationFilterView(ListAPIView):
    serializer_class = ListReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        q = None
        kwarg = self.kwargs['type_user']
        if kwarg == 'client':
            # A queryset of all user's reservations as client
            q = Reserve.objects.filter(user=self.request.user)

        elif kwarg == 'host':
            # A querset of all user's reservations as host
            # reference: https://docs.djangoproject.com/en/4.1/topics/db/queries/#following-relationships-backward
            q = Reserve.objects.all().filter(property__owner=self.request.user)
        else:
            # A queryset of all user's 
            # reference: https://docs.djangoproject.com/en/4.1/ref/models/querysets/#or
            q = Reserve.objects.filter(user=self.request.user) | Reserve.objects.all().filter(property__owner=self.request.user)
        print('here')
        print(self.request.user)

        return q
    
class ListReservationStateFilterView(ListAPIView):
    serializer_class = ListReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        # Share status
        host_status = ['pending', 'approve', 'cancel_request', 'complete', 'terminate ', 'cancel_by_user']
        client_status = ['pending', 'denied', 'approve', 'cancel', 'complete', 'terminate_by_host']
        q = None
        user_type = self.kwargs['type_user']
        state = self.kwargs['state']
        if user_type == 'client':
            # A queryset of all user's reservations as client
            if state in client_status and state == 'approve':
                q = Reserve.objects.filter(user=self.request.user, status=state)
            else:
                q = Reserve.objects.none()
                print('client_empty_here')
        elif user_type == 'host':
            if state in host_status:
                # There are two type of complete: one is reservation normally complete, the other one is cancel by user.
                q = Reserve.objects.filter(property__owner=self.request.user, status=state)
            else:
                q = Reserve.objects.none()
                print('host_empty_here')
        return q
    
class DetailReservation(RetrieveAPIView):

    serializer_class = ListReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Reserve, id=self.kwargs['pk'])


class DetailReservationStateUpdateView(RetrieveAPIView):
    serializer_class = ListReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # User can only make a request to cancel reservation if user already approved. If user's reservation request is pending, user can cancel it directly without approve.

        # Host can approve/denied pending reservation, deny cancel request, and terminate reservation
        return get_object_or_404(Reserve, id=self.kwargs['pk'])