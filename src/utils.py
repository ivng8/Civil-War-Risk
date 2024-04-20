import pygame as pg


def draw_text(screen, font, text, color, x, y, center=False, size=20):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


def draw_multiline_text(
    screen, font, multitext: list, color, x, y, center=False, size=20
):
    for text in multitext:
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if center:
            text_rect.center = (x, y)
        else:
            text_rect.topleft = (x, y)
        screen.blit(text_surface, text_rect)
        y += text_surface.get_height()


def keyevent(attack: str, defend: str):
    if (attack.find('Virgina') + defend.find('Virgina') > -1):
        print("Battle of New Market Heights (1864): United States Colored Troops (USCT)," +
              "primarily composed of African American soldiers, played a crucial role in the Union victory.")
    elif (attack.find('South Carolina') + defend.find('South Carolina') > -1):
        print("Battle of Fort Wagner (1863): The 54th Massachusetts Infantry Regiment," +
              "comprised of African American soldiers, led the assault on Fort Wagner," + 
              "showcasing their bravery despite heavy casualties.")
    elif (attack.find('Oklahoma') + defend.find('Oklahoma') > -1):
        print("Battle of Honey Springs (1863): Native American troops, including those from the Cherokee," + 
              "Choctaw, and Creek nations, fought on both sides of the conflict. The battle in Indian Territory" + 
              "(now Oklahoma) saw Native American units engaging in combat. Furthermore, Battle of Pea Ridge (1862):" + 
              "Cherokee, Creek, and Seminole troops fought alongside Confederate forces in this engagement.")
    elif (attack.find('Arkansas') + defend.find('Arkansas') > -1):
        print("Battle of Pea Ridge (1862): Cherokee, Creek, and Seminole troops fought alongside" + 
              "Confederate forces in this engagement in Arkansas.")