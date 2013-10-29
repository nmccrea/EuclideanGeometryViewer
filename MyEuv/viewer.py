#!/usr/bin/env python

import pygtk
import gtk

from math import *

class Viewer:
  
  def __init__( self ):
    
    # initialize the window
    self.window = gtk.Window( gtk.WINDOW_TOPLEVEL )
    self.window.set_title( "Application" )
    self.window.connect( "delete_event", self.delete_event )
    
    # initialize the layout container
    self.layout_box = gtk.VBox()
    self.window.add( self.layout_box )
    
    # initialize the drawing drawing_area
    self.drawing_area = gtk.DrawingArea()
    self.drawing_area.set_size_request( 800, 800 )
    self.drawing_area.connect( "expose_event", self.expose_event )
    self.layout_box.pack_start( self.drawing_area )
    
    
    
    
    self.button = gtk.Button("Click Here")
    self.button.set_size_request( 120, 30 )
    self.layout_box.pack_start( self.button, True, False, 5 )
    
    
    
    
    
    self.window.show_all()
    
    
  def expose_event( self, widget, event ):
    
    
    print "\n\nI'M EXPOSING MYSELF!\n\n"
    
    cr = widget.window.cairo_create()
    
    
    
    cr.set_source_rgb(0, 0, 0)
    cr.new_path()
    cr.move_to( 400, 400 )
    n = 10
    r = 50
    for p in range( n+1 ):
      theta = ( 2 * pi * p ) / n
      x = ( r * cos( theta ) ) + 400
      y = ( r * sin( theta ) ) + 400
      cr.line_to( x, y )
    cr.fill()
    
    
  def delete_event( self, widget, event ):
    gtk.main_quit()
    return False
    
    
def main():
  print "\n\nHELLO\n\n"
  v = Viewer()
  gtk.main()
  
main()