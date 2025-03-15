GAME_DRAW_SIZE_X = 320
GAME_DRAW_SIZE_Y = 180
RENDER_BUFFER = None
CLOCK = None
SCREEN_MULT = 0


BG_BLACK = (14,4,33)
BG_DARK_BLUE = (12,11,66)
BG_DARK_PURPLE = (34,0,41)
WHITE = (199,212,225)
GRAYS = ((57,41,70),(91,83,125),(146,183,184))

MAP_SIZE = 1024

class AllLevels:
    import readers as r
    import sound_manager.melodies as m
    from levels_manager.level import Level

    ALL_LEVELS = [
        [Level(r.read_level("resources/levels/tutorial.txt"),m.Melody(r.read_melody("resources/melodies/tutorial.txt"))), (70, 250)],
        [Level(r.read_level("resources/levels/level1.txt"),m.Melody(r.read_melody("resources/melodies/level1.txt"))), (120, 200)],
        [Level(r.read_level("resources/levels/level2.txt"),m.Melody(r.read_melody("resources/melodies/level2.txt"))), (170, 230)],
        [Level(r.read_level("resources/levels/level3.txt"),m.Melody(r.read_melody("resources/melodies/level3.txt"))), (220, 270)],
        [Level(r.read_level("resources/levels/level4.txt"),m.Melody(r.read_melody("resources/melodies/level4.txt"))), (270, 240)],
        [Level(r.read_level("resources/levels/level5.txt"),m.Melody(r.read_melody("resources/melodies/level5.txt"))), (320, 210)],
    ]