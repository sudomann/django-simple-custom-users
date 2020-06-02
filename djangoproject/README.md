You can easily set up a postgres db to work with using docker

```bash
$ docker run --name some-postgres -e POSTGRES_USER=postgres -e POSTGRES_HOST_AUTH_METHOD=trust -e POSTGRES_DB=django_simple_custom_users --rm -d -p 5432:5432 postgres
```
