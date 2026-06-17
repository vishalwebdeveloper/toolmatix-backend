import json
import re
from fastapi import HTTPException

from models import Blog
# from cloudinary_service import (
#     upload_featured_image
# )


def generate_slug(title):

    slug=title.lower()

    slug=re.sub(
        r'[^a-z0-9]+',
        '-',
        slug
    )

    return slug.strip('-')
# new crud api
def create_blog(
    db,
    title,
    short_description,
    description,
    tags,
    status,
    featured_image
):

    blog = Blog(
        title=title,
        slug=generate_slug(title),
        short_description=short_description,
        description=description,
        featured_image=featured_image,  # Direct Cloudinary URL
        tags=tags,
        status=status
    )

    db.add(blog)
    db.commit()
    db.refresh(blog)

    return blog
# old crud api

# def create_blog(
#     db,
#     title,
#     short_description,
#     description,
#     tags,
#     status,
#     featured_image
# ):

#     featured_url = upload_featured_image(
#         featured_image
#     )

#     blog = Blog(
#         title=title,
#         slug=generate_slug(title),
#         short_description=short_description,
#         description=description,
#         featured_image=featured_url,
#         tags=tags,
#         status=status
#     )

#     db.add(blog)

#     db.commit()

#     db.refresh(blog)

#     return blog

def get_all_blogs(db):

    return (
        db.query(Blog)
        .order_by(Blog.id.desc())
        .all()
    )

def get_published_blogs(db):

    return (
        db.query(Blog)
        .filter(
            Blog.status == "published"
        )
        .order_by(Blog.id.desc())
        .all()
    )

def get_blog_by_id(db, blog_id: int):

    blog = (
        db.query(Blog)
        .filter(Blog.id == blog_id)
        .first()
    )

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    return blog

def get_blog_by_slug(db, slug: str):

    blog = (
        db.query(Blog)
        .filter(Blog.slug == slug)
        .first()
    )

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    return blog

def delete_blog(db, blog_id: int):

    blog = (
        db.query(Blog)
        .filter(Blog.id == blog_id)
        .first()
    )

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    db.delete(blog)
    db.commit()

    return {
        "success": True,
        "message": "Blog deleted successfully"
    }


def update_blog(
    db,
    blog_id,
    title,
    short_description,
    description,
    tags,
    status,
    featured_image
):

    blog = (
        db.query(Blog)
        .filter(Blog.id == blog_id)
        .first()
    )

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    blog.title = title
    blog.slug = generate_slug(title)
    blog.short_description = short_description
    blog.description = description
    blog.tags = tags
    blog.status = status
    blog.featured_image = featured_image

    db.commit()
    db.refresh(blog)

    return blog


def update_blog_status(
    db,
    blog_id: int
):

    blog = (
        db.query(Blog)
        .filter(Blog.id == blog_id)
        .first()
    )

    if not blog:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    current_status = (
        blog.status.lower()
    )

    if current_status == "draft":
        blog.status = "published"
        message = (
            "Blog published successfully"
        )

    else:
        blog.status = "draft"
        message = (
            "Blog moved to draft successfully"
        )

    db.commit()
    db.refresh(blog)

    return {
        "success": True,
        "blog_id": blog.id,
        "status": blog.status,
        "message": message
    }