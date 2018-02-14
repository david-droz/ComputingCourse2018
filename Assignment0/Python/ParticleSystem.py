from __future__ import absolute_import, print_function, division
import numpy as np
import math
from Particle import Particle

class ParticleSystem(object):
	'''
	Some documentation
	'''
	
	def __init__(self):
		
		self.particle_list = []
		self.k = 2307077.5 * 1e-34
		
	def addParticle(self,p):
		
		self.particle_list.append(p)
		
	def writeToFile(self,f):
		
		for p in self.particle_list :
			f.write(str(p))
		f.write('\n')
		
	def evolve(self,dt):
		
		def _distance(p1,p2):
			return p1.getDistance(p2.get_x(),p2.get_y(),p2.get_z())
		def _coulombForce(p1,p2):
			d = _distance(p1,p2)
			cF = self.k * (p1.get_charge() * p2.get_charge()) / (d**2)
			dx = (p1.get_x() - p2.get_x())/d
			dy = (p1.get_y() - p2.get_y())/d
			dz = (p1.get_z() - p2.get_z())/d
			return cF * dx, cF * dy, cF * dz
			
		new_kin = np.zeros((len(self.particle_list),6),dtype=np.float64)		# x,y,z,vx,vy,vz
		
		for i in xrange(len(self.particle_list)):
			
			Fx_total, Fy_total, Fz_total = [0,0,0]
			p1 = self.particle_list[i]
			
			for j in xrange(len(self.particle_list)):
				if i == j: continue
				fdx,fdy,fdz = _coulombForce(p1,self.particle_list[j])
				Fx_total += fdx
				Fy_total += fdy
				Fz_total += fdz
			
			new_kin[i,3] = p1.get_vx() + (Fx_total * dt)/p1.get_mass()	
			new_kin[i,4] = p1.get_vy() + (Fy_total * dt)/p1.get_mass()
			new_kin[i,5] = p1.get_vz() + (Fz_total * dt)/p1.get_mass()
			
			new_kin[i,0] = p1.get_x() + (new_kin[i,3] * dt)
			new_kin[i,1] = p1.get_y() + (new_kin[i,4] * dt)
			new_kin[i,2] = p1.get_x() + (new_kin[i,5] * dt)
		# end loop
		
		for i in xrange(len(self.particle_list)):
			self.particle_list[i].updateKinematics( new_kin[i,0],new_kin[i,1],new_kin[i,2],new_kin[i,3],new_kin[i,4],new_kin[i,5] )
		del new_kin
	
	def evolveAndWriteToFile(self,ntimes,t_ignore,dt,fname):
		
		f = open(fname,'w')
		for i in xrange(ntimes):
			
			if not i % t_ignore :
				self.writeToFile(f)
			self.evolve(dt)
		
		f.close()
		
	def clear(self):
		self.particle_list = []
