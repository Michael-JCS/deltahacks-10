import redis

r = redis.Redis(
  host='redis-13747.c267.us-east-1-4.ec2.cloud.redislabs.com',
  port=13747,
  password='jUutjnOIRlwqKFGW7ho3U812QUu5UcCS',
  decode_responses=True)

# create a new user
def create_user(username):
    r.hset(username,mapping={'name':"",
                        'phone':"",
                        'email':"",
                        'linkedin':"",
                        'summary':'',
                        'skills':'',
                        'education':'',
                        'experience':'',
                        'projects':'',
                        'extracurricular':''})

# set name, phone, email, or linkedin;
# example: set_info("jack133003", "name", "Lebron James")
def set_info(username, field, value):
    r.hset(username,field,value)


#example
create_user("jack133003")
set_info("jack133003", "name", "Lebron James")
set_info("jack133003", "phone", "6471234455")