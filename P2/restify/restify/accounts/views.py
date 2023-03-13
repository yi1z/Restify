from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from . serializers import ThisUserSerializer, ThisUserUpdateSerializer, ListReservationSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView,ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ThisUser, Reserve
from datetime import datetime

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
        host_status = ['pending', 'approve', 'cancel_request', 'complete', 'terminate']
        client_status = ['pending', 'denied', 'approve', 'cancel', 'complete']
        q = None
        user_type = self.kwargs['type_user']
        state = self.kwargs['state']
        
        # Before check the state, we want to update all approved request end_date is yestersday.
        complete_update_queryset = Reserve.objects.filter(status='approve', end_date__lt=datetime.today())
        for each_query in complete_update_queryset:
            each_query.status = 'complete'
            each_query.save()
        
        if user_type == 'client':
            # A queryset of all user's reservations as client
            if state in client_status:
                q = Reserve.objects.filter(user=self.request.user, status=state, end_date__gte=datetime.today())     
            else:
                q = Reserve.objects.none()
                print('client_empty_here')
        elif user_type == 'host':
            if state in host_status:
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
        user_type = self.kwargs['type_user']
        action_on_reservation_id = self.kwargs['pk']
        status = self.kwargs['state']
        action = self.kwargs['action']
        
        # User can only make a request to cancel reservation if user already approved. If user's reservation request is pending, user can cancel it directly without approve.
        if user_type == 'client':
            if status in ['pending', 'approve']:
                if status == 'pending' and action == 'cancel':
                    instance = Reserve.objects.filter(id=action_on_reservation_id, user=self.request.user, status=status)
                    if instance:
                        instance.status = 'cancel'
                        instance.save()
                elif status == 'approve' and action == 'cancel':
                    instance = Reserve.objects.filter(id=action_on_reservation_id, user=self.request.user, status=status)
                    if instance:
                        instance.status = 'cancel_request'
                        instance.save()
                
        # Host can approve/denied pending reservation, deny cancel request, and terminate reservation
        elif user_type == 'host':
            if status in ['pending', 'approve', 'cancel_request']:
                if status == 'pending' and action == 'approve':
                    instance = Reserve.objects.filter(id=action_on_reservation_id, property__owner=self.request.user, status=status)
                    if instance:
                        instance.status = 'approve'
                        instance.save()
                elif status == 'pending' and action == 'denied':
                    instance = Reserve.objects.filter(id=action_on_reservation_id, property__owner=self.request.user, status=status)
                    if instance:
                        instance.status = 'denied'
                        instance.save()
                elif status == 'approve' and action == 'terminate':
                    instance = Reserve.objects.filter(id=action_on_reservation_id, property__owner=self.request.user, status=status)
                    if instance:
                        instance.status = 'terminate'
                        instance.save()
                        
                elif status == 'cancel_request' and action == 'approve':
                    instance = Reserve.objects.filter(id=action_on_reservation_id, property__owner=self.request.user, status=status)
                    if instance:
                        instance.status = 'cancel'
                        instance.save()
                        
                elif status == 'cancel_request' and action == 'denied':
                    instance = Reserve.objects.filter(id=action_on_reservation_id, property__owner=self.request.user, status=status)
                    if instance:
                        instance.status = 'approve'
                        instance.save()
        if user_type == 'host':        
            return get_object_or_404(Reserve, id=action_on_reservation_id, property__owner=self.request.user, status=status)
        elif user_type == 'client':
            return get_object_or_404(Reserve, id=action_on_reservation_id, user=self.request.user, status=status)
          
        return get_object_or_404(Reserve, id=self.kwargs['pk'])