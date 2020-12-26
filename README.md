# test_task_S7
### Pavel Nikulin
test task for S7 job


## Build
```shell script
docker build -t s7_app .
```

## Run
```shell script
docker run -p 8000:8000 s7_app
```

## Test

```shell script
docker run --entrypoint pytest s7_app
```


## Docs
```shell script
http://0.0.0.0:8000/docs
```
