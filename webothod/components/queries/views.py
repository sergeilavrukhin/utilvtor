from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User

from .models import Queries
from .serializers import QueriesSerializer
from ..dicts.models import Regions, QueryType
from ..users.models import UserProfile


class QueriesView(
    GenericViewSet,
):
    @staticmethod
    def one(request, pk=1):
        queries = Queries.objects.filter(pk=pk)
        return Response(
            QueriesSerializer(
                queries.first()
            ).data
        )

    @staticmethod
    def map(request):
        queries = Queries.objects.values('pk')
        return Response(
            queries
        )

    @staticmethod
    def list(request, page=1):
        queries = Queries.objects

        paginator = Paginator(queries.order_by('pk'), 10)
        return Response({
            "count": paginator.num_pages,
            "queries": QueriesSerializer(
                paginator.page(page),
                many=True,
            ).data
        })

    @method_decorator(csrf_protect)
    def create(self, request, *args, **kwargs):
        data = request.data
        data['phone'] = data["phone"].replace('+', '')
        data['phone'] = data["phone"].replace('(', '')
        data['phone'] = data["phone"].replace(')', '')
        data['phone'] = data["phone"].replace('-', '')
        data['phone'] = data["phone"].replace(' ', '')

        if request.user.is_anonymous:
            user = User.objects.filter(
                username=data["email"],
                email=data["email"],
            ).first()
            if user is None:
                user = User.objects.create(
                    username=data["email"],
                    email=data["email"],
                )
                if user:
                    profile = UserProfile.objects.create(
                        user=user,
                        phone=data["phone"],
                        firstname=data["firstname"]
                    )
        else:
            user = request.user
        query = Queries.objects.create(
            waste=data["waste"],
            region=Regions.objects.get(code=data["region"]),
            user=user,
            type=QueryType.objects.get(pk=data["query_type"]),
            description=data["description"],
        )
        if query:
            return Response({'msg': 'ok'}, status=201)
        else:
            return Response({'msg': 'error'}, status=403)
