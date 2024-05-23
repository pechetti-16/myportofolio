import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("VR Interaction")

# Set up VR camera position
vr_camera = pygame.Vector3(400, 300, 0)

# Circle position and radius
circle_pos = pygame.Vector2(400, 300)
circle_radius = 20

# Delay for interaction visibility
interaction_delay = 0.5  # in seconds

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            # Raycast from the center of the VR camera
            ray_direction = pygame.Vector3(0, 0, -1)  # Adjust the direction based on your VR setup
            ray_end = vr_camera + ray_direction * 100  # Adjust the length of the ray

            # Update the circle position to the intersection point
            circle_pos.x, circle_pos.y = ray_end.x, ray_end.y

            # Clear the screen
            screen.fill((255, 255, 255))

            # Draw a circle at the intersection point
            pygame.draw.circle(screen, (0, 0, 255), (int(circle_pos.x), int(circle_pos.y)), circle_radius)

            # Update the display
            pygame.display.flip()

            # Delay for visibility
            time.sleep(interaction_delay)
    
    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw a circle at the intersection point
    pygame.draw.circle(screen, (0, 0, 255), (int(circle_pos.x), int(circle_pos.y)), circle_radius)

    # Update the display
    pygame.display.flip()
