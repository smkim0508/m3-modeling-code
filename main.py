#import matplotlib.pyplot as plt

med = 0.87
personal = 0.83
customer = 0.76
leisure = 0.75
homesupport = 0.70
warehouse = 0.70
office = 0.68
classroom = 0.68
transport = 0.58
outdoor = 0.54

average_weight = (0.87 + 0.54)/2

num_med21 = 272100/2
num_personal21 = 71100
num_customer21 = 100400
num_leisure21 = 150600/2
num_homesupport21 = 150600/2
num_warehouse21 = 390300/2 + 168400
num_office21 = 295700
num_classroom21 = 272100/2
num_transport21 = 390300/2
num_outdoor21 = 129900




total_worker_2020 = num_med + num_personal + num_customer + num_leisure + num_homesupport + num_warehouse + num_office + num_classroom + num_transport + num_outdoor

monthls = [100]
percentvirtual = [0.54, 0.39, 0.35, 0.36, 0.34, 0.31, 0.26, 0.23, 0.25]

#weighted percentage of virtual workers per industry
medw = [0] * 100
personalw = [0] * 100
customerw = [0] * 100
leisurew = [0] * 100
homesupportw = [0] * 100
warehousew = [0] * 100
officew = [0] * 100
classroomw = [0] * 100
transportw = [0] * 100
outdoorw = [0] * 100
#number of virtual workers per industry
medn = [0] * 100
personaln = [0] * 100
customern = [0] * 100
leisuren = [0] * 100
homesupportn = [0] * 100
warehousen = [0] * 100
officen = [0] * 100
classroomn = [0] * 100
transportn = [0] * 100
outdoorn = [0] * 100

total_virtual = [0] * 100
rr_percentage_per_month = [0] * 100

#for month in range (3,24,3):
    #print(month)



for i in range (0,8):
    monthp = i*3

    monthls.append(monthp)
    medw[monthp] = (med/average_weight)*percentvirtual[i]
    personalw[monthp] = (personal/average_weight)*percentvirtual[i]
    customerw[monthp] = (customer/average_weight)*percentvirtual[i]
    leisurew[monthp] = (leisure/average_weight)*percentvirtual[i]
    homesupportw[monthp] = (homesupport/average_weight)*percentvirtual[i]
    warehousew[monthp] = (warehouse/average_weight)*percentvirtual[i]
    officew[monthp] = (office/average_weight)*percentvirtual[i]
    classroomw[monthp] = (classroom/average_weight)*percentvirtual[i]
    transportw[monthp] = (transport/average_weight)*percentvirtual[i]
    outdoorw[monthp] = (outdoor/average_weight)*percentvirtual[i]
 
for month in range (3,24,3):
    if medw[month] > 0.5:
        medw[month] = 1
    if personalw[month] > 0.5:
        personalw[month] = 1
    if customerw[month] > 0.5:
        customerw[month] = 1
    if leisurew[month] > 0.5:
        leisurew[month] = 1
    if homesupportw[month] > 0.5:
        homesupportw[month] = 1
    if warehousew[month] > 0.5:
        warehousew[month] = 1
    if officew[month] > 0.5:
        officew[month] = 1
    if classroomw[month] > 0.5:
        classroomw[month] = 1
    if transportw[month] > 0.5:
        transportw[month] = 1
    if outdoorw[month] > 0.5:
        outdoorw[month] = 1
    
    medn[month] = medw[month] * num_med
    total_virtual[month] += medn[month]

    personaln[month] = personalw[month] * num_personal
    total_virtual[month] += personaln[month]

    customern[month] = customerw[month] * num_customer
    total_virtual[month] += customern[month]

    leisuren[month] = leisurew[month] * num_leisure
    total_virtual[month] += leisuren[month]

    homesupportn[month] = homesupportw[month] * num_homesupport
    total_virtual[month] += homesupportn[month]

    warehousen[month] = warehousew[month] * num_warehouse
    total_virtual[month] += warehousen[month]

    officen[month] = officew[month] * num_office
    total_virtual[month] += officen[month]

    classroomn[month] = classroomw[month] * num_classroom
    total_virtual[month] += classroomn[month]

    transportn[month] = transportw[month] * num_transport
    total_virtual[month] += transportn[month]

    outdoorn[month] = outdoorw[month] * num_outdoor
    total_virtual[month] += outdoorn[month]

    rr_percentage_per_month[month] = total_virtual[month]/total_worker_2020
    

for month in range (3,24,3):
    print(rr_percentage_per_month[month])
    #plt.plot(month, rr_percentage_per_month)

#plt.show()


#find weighted percentage for each industry that worked at home
#if at any point the percentage > 50% assume entire industry is remote-ready since majority virtual -> covid got bad enough to force industry to turn virtual
#times the number of workers in each industry sum for each given time point
#divide total sum of remote-ready workers/total number of workers

## differentiate num for each year (2020 ~ 2021)