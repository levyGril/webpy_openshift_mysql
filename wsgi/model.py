'''
Created on 2012-6-13

@author: Jason
'''
import web
import os

db = web.database(dbn='mysql', 
    db=os.environ['OPENSHIFT_GEAR_NAME'], 
    user=os.environ['OPENSHIFT_DB_USERNAME'], 
    pw=os.environ['OPENSHIFT_DB_PASSWORD'],
    host=os.environ['OPENSHIFT_DB_HOST']
)

def get_todos():
    return db.select('todo', order='id')

def new_todo(text):
    db.insert('todo', title=text)

def del_todo(id):
    db.delete('todo', where="id=$id", vars=locals())
