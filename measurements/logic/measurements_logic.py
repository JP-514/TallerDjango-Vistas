from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mnt_pk):
    measurement = Measurement.objects.get(pk=mnt_pk)
    return measurement

def update_measurement(mnt_pk, new_mnt):
    measurement = get_measurement(mnt_pk)
    measurement.variable = new_mnt["variable"]
    measurement.value = new_mnt["value"]
    measurement.unit = new_mnt["unit"]
    measurement.place = new_mnt["place"]
    measurement.dateTime = new_mnt["dateTime"]
    measurement.save()
    return measurement

def create_measurement(mnt):
    measurement = Measurement(variable=mnt["variable"],
                            value=mnt["value"], 
                            unit=mnt["unit"], 
                            place=mnt["place"], 
                            dateTime=mnt["dateTime"])
    measurement.save()
    return measurement

def delete_measurement(mnt_pk):
    measurement = Measurement.objects.get(pk=mnt_pk)
    return measurement.delete()
