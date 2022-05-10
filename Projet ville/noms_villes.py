def ville():
    import lib.random as ra
    
    with open("city_name/city_names.txt","r") as v:
        NomsVilles = v.read().split("\n")
    return NomsVilles[ra.randint(0,len(NomsVilles)-1)]