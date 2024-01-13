import redis

r = redis.Redis(
  host='redis-13747.c267.us-east-1-4.ec2.cloud.redislabs.com',
  port=13747,
  password='jUutjnOIRlwqKFGW7ho3U812QUu5UcCS',
  decode_responses=True)

#create a new user
def create_user(username):
    r.hset(username,mapping={'name':"",
                        "phone":"",
                        "email":"",
                        "linkedin":"",
                        "summary":"",
                        "skills":"",
                        "education":"",
                        "experience":"",
                        "projects":"",
                        "extracurricular":""})

#example
create_user("jack133003")