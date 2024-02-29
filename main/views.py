from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from .serializers import BranchSerializer, TourPaketSerializer, ClientSerializer, MeetingSerializer
from .models import Branch, TourPaket, Client, Meeting, BranchStatistics


class BranchCreateAPIView(generics.CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class BranchListAPIView(generics.ListAPIView):
    serializer_class = BranchSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        search = self.request.query_params.get('search')
        queryset = Branch.objects.all()
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset


class BranchRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class TourPaketCreateAPIView(generics.CreateAPIView):
    queryset = TourPaket.objects.all()
    serializer_class = TourPaketSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class TourPaketListAPIView(generics.ListAPIView):
    serializer_class = TourPaketSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = TourPaket.objects.all()
        paket_type = self.request.query_params.get('paket_type')
        search = self.request.query_params.get('search')
        month = self.request.query_params.get('month')
        if paket_type:
            queryset = queryset.filter(type_paket=paket_type)
        if search:
            queryset = queryset.filter(name__icontains=search)
        if month:
            queryset = queryset.filter(date_go__month=month)
        return queryset


class TourPaketUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = TourPaket.objects.all()
    serializer_class = TourPaketSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        tour_paket = TourPaket.objects.filter(id=request.data.get('paket')).first()
        tour_paket.current_quantity += 1
        tour_paket.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, last_updater=self.request.user)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class ClientListAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        paket_id = self.request.query_params.get('paket_id')
        search = self.request.query_params.get('search')
        queryset = Client.objects.filter(paket_id=paket_id)
        if search:
            queryset = queryset.filter(full_name__icontains=search)
        return queryset


class FullClientListAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        if self.request.user.role == 'Operator' or self.request.user.role == 'HeadBranch':
            queryset = Client.objects.filter(owner__branch=self.request.user.branch)
        else:
            queryset = Client.objects.all()
        filial = self.request.query_params.get('filial')
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(full_name__icontains=search)
        if filial:
            queryset = queryset.filter(owner__branch_id=filial)
        return queryset


class ClientUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        instance.last_updater = self.request.user
        instance.save()
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class ClientDeleteAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class TurPaketStatisticsForBranch(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        data = []
        tour_paket_id = self.kwargs['pk']
        branch = Branch.objects.all()
        clients = Client.objects.filter(paket_id=tour_paket_id)
        stats = BranchStatistics.objects.filter(paket_id=tour_paket_id)
        for b in branch:
            cost, count, taken = 0, 0, 0
            for c in clients:
                if c.owner.branch.id == b.id:
                    cost = cost + c.price
                    count = count + 1
            for i in stats:
                if branch.id == b.id:
                    taken = taken + i.taken_payment
            data.append(dict(
                id=b.id,
                name=b.name,
                count=count,
                cost=cost,
                taken=taken,
                qarz=cost - taken
            ))
        return Response(data)


class ChangePaketStatisticsForBranch(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        branch_id = request.data['branch_id']
        paket_id = request.data['paket_id']
        cost = request.data['cost']
        branch = BranchStatistics.objects.filter(branch_id=branch_id).first()
        if branch:
            branch.taken_payment += cost
            branch.save()
        new = BranchStatistics.objects.create(
            branch_id=branch_id,
            paket_id=paket_id,
            taken_payment=cost,
            user_id=self.request.user.id
        )
        new.save()
        return Response('success', status=status.HTTP_200_OK)


class MeetingCreateAPIView(generics.CreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class MeetingListAPIView(generics.ListAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class MeetingUpdateAPIView(generics.UpdateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
