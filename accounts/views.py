from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Account, FAQ
from .serializers import RegisterSerializer, LoginSerializer, AccountSerializer, FAQSerializer
from rest_framework.views import APIView
from main.models import Client
import datetime
from django.db.models import Sum


class FAQListAPIView(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()


class AccountRUDAPIView(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def retrieve(self, request, *args, **kwargs):
        instance = Account.objects.filter(id=self.request.user.id).first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = Account.objects.filter(id=self.request.user.id).first()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class RegisterAPIView(generics.GenericAPIView):
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        if not phone:
            return Response({'msg': 'phone not'}, status=400)
        if Account.objects.filter(phone=phone).first():
            return Response({'msg': 'Bunday user mavjud'}, status=404)
        user = Account.objects.create(
            phone=phone,
            name=request.data.get('name'),
            role=request.data.get('role'),
            branch_id=request.data.get('branch'),
            password=request.data.get('password'),
            is_active=True,
            is_staff=True
        )
        user.save()
        return Response({'msg': 'Account created'}, status=201)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        password = request.data.get('password')
        if not phone or not password:
            return Response({"msg": "Invalid info"}, status=400)
        user = Account.objects.filter(phone=phone, password=password).first()
        if not user:
            return Response({'msg': 'Password or phone incorrect'}, status=400)
        token, _ = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
            'user_id': user.id,
            'role': user.role,
            'name': user.name
        }
        return Response(data, status=200)


class TopOperatorListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        search = self.request.query_params.get('search')
        filter_month = self.request.query_params.get('filter')
        data = []
        accounts = Account.objects.filter(role='Operator').all()
        if search:
            accounts = accounts.filter(name__icontains=search)
        for i in accounts:
            data.append(dict(
                name=i.name,
                info=i.count_clients,
                branch_name=i.branch.name
            ))
        return Response(data)


# class TopOperatorListAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         search = self.request.query_params.get('search')
#         filter_month = self.request.query_params.get('filter')
#         data = []
#         accounts = Account.objects.all().exclude(role='SuperAdmin')
#         if search:
#             accounts = accounts.filter(name__icontains=search)
#         for i in accounts:
#             data.append(dict(
#                 name=i.name,
#                 info=i.count_clients,
#                 branch_name=i.branch.name
#             ))
#         return Response(data)


class CommonStatsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        if request.user.role == 'Operator' or request.user.role == 'HeadBranch':
            print('adawdwa')
            clients = Client.objects.filter(owner__branch=request.user.branch)
            full_clients = clients.aggregate(Sum('price'))
            this_year = clients.filter(date_added__year=datetime.datetime.now().year).aggregate(Sum('price'))
            this_month = clients.filter(date_added__month=datetime.datetime.now().month).aggregate(Sum('price'))
        else:
            full_clients = Client.objects.all().aggregate(Sum('price'))
            this_year = Client.objects.filter(date_added__year=datetime.datetime.now().year).aggregate(Sum('price'))
            this_month = Client.objects.filter(date_added__month=datetime.datetime.now().month).aggregate(Sum('price'))
        data = {
            'full': full_clients,
            'month': this_month,
            'year': this_year
        }
        return Response(data, status=200)


class ListOfWorkersAPIView(generics.ListAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        if self.request.user.role == 'Operator' or self.request.user.role == 'HeadBranch':
            accounts = Account.objects.filter(branch=self.request.user.branch)
        else:
            accounts = Account.objects.all().exclude(role='SuperAdmin').exclude(role='Boss')
        search = self.request.query_params.get('search')
        filial = self.request.query_params.get('filiall')
        if search:
            accounts = accounts.filter(name__icontains=search)
        if filial:
            accounts = accounts.filter(branch_id=filial)
        return accounts


class CountOfClientsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        if request.user.role == 'Operator' or request.user.role == 'HeadBranch':
            print('adawdwa')
            clients = Client.objects.filter(owner__branch=request.user.branch)
            data = {
                'jan': clients.filter(date_added__month=1).count(),
                'feb': clients.filter(date_added__month=2).count(),
                'mar': clients.filter(date_added__month=3).count(),
                'apr': clients.filter(date_added__month=4).count(),
                'may': clients.filter(date_added__month=5).count(),
                'jun': clients.filter(date_added__month=6).count(),
                'jul': clients.filter(date_added__month=7).count(),
                'aug': clients.filter(date_added__month=8).count(),
                'sep': clients.filter(date_added__month=9).count(),
                'oct': clients.filter(date_added__month=10).count(),
                'nov': clients.filter(date_added__month=11).count(),
                'dec': clients.filter(date_added__month=12).count(),
            }
        else:
            clients = Client.objects.filter(owner__branch=request.user.branch)
            data = {
                'jan': clients.filter(date_added__month=1).count(),
                'feb': clients.filter(date_added__month=2).count(),
                'mar': clients.filter(date_added__month=3).count(),
                'apr': clients.filter(date_added__month=4).count(),
                'may': clients.filter(date_added__month=5).count(),
                'jun': clients.filter(date_added__month=6).count(),
                'jul': clients.filter(date_added__month=7).count(),
                'aug': clients.filter(date_added__month=8).count(),
                'sep': clients.filter(date_added__month=9).count(),
                'oct': clients.filter(date_added__month=10).count(),
                'nov': clients.filter(date_added__month=11).count(),
                'dec': clients.filter(date_added__month=12).count(),
            }
        return Response(data, status=200)
