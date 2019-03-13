from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# TEST CASE (weird creepy smile):
parse_file( 'script', edges, transform, screen, color )
# MY CASE (weird creepy stapler):
# parse_file( 'script3', edges, transform, screen, color )
