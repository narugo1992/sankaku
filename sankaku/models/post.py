from typing import Optional, Any
from datetime import datetime

from pydantic import BaseModel, Field, validator

from sankaku import types


class Author(BaseModel):
    id: int
    name: str
    avatar: str
    avatar_rating: types.Rating


class Tag(BaseModel):
    id: int
    name_en: str
    name_ja: Optional[str]
    type: types.Tag
    count: int
    post_count: int
    pool_count: int
    series_count: int
    locale: str
    rating: Optional[types.Rating]
    version: Optional[int]
    tagName: str
    total_post_count: int
    total_pool_count: int
    name: str


class Post(BaseModel):
    id: int
    rating: types.Rating
    status: str
    author: Author
    sample_url: Optional[str]
    sample_width: int
    sample_height: int
    preview_url: Optional[str]
    preview_width: Optional[int]
    preview_height: Optional[int]
    file_url: Optional[str]
    width: int
    height: int
    file_size: int
    extension: str = Field(alias="file_type")
    created_at: dict[str, str | int] | datetime
    has_children: bool
    has_comments: bool
    has_notes: bool
    is_favorite: bool = Field(alias="is_favorited")
    user_vote: Optional[int]
    md5: str
    parent_id: Optional[int]
    change: Optional[int]
    fav_count: int
    recommended_posts: int
    recommended_score: int
    vote_count: int
    total_score: int
    comment_count: Optional[int]
    source: Optional[str]
    in_visible_pool: bool
    is_premium: bool
    is_rating_locked: bool
    is_note_locked: bool
    is_status_locked: bool
    redirect_to_signup: bool
    sequence: Optional[int]
    generation_directives: Any
    tags: list[Tag]
    video_duration: Optional[float]

    similar_posts: list["Post"] = []

    @validator("created_at", pre=True)
    def convert_ts_to_datetime(cls, v) -> datetime:  # noqa
        return datetime.utcfromtimestamp(v["s"]).astimezone()

    @validator("extension", pre=True)
    def get_extension(cls, v) -> str:  # noqa
        return v.split("/")[1]

    @property
    def file_type(self) -> types.File:
        match self.extension:
            case "png" | "jpeg" | "webp":
                return types.File.IMAGE
            case "webm" | "mp4":
                return types.File.VIDEO
            case "gif":
                return types.File.GIF
            case _:
                raise ValueError(f"Undefined file extension [{self.extension}]")


class Page(BaseModel):
    number: int
    posts: list[Post]
