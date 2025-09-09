#North Carolina Lookup System based on area of study
#Michael Timm

experts = open("Experts-1.txt", "r")
profiles = open("Profiles-1.txt", "r")

#creates the dictionary of scholars with nested dictionaries of colleges
def createDictionaryColleges(experts):
    scholars ={}
    for line in experts:
        line = line.strip('"')
        line = line.split(" ")
        if(line[5].split(",")[0] not in scholars): #Takes just the position of the college in each line of text
            scholars[(line[5].split(","))[0]] = {"math" : {}, "computer science" : {}} #adds math and computer science to each college
    return scholars

#using the id from experts of those in math or computer science, adds their name and field of study to the nested dictionary
def addScholars(experts, profiles, scholars):
    return scholars