import json
import re

from models import Blog
from cloudinary_service import (
    upload_featured_image
)


def generate_slug(title):

    slug=title.lower()

    slug=re.sub(
        r'[^a-z0-9]+',
        '-',
        slug
    )

    return slug.strip('-')


def create_blog(
    db,
    title,
    short_description,
    description,
    tags,
    status,
    featured_image
):

    featured_url = upload_featured_image(
        featured_image
    )

    blog = Blog(
        title=title,
        slug=generate_slug(title),
        short_description=short_description,
        description=description,
        featured_image=featured_url,
        tags=tags,
        status=status
    )

    db.add(blog)

    db.commit()

    db.refresh(blog)

    return blog

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