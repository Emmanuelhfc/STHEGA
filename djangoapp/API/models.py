from django.db import models


class Layout(models.Model):
    name = models.CharField()
    angle = models.FloatField()
    description = models.CharField()

    def __str__(self):
        return f"{self.name}-{self.angle}"
class TubeDiameter(models.Model):
    diameter_meters = models.FloatField()
    diameter_inch = models.FloatField()
    description = models.CharField(null=True)

    def __str__(self) -> str:
        return f'{self.description}'
    
class ConstantsB(models.Model):
    reynolds_min = models.FloatField()
    reynolds_max = models.FloatField()
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    b1 = models.FloatField()
    b2 = models.FloatField()
    b3 = models.FloatField()
    b4 = models.FloatField()

class ConstantsA(models.Model):
    reynolds_min = models.FloatField()
    reynolds_max = models.FloatField()
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    a1 = models.FloatField()
    a2 = models.FloatField()
    a3 = models.FloatField()
    a4 = models.FloatField()

class LiLo(models.Model):
    pressure_class_pascal = models.FloatField()
    pressure_class_psi = models.FloatField()
    li_meters = models.FloatField()
    lo_meters = models.FloatField()
    li_inch = models.FloatField()
    lo_inch = models.FloatField()

class Pitch(models.Model):
    de = models.ForeignKey(TubeDiameter, on_delete=models.CASCADE)
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    pitch_meters = models.FloatField()
    pitch_inch = models.FloatField()
    pp_meters = models.FloatField()
    pp_inch = models.FloatField()
    pn_meters = models.FloatField()
    pn_inch = models.FloatField()
    description = models.CharField(null=True)

    def __str__(self) -> str:
        return f'{self.description}'
    
class TubeCount(models.Model):
    Ds_meters = models.FloatField()
    Ds_inch = models.FloatField()
    Dotl_meters = models.FloatField()
    Dotl_inch = models.FloatField()
    de = models.ForeignKey(TubeDiameter, on_delete=models.CASCADE)
    pitch = models.ForeignKey(Pitch, on_delete=models.CASCADE)
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)
    n1 = models.PositiveIntegerField(null=True, blank=True)
    n2 = models.PositiveIntegerField(null=True, blank=True)
    n4 = models.PositiveIntegerField(null=True, blank=True)
    n6 = models.PositiveIntegerField(null=True, blank=True)
    n8 = models.PositiveIntegerField(null=True, blank=True)


class DeltaSB(models.Model):
    Dn_min_meters = models.FloatField(unique=True)
    Dn_max_meters = models.FloatField(unique=True)
    Dn_min_inch = models.FloatField(unique=True)
    Dn_max_inch = models.FloatField(unique=True)
    DeltaSB_meters = models.FloatField()
    DeltaSB_inch = models.FloatField()

class NozzleDiameter(models.Model):
    Dc_min_meters = models.FloatField(unique=True)
    Dc_max_meters = models.FloatField(unique=True)
    Dc_min_inch = models.FloatField(unique=True)
    Dc_max_inch = models.FloatField(unique=True)
    nozzle_diameter_meters = models.FloatField()
    nozzle_diameter_inch = models.FloatField()