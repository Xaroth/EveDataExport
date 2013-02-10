import logging

from django.db import models

class LoggableManager(models.Manager):
	"""
	A Loggable Manager MixIn.

	This MixIn allows one to add simple logging capabilities to a django.db.models.Manager,
	using the Manager's class name and its model's class path as channel.
	"""
	@property
	def log(self):
		log = getattr(self, '_logger', None)
		if log == None:
			log = self._logger = logging.getLogger("%s.%s.%s" % (self.model.__module__, self.model.__name__, self.__class__.__name__))
		return log

class LoggableObject(object):
	"""
	A Loggable Object MixIn.

	This MixIn allows one to add simpel logging capabilities to any class, using the
	class path as channel.
	"""
	@property
	def log(self):
		log = getattr(self, '_logger', None)
		if log == None:
			log = self._logger = logging.getLogger("%s.%s" % (self.__class__.__module__, self.__class__.__name__))
		return log