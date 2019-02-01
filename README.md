# yukon_test

How to user api:

List of BlogPosts:
$ curl -H 'Accept: application/json;' -u login:password -X GET http://127.0.0.1:8000/api/blogposts/
response: [{"name": "new", "created_by_id": 1, "id": 2, "created_date": "2019-01-31T18:21:56.022Z", "updated_date": "2019-01-31T18:21:56.022Z", "text": "sdfsdfs\r\nd\r\nfsadf\r\nsad\r\nfas"}, ... ]


Add BlogPost's object:
$ curl -H 'Accept: application/json;' -u login:password -X POST http://127.0.0.1:8000/api/blogposts/ -d '{"name": "goodname", "text": "goodtext"}'
response: {"created": {"name": "goodname", "text": "goodtext"}}


Get BlogPost object with id==21:
$ curl -H 'Accept: application/json;' -u login:password -X GET http://127.0.0.1:8000/api/blogposts/21/
response: [{"name": "new name", "created_by_id": 5, "id": 21, "created_date": "2019-02-01T08:43:10.273Z", "updated_date": "2019-02-01T08:49:02.850Z", "text": "go"}]


Update BlogPost object with id==21:
$ curl -H 'Accept: application/json;' -u login:password -X PUT http://127.0.0.1:8000/api/blogposts/21/ -d '{"name": "new name", "text": "go"}'
response: {"updated": {"name": "new name", "text": "go"}}


Delete BlogPost object with id==21
$ curl -H 'Accept: application/json;' -u login:password -X DELETE http://127.0.0.1:8000/api/blogposts/21/
response: {"pk_obj": 21, "deleted": true}
