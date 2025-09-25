from sqlalchemy.orm import Session
from .models import ShortUrl 
from .utils import get_six_digits

def get_short_link(db: Session, ori_url: str) -> ShortUrl:      
    short_one = get_six_digits()
    
    ori_url = str(ori_url)  # ensure the input is a string

    db_short_url = ShortUrl(short_one = short_one, ori_url = ori_url)

    db.add(db_short_url)
    db.commit()
    db.refresh(db_short_url)

    return db_short_url

def get_ori_url(db: Session, short_one: str) -> str|None:    # return original URL if the short code exists
    db_short_url = db.query(ShortUrl).filter(ShortUrl.short_one == short_one).first() 
    if db_short_url is None:
        return None                                        
    return db_short_url.ori_url

def incre_count(db: Session, short_one: str):     # increment access count for a short link
    db_short_url = db.query(ShortUrl).filter(ShortUrl.short_one == short_one).first()
    if db_short_url:
        db_short_url.count_c += 1
        db.commit()                                     
        db.refresh(db_short_url)
        return db_short_url
    return None                                   

def get_all_shortlink(db: Session):     # return a clean list of all short codes
    allshort = db.query(ShortUrl.short_one).all()
    return [i[0] for i in allshort]                              

