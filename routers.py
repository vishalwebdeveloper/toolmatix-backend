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
    get_published_blogs,
    get_blog_by_id,
    delete_blog,
    update_blog,
    update_blog_status,
    get_blog_by_slug
)
from cloudinary_service import (
    upload_editor_image
)
from database import get_db
 
router=APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)
@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": "alive"
    }
# create a blog api endpoint
@router.post("")
async def create_blog_api(
    title: str = Form(...),
    short_description: str = Form(...),
    description: str = Form(...),
    tags: str = Form(""),
    status: str = Form("draft"),
    featured_image: str = Form(...),  # Cloudinary URL
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

# old api code
# @router.post("")
# async def create_blog_api(
#     title: str = Form(...),
#     short_description: str = Form(...),
#     description: str = Form(...),
#     tags: str = Form(""),
#     status: str = Form("draft"),
#     featured_image: UploadFile = File(...),
#     db: Session = Depends(get_db)
# ):

#     return create_blog(
#         db,
#         title,
#         short_description,
#         description,
#         tags,
#         status,
#         featured_image
#     )
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

@router.get("/id/{blog_id}")
def get_blog(
    blog_id: int,
    db: Session = Depends(get_db)
):
    return get_blog_by_id(
        db,
        blog_id
    )

@router.get("/{slug}")
def get_blog(
    slug: str,
    db: Session = Depends(get_db)
):
    return get_blog_by_slug(
        db,
        slug
    )

@router.delete("/{blog_id}")
def remove_blog(
    blog_id: int,
    db: Session = Depends(get_db)
):
    return delete_blog(
        db,
        blog_id
    )

@router.put("/{id}")
async def edit_blog(
    blog_id: int,
    title: str = Form(...),
    short_description: str = Form(...),
    description: str = Form(...),
    tags: str = Form(""),
    status: str = Form("draft"),
    featured_image: str = Form(...),
    db: Session = Depends(get_db)
):

    return update_blog(
        db,
        blog_id,
        title,
        short_description,
        description,
        tags,
        status,
        featured_image
    )

@router.patch("/{blog_id}/status")
def change_status(
    blog_id: int,
    db: Session = Depends(get_db)
):
    return update_blog_status(
        db,
        blog_id
    )

