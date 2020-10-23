chemodan1 = ["пиджак", "граната"] 
chemodan2 = ["пиджак", "платье"] 
zapret = ["граната", "открывашка"] 

def scaner(chemodan: list):
    """ Принимает список, возвращает True или False """
    for vesch  in chemodan:
        if vesch in zapret:
           return False
        else:
            continue
    return True

print (scaner(chemodan1))

     