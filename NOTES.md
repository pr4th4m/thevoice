#### NOTES:

**Few considerations**
- Application running on development server and not production server, we can configure wsgi with nginx reverse proxy for production.
- We are using JWT and many settings related to sessions can be disabled, however, they aren't becasue django panel / django rest framework are enabled.
- Considering login will be only with admin (is_superuser=True) and mentor (is_superuser=False). We can use AbstractUser for more complex user roles.
- Logging in settings is simple, for more complex loggin we can send logs to sentry or something similar.
- Management commands and user fixtues are in team app (for convinience only).
