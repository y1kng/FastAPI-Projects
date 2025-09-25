import string                  
import random                  

def get_six_digits(length: int=6) -> str:  
    charac = string.ascii_letters + string.digits                                  
    return ''.join(random.choices(charac, k=length))   