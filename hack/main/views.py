from django.shortcuts import render
from .models import *
import json
from datetime import datetime
# Create your views here.


def index(request):
    return render(request, 'index.html', {'data': RunDetails.objects.all()})

def other(request, thing):
    rund = RunDetails.objects.get(pk=int(thing))
    return render(request, 'other.html', {'data': rund.parts.all(), 'rund':rund} )


def importJSON(request):

    if request.method == 'POST':
        data = json.loads(request.POST['data'])

        rund = RunDetails(FileName=data['RunDetails']['FileName'],
                        FilePath=data['RunDetails']['FilePath'],
                        LoadNumber=data['RunDetails']['LoadNumber'],
                        Equipment=data['RunDetails']['Equipment'],
                        RunRecipe=data['RunDetails']['RunRecipe'],
                        RunDuration=float(data['RunDetails']['RunDuration']),
                        FileLength=int(data['RunDetails']['FileLength']),
                        OperatorName=data['RunDetails']['OperatorName'],
                        ExportControl=data['RunDetails']['ExportControl'],
                        RunStart=datetime.strptime(data['RunDetails']['RunStart'], '%Y-%m-%dT%H:%M:%S'),
                        RunEnd=datetime.strptime(data['RunDetails']['RunEnd'], '%Y-%m-%dT%H:%M:%S'))

        rund.save()


        for partInfo in data['PartInformation']:
            tsc = ''
            prob = ''
            for i in partInfo['PartTCs']:
                tsc += i
            for i in partInfo['PartProbes']:
                prob += i

            part = PartInformation(WorkOrder = partInfo['WorkOrder'],
                            PartNumber=partInfo['PartNumber'],
                            PartDescription=partInfo['PartDescription'],
                            ToolLocation=partInfo['ToolLocation'],
                            Comment1=partInfo['Comment1'],
                            Comment2=partInfo['Comment2'],
                            Comment3=partInfo['Comment3'],
                            PartTCs=tsc,
                            PartProbes=prob)
            part.save()
            rund.parts.add(part)


    return render(request, 'import.html', {'Status': 'fish'})
