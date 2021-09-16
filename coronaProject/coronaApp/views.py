from datetime import date
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import csv
from .models import *
import pandas as pd

# Create your views here.
def index(request):
    return render(request, 'coronaApp/index.html')

def coronaWeek(request):
    coronadate=coronaDate.objects.all()
    coronalist=coronadate.values('date','confirmed')
    df_corona=pd.DataFrame.from_dict(coronalist)
    df_corona=df_corona.iloc[-7:]
    mean=int(df_corona['confirmed'].mean())
    max=0
    for i in range(len(df_corona)):
        if(df_corona.iloc[i,1]>max):
            max=df_corona.iloc[i,1]
            max_date=df_corona.iloc[i,0]
    return render(request, 'coronaApp/coronaWeek.html', {'mean':mean, 'max':max, 'max_date':max_date} )

def coronaMonth(request):
    coronadate=coronaDate.objects.all()
    coronalist=coronadate.values('date','confirmed')
    df_corona=pd.DataFrame.from_dict(coronalist)
    df_corona=df_corona.iloc[-31:]
    mean=int(df_corona['confirmed'].mean())
    max=0
    for i in range(len(df_corona)):
        if(df_corona.iloc[i,1]>max):
            max=df_corona.iloc[i,1]
            max_date=df_corona.iloc[i,0]
    return render(request, 'coronaApp/coronaMonth.html', {'mean':mean, 'max':max, 'max_date':max_date} )

def corona3Month(request):
    coronadate=coronaDate.objects.all()
    coronalist=coronadate.values('date','confirmed')
    df_corona=pd.DataFrame.from_dict(coronalist)
    df_corona=df_corona.iloc[-92:]
    mean=int(df_corona['confirmed'].mean())
    max=0
    for i in range(len(df_corona)):
        if(df_corona.iloc[i,1]>max):
            max=df_corona.iloc[i,1]
            max_date=df_corona.iloc[i,0]
    return render(request, 'coronaApp/corona3Month.html', {'mean':mean, 'max':max, 'max_date':max_date} )

def corona6Month(request):
    coronadate=coronaDate.objects.all()
    coronalist=coronadate.values('date','confirmed')
    df_corona=pd.DataFrame.from_dict(coronalist)
    df_corona=df_corona.iloc[-183:]
    mean=int(df_corona['confirmed'].mean())
    max=0
    for i in range(len(df_corona)):
        if(df_corona.iloc[i,1]>max):
            max=df_corona.iloc[i,1]
            max_date=df_corona.iloc[i,0]
    return render(request, 'coronaApp/corona6Month.html', {'mean':mean, 'max':max, 'max_date':max_date} )

def districtcorona(request):
    coronadistrict=coronaDistrict.objects.all()
    coronalist=coronadistrict.values('rank','district','confirmed')
    return render(request, 'coronaApp/coronaDistrict.html',{'coronalist':coronalist} )

def vaccine(request):
    vaccinerate=vaccineRate.objects.all()
    vaccinelist=vaccinerate.values('district','rate')
    df_vaccine=pd.DataFrame.from_dict(vaccinelist)
    mean=df_vaccine['rate'].mean()
    mean=round(mean, 2)
    rate1 = rate2 = rate3 = 100
    i1=i2=i3=0
    for i in range(len(df_vaccine)):
        if(df_vaccine.iloc[i,1]<rate1):
            rate3 = rate2
            rate2 = rate1
            rate1 = df_vaccine.iloc[i,1]
            i3=i2
            i2=i1
            i1=i
        elif(df_vaccine.iloc[i,1]<rate2):
            rate3=rate2
            rate2=df_vaccine.iloc[i,1]
            i3=i2
            i2=i
        elif(df_vaccine.iloc[i,1]<rate3):
            rate3=df_vaccine.iloc[i,1]
            i3=i
    district1 = df_vaccine.iloc[i1,0]
    district2 = df_vaccine.iloc[i2,0]
    district3 = df_vaccine.iloc[i3,0]

    vaccinerate2=vaccinepercorona.objects.all()
    vaccinelist2=vaccinerate2.values('district','rate')
    df_vaccine2=pd.DataFrame.from_dict(vaccinelist2)
    mean2=df_vaccine2['rate'].mean()
    mean2=round(mean2, 2)
    prate1 = prate2 = prate3 = 100
    i1=i2=i3=0
    for i in range(len(df_vaccine2)):
        if(df_vaccine2.iloc[i,1]<prate1):
            prate3 = prate2
            prate2 = prate1
            prate1 = df_vaccine2.iloc[i,1]
            i3=i2
            i2=i1
            i1=i
        elif(df_vaccine2.iloc[i,1]<prate2):
            prate3=prate2
            prate2=df_vaccine2.iloc[i,1]
            i3=i2
            i2=i
        elif(df_vaccine2.iloc[i,1]<prate3):
            prate3=df_vaccine2.iloc[i,1]
            i3=i
    pdistrict1 = df_vaccine2.iloc[i1,0]
    pdistrict2 = df_vaccine2.iloc[i2,0]
    pdistrict3 = df_vaccine2.iloc[i3,0]
    return render(request, 'coronaApp/vaccine.html', {'mean':mean, 'district1':district1, 'district2':district2,'district3':district3,'rate1':rate1,'rate2':rate2,'rate3':rate3,
    'pdistrict1':pdistrict1,'pdistrict2':pdistrict2,'pdistrict3':pdistrict3,'prate1':prate1,'prate2':prate2,'prate3':prate3, 'pmean':mean2})

def board(request):
    boards = {'boards':Board.objects.all()}
    return render(request, 'coronaApp/board.html', boards)

def addBoard(request):
    user_input_str = request.POST['boardContent']
    new_board = Board(content = user_input_str)
    new_board.save()
    return HttpResponseRedirect(reverse('board'))

def deleteBoard(request):
    delete_board = request.GET['boardNum']
    board = Board.objects.get(id = delete_board)
    board.delete()
    return HttpResponseRedirect(reverse('board'))

def createdb1(request):
    path = 'C:/Users/sja95/CoronaWeb/coronaDate.csv'
    file = open(path)
    reader = csv.reader(file)
    print('-----',reader)
    list = []
    for row in reader :
        row[1] = int(row[1])
        list.append(coronaDate(date = row[0], confirmed = row[1]))
    
    coronaDate.objects.bulk_create(list)
    return HttpResponse('create model')

def createdb2(request):
    path = 'C:/Users/sja95/CoronaWeb/coronaDistrict.csv'
    file = open(path)
    reader = csv.reader(file)
    print('-----',reader)
    list = []
    for row in reader :
        row[2] = int(row[2])
        list.append(coronaDistrict(rank = row[0], district = row[1], confirmed = row[2]))

    coronaDistrict.objects.bulk_create(list)
    return HttpResponse('create model')

def createdb3(request):
    path='C:/Users/sja95/CoronaWeb/vaccineRate.csv'
    file=open(path)
    reader = csv.reader(file)
    print('-----',reader)
    list=[]
    for row in reader :
        list.append(vaccineRate(district=row[0],rate=row[1]))

    vaccineRate.objects.bulk_create(list)
    return HttpResponse('create model')

def createdb4(request):
    path='C:/Users/sja95/CoronaWeb/vaccinepercorona.csv'
    file=open(path)
    reader = csv.reader(file)
    print('-----', reader)
    list=[]
    for row in reader :
        list.append(vaccinepercorona(district=row[0],rate=row[1]))
    vaccinepercorona.objects.bulk_create(list)
    return HttpResponse('create model')
