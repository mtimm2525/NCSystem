#North Carolina Lookup System based on area of study
#Michael Timm

experts = open("Experts-1.txt", "r")
profiles = open("Profiles-1.txt", "r")

#creates the dictionary of scholars with nested dictionaries of colleges
def createDictionaryColleges(experts):
    scholars ={}
    for line in experts:
        line = line.replace("\t", " ")
        line = line.split('" "')
        line = line.strip('"')
        if(line[5].split(", ")[0] not in scholars): #Takes just the position of the college in each line of text
            scholars[(line[5].split(","))[0]] = {"math" : {}, "computer science" : {}} #adds math and computer science to each college
    return scholars

#using the id from experts of those in math or computer science, adds their name and field of study to the nested dictionary
def addScholars(experts, profiles, scholars):
    for line in experts:
        line = line.replace("\t", " ")
        line = line.split('" "')
        line = line.strip('"')
        if line[5].split(", ")[2] == "Mathematics" or line[5] == "Computer Science":
            id = line[0]
        else:
            continue
        for person in profiles:
            person = person.replace("\t", " ")
            person = person.split('" "')
            person = person.strip('"')
            if id == person[0]:
                if line[5].split(", ")[2] == "Mathematics":
                    scholars[line[5].split(", ")[0]["math"]] = {line[1] + " " + line[2]: [person[2].split(",")]}
                else:
                    scholars[line[5].split(", ")[0]["computer science"]] = {line[1] + " " + line[2]: [person[2].split(",")]}  
    return scholars

def searchByField(scholars):
    college = input("Select an Institute: ")
    college = college.upper()
    print("{college} has the following scholars in computer science: ")
    for collegeName, dpt in scholars.items():
        if collegeName.upper() == college:
            for area, scholarNames in dpt.items():
                if area == "computer science":
                    for name in scholarNames:
                        print(name)
    print("{college} has the following scholars in math: ")
    for collegeName, dpt in scholars.items():
        if collegeName.upper() == college:
            for area, scholarNames in dpt.items():
                if area == "math":
                    for name in scholarNames:
                        print(name)
    study = input("Input area of study: ")
    study = study.lower()
    csinField = []
    minField = []
    for collegeName, dpt in scholars.items():
        if collegeName.upper() == college:
            for area, scholarNames in dpt.items():
                if area == "computer science":
                    for name, studyField in scholarNames:
                        for field in studyField:
                            if study in field.lower():
                                csinField.append(name)
                if area == "math":
                    for name, studyField in scholarNames:
                        for field in studyField:
                            if study in field.lower():
                                minField.append(name)
    if not csinField:
        for collegeName, dpt in scholars.items():
            if collegeName.upper() == college:
                for area, scholarNames in dpt.items():
                    if area == "computer science":
                        for name, studyField in scholarNames:
                            for field in studyField:
                                for word in study.split():
                                    if word in field.lower():
                                        csinField.append(name + " (" + field + ")")
                    if area == "math":
                        for name, studyField in scholarNames:
                            for field in studyField:
                                for word in study.split():
                                    if word in field.lower():
                                        minField.append(name + " (" + field + ")")