def is_ipv4_address(ip):
    octects=ip.split(".")
    i=0
    while(i<len(octects)):
        if octects[i].isdigit():
        
            if int(octects[i])>=0 and int(octects[i])<=255 :
                i=i+1
                continue
            else :
                return False
                break
        else :
            return False
            break
    return True

