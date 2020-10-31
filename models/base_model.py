#!/usr/bin/pyhton3
"""
import the modules
"""
import datetime
import uuid
import models

"""
Class base model
"""

class BaseModel():

	def __str__(self):

	def __int__(self, *args, **kwargs):
        """Instatntiates a new model"""
		if kwargs:
			for key, value in kwargs.items():
				if key != "__class__":
					setattr(self, key, value)
				if key == "created_at" or key == "update_at":
					setattr(self, key, datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))

		else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)

	def __str__(self):
	name = self.__class__.__name__
        dic = self.__dict__
        return "[{}] ({}) {}".format(name, self.id, dic)

	def save(self):
        """ save
        """
        self.updated_at = datetime.now()

        def to_dict(self):
    	name = self.__class__.__name__
    	dictionary["__class__"] = name
    	dictionary["updated_at"] = dictionary["updated_at"].isoformat()
    	dictionary["created_at"] = dictionary["created_at"].isoformat()
    	
    	return dictionary
