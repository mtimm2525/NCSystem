#North Carolina Lookup System based on area of study
#Michael Timm

experts = open("Experts-1.txt", "r")
profiles = open("Profiles-2.txt", "r")
next(experts) #skips the top line of experts as it is headings

profiles = profiles.readlines()[1:] #makes profiles into a list of lines since we iterate through it multiple times

#creates the dictionary of scholars with nested dictionaries of colleges
def createDictionaryColleges(experts):
    scholars ={}
    for line in experts:
        line = [category.strip().strip('"') for category in line.strip().split("\t")]
        if line[5].split(",")[0].strip() not in scholars: #Takes just the position of the college in each line of text
            scholars[(line[5].split(","))[0].strip()] = {"math" : {}, "computer science" : {}} #adds math and computer science to each college
    return scholars

#using the id from experts of those in math or computer science, adds their name and field of study to the nested dictionary
def addScholars(experts, profiles, scholars):
    fieldOfStudyId = {}
    for person in profiles:  #creating a dictionary of all scholars to avoid extremely long lookup times
        person = [category.strip().strip('"') for category in person.strip().split("\t")]
        ExpertId = person[0]
        if ExpertId in fieldOfStudyId:
            fieldOfStudyId[ExpertId].append(person[2].strip())
        else:
            fieldOfStudyId[ExpertId] = [person[2].strip()]
    for line in experts:    #iterates through expert file to add scholars to the scholar dictionary
        line = [category.strip().strip('"') for category in line.strip().split("\t")]
        id = line[0]
        if "Mathematics" in line[5] or "Computer Science" in line[5]:
            college = line[5].split(",")[0].strip()
            name = line[2] + " " + line[1]
            aofStudy = fieldOfStudyId.get(id, [])
            if "Mathematics" in line[5]:
                scholars[college]["math"][name] = aofStudy
            else:
                scholars[college]["computer science"][name] = aofStudy
        else:
            continue
    return scholars

#takes scholar dictionary and input from user to search for scholars by field of study
def searchByField(scholars):
    college = input("Select an Institute: ")
    college = college.upper()
    print(f"{college} has the following scholars in computer science: ")
    #next two nested loops iterate through lists of scholars in each department of chose college
    for collegeName, dpt in scholars.items():
        if collegeName.upper() == college:
            for area, scholarNames in dpt.items():
                if area == "computer science":
                    for name in scholarNames: 
                        print(name)
    print(f"{college} has the following scholars in math: ")
    for collegeName, dpt in scholars.items():
        if collegeName.upper() == college:
            for area, scholarNames in dpt.items():
                if area == "math":
                    for name in scholarNames:
                        print(name)
    study = input("Input area of study: ")
    study = study.lower()
    csinField = []
    iscsinField = False #make two arrays of those in each field of study under each department as well as booleans of if therea are any in that field at all
    minField = []
    isminField = False
    for collegeName, dpt in scholars.items():
        if collegeName.upper() == college:
            for area, scholarNames in dpt.items():
                if area == "computer science":
                    for name, studyField in scholarNames.items():
                        for field in studyField:
                            if study.lower() in field.lower():  #checks for both computer science and math if the field of study is in any scholar's list
                                csinField.append(name)
                                iscsinField = True
                if area == "math":
                    for name, studyField in scholarNames.items():
                        for field in studyField:
                            if study.lower() in field.lower():
                                minField.append(name)
                                isminField = True
    if iscsinField:
        print(f"The following computer science scholars at {college} study {study}: ")
        for name in csinField: #if there are cs scholars, prints them
            print(name + ", ", end ="")
    else: #otherwise counts the number of similar words in each scholar's field of studies to add to list of similar scholars
        studyWords = [word for word in study.lower().split()]
        closest = 0
        similarFields = []
        for collegeName, dpt in scholars.items():
            if collegeName.upper() == college:
                for area, scholarNames in dpt.items():
                    if area == "computer science":
                        for name, studyField in scholarNames.items():
                            for studyName in studyField:
                                studyLower = studyName.lower()
                                matchCount = 0
                                for word in studyWords:
                                    if word in studyLower:
                                        matchCount += 1
                                if matchCount > closest:
                                    closest = matchCount
                                    similarFields = [f"{name} ({study})"]     
                                elif matchCount == closest and matchCount != 0:
                                    similarFields.append(f"{name} ({study})")
        print(f"No computer science scholars at {college} study {study}. Here are some similar scholars: ")
        for name in similarFields:
            print(name + ", ", end="")
    if isminField:
        print(f"The following math scholars at {college} study {study}: ")
        for name in minField: #mimics the computer science logic for the math department
            print(name + ", ", end ="")
    else:
        studyWords = [word for word in study.lower().split()]
        closest = 0
        similarFields = []
        for collegeName, dpt in scholars.items():
            if collegeName.upper() == college:
                for area, scholarNames in dpt.items():
                    if area == "math":
                        for name, studyField in scholarNames.items():
                            for studyName in studyField:
                                studyLower = studyName.lower()
                                matchCount = 0
                                for word in studyWords:
                                    if word in studyLower:
                                        matchCount += 1
                                if matchCount > closest:
                                    closest = matchCount
                                    similarFields = [f"{name} ({study})"]     
                                elif matchCount == closest and matchCount != 0:
                                    similarFields.append(f"{name} ({study})")
        print(f"No math scholars at {college} study {study}. Here are some similar scholars: ")
        for name in similarFields:
            print(name + ", ", end="")

#main driver function that allows the user to quit when done
def main(scholars):
    key = "c"
    while key.lower() == "c":
        searchByField(scholars)
        key = input("Press 'c' to continue or any other key to exit: ")

#assembles the helper functions
if __name__ == "__main__":
    print("Welcome to the NC lookup system")
    print("We currently include scholars from the following institutes: ")
    scholars = createDictionaryColleges(experts)
    experts = open("Experts-1.txt", "r")
    next(experts)
    scholars = addScholars(experts, profiles, scholars)
    for college in scholars:
        print(college, end=", ")
    main(scholars)
    print("Thanks for using the system!")