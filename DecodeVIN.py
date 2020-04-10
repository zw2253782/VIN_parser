from pyvin import VIN
import pandas as pd 
import PySimpleGUI as sg
import time


def read_excel(path_):
    df = pd.read_excel (path_)
    df_list = df[df.columns[0]].values.tolist()
    return df_list

def rewrite_vin(path_):
    filled =[]
    for piece in read_excel(path_):
        print(piece)
        veh = VIN(eval(piece))
        filled.append([veh.VIN, veh.Make, veh.Model, veh.ModelYear, veh.BodyClass, veh.Trim, veh.VehicleType, veh.GVWR])
    df1 = pd.DataFrame(filled,columns=['VIN', 'Make','Model','ModelYear','BodyClass','Trim','VehicleType','GVWR'])
    df1.to_excel("output" + str(time.time()) + ".xlsx")  


if __name__ == "__main__":
    ######################### GUI ########################
    sg.theme('Dark Blue 3')  # please make your creations colorful

    layout = [  [sg.Text('Filename')],
                [sg.Input(), sg.FileBrowse()], 
                [sg.OK(), sg.Cancel()]] 

    window = sg.Window('Please input the excel file you want to process', layout)
    event, values = window.Read()
    vin_dir = (values['Browse'])
    window.close()

    ######################### process all date in excel ########################
    print(vin_dir)
    rewrite_vin(vin_dir)