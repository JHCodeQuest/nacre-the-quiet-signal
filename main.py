import pygame

pygame.init()

screen = pygame.display.set_mode((1100, 720))
pygame.display.set_caption("Narce - The Quiet Signal")
clock = pygame.time.Clock()
title_font = pygame.font.Font(None, 48)
body_font = pygame.font.Font(None,28)

opening_lines = [
    "Your exploration vessel waits in Kestrel Station's salvage hangar.",
    "Patch rolls out from beneath an open maintenance panel.",
    "",
    'PATCH: "Engines operational. Coffee system... less confidently so."',
    "",
    "Beyond the hangar doors, an unidentified signal repeats.",
]

signal_button = pygame.Rect(50,420,450,55)
patch_button = pygame.Rect(50,495,450,55)

response = ""

signal_inspected = False
observe_button = pygame.Rect(530,420,500,55)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if signal_button.collidepoint(event.pos):
                response = (
                    "The signal repeats every twelve seconds. "
                    "Its source is unknown."
                )
                signal_inspected = True

            elif patch_button.collidepoint(event.pos):
                response = (
                    'PATCH: "Ready to explore. '
                    'A long-range scanner would help."'
                )
            elif signal_inspected and observe_button.collidepoint(event.pos):
                response = "Three cycles recorded. The signal's origin remains unknown."

    screen.fill((10,18,28))
    title = title_font.render("KESTREL STATION", True, (100,220,210))
    screen.blit(title, (50,50))

    for index, line in enumerate(opening_lines):
        text = body_font.render(line, True, (220,230,240))
        screen.blit(text, (50, 140 + index * 36))

    for button, label in [
        (signal_button, "Inspect the signal"),
        (patch_button, "Ask Patch about the ship"),
    ]:
        pygame.draw.rect(screen, (25,65,80), button, border_radius=8)
        button_text = body_font.render(label, True, (220, 230, 240))
        screen.blit(button_text, (button.x + 16, button.y + 16))

    if signal_inspected:
        pygame.draw.rect(
            screen,
            (25,65,80),
            observe_button,
            border_radius=8,
        )

        observe_text = body_font.render(
            "Record more signal cycles",
            True,
            (220,230,240),
        )
        screen.blit(
            observe_text,
            (observe_button.x + 16, observe_button.y + 16),
        )

    response_text = body_font.render(response, True, (240,210,140))
    screen.blit(response_text, (50, 590))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
