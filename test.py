from MyEuv.viewer import *
from MyEuv.frame import *
from math import *

class World:
  def __init__( self, period_millis ):
    self.current_time = 0
    self.period = period_millis / 1000.0 # seconds
    
    # simulated values
    self.pos = [400, 400]
    self.rad = 5
    
  def step( self ):
    self.pos[0] += cos( self.current_time )
    self.pos[1] += sin( self.current_time )
    self.rad += cos( 2.0 * self.current_time )
    
    # increment the current time
    self.current_time += self.period
    
    
    
    
    
class WorldView():
  
  def __init__( self, world ):
    # initialize the viewer
    self.viewer = Viewer()
    
    # bind the simulator world
    self.world = world
    
    # initialize the world frame
    self.current_frame = Frame()
    
  def render_frame( self ):
    # draw the simulated circle
    self.current_frame.add_circle(  self.world.pos,
                                    self.world.rad,
                                    color = 'blue',
                                    alpha = 1.0 )
    
    # cycle the frame
    self.viewer.add_frame( self.current_frame )
    self.current_frame = Frame()
    
    
    
    
    
import gtk
import glib

class Simulator:
  def __init__( self ):
    self.frequency = 20                         # hertz
    self.period = int( 1000 / self.frequency )  # milliseconds
    self.max_frames = 1000
    self.total_frames = 0
    
    self.world = World( self.period )
    self.world_view = WorldView( self.world )
    
    glib.idle_add( self.runsim )
    gtk.main()
    
  def runsim( self ):
    if self.total_frames < self.max_frames:
      self.total_frames += 1
      
      self.world.step()
      self.world_view.render_frame()
      glib.timeout_add( self.period, self.runsim )
      
      
      
      
      
s = Simulator()