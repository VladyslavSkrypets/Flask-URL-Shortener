# Getting Started with Flask-URL-Shortener API

API provides functionality for creating short links from extraction. All requests body must be valid JSON.


## Create short URL

**You send:**
1. Your link in the `link` field. ( Required! )
2. Link lifetime in days in the `expire_days`. Field can takes only integer format. ( Optional - default 90 days ).

**Request:**
```json
POST /api/v1/add HTTP/1.1
Content-Type: application/json
{
    "link": "https://ua.jooble.org/%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-junior-python/%D0%9A%D0%B8%D0%B5%D0%B2",
    "expire_days": 180
}
```

**Response:**
```json
HTTP/1.1 201 OK
Server: My RESTful API
Content-Type: application/json

{
    "short_url": "http://127.0.0.1:5000/7z6Qu8Ke"
}
```

## Find full link by UID

**You send:**
1. UID of start url (8 characters after `/`)

**Request:**
```json
POST /api/v1/fetch_one HTTP/1.1
Content-Type: application/json
{
    "uid": "yW1PFml9"
}
```

**Successful Response:**
```json
HTTP/1.1 200 OK
Server: My RESTful API
Content-Type: application/json

{
    "created_date": "2021-10-02T15:17:59",
    "expire_at": "2022-07-28T15:18:05",
    "id": 5,
    "short_url": "http://127.0.0.1:5000/yW1PFml9",
    "uid": "yW1PFml9",
    "url": "https://www.youtube.com"
}
```

**Failed Response:**
```json
HTTP/1.1 200 OK
Server: My RESTful API
Content-Type: application/json

{
    "error": "There are no results"
}
``` 

## Select all info about url

**Request:**
```json
POST|GET /api/v1/fetch_all HTTP/1.1
Content-Type: application/json
```

**Response:**
```json
HTTP/1.1 201 OK
Server: My RESTful API
Content-Type: application/json

[
    {
        "created_date": "2021-10-02T14:35:24",
        "expire_at": "2021-12-31T14:36:13",
        "id": 1,
        "short_url": "http://127.0.0.1:5000/dfk0u8Ao",
        "uid": "dfk0u8Ao",
        "url": "https://example.com"
    },
    {
        "created_date": "2021-10-02T15:04:58",
        "expire_at": "2021-10-12T15:06:19",
        "id": 2,
        "short_url": "http://127.0.0.1:5000/qFJCcBlH",
        "uid": "qFJCcBlH",
        "url": "https://www.google.com/"
    }
]
```
