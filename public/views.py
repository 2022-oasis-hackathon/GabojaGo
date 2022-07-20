from django.shortcuts import render
from .models import ScamData
from headquarters.models import Offender


# Create your views here.
def index(request):
    return render(request, 'home.html')


def post(request):
    if request.method == 'POST':
        register_name = request.POST['register_name']
        register_phone = request.POST['register_phone']
        site_name = request.POST['site_name']
        select_transaction = request.POST['select_transaction']
        object_name = request.POST['object_name']
        site_link = request.POST['site_link']
        bank_name = request.POST['bank_name']
        yong_id = request.POST['yong_id']
        yong_account = request.POST['yong_account']
        account_real_name = request.POST['account_name']
        if Offender.objects.filter(name=account_real_name):
            account_name = Offender.objects.get(name=account_real_name)
        else:
            account_name = Offender.objects.create(name=account_real_name)
        trans_money = request.POST['trans_money']
        trans_date = request.POST['trans_date']
        trans_phone = request.POST['trans_phone']
        trans_sex = 'Default'
        try:
            if request.POST['male']:
                trans_sex = 'male'
        except:
            if request.POST['female']:
                trans_sex = 'female'
        h_area1 = request.POST['h_area1']
        h_area2 = request.POST['h_area2']
        if ScamData.objects.filter(register_name=register_name, register_phone=register_phone, site_name=site_name,
                                   transaction=select_transaction, object_name=object_name, site_link=site_link,
                                   yong_id=yong_id,
                                   yong_account=yong_account, account_name=account_name, trans_money=trans_money,
                                   trans_date=trans_date, trans_sex=trans_sex,
                                   trans_phone=trans_phone, bank_name=bank_name, h_area1=h_area1, h_area2=h_area2):
            return render(request, 'register.html')
        else:
            data = ScamData(register_name=register_name, register_phone=register_phone, site_name=site_name,
                            transaction=select_transaction, object_name=object_name, site_link=site_link,
                            yong_id=yong_id,
                            yong_account=yong_account, account_name=account_name, trans_money=trans_money,
                            trans_date=trans_date, trans_sex=trans_sex,
                            trans_phone=trans_phone, bank_name=bank_name, h_area1=h_area1, h_area2=h_area2)
            data.save()
            return render(request, 'registerEnd.html')
    else:
        return render(request, 'register.html')


def analysis(request):
    data = ScamData.objects.all()
    context = {'data': data}
    return render(request, 'analysis.html', context)


def list(request):
    data = ScamData.objects.all()
    context = {'data': data}
    return render(request, 'Personal_List.html', context)


def search(request):
    string = request.GET['keyword']
    if ScamData.objects.filter(account_name__name=string):
        data = ScamData.objects.filter(account_name__name=string)
        tran1 = len(data.filter(transaction='직거래'))
        tran2 = len(data.filter(transaction='게임/비실물'))
        tran3 = len(data.filter(transaction='상태/배송'))
        tran4 = len(data.filter(transaction='암호화폐'))
        context = {'data': len(data), 'tran1': tran1, 'tran2': tran2, 'tran3': tran3, 'tran4': tran4}
        return render(request, 'searching.html', context)
    elif ScamData.objects.filter(trans_phone=int(string)):
        data = ScamData.objects.filter(trans_phone=string)
        tran1 = len(data.filter(transaction='직거래'))
        tran2 = len(data.filter(transaction='게임/비실물'))
        tran3 = len(data.filter(transaction='상태/배송'))
        tran4 = len(data.filter(transaction='암호화폐'))
        context = {'data': len(data), 'tran1': tran1, 'tran2': tran2, 'tran3': tran3, 'tran4': tran4}
        return render(request, 'searching.html', context)
    elif ScamData.objects.filter(yong_account=int(string)):
        data = ScamData.objects.filter(yong_account=int(string))
        tran1 = len(data.filter(transaction='직거래'))
        tran2 = len(data.filter(transaction='게임/비실물'))
        tran3 = len(data.filter(transaction='상태/배송'))
        tran4 = len(data.filter(transaction='암호화폐'))
        context = {'data': len(data), 'tran1': tran1, 'tran2': tran2, 'tran3': tran3, 'tran4': tran4}
        return render(request, 'searching.html', context)
    return render(request, 'searching.html')
