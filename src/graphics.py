import file
import settings

sprites = {}
cats = {}


try:
    small_sheet = file.load_image("fingertwisternavbuttons.png", settings.ASSETS_FOLDER)
    small_size = (40, 40)
    large_sheet = file.load_image("fingertwisterbuttonsheet.png", settings.ASSETS_FOLDER)
    large_size = (100, 100)
    button_flash = file.load_image("fingertwisteroutline.png", settings.ASSETS_FOLDER)
    button_flash_size = (160, 120)
    button_flash_fail = file.load_image("fingertwisteroutlinefail.png", settings.ASSETS_FOLDER)
    button_flash_fail_size = (160, 120)

    #Small nav buttons
    sprites["small_white"] = small_sheet.subsurface(((0, 0), small_size)).copy()
    sprites["small_white_pressed"] = small_sheet.subsurface(((40, 0), small_size)).copy()
    sprites["small_white_muted"] = small_sheet.subsurface(((80, 0), small_size)).copy()
    sprites["small_white_pressed_muted"] = small_sheet.subsurface(((120, 0), small_size)).copy()

    #TODO fix these large decals like the small ones
    #large decal buttons
    sprites["large_yellow"] = large_sheet.subsurface(((0, 0), large_size)).copy()
    sprites["large_yellow_pressed"] = large_sheet.subsurface(((100, 0), large_size)).copy()
    sprites["large_yellow_muted"] = large_sheet.subsurface(((200, 0), large_size)).copy()
    sprites["large_yellow_pressed_muted"] = large_sheet.subsurface(((300, 0), large_size)).copy()

    sprites["large_red"] = large_sheet.subsurface(((400, 0), large_size)).copy()
    sprites["large_red_pressed"] = large_sheet.subsurface(((500, 0), large_size)).copy()
    sprites["large_red_muted"] = large_sheet.subsurface(((600, 0), large_size)).copy()
    sprites["large_red_pressed_muted"] = large_sheet.subsurface(((700, 0), large_size)).copy()

    sprites["large_green"] = large_sheet.subsurface(((800, 0), large_size)).copy()
    sprites["large_green_pressed"] = large_sheet.subsurface(((900, 0), large_size)).copy()
    sprites["large_green_muted"] = large_sheet.subsurface(((1000, 0), large_size)).copy()
    sprites["large_green_pressed_muted"] = large_sheet.subsurface(((1100, 0), large_size)).copy()

    sprites["large_blue"] = large_sheet.subsurface(((1200, 0), large_size)).copy()
    sprites["large_blue_pressed"] = large_sheet.subsurface(((1300, 0), large_size)).copy()
    sprites["large_blue_muted"] = large_sheet.subsurface(((1400, 0), large_size)).copy()
    sprites["large_blue_pressed_muted"] = large_sheet.subsurface(((1500, 0), large_size)).copy()

    sprites["large_white"] = large_sheet.subsurface(((1600, 0), large_size)).copy()
    sprites["large_white_pressed"] = large_sheet.subsurface(((1700, 0), large_size)).copy()
    sprites["large_white_muted"] = large_sheet.subsurface(((1800, 0), large_size)).copy()
    sprites["large_white_pressed_muted"] = large_sheet.subsurface(((1900, 0), large_size)).copy()

    #cats
    lane = file.load_image("lane.jpg", settings.ASSETS_FOLDER)
    weeb = file.load_image("weeb.jpg", settings.ASSETS_FOLDER)
    kevin = file.load_image("kevin.png", settings.ASSETS_FOLDER)
    onyxmaisie = file.load_image("onyxmaisie.jpg", settings.ASSETS_FOLDER)
    eggfia = file.load_image("eggfia.png", settings.ASSETS_FOLDER)
    cats["lane"] = lane
    cats["weeb"] = weeb
    cats["kevin"] = kevin
    cats["onyxmaisie"] = onyxmaisie
    cats["eggfia"] = eggfia

except Exception as e:
    print("image load failed")
    print(e)
