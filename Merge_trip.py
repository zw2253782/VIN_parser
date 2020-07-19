import pandas as pd 
import PySimpleGUI as sg
import time

def merge(f1,f2):
    csv1 = pd.read_csv("StartSample.csv")
    csv2 = pd.read_csv("ENDSample.csv")
    print("file 1 shape is: ",csv1.shape)
    print("file 2 shape is: ",csv2.shape)

    inner_merged_total = pd.merge(csv1, csv2, on=["PersonID"])

    #print(inner_merged_total.head())
    print("merged file shape is: ", inner_merged_total.shape)
    
    StartTime = -1
    EndTime= 1000000000000000000000000
    rowList = []
    for index, row in inner_merged_total.iterrows():
        if (row['StartTime']) > (row['EndTime']):
            rowList.append(index)
            #print(index)
    #print(len(rowList))
    #print((rowList[0:10]))

    df_new = inner_merged_total.drop(index = rowList)
    #print(df_new.head())

    newList =[]
    for index, row in df_new.iterrows():
        if (row['StartTime']) == StartTime:
            if (row['EndTime'])>EndTime:
                newList.append(index)
            else:
                newList.append(index+1)
        StartTime = row['StartTime']
        EndTime = row['EndTime']
    #print(len(newList))
    #print((newList[0:10]))

    df_new2 = df_new.drop(index = newList)
    #print(df_new2.head())
    print("Cleaned merged file shape is: ",df_new2.shape)



if __name__ == "__main__":
    ######################### GUI ########################
    sg.theme('Dark Blue 3')  # please make your creations colorful

    layout = [  [sg.Text('Filename')],
                [sg.Input(), sg.FileBrowse()], 
                [sg.OK(), sg.Cancel()]] 

    window = sg.Window('Please input the start sample excel file you want to process', layout)
    event1, values1 = window.Read()
    #vin_dir = (values1['Browse'])
    window.close()

    ######################### GUI ########################
    sg.theme('Dark Blue 3')  # please make your creations colorful

    layout = [  [sg.Text('Filename')],
                [sg.Input(), sg.FileBrowse()], 
                [sg.OK(), sg.Cancel()]] 

    window = sg.Window('Please input the end sample excel file you want to process', layout)
    event2, values2 = window.Read()
    #vin_dir = (values2['Browse'])
    window.close()
    ######################### process all date in excel ########################
    merge(values1['Browse'],values2['Browse'])