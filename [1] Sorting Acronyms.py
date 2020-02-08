def main():
    num = int(input())
    countries = []
    for _ in range(num):
        countries.append(input())
    for acronym in countryAcroSort(toAcronym(countries)):
        print(acronym)

# convert list of full name to Acronym
def toAcronym(countries):
        countriesAcronym = []
        for country in countries:
            contryAcro = ""
            words = country.split(" ")
            for letter in words:
                if letter[0].isupper():
                    contryAcro += letter[0]
            countriesAcronym.append(contryAcro)
        return countriesAcronym

 # bubble sort
def countryAcroSort(countriesAcronym):
        while(True):
            status = False
            for index in range(len(countriesAcronym)-1):
                # in case of len of two acronym equal
                if len(countriesAcronym[index+1]) == len(countriesAcronym[index]):
                    if countriesAcronym[index+1] < countriesAcronym[index]:
                        temp = countriesAcronym[index]
                        temp2 = countriesAcronym[index+1]
                        countriesAcronym[index+1] = temp
                        countriesAcronym[index] = temp2
                        status = True

                elif len(countriesAcronym[index+1]) > len(countriesAcronym[index]):
                    temp = countriesAcronym[index]
                    temp2 = countriesAcronym[index+1]
                    countriesAcronym[index+1] = temp
                    countriesAcronym[index] = temp2
                    status = True
            if not status:
                break
        return countriesAcronym
    

main()
    