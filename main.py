'''This is the main code for the game'''
import pygame
import time
import random
pygame.font.init() # Initialize font module

# Initialize game window
WIDTH, HEIGHT = 1000, 800  # Set window dimensions
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Set window size
pygame.display.set_caption("My Game") # Set the window title

PLAYER_VEL = 5  # Player velocity constant

FONT = pygame.font.SysFont('comicsans', 15)  # Font for displaying text

def draw(player, elapsed_time, bacteria):
    '''Function to draw game elements'''
    WIN.fill((0, 0, 0))  # Fill the window with black
    
    time_text = FONT.render(f'Time: {int(elapsed_time)}s', 1, (255, 255, 255))  # Render elapsed time
    WIN.blit(time_text, (10, 10))  # Draw the time text on
    
    for b in bacteria:
        pygame.draw.rect(WIN, (0, 255, 0), b)  # Draw each bacteria as a green rectangle

    pygame.draw.rect(WIN, (255, 0, 0), player)  # Draw the player as a red rectangle
    
    pygame.display.update() # Update the display

def main():
    '''Main function to run the game loop'''
    run = True

    player = pygame.Rect(100, 100, 10, 10)  # Example player rectangle
    clock = pygame.time.Clock()  # Create a clock object to manage frame rate
    start_time = time.time()  # Record the start time of the game
    elapsed_time = 0  # Initialize elapsed time
    bacteria_add_interval = 2000  # Interval to add bacteria in milliseconds
    last_bacteria_add_time = 0  # Last time bacteria was added

    bacteria = []  # List to hold bacteria objects

    # Game loop
    while run:
        last_bacteria_add_time += clock.tick(60)  # Update the time since last frame
        clock.tick(60)  # Limit the frame rate to 60 FPS
        elapsed_time = time.time() - start_time  # Update elapsed time

        # Add bacteria at intervals
        if last_bacteria_add_time > bacteria_add_interval:
            for _ in range(3):  # Add 3 bacteria
                bac_size = random.randint(5, 10+player.width)  # Random size for bacteria
                x = random.randint(0, WIDTH - bac_size)
                y = random.randint(0, HEIGHT - bac_size)
                bacteria.append(pygame.Rect(x, y, bac_size, bac_size))  # Add new bacteria rectangle
            last_bacteria_add_time = 0  # Reset the timer

        # Handle quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL 

        #Handle bacteria collision and absorption
        for b in bacteria[:]:
            if player.colliderect(b):
                print(f"Bacteria hit at size {b.width}x{b.height}")
                bacteria.remove(b)  # Remove bacteria on collision

                if player.width >= b.width and player.height >= b.height:
                    print("You absorbed a bacteria! Your size increased.")    
                    player.width += b.width  # Increase player size on hit
                    player.height += b.height # Increase player size on hit
                else:
                    print("Game Over! You hit a bacteria larger than you.")
                    run = False
                break


        if player.width >= WIDTH//2.5 or player.height >= HEIGHT//2.5:
            print("Congratulations! You have absorbed all bacteria and won the game!")
            run = False

        

        # Call the draw function to update the game display
        draw(player, elapsed_time, bacteria)

    
    pygame.quit()

# Entry point of the program
if __name__ == "__main__":
    main()