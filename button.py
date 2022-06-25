import pygame

class Button:

    def __init__(self, surface, x, y, width, height, color, image, bg):

        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.image = image
        self.bg = bg

    def draw(self):

        if self.image == None:
            self.button = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(self.surface, self.color, self.button)
        elif self.bg:
            self.bg = pygame.Rect(self.x, self.y,self.width, self.height)
            pygame.draw.rect(self.surface, self.color, self.bg)
            self.surface.blit(self.image, (self.x + self.width/2 - self.image.get_width()/2,
                                            self.y + self.height/2 - self.image.get_height()/2))
        else:
            self.surface.blit(self.image, (self.x, self.y))



    def mouse_on(self):

        self.mouse_position = pygame.mouse.get_pos()
        if self.x + self.width >= self.mouse_position[0] >= self.x and self.y + self.height >= self.mouse_position[1] >= self.y:
            return True

    def is_pressed_left(self, event):

        self.mouse_position = pygame.mouse.get_pos()
        if self.x + self.width >= self.mouse_position[0] >= self.x and self.y + self.height >= self.mouse_position[1] >= self.y:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def is_pressed_middle(self, event):

        self.mouse_position = pygame.mouse.get_pos()
        if self.x + self.width >= self.mouse_position[0] >= self.x and self.y + self.height >= self.mouse_position[1] >= self.y:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def is_pressed_right(self, event):

        self.mouse_position = pygame.mouse.get_pos()
        if self.x + self.width >= self.mouse_position[0] >= self.x and self.y + self.height >= self.mouse_position[1] >= self.y:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
