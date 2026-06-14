from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime
from database import Base


class Blog(Base):

    __tablename__="blogs"

    id=Column(Integer,primary_key=True,index=True)

    title=Column(String(255),nullable=False)

    slug=Column(String(255),unique=True,index=True)

    short_description=Column(Text,nullable=False)

    description=Column(Text,nullable=False)

    featured_image=Column(Text,nullable=False)

    tags=Column(Text,nullable=False)

    status = Column(String(20),default="draft")
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )