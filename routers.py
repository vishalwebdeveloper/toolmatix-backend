from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form
from fastapi import Depends

from sqlalchemy.orm import Session
from typing import List
from crud import (
    create_blog,
    get_all_blogs,
    get_published_blogs
)
from cloudinary_service import (
    upload_editor_image
)
from database import get_db
 
router=APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

# create a blog api endpoint
@router.post("")
async def create_blog_api(
    title: str = Form(...),
    short_description: str = Form(...),
    description: str = Form(...),
    tags: str = Form(""),
    status: str = Form("draft"),
    featured_image: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    return create_blog(
        db,
        title,
        short_description,
        description,
        tags,
        status,
        featured_image
    )
# upload editor image for the description image api endpoint

@router.post(
    "/upload-editor-image"
)
async def upload_editor_image_api(
    file: UploadFile = File(...)
):

    image_url = upload_editor_image(
        file
    )

    return {
        "success": True,
        "url": image_url
    }

# get all blogs api endpoint
@router.get("")
def get_blogs(
    db:Session=Depends(get_db)
):

    return get_all_blogs(db)

@router.get("/published")
def published_blogs(
    db: Session = Depends(get_db)
):

    return get_published_blogs(db)