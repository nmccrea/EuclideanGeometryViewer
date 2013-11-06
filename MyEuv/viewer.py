#!/usr/bin/env python

import pygtk
import gtk

from painter import *

class Viewer:
  
  def __init__( self ):
    
    # initialize the window
    self.window = gtk.Window( gtk.WINDOW_TOPLEVEL )
    self.window.set_title( "Application" )
    self.window.connect( "delete_event", self.delete_event )
    
    # initialize the layout container
    self.layout_box = gtk.VBox()
    self.window.add( self.layout_box )
    
    # initialize the drawing_area
    self.drawing_area = gtk.DrawingArea()
    self.drawing_area.set_size_request( 800, 800 )
    self.drawing_area.connect( "expose_event", self.expose_event )
    self.layout_box.pack_start( self.drawing_area )
    
    # initialize the painter
    self.painter = Painter( self.drawing_area )
    
    
    
    self.button = gtk.Button("Click Here")
    self.button.set_size_request( 120, 30 )
    self.layout_box.pack_start( self.button, True, False, 5 )
    
    
    
    
    
    self.window.show_all()
    
    
  def expose_event( self, widget, event ):
    self.painter.draw_frame( [] )
    
    
  def delete_event( self, widget, event ):
    gtk.main_quit()
    return False
    
    
def main():
  v = Viewer()
  gtk.main()
  
main()