'''
Start of SharkyWaters code contribution
'''
import datetime

startTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
fileName = "test_"+ str(startTime) + ".csv"

toFileStr = 'YYMMDDhhmmss.ssssss'
toFileStr += ","
toFileStr += 'function'
toFileStr += ","
toFileStr += 'battery_percentage'
toFileStr += ","
toFileStr += 'battery_voltage'
toFileStr += ","
toFileStr += 'controller_temperature'
toFileStr += ","
toFileStr += 'battery_temperature'
toFileStr += ","
toFileStr += 'load_voltage'
toFileStr += ","
toFileStr += 'load_current'
toFileStr += ","
toFileStr += 'load_power'
toFileStr += ","
toFileStr += 'pv_voltage'
toFileStr += ","
toFileStr += 'pv_current'
toFileStr += ","
toFileStr += 'pv_power'
toFileStr += ","
toFileStr += 'max_charging_power_today'
toFileStr += ","
toFileStr += 'max_discharging_power_today'
toFileStr += ","
toFileStr += 'charging_amp_hours_today'
toFileStr += ","
toFileStr += 'discharging_amp_hours_today'
toFileStr += ","
toFileStr += 'power_generation_today'
toFileStr += ","
toFileStr += 'power_generation_total'
toFileStr += ","
toFileStr += 'charging_status'
toFileStr += "\n"

with open(fileName, 'a') as myFile:
    myFile.write(toFileStr)

'''
End of SharkyWaters code contribution
'''

#=================================================================================

'''
Start of Cyrils code avaialble at https://github.com/cyrils/renogy-bt1
'''
import logging 
from BTOneApp import BTOneApp 

logging.basicConfig(level=logging.DEBUG)

ADAPTER = "hci0"
MAC_ADDR = "E0:7D:EA:7D:04:89"     #2) last 8 characters same as DEVICE_ALIAS - see BLE Scanner app for field marked as 'Advertisement Manufacturer Data' for the first 4 digits (e.g.<e07dea7d0489> in this case)
DEVICE_ALIAS = "BT-TH-EA7D0489"    #1) edit based on mac address of specific BT1 module (use ap such as BLE Scanner for this)
POLL_INTERVAL = 0.1 # USER DEFINED data interval read rate (in seconds)


def on_connected(app: BTOneApp):
    app.poll_params() # OR app.set_load(1)

def on_data_received(app: BTOneApp, data):
    logging.debug("{} => {}".format(app.device.alias(), data))
    
    #code added by SharkyWaters to format string that is sritten to the log file
    toFileStr = datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f')
    toFileStr += ","
    toFileStr += str(data['function'])
    toFileStr += ","
    toFileStr += str(data['battery_percentage'])
    toFileStr += ","
    toFileStr += str(data['battery_voltage'])
    toFileStr += ","
    toFileStr += str(data['controller_temperature'])
    toFileStr += ","
    toFileStr += str(data['battery_temperature'])
    toFileStr += ","
    toFileStr += str(data['load_voltage'])
    toFileStr += ","
    toFileStr += str(data['load_current'])
    toFileStr += ","
    toFileStr += str(data['load_power'])
    toFileStr += ","
    toFileStr += str(data['pv_voltage'])
    toFileStr += ","
    toFileStr += str(data['pv_current'])
    toFileStr += ","
    toFileStr += str(data['pv_power'])
    toFileStr += ","
    toFileStr += str(data['max_charging_power_today'])
    toFileStr += ","
    toFileStr += str(data['max_discharging_power_today'])
    toFileStr += ","
    toFileStr += str(data['charging_amp_hours_today'])
    toFileStr += ","
    toFileStr += str(data['discharging_amp_hours_today'])
    toFileStr += ","
    toFileStr += str(data['power_generation_today'])
    toFileStr += ","
    toFileStr += str(data['power_generation_total'])
    toFileStr += ","
    toFileStr += str(data['charging_status'])
    toFileStr += "\n"
    
    #code added by SharkyWaters to write string to log file
    with open(fileName, 'a') as myFile:
        myFile.write(toFileStr)

    # app.disconnect() # disconnect here if you do not want polling

bt1 = BTOneApp(ADAPTER, MAC_ADDR, DEVICE_ALIAS, on_connected, on_data_received, POLL_INTERVAL)
bt1.connect()
