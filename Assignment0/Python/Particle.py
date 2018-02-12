from __future__ import absolute_import, print_function, division
import math

class Particle(object):
	'''
	Some documentation
	'''
	
	def __init__(self,charge,mass,x,y,z,speed_x=0,speed_y=0,speed_z=0):
		
		self.charge = charge 
		self.mass = mass 
		self.position = [x,y,z]
		self.speed = [speed_x,speed_y,speed_z]
		self.v = math.sqrt( sum([x**2 for x in self.speed]) )
		
		if mass < 0: raise Exception("Particle class: Mass cannot be negative")
		if self.v > 3e+8 : raise Exception("Particle class: Speed greater than speed of light")
	
	def __repr__(self):
		return "{x} {y} {z} {vx} {vy} {vz} {m} {q}".format(x=self.position[0],y=self.position[1],z=self.position[2],vx=self.speed[0],vy=self.speed[1],vz=self.speed[2],m=self.mass,q=self.charge)
		
	# "get" functions
	def get_charge(self): return self.charge 
	def get_mass(self): return self.mass 
	def get_x(self): return self.position[0]
	def get_y(self): return self.position[1]
	def get_z(self): return self.position[2]
	def get_vx(self): return self.speed[0]
	def get_vy(self): return self.speed[1]
	def get_vz(self): return self.speed[2]
	def getDistance(self): return math.sqrt( sum([x**2 for x in self.position]) )	# distance to origin
	def getDistance(self,x,y,z):													# distance to point
		return math.sqrt( (self.position[0]-x)**2 + (self.position[1]-y)**2 + (self.position[2]-z)**2 )
		
	def getSpeed(self): return self.v
	
	def updateKinematics(self,x,y,z,vx,vy,vz):
		self.position = [x,y,z]
		self.speed = [vx,vy,vz]
	
