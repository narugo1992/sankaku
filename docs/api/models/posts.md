# Documentation for `posts.py`

::: sankaku.models.posts.GenerationDirectives
    options:
      show_source: false
      members:
        - width
        - height
        - prompt
        - batch_size
        - batch_count
        - sampling_steps
        - negative_prompt

---

::: sankaku.models.posts.BasePost
    options:
      show_source: false
      members:
        - id
        - created_at
        - rating
        - status
        - author
        - file_url
        - preview_url
        - width
        - height
        - file_size
        - extension
        - generation_directives
        - md5
        - tags
        - file_type

---

::: sankaku.models.posts.Comment
    options:
      show_source: false
      members:
        - id
        - created_at
        - post_id
        - author
        - body
        - score
        - parent_id
        - children
        - deleted
        - deleted_by
        - updated_at
        - can_reply
        - reason

---

::: sankaku.models.posts.Post
    options:
      show_source: false
      members:
        - sample_url
        - sample_width
        - sample_height
        - preview_width
        - preview_height
        - has_children
        - has_comments
        - has_notes
        - is_favorited
        - user_vote
        - parent_id
        - change
        - fav_count
        - recommended_posts
        - recommended_score
        - vote_count
        - total_score
        - comment_count
        - source
        - in_visible_pool
        - is_premium
        - is_rating_locked
        - is_note_locked
        - is_status_locked
        - redirect_to_signup
        - sequence
        - video_duration

---

::: sankaku.models.posts.AIPost
    options:
      show_source: false
      members:
        - updated_at
        - post_associated_id