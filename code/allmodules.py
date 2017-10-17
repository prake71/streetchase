#all modules
#this is simply to ensure init type functions
#will work, because all needed game modules will
#be imported. groove on


#we'll just parse this string out and import everything in it

# example:
'''
modules_string = """
ammobar, attractmode, constants, data, enemy, explosion, fragment,
game, gamemode, gameovermode, gametitle, intro, phaser, pirate,
playmode, powerup, score, soundmanager, spaceship, spritesheet,
starfield, title
"""
'''
modules_string = """
attractmode, constants, data, game, gamemode, gameovermode, playmode, spritesheet
"""

def modules_import():
    mods = modules_string.split(',')
    for m in mods:
        m = m.strip()
        __import__(m)

modules_import()
