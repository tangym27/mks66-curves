from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 0, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

parse_file( 'script2', edges, transform, screen, color )
# bezier
# 100 250 100 400 400 400 400 250
# bezier
# 101 251 100 400 400 399 400 249
print (" \n\n")
i = 0
j = 0

k = 400
l = 250
# + + + - + - - -

counter = 0
while (counter < 50 ):
    print("line\n"+ str(100+i)+ " " +str(250+j) +" 100 " + str(395-i) + " "+  str(250+j)+ " 100")

#    print("bezier\n"+ str(100+counter)+" "+str(250+counter)+" "+ str(100+counter)+" "+ str(400-counter)+" "+ str(400+counter)+" "+ str(400-counter)+" "+ str(400-counter)+" "+ str(250-counter))
    i += .5
    j += 1
    k -= 1
    l -=1
    counter += 1
