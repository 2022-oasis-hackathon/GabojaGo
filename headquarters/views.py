from django.shortcuts import render
from public.models import ScamData
from .models import Offender


# Create your views here.
def index(request):
    p_scam = ScamData.objects.all()
    o_data = Offender.objects.all()
    context = {'p_scam': p_scam, 'o_data': o_data}
    return render(request, 'admin.html', context)
