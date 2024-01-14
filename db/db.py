import redis

r = redis.Redis(
  host='redis-13747.c267.us-east-1-4.ec2.cloud.redislabs.com',
  port=13747,
  password='jUutjnOIRlwqKFGW7ho3U812QUu5UcCS',
  decode_responses=True)

# create a new user, username must be unique
def create_user(username):
    r.hset(username, mapping={'name':"",
                        'phone':"",
                        'email':"",
                        'linkedin':"",
                        'summary':username+'_summary',
                        'skills':username+'_skills',
                        'education':username+'_educations',
                        'experience':username+'_jobs',
                        'projects':username+'_projects',
                        'extracurricular':username+'_extracurricular'})

# add name, phone, email, or linkedin;
# example: set_info("jack133003", "name", "Lebron James")
def set_info(username, field, value):
    r.hset(username, field, value)

# get name, phone, email, or linkedin;
def get_info(username, field):
    return r.hget(username, field)

# add a line to the summary set (set of sentences)
def add_summary(username, line):
    r.sadd(username+'_summary', line)

# add a new job, job_key must be unique between all users
def add_job(username, job_key):
    r.sadd(username+'_jobs', job_key)
    r.hset(job_key, mapping={'position':"",
                             'company':"",
                             'location':"",
                             'start date':"",
                             'end date':"",
                             'skills':job_key+'_skills',
                             'description':job_key+'_description'})

# set position, company, location, start date, or end date;
# example: set_job_info("jack133003_job1", "company", "Intel")
def set_job_info(job_key, field, value):
    r.hset(job_key, field, value)

# get position, company, location, start date, or end date;
def get_job_info(job_key, field):
    return r.hget(job_key, field)

# add a new education, education_key must be unique between all users
def add_education(username, education_key):
    r.sadd(username+'_educations', education_key)
    r.hset(education_key, mapping={'major':"",
                             'degree':"",
                             'school':"",
                             'level':"",
                             'location':"",
                             'GPA':"",
                             'start date':"",
                             'end date':"",
                             'description':education_key+'_description'})

# set major, degree, school, level, location, GPA, start date, or end date;
# example: set_education_info("jack133003_education1", "school", "McMaster University")
def set_education_info(education_key, field, value):
    r.hset(education_key, field, value)

# get major, degree, school, level, location, GPA, start date, or end date;
def get_education_info(education_key, field):
    return r.hget(education_key, field)

#example
create_user("jack133003")

set_info("jack133003", "name", "Lebron James")
set_info("jack133003", "phone", "6471234455")
set_info("jack133003", "email", "lebron.james@gmail.com")
set_info("jack133003", "linkedin", "linkedin.com/in/lebron-james")

print(get_info("jack133003","name"))

add_summary("jack133003","I am in 3rd year")
add_summary("jack133003", "I am in Electrical Engineering")

add_job("jack133003", "jack133003_job1")

set_job_info("jack133003_job1", "company", "Intel")
set_job_info("jack133003_job1", "position", "Electrical Engineer Co-op")
set_job_info("jack133003_job1", "start date", "May 2022")
set_job_info("jack133003_job1", "end date", "September 2023")
set_job_info("jack133003_job1", "location", "Toronto, ON")

print(get_job_info("jack133003_job1", "position"))

add_education("jack133003", "jack133003_education1")

set_education_info("jack133003_education1", "major", "Electrical Engineering")
set_education_info("jack133003_education1", "degree", "Bachelor of Engineering (Co-op)")
set_education_info("jack133003_education1", "school", "McMaster University")
set_education_info("jack133003_education1", "level", "3")
set_education_info("jack133003_education1", "location", "Hamilton, ON")
set_education_info("jack133003_education1", "GPA", "3.0")
set_education_info("jack133003_education1", "start date", "September 2021")
set_education_info("jack133003_education1", "end date", "June 2026")

print(get_education_info("jack133003_education1", "degree"))