# Comment System for django_blog

## Overview
- `Comment` model linked to `Post` and `User`.
- Authenticated users can add, edit, delete their own comments.
- Comments are shown on the post detail page.

## Files added/changed
- `blog/models.py` (Comment model)
- `blog/forms.py` (CommentForm)
- `blog/views.py` (add_comment, edit_comment, delete_comment; PostDetailView context update)
- `blog/urls.py` (comment routes)
- Templates:
  - `blog/templates/blog/edit_comment.html`
  - `blog/templates/blog/delete_comment.html`
  - integrated comments block in `post_detail.html`

## How to test
1. Run migrations: `python manage.py makemigrations && python manage.py migrate`
2. Start server: `python manage.py runserver`
3. As a logged-in user:
   - Visit a post detail page
   - Add a comment
   - Edit and delete your own comment
4. Verify unauthenticated users cannot post comments and only authors can edit/delete.

## Notes
- The comment creation route uses POST at `/post/<post_pk>/comments/new/`.
- Edit route: `/post/<post_pk>/comments/<comment_pk>/edit/`
- Delete route: `/post/<post_pk>/comments/<comment_pk>/delete/`
