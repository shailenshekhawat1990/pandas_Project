import pandas as pd

titanic_data = pd.read_csv('titanic.csv')

print(titanic_data)

print(titanic_data.head())

print(titanic_data.info())

print(titanic_data.isnull().sum())
print(titanic_data.describe())
print(titanic_data.describe(include='object'))

#ANS

selected_columns = ['Name', 'Age']
result = titanic_data[selected_columns]
print(result)

#ANS
#SibSp: Number of siblings/spouses aboard
#Parch: Number of parents/children aboard


titanic_data['FamilySize'] = titanic_data['SibSp'] + titanic_data['Parch'] + 1


#Printing the Total Number of Persons

total_persons = titanic_data['Persons'].sum()
print("Total number of persons:", total_persons)

cleaned_data = titanic_data[titanic_data['Embarked'] != 'C']



