from interfaces.databaseinterface import DatabaseHelper

database = DatabaseHelper('monster.db')

#database.ViewQueryHelper("SELECT * FROM users WHERE email=? AND password=?",(email,password))

#database.ModifyQueryHelper("DELETE FROM users WHERE userid = ?",(userid,)) 