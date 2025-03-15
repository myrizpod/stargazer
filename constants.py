GAME_DRAW_SIZE_X = 320
GAME_DRAW_SIZE_Y = 180
RENDER_BUFFER = None
CLOCK = None
SCREEN_MULT = 0


BG_BLACK = (14,15,33)
BG_DARK_BLUE = (12,11,66)
BG_DARK_PURPLE = (34,0,41)
WHITE = (199,212,225)

MAP_SIZE = 1024

class AllLevels:
    import readers as r
    import sound_manager.melodies as m
    from levels_manager.level import Level

    ALL_LEVELS = [
        [Level(r.read_level("resources/levels/tutorial.txt"),m.Melody(r.read_melody("resources/melodies/tutorial.txt"))), (0, 250)],
        [Level(r.read_level("resources/levels/level1.txt"),m.Melody(r.read_melody("resources/melodies/level1.txt"))), (50, 50)],
        [Level(r.read_level("resources/levels/level2.txt"),m.Melody(r.read_melody("resources/melodies/level2.txt"))), (100, 20)],
        [Level(r.read_level("resources/levels/level3.txt"),m.Melody(r.read_melody("resources/melodies/level3.txt"))), (150, 120)],
        [Level(r.read_level("resources/levels/level4.txt"),m.Melody(r.read_melody("resources/melodies/level4.txt"))), (200, 80)],
        [Level(r.read_level("resources/levels/level5.txt"),m.Melody(r.read_melody("resources/melodies/level5.txt"))), (250, 20)],
    ]