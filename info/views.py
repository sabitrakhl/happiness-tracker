from datetime import date

from django.db.models import Count, Avg

from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from info.models import HappinessInfo
from info.serializers import InfoCreateSerializer, InfoRetrieveSerializer


class InfoCreateAPI(CreateAPIView):
    queryset = HappinessInfo.objects.all()
    serializer_class = InfoCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        queryset = HappinessInfo.objects.filter(user=self.request.user, date=date.today())
        if queryset.exists():
            raise ValidationError({'error': 'You have already posted info for today.'})
        serializer.save(user=self.request.user)


class InfoRetrieveAPI(APIView):
    def get(self, request, *args, **kwargs):
        qs = HappinessInfo.objects.filter(date=date.today())
        if self.request.user.is_authenticated:
            # assuming that user is assigned to only one group
            user_group = self.request.user.groups.first()

            if user_group:
                group_members = user_group.user_set.all()

                qs = qs.filter(user__in=group_members)
            else:
                # if user is not assigned to any group return their data only.
                qs = qs.filter(user=self.request.user)

            info = qs.values('happiness_level').order_by('happiness_level').annotate(count=Count('happiness_level'))

            serializer_data = InfoRetrieveSerializer(info, many=True).data

            avg_happiness = qs.aggregate(Avg('happiness_level'))

            response = avg_happiness
            response['happiness_info'] = serializer_data
        else:
            avg_happiness = qs.aggregate(Avg('happiness_level'))
            response = avg_happiness

        return Response(response)
