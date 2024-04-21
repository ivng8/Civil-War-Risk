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
    if (attack.find('Virgina') + defend.find('Virgina') > -2):
        print("Battle of New Market Heights (1864): United States Colored Troops (USCT)," +
              "primarily composed of African American soldiers, played a crucial role in the Union victory." + 
              "Battle of the Crater (1864): Although not primarily a battle involving racial minorities, " + 
              "the involvement of the 4th Division of the United States Colored Troops in the failed assault " + 
              "on Petersburg, Virginia, is notable. The Union plan to detonate explosives in a mine under " + 
              "Confederate lines and exploit the resulting crater failed, resulting in heavy casualties, " + 
              "including for African American soldiers.")
    elif (attack.find('South Carolina') + defend.find('South Carolina') > -1):
        print("Battle of Fort Wagner (1863): The 54th Massachusetts Infantry Regiment," +
              "comprised of African American soldiers, led the assault on Fort Wagner," + 
              "showcasing their bravery despite heavy casualties.")
    elif (attack.find('Oklahoma') + defend.find('Oklahoma') > -2):
        print("Battle of Honey Springs (1863): Native American troops, including those from the Cherokee," + 
              "Choctaw, and Creek nations, fought on both sides of the conflict. The battle in Indian Territory" + 
              "(now Oklahoma) saw Native American units engaging in combat. Furthermore, Battle of Pea Ridge (1862):" + 
              "Cherokee, Creek, and Seminole troops fought alongside Confederate forces in this engagement.")
    elif (attack.find('Arkansas') + defend.find('Arkansas') > -2):
        print("Battle of Pea Ridge (1862): Cherokee, Creek, and Seminole troops fought alongside" + 
              "Confederate forces in this engagement in Arkansas.")
    elif (attack.find('Missouri') + defend.find('Missouri') > -2):
        print("Battle of Island Mound (1862): This engagement in Missouri is notable for being one of the first times" + 
              "African American soldiers fought in combat during the Civil War. The 1st Kansas Colored Volunteer" + 
              "Infantry, primarily composed of African American soldiers, repelled Confederate guerrilla forces.")
    elif (attack.find('Louisiana') + defend.find('Lousisiana') > -2):
        print("Battle of Milliken's Bend (1863): African American troops, including the 9th and 11th Louisiana " + 
              "Native Guard (later reorganized as the 1st and 2nd Louisiana Native Guard), played a significant " + 
              "role in repelling a Confederate attack on a Union supply depot in Louisiana.")
    elif (attack.find('Tennessee') + defend.find('Tennessee') > -2):
        print("Battle of Fort Pillow (1864): This infamous battle in Tennessee saw a significant engagement" + 
              " between Union forces, including African American troops, and Confederate forces led by General Nathan " + 
              "Bedford Forrest. The Confederate troops massacred African American soldiers who had surrendered, " + 
              "leading to outrage in the North and contributing to the escalation of the conflict.")
    elif (attack.find('Florida') + defend.find('Florida') > -2):
        print("Battle of Olustee (1864): This battle in Florida involved the 54th Massachusetts Infantry Regiment, " + 
              "one of the most well-known African American units in the Union Army. Despite their valor, the Union forces, " + 
              "including the 54th Massachusetts, were defeated by Confederate troops.")
