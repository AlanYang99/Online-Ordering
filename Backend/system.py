from flask import render_template, request, redirect, url_for, abort
from server import app, system
import pickle
import datetime
from order import *
from mains2 import *
from inventory1 import Food


class order_id:

    id_generator = 1

    def __init__(self,order): #Not sure if we need status tbh
                                    #When the order is created, the status should begin ('In preparation')
        self._order = order
        self._status = 'In preparation'
        self._id = id_generator #This part needs some changing, because we are going to
        self._time = datetime.datetime.now()
        id_generator +=1
                              #method that updates order1
                                #Just think about it this way, there may be 2 identical ids
    def update_status(self,status):
        self._status = status

class orders:

    def __init__(self):
        self._orders = []

    def deleteOrder(self,id):
        for order in self._orders:
            if order._id is order:
                self._orders.remove(order)

    def getOrder(self,id):
        for order in self._orders:
            if order._id is order:
                return order
        return None

    def make_order(self,mains,sides,drinks):

        #Checking if available ingredients 1st
        new_order = Order(mains,sides,drinks)
        self._orders.append(new_order)

class updateInventory:

    @staticmethod
    def addingredients(name,price,amount):
        infile = open("Ingredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        inventory.append(Food(name,price,amount))
        outfile = open("Ingredients","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def addburgerIngredients(name,price,amount):
        infile = open("burgerIngredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        inventory.append(Food(name,price,amount))
        outfile = open("burgerIngredients","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def addwrapIngredients(name,price,amount):
        infile = open("wrapIngredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        inventory.append(Food(name,price,amount))
        outfile = open("wrapIngredients","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def addsides(name,price,amount):
        infile = open("sides",'rb')
        inventory = pickle.load(infile)
        infile.close()
        inventory.append(Food(name,price,amount))
        outfile = open("sides","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def adddrinks(name,price,amount):
        infile = open("drinks",'rb')
        inventory = pickle.load(infile)
        infile.close()
        inventory.append(Food(name,price,amount))
        outfile = open("drinks","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def increment_ingredients(name,amount):
        infile = open("Ingredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        for i in inventory:
            if(i._name is name):
                i._amount += amount
        outfile = open("Ingredients","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def increment_wraps_ingredients(name,amount):
        infile = open("wrapIngredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        for i in inventory:
            if(i._name is name):
                i._amount += amount
        outfile = open("wrapIngredients","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def increment_burger_ingredients(name,amount):
        infile = open("burgerIngredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        for i in inventory:
            if(i._name is name):
                i._amount += amount
        outfile = open("burgerIngredients","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def increment_sides(name,amount):
        infile = open("sides",'rb')
        inventory = pickle.load(infile)
        infile.close()
        for i in inventory:
            if(i._name is name):
                i._amount += amount
        outfile = open("sides","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def increment_drinks(name,amount):
        infile = open("drinks",'rb')
        inventory = pickle.load(infile)
        infile.close()
        for i in inventory:
            if(i._name is name):
                i._amount += amount
        outfile = open("drinks","wb")
        pickle.dump(inventory,outfile)
        outfile.close()


#For make order function, should take in same parameters as order1
#Checks if the ingredients are available
#if it is then make order (using the order class)
#Have another class honestly, will make things so much easier
#the class will consist of time_ordered (use datetime),id,status,and obv the order itself
#when you make an order, append it to an order list
