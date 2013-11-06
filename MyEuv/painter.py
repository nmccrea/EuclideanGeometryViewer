#!/usr/bin/env python

from color_palette import *
from math import *

class Painter:
  
  def __init__( self, drawing_area ):
    self.drawing_area = drawing_area
    
  def draw_frame( self, frame ):
    context = self.drawing_area.window.cairo_create()
    
    self.set_color( context, "blue" )
    context.new_path()
    context.move_to( 400, 400 )
    n = 4
    r = 20
    for p in range( n+1 ):
      theta = ( 2 * pi * p ) / n
      x = ( r * cos( theta ) ) + 400
      y = ( r * sin( theta ) ) + 400
      context.line_to( x, y )
    context.fill()
    
    self.draw_circle( context, (400, 200), 25, "purple" )
    
  def draw_circle( self, context,
                   pos, radius, color ):
                    
    self.set_color( context, color )
    context.arc( pos[0], pos[1], radius, 0, 2.0 * pi)
    context.fill()
    
  def set_color( self, cairo_context, color_string ):
    ColorPalette.set_color( cairo_context, color_string )