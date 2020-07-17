from interfaces.databaseinterface import DatabaseHelper

database = DatabaseHelper('monsters.db')

results = database.ViewQueryHelper("SELECT * FROM MonsterTable")
for row in results:
    print("Monster: " + row['MonsterName'])
    print("Defence: " + str(row['Defence']))
    print("Health: " + str(row['Health']))
    print("Points: " + str (row['Points']))

#database.ModifyQueryHelper("DELETE FROM users WHERE userid = ?",(userid,)) 