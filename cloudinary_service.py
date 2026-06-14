import cloudinary
import cloudinary.uploader

from config import settings

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
    secure=True
)


def upload_featured_image(file):

    result = cloudinary.uploader.upload(
        file.file,
        folder="toolmatix/blogs/featured"
    )

    return result["secure_url"]

def upload_editor_image(file):

    result = cloudinary.uploader.upload(
        file.file,
        folder="toolmatix/blogs/editor"
    )

    return result["secure_url"]

# def upload_blog_images(files):

#     image_urls = []

#     for file in files:

#         result = cloudinary.uploader.upload(
#             file.file,
#             folder="toolmatix/blogs/gallery"
#         )

#         image_urls.append(result["secure_url"])

#     return image_urls