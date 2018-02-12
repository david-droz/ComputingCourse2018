from __future__ import absolute_import, print_function, division
import numpy as np
import math
from Particle import Particle

class Particle(object):
	'''
	Some documentation
	'''
	
	self.k = 2307077.5 * 1e-34
	
	def __init__(self):
		
		self.particle_list = []
		
	def addParticle(self,p):
		
		self.particle_list.append(p)
		
	def writeToFile(self,f):
		
		for p in self.particle_list :
			f.write(str(p))
		f.write('\n')
		
	def evolve(self,dt):
		
		def _distance(p1,p2):
			return p1.getDistance(p2.get_x(),p2.get_y(),p3.get_y())
		def _coulombForce(p1,p2):
			cF = self.k * (abs(p1.get_charge() * p2.get_charge())) / (_distance(p1,p2)**2)
