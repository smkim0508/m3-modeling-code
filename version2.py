#import matplotlib.pyplot as plt

mine = 0.54 #outdoor
manufacture = 0.70
trade = 0.58 
info = 0.68 #office
finance = 0.68 #office
business = (0.68+0.76)/2 #office and customer combined
eduhealth = (0.68+0.87)/2 #classroom and medical combined
leisure = 0.75
other = (0.83+0.70)/2 #personal and homesupport combined
government = 0.68 #office work

average_weight = (mine + manufacture + trade + info + finance + business + eduhealth + leisure + other + government)/10
print(average_weight)

num_mine20 = 129900
num_manufacture20 = 168400
num_trade20 = 390300
num_info20 = 133700
num_finance20 = 100400
num_business20 = 295700
num_eduhealth20 = 272100
num_leisure20 = 150600
num_other20 = 71100
num_government20 = 266000

num_mine21 = 109600
num_manufacture21 = 142200
num_trade21 = 332600
num_info21 = 139000
num_finance21 = 87600
num_business21 = 277500
num_eduhealth21 = 223500
num_leisure21 = 133000
num_other21 = 59300
num_government21 = 206700

total_worker_2020 = num_mine20 + num_manufacture20 + num_trade20 + num_info20 + num_finance20 + num_business20 + num_eduhealth20 + num_leisure20 + num_other20 + num_government20
total_worker_2021 = num_mine21 + num_manufacture21 + num_trade21 + num_info21 + num_finance21 + num_business21 + num_eduhealth21 + num_leisure21 + num_other21 + num_government21

monthls = [0] * 9

percentvirtual = [0.54, 0.39, 0.35, 0.36, 0.34, 0.31, 0.26, 0.23, 0.25]

#weighted percentage of virtual workers per industry per month
minew = [0] * 9
manufacturew = [0] * 9
tradew = [0] * 9
infow = [0] * 9
financew = [0] * 9
businessw = [0] * 9
eduhealthw = [0] * 9
leisurew = [0] * 9
otherw = [0] * 9
governmentw = [0] * 9

#number of virtual workers per industry per month
minen = [0] * 9
manufacturen = [0] * 9
traden = [0] * 9
infon = [0] * 9
financen = [0] * 9
businessn = [0] * 9
eduhealthn = [0] * 9
leisuren = [0] * 9
othern = [0] * 9
governmentn = [0] * 9

total_virtual = [0] * 9

rr_percentage_per_month = [0] * 9

for month in range (0,9):
    
    monthls[month] = month

    minew[month] = (mine/average_weight)*percentvirtual[month]
    manufacturew[month] = (manufacture/average_weight)*percentvirtual[month]
    tradew[month] = (trade/average_weight)*percentvirtual[month]
    financew[month] = (finance/average_weight)*percentvirtual[month]
    businessw[month] = (business/average_weight)*percentvirtual[month]
    eduhealthw[month] = (eduhealth/average_weight)*percentvirtual[month]
    leisurew[month] = (leisure/average_weight)*percentvirtual[month]
    otherw[month] = (other/average_weight)*percentvirtual[month]
    governmentw[month] = (government/average_weight)*percentvirtual[month]
    
    if minew[month] > 0.5:
        minew[month] = 1
    if manufacturew[month] > 0.5:
        manufacturew[month] = 1
    if tradew[month] > 0.5:
        tradew[month] = 1
    if financew[month] > 0.5:
        financew[month] = 1
    if businessw[month] > 0.5:
        businessw[month] = 1
    if eduhealthw[month] > 0.5:
        eduhealthw[month] = 1
    if leisurew[month] > 0.5:
        leisurew[month] = 1
    if otherw[month] > 0.5:
        otherw[month] = 1
    if governmentw[month] > 0.5:
        governmentw[month] = 1
    
    if month < 4:
        minen[month] = minew[month] * num_mine20
        total_virtual[month] += minen[month]

        manufacturen[month] = manufacturew[month] * num_manufacture20
        total_virtual[month] += manufacturen[month]

        traden[month] = tradew[month] * num_trade20
        total_virtual[month] += traden[month]

        financen[month] = financew[month] * num_finance20
        total_virtual[month] += financen[month]

        businessn[month] = businessw[month] * num_business20
        total_virtual[month] += businessn[month]

        eduhealthn[month] = eduhealthw[month] * num_eduhealth20
        total_virtual[month] += eduhealthn[month]

        leisuren[month] = leisurew[month] * num_leisure20
        total_virtual[month] += leisuren[month]

        othern[month] = otherw[month] * num_other20
        total_virtual[month] += othern[month]

        governmentn[month] = governmentw[month] * num_government20
        total_virtual[month] += governmentn[month]

        rr_percentage_per_month[month] = total_virtual[month]/total_worker_2020

    elif month > 3:
        minen[month] = minew[month] * num_mine21
        total_virtual[month] += minen[month]

        manufacturen[month] = manufacturew[month] * num_manufacture21
        total_virtual[month] += manufacturen[month]

        traden[month] = tradew[month] * num_trade21
        total_virtual[month] += traden[month]

        financen[month] = financew[month] * num_finance21
        total_virtual[month] += financen[month]

        businessn[month] = businessw[month] * num_business21
        total_virtual[month] += businessn[month]

        eduhealthn[month] = eduhealthw[month] * num_eduhealth21
        total_virtual[month] += eduhealthn[month]

        leisuren[month] = leisurew[month] * num_leisure21
        total_virtual[month] += leisuren[month]

        othern[month] = otherw[month] * num_other21
        total_virtual[month] += othern[month]

        governmentn[month] = governmentw[month] * num_government21
        total_virtual[month] += governmentn[month]
        
        rr_percentage_per_month[month] = total_virtual[month]/total_worker_2021
    
    

for month in range (0, 9):
    print(rr_percentage_per_month[month])
    #plt.plot(month, rr_percentage_per_month)

#plt.show()
