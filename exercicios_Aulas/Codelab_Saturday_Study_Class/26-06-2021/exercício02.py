#02 - Crie um programa que leia nome, gênero e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em
# uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) A média de idade;
# C) Uma lista de pessoas com idade acima da média;
# D) Uma lista com todos os dados cadastrados de todas as pessoas.
persons = list()
person = dict(
        {
            'name':'',
            'gender':'',
            'age':0
        })
def register():
    while True:
        person['name'] = input("Enter with the name of one person: ")
        person['gender'] = input("Enter with the gender of this person: ")
        person['age'] = int(input("Enter with the age of this person: "))
        persons.append(person)
        if input("You have another person to register? (Y|N) ").lower().strip(" ").startswith('n'):
            break
        
def createTheResults():
    results = dict()
    results['numberofregisters'] = len(persons)
    results['middle'] = 0
    results['highages'] = list()
    for i in persons:
        results['middle'] +=i['age']/results['numberofregisters']
    for i in persons:
        if i['age']>results['middle']:
            results['highages'].extend(i['name'])
    return results
def showTheResults(results = dict()):
    print("The number of registered persons is:",results['numberofregisters'])
    print("The middle of ages is:",results['middle'])
    print("The list of persons with high age is:",results['highages'])
    for i in persons:
        print("The name of this person is:", i['name'])
        print("where the gender is:",i['gender'])
        print("And the age is:",i['age'],"\n")
        
def main():
    register()
    showTheResults(createTheResults()) 

main()   