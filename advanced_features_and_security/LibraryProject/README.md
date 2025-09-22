# LibraryProject

## Permissions and Groups

This project uses Django permissions and groups to control access:

- **Custom Permissions:** can_view, can_create, can_edit, can_delete (Book model)
- **Groups:** Editors, Viewers, Admins
- **Views:** Protected with @permission_required decorators

## How to Use

1. Create users and assign them to groups in the Django admin.
2. Users can access functionality based on their group permissions:
   - Editors: can create and edit books
   - Viewers: can only view books
   - Admins: full access
3. Visit `/books/` to view the book list.
