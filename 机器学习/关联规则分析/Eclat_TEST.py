from AssociationAnalysis import Eclat
import time

trainData = [['bread', 'milk', 'vegetable', 'fruit', 'eggs'],
            ['noodle', 'beef', 'pork', 'water', 'socks', 'gloves', 'shoes', 'rice'],
            ['socks', 'gloves'],
            ['bread', 'milk', 'shoes', 'socks', 'eggs'],
            ['socks', 'shoes', 'sweater', 'cap', 'milk', 'vegetable', 'gloves'],
            ['eggs', 'bread', 'milk', 'fish', 'crab', 'shrimp', 'rice']]

time_start1 = time.time()
clf1 = Eclat()
pred1 = clf1.train(trainData)
time_end1 = time.time()
print("Runtime of Eclat:", time_end1-time_start1)
