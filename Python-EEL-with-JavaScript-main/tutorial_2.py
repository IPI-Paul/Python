import eel
from datetime import datetime
import platform
import psutil


eel.init('html')
@eel.expose

def generate_data():
    def size_utility(size, initials="B"):
        factor=1024
        for memory_unit in ['','k', 'M', 'G', 'T', 'P']:
            if size<factor:
                return ('%.2f%s%s'%(size, memory_unit, initials))
            size/=factor
    system=platform.uname()
    data={}
    data.update({len(data)+1:{"Operating System Type":system.system}})
    data.update({len(data)+1:{"System Name":system.node}})
    data.update({len(data)+1:{"OS Release":system.release}})
    data.update({len(data)+1:{"OS Version":system.version}})
    data.update({len(data)+1:{"Processor Type":system.machine}})
    data.update({len(data)+1:{"Processor Category":system.processor}})
    memory_info=psutil.virtual_memory()
    data.update({len(data)+1:{"Total RAM":size_utility(memory_info.total)}})
    data.update({len(data)+1:{"Available RAM":size_utility(memory_info.available)}})
    data.update({len(data)+1:{"Used RAM":size_utility(memory_info.used)}})
    data.update({len(data)+1:{"Percentage Used":str(memory_info.percent)+'%'}})
    partition_info=psutil.disk_partitions()
    for partition in partition_info:
        try:
            drive_size=psutil.disk_usage(partition.mountpoint)
            data.update({len(data)+1:{"Drive Name":partition.mountpoint}})
            data.update({len(data)+1:{"Drive Size":size_utility(drive_size.total)}})
            data.update({len(data)+1:{"Drive Used":size_utility(drive_size.used)}})
            data.update({len(data)+1:{"Drive Free Space":size_utility(drive_size.free)}})
            data.update({len(data)+1:{"Drive Used Percentage":str(drive_size.percent)+'%'}})
        except:
            pass
    return data

eel.start("tutorial_2.html", size=(1024, 900))
