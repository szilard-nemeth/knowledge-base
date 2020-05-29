1. print environment variables of container

```docker exec <container> bash -c 'echo "$ENV_VAR"'```

2. Peek into container
```docker run --name container-name -it image-name /bin/bash```