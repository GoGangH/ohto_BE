# Server Config using docker compose

## 1. build image and download package for django

```
docker-compose up -d
```
### this stage will probably cause error So,

## 2. Stop container using docker-compose stop

```
docker-compose stop
```

## 3. second build for proper linking between container

```
docker-compose up -d
```

### after this command, all containers would be connected to each other


## 4. data push

### attach to django container to push song data

```
docker exec -i django-main sh
```

### then push data
```
python3 manage.py dataframe_inject && python3 manage.py json_data_inject
```