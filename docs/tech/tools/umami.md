# Umami

| What          | Where                                     |
|---------------|-------------------------------------------|
| Official Page | <https://umami.is/>                       |
| Docs          | <https://umami.is/docs>                   |
| Source        | <https://github.com/umami-software/umami> |

Umami is an open-source, self-hosted web analytics solution.

## Reset Credentials

If is still possible to access the database, add a new user with the default credentials e.g.:

``` sql
insert into user (user_id, username, password, role) 
values ('11688f5e-5af6-11ed-8d3f-d30dc6ba5371', 'admin', '$2b$10$BUli0c.muyCW1ErNJc3jL.vFRFtFJWrT8/GcR4A.sUdCznaXiqFXa', 'admin');
```

This will create a user with the default credentails

- username: `admin`
- password: `umami`

Use the admin user to reset the password of your user(s) and remember to delete the admin user once successfull.
