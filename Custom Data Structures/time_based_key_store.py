'''

PROBLEM: 

Implement a data structure that can store multiple values of the same key at different 
timestamps and retrieve the key's value at a certain timestamp. 

You'll need to implement the TimeStamp class. This class has the following functions: 
- Init(): This function initializes the values dictionary and timestamp dictionary. 
- Set Value(key, value, timestamp): This function stores the key and value at any given timestamp. 
- Get Value(key, timestamp): This function returns the value set for this key at the specified timestamp. 

Note: When a query requests the value of a key at a timestamp that is more recent than the most 
recent entry for that key, our data structure should return the value corresponding to the most 
recent timestamp.

--------------------------------
PATTERN: CUSTOM DATA STRUCTURES
--------------------------------

'''


# PASSES ALL BUT ONE TEST CASE --> 
'''
put
["TimeStamp", "set_value", "set_value", "get_value", "get_value"] , [[], ["foo", "tan", 7], ["foo", "ban", 9], ["foo", 8], ["foo", 9]]

Output
[null, null, null, "", "ban"]


Expected
[null, null, null, "tan", "ban"]


'''



class TimeStamp:
    def __init__(self):
        self.values_dict = {}
        self.timestamps_dict = {}

    #  Set TimeStamp data variables
    def set_value(self, key, value, timestamp):
        
        if key in self.timestamps_dict :
            if self.timestamps_dict[key] < timestamp :
                self.timestamps_dict[key] = timestamp
        else :
            self.timestamps_dict[key] = timestamp
        
        if key in self.values_dict :
            other_dict = self.values_dict[key]
            other_dict[timestamp] = value
        else :
            new_dict = dict()
            self.values_dict[key] = new_dict

            new_dict[timestamp] = value 
        

        

    # Get time_stamp data variables
    def get_value(self, key, timestamp):
        old_time = None
        if key in self.timestamps_dict and self.timestamps_dict[key] < timestamp :
            old_time = 
            time = self.timestamps_dict[key]
        else : time = timestamp

        if key in self.values_dict :
            other_dict = self.values_dict[key]

            if time in other_dict : return other_dict[time]
            else : return ""
        else : return ""














