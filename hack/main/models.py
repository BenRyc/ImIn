from django.db import models

# Create your models here.


class PartInformation(models.Model):
    WorkOrder = models.IntegerField()
    PartNumber = models.CharField(max_length=200)
    PartDescription = models.CharField(max_length=200)
    ToolLocation = models.CharField(max_length=200)
    Comment1 = models.CharField(max_length=200)
    Comment2 = models.CharField(max_length=200)
    Comment3 = models.CharField(max_length=200)
    PartTCs = models.CharField(max_length=200)
    PartProbes = models.CharField(max_length=200)

    def __str__(self):
        return self.PartNumber



class RunDetails(models.Model):
    FileName = models.CharField(max_length=200)
    FilePath = models.CharField(max_length=200)
    LoadNumber = models.IntegerField()
    Equipment = models.CharField(max_length=200)
    RunRecipe = models.CharField(max_length=200)
    RunStart = models.DateTimeField()
    RunEnd = models.DateTimeField()
    RunDuration = models.FloatField()
    FileLength = models.IntegerField()
    OperatorName = models.CharField(max_length=200)
    ExportControl = models.CharField(max_length=200)

    parts = models.ManyToManyField(PartInformation)

    def __str__(self):
        return self.FileName
