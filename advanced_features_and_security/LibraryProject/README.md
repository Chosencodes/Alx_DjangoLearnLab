# LibraryProject

## Custom User

- `CustomUser` extends `AbstractUser` with `date_of_birth` and `profile_photo`.

## Book Model

- Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`.
- Views enforce permissions with `@permission_required`.

## Admin

- `CustomUserAdmin` configured to include extra fields.

## Templates

- `book_list.html` for viewing/searching books.
- `form_example.html` for add/edit book forms.

## Security

- CSRF tokens included in all forms.
- Permissions applied to restrict access to views.
