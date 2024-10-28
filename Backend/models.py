from database import db
from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects.postgresql import JSON

class Video(db.Model):
    __tablename__ = "videos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Primary key, auto-incremented
    video_id = db.Column(db.String, nullable=True)  # YouTube video ID as a string, no unique or foreign key constraint
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    sbert_embedding = db.Column(Vector(384), nullable=False)
    transcript_chunks = db.Column(JSON, nullable=False)

class VideoChunk(db.Model):
    __tablename__ = "video_chunks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Primary key, auto-incremented
    video_id = db.Column(db.String, nullable=True)  # Independent string column for video ID (not linked to videos table)
    start_time = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)
    sbert_embedding = db.Column(Vector(384), nullable=False)