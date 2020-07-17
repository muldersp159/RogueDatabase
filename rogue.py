from interfaces.databaseinterface import DatabaseHelper
import random

database = DatabaseHelper('monsters.db')
results = database.ViewQueryHelper("SELECT * FROM MonsterTable") 
monster = random.choice(results) #python dictionary 
monstername = monster['MonsterName'] #store the monstername

print("Welcome to the dungeon of death")
print("Oh no, you have been attacked!!!")
print("Monster: " + monster['MonsterName'])
print("Defence: " + str(monster['Defence']))
print("Health: " + str(monster['Health']))
print("Points: " + str (monster['Points']))

results = database.ViewQueryHelper("SELECT * FROM Abilities WHERE MonsterName = ?",(monstername,))
for row in results:
    print(row['AttackName'])

#database.ModifyQueryHelper("DELETE FROM users WHERE userid = ?",(userid,)) 