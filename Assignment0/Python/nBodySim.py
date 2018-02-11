from Particle import Particle
from ParticleSystem import ParticleSystem


# Used throughout the program
pSystem = ParticleSystem()
chargeElectron = -1
chargeProton   = +1
massElectron   = 9.109e-31
massProton     = 1.673e-27

# Part 1
# Simple system with a pair of electrons starting at rest
# They should repel each other
# The speed should increase rapidly at first, and then plateau
pSystem.addParticle(Particle(chargeElectron,massElectron,0,+0.5,0))
pSystem.addParticle(Particle(chargeElectron,massElectron,0,-0.5,0))
pSystem.evolveAndWriteToFile(5000,10,1.e-4,"part1.dat")


# Part 2
# Simple system where an electron and proton both start at rest
# The attract each other until they meet
# They then leave the realm where the Coulomb law is valid
# As such, the behaviour past their meeting point is non-physical
pSystem.clear()
pSystem.addParticle(Particle(chargeProton,massProton,0,0,0))
pSystem.addParticle(Particle(chargeElectron,massElectron,0,1,0))
pSystem.evolveAndWriteToFile(720,10,1.e-4,"part2.dat")


# Part 3
# Simple system where an electron starts with enough velocity to orbit a proton
# The proton starts stationary, and approximately remains so as the electron circles it
pSystem.clear()
pSystem.addParticle(Particle(chargeProton,massProton,0,0,0))
pSystem.addParticle(Particle(chargeElectron,massElectron,0,1,0,15.9,0,0))
pSystem.evolveAndWriteToFile(5000,10,1.e-4,"part3.dat")


# Part 4
# Complex system where there are two electrons offset from a proton
# The two electrons start closer to the proton than each other, so are attracted
# They get very close to each other and the proton at about the same time
# There is some intermediate range where they attract and repel each other
# Then they get far from the proton and the electron repulsion dominates
# This sends them far away, until the proton attraction counters the velocity
# Then they come back closer again to repeat the process
pSystem.clear()
pSystem.addParticle(Particle(chargeProton,massProton,1,0,0))
pSystem.addParticle(Particle(chargeElectron,massElectron,0,+1,0))
pSystem.addParticle(Particle(chargeElectron,massElectron,0,-1,0))
pSystem.evolveAndWriteToFile(4000,10,1.e-4,"part4.dat")


# Part 5
# Complex system where there are eight particles as below
#      e  p  e
#      p     p
#      e  p  e
# The protons are approximately stationary in the timescale of the electrons
# The electrons will be oscillating back and forth as they want to go to
# the center, but will be repelled by the other electrons when they do so
pSystem.clear()
pSystem.addParticle(Particle(chargeElectron,massElectron,-1,+1,0))
pSystem.addParticle(Particle(chargeElectron,massElectron,+1,+1,0))
pSystem.addParticle(Particle(chargeElectron,massElectron,-1,-1,0))
pSystem.addParticle(Particle(chargeElectron,massElectron,+1,-1,0))
pSystem.addParticle(Particle(chargeProton,massProton,-1,0,0))
pSystem.addParticle(Particle(chargeProton,massProton,0,+1,0))
pSystem.addParticle(Particle(chargeProton,massProton,+1,0,0))
pSystem.addParticle(Particle(chargeProton,massProton,0,-1,0))
pSystem.evolveAndWriteToFile(5000,10,1.e-4,"part5.dat")


# Part 6
# Complex system where there are a set of four protons which are ~stationary
# and one electron that has a large initial velocity, being fired into the
# region between the protons
pSystem.clear()
pSystem.addParticle(Particle(chargeElectron,massElectron,-2,+1,0,10,-20,0))
pSystem.addParticle(Particle(chargeProton,massProton,-1,+1,0))
pSystem.addParticle(Particle(chargeProton,massProton,+1,+1,0))
pSystem.addParticle(Particle(chargeProton,massProton,-1,-1,0))
pSystem.addParticle(Particle(chargeProton,massProton,+1,-1,0))
pSystem.evolveAndWriteToFile(10300,10,1.e-4,"part6.dat")

