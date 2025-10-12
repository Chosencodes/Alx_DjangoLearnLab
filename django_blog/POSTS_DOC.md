# Blog Post Management Features

## Overview
Implements CRUD functionality for the Post model using Django’s class-based views.

## Features
- View all posts (`PostListView`)
- View individual post details (`PostDetailView`)
- Authenticated users can:
  - Create (`PostCreateView`)
  - Update (`PostUpdateView`)
  - Delete (`PostDeleteView`) their own posts

## Access Control
- `LoginRequiredMixin`: ensures only logged-in users can create/edit/delete
- `UserPassesTestMixin`: ensures only post authors can edit/delete
- All users can view posts

## How to Test
1. Run `python manage.py runserver`
2. Visit:
   - `/` — list view
   - `/posts/<id>/` — detail
   - `/posts/new/` — create
   - `/posts/<id>/edit/` — update
   - `/posts/<id>/delete/` — delete
3. Log in/out to confirm permission logic.
