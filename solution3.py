#Function to output predicted total number of remote workers in a given city and year

#predicted remote readiness for each given city and year
remoteReadydict = {
    "seattle_2024" : 0.4186,
    "seattle_2027" : 0.4290,
    "omaha_2024" : 0.4190,
    "omaha_2027" : 0.4289,
    "scranton_2024" : 0.3446,
    "scranton_2027" : 0.3539,
    "liverpool_2024" : 0.2745,
    "liverpool_2027" : 0.2855,
    "barry_2024" : 0.4683,
    "barry_2027" : 0.4780
}

#compound annual total industry growth rate for each city
industryGrowthdict = {
    "seattle" : 0.0198,
    "omaha" : 0.007,
    "scranton" : -0.0005,
    "liverpool" : 0.0238,
    "barry" : 0.0087
}

#total industry size for each city in 2020
industrySizedict = {
    "seattle" : 1665200,
    "omaha" : 444800,
    "scranton" : 261100,
    "liverpool" : 635300,
    "barry" : 55200
}

#outputs the percentage of people working in-person given an age (assumed constant)
def numInPerson(age):
    percent = 0
    if age < 16:
        percent = 0
    if age >= 16 and age < 25: 
        percent = (1 - 0.1194108058) * 100 
    if age >= 25 and age < 55:
        percent = (1 - 0.2884494964) * 100
    if age >= 55 and age < 65:
        percent = (1 - 0.2479749047) * 100
    if age >= 65:
        percent = (1 - 0.2227850718) * 100
    return percent


def model(city, year, Age, C, P, D):

    remoteready = remoteReadydict[city+"_"+str(year)]
    percentwilling = (100 - (numInPerson(Age) - pow(1.1586, (C-30)) + P - min(62*D, 62)))
    #print(industrySizedict[city])
    #print(year-2000)
    #print(1+industryGrowthdict[city])
    predindustrysize = industrySizedict[city]* pow((1+industryGrowthdict[city]),(year-2000))

    num_remote = remoteready * percentwilling * 0.01 * predindustrysize #we take *0.01 to convert percentage to decimal

    return num_remote

#When predicting the average number of remote workers for each given time and city, we assume that the average time taken for commute is 30 minutes as noted in our references. 
#The national controlled median pay comparison between in-person and fully-remote workers is 1.9 percent increase, which would mean a paycut, P, value of -1.9. This source has been noted in our references. 
#Now, we use the stats that 32 percent of workers have at least one child under the age of 18 as noted in our references. 
#Next, we can factor in the number of workers for each age group using the given data. The median age for each age group is used as dummy input to weigh the final average. 
#Finally, we account for the percentage of workers in each age group who has a children. The data for this is assumed to be constant between men and women. We also assume that workers after the age of 55 have at least one child who is already over the age of 18, therefore we consider this case the same as having no child.

def prediction(city, year):
    age16_24_nochild = 17176*0.786*model(city, year, 20, 30, -1.9, 0)
    age16_24_child = 17176*0.214*model(city, year, 20, 30, -1.9, 1)
    age25_54_nochild = 94221*0.2764*model(city, year, 40, 30, -1.9, 0)
    age25_54_child = 94221*0.2764*model(city, year, 40, 30, -1.9, 1)
    age55_64 = 25184*model(city, year, 60, 30, -1.9, 0)
    age_65 = 9673*model(city, year, 65, 30, -1.9, 0)
    
    total = age16_24_nochild + age16_24_child + age25_54_nochild + age25_54_child + age55_64 + age_65
    average = total/146254

    return average

#we can simply input the city name and the year to output the average number of remote workers

predictremote = prediction("seattle", 2024)
#predictremote = prediction("seattle", 2027)
#predictremote = prediction("omaha", 2024)
#predictremote = prediction("omaha", 2027)
#predictremote = prediction("scranton", 2024)
#predictremote = prediction("scranton", 2027)
#predictremote = prediction("liverpool", 2024)
#predictremote = prediction("liverpool", 2027)
#predictremote = prediction("barry", 2024)
#predictremote = prediction("barry", 2027)

print("The Predicted Number of Remote Workers is: ", predictremote)

