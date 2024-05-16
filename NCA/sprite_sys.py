import pygame

class Sprites():
    def __init__(self):
        
        self.pause=pygame.image.load("assets/Sprites/Pause Logo.png").convert_alpha()
        #character
        player_sheet=pygame.image.load("assets/Sprites/Character_Sheet.png").convert_alpha()
        
        
        self.character_sheet={"Right"   : [player_sheet.subsurface(pygame.Rect(0,0,17,21)),
                                           player_sheet.subsurface(pygame.Rect(19,0,17,21)),
                                           player_sheet.subsurface(pygame.Rect(0,0,17,21)),
                                           player_sheet.subsurface(pygame.Rect(38,0,17,21))],
                              "Left"    : [player_sheet.subsurface(pygame.Rect(0,23,17,21)),
                                           player_sheet.subsurface(pygame.Rect(19,23,17,21)),
                                           player_sheet.subsurface(pygame.Rect(0,23,17,21)),
                                           player_sheet.subsurface(pygame.Rect(38,23,17,21))],
                              
                              "Right Arm" : player_sheet.subsurface(pygame.Rect(57,0,14,10)),
                              
                              "Left Arm" : player_sheet.subsurface(pygame.Rect(57,11,14,10))
                              }
        
        #cheese
        cheese_sheet=pygame.image.load("assets/Sprites/cheese_Sheet.png").convert_alpha()
        
        
        self.cheese_sheet={"Right"   : [cheese_sheet.subsurface(pygame.Rect(0,0,14,24)),
                                           cheese_sheet.subsurface(pygame.Rect(15,0,14,24)),
                                           cheese_sheet.subsurface(pygame.Rect(0,0,14,24)),
                                           cheese_sheet.subsurface(pygame.Rect(30,0,14,24))],
                           "Left"    : [cheese_sheet.subsurface(pygame.Rect(0,26,14,24)),
                                           cheese_sheet.subsurface(pygame.Rect(15,26,14,24)),
                                           cheese_sheet.subsurface(pygame.Rect(0,26,14,24)),
                                           cheese_sheet.subsurface(pygame.Rect(30,26,14,24))],
                           
                           "Right Belly"     : cheese_sheet.subsurface(pygame.Rect(71,0,25,24)),
                           "Right Back"     : cheese_sheet.subsurface(pygame.Rect(45,0,25,24)),
                          "Left Belly"     : cheese_sheet.subsurface(pygame.Rect(71,26,25,24)),
                          "Left Back"     : cheese_sheet.subsurface(pygame.Rect(45,26,25,24))
                                  
                              }
        
        self.lilcheese_sheet={"Right"   :   [cheese_sheet.subsurface(pygame.Rect(0,52,14,19)),
                                           cheese_sheet.subsurface(pygame.Rect(15,52,14,19)),
                                           cheese_sheet.subsurface(pygame.Rect(0,52,14,19)),
                                           cheese_sheet.subsurface(pygame.Rect(30,52,14,19))],
                            
                           "Left"    : [cheese_sheet.subsurface(pygame.Rect(0,72,14,19)),
                                           cheese_sheet.subsurface(pygame.Rect(15,72,14,19)),
                                           cheese_sheet.subsurface(pygame.Rect(0,72,14,19)),
                                           cheese_sheet.subsurface(pygame.Rect(30,72,14,19))],
                           
                           "Right Belly"     : cheese_sheet.subsurface(pygame.Rect(45,52,19,19)),
                           "Right Back"     : cheese_sheet.subsurface(pygame.Rect(65,52,19,19)),
                          "Left Belly"     : cheese_sheet.subsurface(pygame.Rect(45,72,19,19)),
                          "Left Back"     : cheese_sheet.subsurface(pygame.Rect(65,72,19,19))
                                  
                              }
                
                
