from interfaces.databaseinterface import DatabaseHelper

database = DatabaseHelper('monsters.db')

results = database.ViewQueryHelper("SELECT * FROM MonsterTable")
for row in results:
    print(row['MonsterName'])

#database.ModifyQueryHelper("DELETE FROM users WHERE userid = ?",(userid,)) 