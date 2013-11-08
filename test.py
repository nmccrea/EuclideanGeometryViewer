from MyEuv.viewer import *
from MyEuv.frame import *
from math import *

class World:
  def __init__( self, period_millis ):
    self.current_time = 0
    self.period = period_millis / 1000.0 # seconds
    
    # simulated values
    self.circle_pos = [400, 400]
    self.circle_rad = 5
    self.polygon_n = 4
    self.polygon = [ [  30 * cos( t * 2 * pi / self.polygon_n ) + 300,
                        20 * sin( t * 2 * pi / self.polygon_n ) + 500 ]     for t in range( self.polygon_n ) ]
    self.line_n = 20
    self.linewidth = 4
    self.line = [ [ 20 * t + 450,
                    35 * cos( 2 * t * 2 * pi / self.line_n ) + 600 ]        for t in range( self.line_n ) ]
    
    
  def step( self ):
    self.circle_pos[0] += cos( self.current_time )
    self.circle_pos[1] += sin( self.current_time )
    self.circle_rad += cos( 2.0 * self.current_time )
    
    self.polygon = [ [  point[0] - 2 * cos( self.current_time ),
                        point[1] - 3 * sin( self.current_time )]    for point in self.polygon ]
                        
    self.line = [ [ point[0] + sin( self.current_time ),
                    point[1] - sin( self.current_time ) ]    for point in self.line ]
    
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
    self.current_frame.add_circle( self.world.circle_pos,
                                   self.world.circle_rad,
                                   color = 'blue',
                                   alpha = 1.0 )
                                    
    # draw the simulated polygon
    self.current_frame.add_polygons( [ self.world.polygon ],
                                     color = 'red',
                                     alpha = 1.0 )
                                     
    # draw the simulated line
    self.current_frame.add_lines( [ self.world.line ],
                                  self.world.linewidth,
                                  color = 'black',
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