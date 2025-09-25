from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/shorten", response_model=schemas.SysCheck)
def new_short_code(payload: schemas.UserCheck, db: Session = Depends(get_db)):
    my_short = crud.get_short_link(db, payload.ori_url)
    return my_short

@router.get("/original/{short_code}", response_model=schemas.UserCheck)  
def get_original_url(short_code: str, db: Session = Depends(get_db)):
    ur_long = crud.get_ori_url(db, short_code)
    if ur_long is None:
        raise HTTPException(status_code=404, detail="No matched original URL") 
    else:
        return {"ori_url": ur_long} 

@router.put("/click/{short_code}", response_model=schemas.SysCheck)
def increase_count_click(short_code: str, db: Session = Depends(get_db)):
    ur_click = crud.incre_count(db, short_code)
    if ur_click is None:
        raise HTTPException(status_code=404, detail="No matched object found")
    else:
        return ur_click

@router.get("/allshort", response_model=List[str])
def get_all_shortcode(db: Session = Depends(get_db)):
    all_ur_short = crud.get_all_shortlink(db)
    return all_ur_short