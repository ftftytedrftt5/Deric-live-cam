import pygame
import random
pygame.font.init()

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Deric Live Cam")

BG = pygame.transform.scale(pygame.image.load("Deric.jpg"), (WIDTH, HEIGHT))

FONT = pygame.font.SysFont("comicsans", 30)
dericin = "Loading..."

def draw():
    WIN.blit(BG, (0, 0))

    # dericout = FONT.render(f"{dericin}", 1, "white")
    # WIN.blit(dericout, (250, 400))

    pygame.display.update()

def main():
    run = True

    clock = pygame.time.Clock()

    while run:
        clock.tick(5)
        global BG, dericin, dericlast

        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_window_size()

        rn = random.randint(1, 9)

        if rn == 1:
            BG = pygame.transform.scale(pygame.image.load("DericBL.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        else:
            BG = pygame.transform.scale(pygame.image.load("Deric.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # rn = random.randint(1, 16)
        
        # if rn == 1:
        #     rn = random.randint(1, 12)

        #     if rn == 2:
        #         dericin = "Hello!"
        #     elif rn == 3:
        #         dericin = "What time is it?"
        #     elif rn == 4:
        #         dericin = "How are you guys today?"
        #     elif rn == 5:
        #         dericin = "I think its time to study..."
        #     elif rn == 6:
        #         dericin = "I know you're there, Timothy!"
        #     elif rn == 7:
        #         dericin = "Do you guys renember my name?"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw()
    pygame.quit()
            
if __name__ == "__main__":
    main()
