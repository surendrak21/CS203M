import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 225, 0)
GREEN = (0, 255, 0)
BLUE = (135, 206, 250)
SCREEN_WIDTH_CM = 38.1
SCREEN_WIDTH_PIXELS = WIDTH
PIXELS_TO_CM = SCREEN_WIDTH_CM / SCREEN_WIDTH_PIXELS

# Set up some variables
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Strategy - 1 : Angle Method")


# Set up circle parameters
circle_radius_cm = 10
circle_radius = int(circle_radius_cm / PIXELS_TO_CM)
circle_position = (WIDTH // 2, HEIGHT // 2)

# Function to generate random chord points
def generate_random_chord():
    z=random.uniform(0,math.pi)
    xr1 = circle_position[0]
    yr1 = circle_position[1] - circle_radius
    xr2 =xr1 + 2*circle_radius*math.sin(z)*math.cos(z)
    yr2 =yr1 + 2*circle_radius*math.sin(z)*math.sin(z)
    return ((xr1, yr1), (xr2, yr2))

def chord_length(chord):
    xr1, yr1 = chord[0]
    xr2, yr2 = chord[1]
    return math.sqrt((xr2 - xr1) ** 2 + (yr2 - yr1) ** 2)



# Set up the main game loop
clock = pygame.time.Clock()
chords = []
chord_timer = 0
chord_interval = 0.2  # Interval between chords (in seconds)
running = True
r=0
b=0
font = pygame.font.Font('freesansbold.ttf', 22)
 
# create a text surface object,
# on which text is drawn on it.
text = font.render("hh", True, WHITE)
 
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (WIDTH // 2, 20)

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate random chords
    chord_timer += clock.get_time() / 1000  # Convert milliseconds to seconds
    if chord_timer >= chord_interval:
        chord_timer -= chord_interval
        chords.append(generate_random_chord())

    # Clear the screen
    window.fill(BLACK)

    # Draw the circle
    center = (WIDTH // 2, HEIGHT // 2)
    pygame.draw.circle(window, WHITE, circle_position, circle_radius, 2)

    # Draw the center of the circle (white color)
    pygame.draw.circle(window, WHITE, circle_position,1, 2)

    pygame.draw.circle(window, WHITE, (circle_position[0],circle_position[1] - circle_radius),3, 2)

    x1 , y1 = 5 * math.sqrt(3)/PIXELS_TO_CM,5/PIXELS_TO_CM
    x2 , y2 = 0 , -10/PIXELS_TO_CM
    x3, y3 = -5/PIXELS_TO_CM * math.sqrt(3), 5/PIXELS_TO_CM
    
    pygame.draw.line(window,WHITE, (center[0] + x1, center[1] + y1), (center[0] + x2, center[1] + y2))
    pygame.draw.line(window, WHITE, (center[0] + x2, center[1] + y2), (center[0] + x3, center[1] + y3))
    pygame.draw.line(window, WHITE, (center[0] + x1, center[1] + y1), (center[0] + x3, center[1] + y3))

    for chord in chords:
        # Draw chord
        if chord_length(chord) * PIXELS_TO_CM >= 10*math.sqrt(3) :
            pygame.draw.line(window, BLUE, chord[0], chord[1], 2)
            b=b+1
        else:
            pygame.draw.line(window, YELLOW, chord[0], chord[1], 2)
            r=r+1
        text=font.render("probability= "+str(b/(r+b)),False,WHITE)
        window.blit(text, (100, 30))
        


    # Flip the display
    pygame.display.flip()

    #Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()