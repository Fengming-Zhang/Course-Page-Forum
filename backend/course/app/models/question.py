from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.models.base import Base


class Question(Base):
    qid = Column(Integer, primary_key=True)
    content = Column(Text)
    author_id = Column(String(10), ForeignKey('user.gid'))
    stars = Column(Integer, default=0)
    answer = relationship('Answer', backref='question')
    discussions = relationship('Discussion', backref='question')
    course_id = Column(Integer, ForeignKey('course.cid'))
    tags = relationship('Tag', backref='question', secondary='QuestionTag')