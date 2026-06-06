import pygame
import socket

BUTTON_FONT_SIZE = 30
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
RECTANGLE_WIDTH, RECTANGLE_HEIGHT = 200, 50
BACKGROUND_COLOR = (237, 174, 88)
FONT_COLOR = (255, 255, 255)
RECTANGLE_COLOR = (184, 118, 37)
BORDER_RAD = 10
var = 300
height_their_message = 10
height_your_message = 80

# INITIALIZE PYGAME!!!
pygame.init()

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def choose_screen():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.Clock()
    
    # Font init​
    font_surface = pygame.font.SysFont("monocraft", BUTTON_FONT_SIZE)
    join_font = font_surface.render("Join a local chat", True, FONT_COLOR)
    host_font = font_surface.render("Host a local chat", True, FONT_COLOR)

    # Rectangle (Buttons) init
    join_button_pos = (SCREEN_WIDTH / 2 - RECTANGLE_WIDTH - 50, SCREEN_HEIGHT / 2 - RECTANGLE_HEIGHT - 75)
    host_button_pos = (SCREEN_WIDTH / 2 - RECTANGLE_WIDTH - 50, SCREEN_HEIGHT / 2 - RECTANGLE_HEIGHT + 75)

    rectangle_hitbox_join = pygame.Rect(join_button_pos[0], join_button_pos[1], 500, 100)
    rectangle_hitbox_host = pygame.Rect(host_button_pos[0], host_button_pos[1], 500, 100)
    # Game loop
    while True:
        for event in pygame.event.get():
            
            # Quit game if x button clicked 
            if event.type == pygame.QUIT:
                pygame.quit()
                
            # Check if button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if rectangle_hitbox_join.collidepoint(mouse_pos):
                    join_screen_enter_ip()
                if rectangle_hitbox_host.collidepoint(mouse_pos):
                    host_server()
        
        screen.fill(BACKGROUND_COLOR)

        pygame.draw.rect(screen, RECTANGLE_COLOR, rectangle_hitbox_host, 0, BORDER_RAD)
        pygame.draw.rect(screen, RECTANGLE_COLOR, rectangle_hitbox_join, 0, BORDER_RAD)
        screen.blit(host_font, (host_button_pos[0] + 75, host_button_pos[1] + 30))
        screen.blit(join_font, (join_button_pos[0] + 75, join_button_pos[1] + 30))

        pygame.display.flip()
        clock.tick(60)

def join_screen_enter_ip():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.Clock()

    text = "enter here"
    color = "gray"

    font_surface = pygame.font.SysFont("monocraft", BUTTON_FONT_SIZE)
    enter_font = font_surface.render("Enter IP", True, FONT_COLOR)
    next_font = font_surface.render("Next", True, FONT_COLOR)

    next_button_pos = (SCREEN_WIDTH / 2 - RECTANGLE_WIDTH - 50, SCREEN_HEIGHT / 2 - RECTANGLE_HEIGHT + 75)
    enter_textbox_pos = (SCREEN_WIDTH / 2 - RECTANGLE_WIDTH - 50, SCREEN_HEIGHT / 2 - RECTANGLE_HEIGHT - 100)
    typed_textbox_pos = (SCREEN_WIDTH / 2 - RECTANGLE_WIDTH - 50, SCREEN_HEIGHT / 2 - RECTANGLE_HEIGHT - 10)
    rectangle_hitbox_next = pygame.Rect(next_button_pos[0], next_button_pos[1], 500, 100)
    first = True

    while True:
        typed_font = font_surface.render(text, True, color)
        for event in pygame.event.get():
            
            # Quit game if x button clicked 
            if event.type == pygame.QUIT:
                pygame.quit()
                
            # Check if button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if rectangle_hitbox_next.collidepoint(mouse_pos):
                    join_screen_enter_port(text)
            
            if event.type == pygame.KEYDOWN:
                if first:
                    text = ""
                    first = False
                    color = "white"
                if event.unicode.isnumeric() or event.key == pygame.K_BACKSPACE or event.key == pygame.K_RETURN or event.key == pygame.K_PERIOD:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key == pygame.K_RETURN:
                        join_screen_enter_port(text)
                        print("going")
                    else:
                        text += event.unicode
                        print(text)
                
        
        screen.fill(BACKGROUND_COLOR)

        pygame.draw.rect(screen, RECTANGLE_COLOR, rectangle_hitbox_next, 0, BORDER_RAD)
        screen.blit(next_font, (next_button_pos[0] + 210, next_button_pos[1] + 30))
        screen.blit(enter_font, enter_textbox_pos)
        screen.blit(typed_font, typed_textbox_pos)


        pygame.display.flip()
        clock.tick(60)


def join_screen_enter_port(ip: str):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.Clock()

    ip_recv = ip
    text = "enter here"
    color = "gray"

    font_surface = pygame.font.SysFont("monocraft", BUTTON_FONT_SIZE)
    enter_font = font_surface.render("Enter Port", True, FONT_COLOR)
    next_font = font_surface.render("Next", True, FONT_COLOR)

    next_button_pos = (SCREEN_WIDTH / 2 - RECTANGLE_WIDTH - 50, SCREEN_HEIGHT / 2 - RECTANGLE_HEIGHT + 75)
    enter_textbox_pos = (SCREEN_WIDTH / 2 - RECTANGLE_WIDTH - 50, SCREEN_HEIGHT / 2 - RECTANGLE_HEIGHT - 100)
    typed_textbox_pos = (SCREEN_WIDTH / 2 - RECTANGLE_WIDTH - 50, SCREEN_HEIGHT / 2 - RECTANGLE_HEIGHT - 10)
    rectangle_hitbox_next = pygame.Rect(next_button_pos[0], next_button_pos[1], 500, 100)
    first = True
    while True:
        typed_font = font_surface.render(text, True, color)
        for event in pygame.event.get():
            
            
            # Quit game if x button clicked 
            if event.type == pygame.QUIT:
              pygame.quit()
                
            # Check if button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if rectangle_hitbox_next.collidepoint(mouse_pos):
                   chat_screen_wait(ip_recv, text)
            
            if event.type == pygame.KEYDOWN:
                if first:
                    text = ""
                    first = False
                    color = "white"
                if event.unicode.isnumeric() or event.key == pygame.K_BACKSPACE or event.key == pygame.K_RETURN:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key == pygame.K_RETURN and int(text) <= 65535:
                        chat_screen_wait(ip_recv, text)
                    else:
                        text += event.unicode
                        print(text)
                
        
        screen.fill(BACKGROUND_COLOR)

        pygame.draw.rect(screen, RECTANGLE_COLOR, rectangle_hitbox_next, 0, BORDER_RAD)
        screen.blit(next_font, (next_button_pos[0] + 210, next_button_pos[1] + 30))
        screen.blit(enter_font, enter_textbox_pos)
        screen.blit(typed_font, typed_textbox_pos)


        pygame.display.flip()
        clock.tick(60)

def chat_screen_wait(ip, port):

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.Clock()

    text = ""
    data = None

    font_surface = pygame.font.SysFont("monocraft", 30)
    textbox = font_surface.render(f"Your Message: {text}", True, FONT_COLOR)
    their_message = font_surface.render(data, True, FONT_COLOR)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, int(port)))
    client.setblocking(False)

    while True:
        textbox = font_surface.render(f"Your Message: {text}", True, FONT_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    if text != "" and text is not None:
                        client.send(text.encode())
                        text = ""
                else:
                    text += event.unicode
        
        screen.fill(BACKGROUND_COLOR)
        
        screen.blit(textbox, (
            SCREEN_WIDTH / 2 - var, 
            SCREEN_HEIGHT / 2 - height_your_message
        ))

        try:
            data = client.recv(1024).decode()
            if data:
                their_message = font_surface.render(f"Their Message: {data}", True, FONT_COLOR)
        except BlockingIOError:
            pass
        except socket.error as e:
            print(e)

        screen.blit(their_message, (
                SCREEN_WIDTH / 2 - var, 
                SCREEN_HEIGHT / 2 - height_their_message
            ))

        pygame.display.flip()
        clock.tick(60)
        


def host_server():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.Clock()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_info = (get_local_ip(), 58372)

    font_surface = pygame.font.SysFont("monocraft", 30)
    info_label_ip = font_surface.render(f"IP for client: {str(local_info[0])}", True, FONT_COLOR)
    info_label_port = font_surface.render(f"Port for client: {str(local_info[1])}", True, FONT_COLOR)
    next_button = font_surface.render("Next", True, FONT_COLOR)

    rectangle = pygame.Rect(SCREEN_WIDTH / 2 - 250, SCREEN_HEIGHT / 2 + 25, 500, 100)

    rendered = False
    server_already_bound = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rendered:
                    mouse_pos = pygame.mouse.get_pos()
                    if rectangle.collidepoint(mouse_pos):
                        server.close()
                        host_chat(local_info[0], local_info[1])
                        

        screen.fill(BACKGROUND_COLOR)

        try:
            if server_already_bound == False:
                server.setblocking(False)
                server.bind(("0.0.0.0", 123))
                server.listen(1)
                server_already_bound = True
            screen.blit(info_label_ip, (SCREEN_WIDTH / 2 - 230, SCREEN_HEIGHT / 2 - 120))
            screen.blit(info_label_port, (SCREEN_WIDTH / 2 - 230, SCREEN_HEIGHT / 2 - 50))
            pygame.draw.rect(screen, RECTANGLE_COLOR, rectangle, 0, BORDER_RAD)
            screen.blit(next_button, (rectangle.center[0] - 50, rectangle.center[1] - 16))
            rendered = True
        except BlockingIOError:
            pass
        except socket.error as e:
            print(e)

        pygame.display.flip()
        clock.tick(60)

def host_chat(ip, port):

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.Clock()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(1)
    server.setblocking(False)

    text = ""
    data = None

    font_surface = pygame.font.SysFont("monocraft", 30)
    their_message = font_surface.render(data, True, FONT_COLOR)

    client = None

    while True:
        textbox = font_surface.render(f"Your message: {text}", True, FONT_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    if client is not None:
                        if text != "" and text is not None:
                            client.send(text.encode())
                            text = ""
                else:
                    text += event.unicode

        screen.fill(BACKGROUND_COLOR)

        screen.blit(textbox, (
            SCREEN_WIDTH / 2 - var, 
            SCREEN_HEIGHT / 2 - height_your_message
        ))
        
        try:
            if client is None:
                client, addr = server.accept()
            data = client.recv(1024).decode()
            if data:
                their_message = font_surface.render(f"Their Message: {data}", True, FONT_COLOR)

        except BlockingIOError:
            pass
        except socket.error as e:
            print(e)
        
        screen.blit(their_message, (
                SCREEN_WIDTH / 2 - var, 
                SCREEN_HEIGHT / 2 - height_their_message
            ))
        pygame.display.flip()
        clock.tick(60)
        
choose_screen()