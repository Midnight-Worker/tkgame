import os
import tkinter as tk
import pygame

root = tk.Tk()
root.geometry("900x600")

left = tk.Frame(root, width=250)
left.pack(side="left", fill="y")

embed = tk.Frame(root)
embed.pack(side="right", fill="both", expand=True)

root.update()  # wichtig: Frame muss existieren

os.environ["SDL_WINDOWID"] = str(embed.winfo_id())
# optional: os.environ["SDL_VIDEODRIVER"] = "windib"  # eher alt/selten nötig

pygame.display.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

x = 10

def tick():
    global x
    for e in pygame.event.get():
        pass

    screen.fill((20, 20, 20))
    pygame.draw.circle(screen, (255, 255, 255), (x, 100), 20)
    pygame.display.flip()

    x = (x + 3) % 640
    clock.tick(60)
    root.after(16, tick)

tick()
root.mainloop()

