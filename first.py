# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 30, 255), (250, 100), 30)
	pygame.draw.circle(screen, (50, 30, 255), (20, 200), 50)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
