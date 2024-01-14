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
                        'projects':username+'_projects'})

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

# add a skill into set of skills
def add_skill(username, skill):
    r.sadd(username+'_skills', skill)

# get all skills in set of skills
def get_skills(username):
    return r.smembers(username+'_skills')

# add a skill that is associated with a job; the job is identified with job_key
def add_job_skill(job_key, skill):
    r.sadd(job_key+'_skills', skill)

# get all skills associated with the job with the entered job_key
def get_job_skills(job_key):
    return r.smembers(job_key+'_skills')

# add a line of description for a job; the job is identified with job_key
def add_job_description(job_key, description):
    r.sadd(job_key+'_description', description)

# get all lines of description written for the job with the entered job_key
def get_job_description(job_key):
    return r.smembers(job_key+'_description')

# add a line of description for an education; the education is identified with education_key
def add_education_description(education_key, description):
    r.sadd(education_key+'_description', description)

# get all lines of description written for the education with the entered education_key
def get_education_description(education_key):
    return r.smembers(education_key+'_description')

# add a new project, project_key must be unique between all users
def add_project(username, project_key):
    r.sadd(username+'_projects', project_key)
    r.hset(project_key, mapping={'name':"",
                             'start date':"",
                             'end date':"",
                             'skills':project_key+'_skills',
                             'description':project_key+'_description'})
    
# set name, start date, or end date;
# example: set_project_info("jack133003_project1", "name", "DC Power Supply")
def set_project_info(project_key, field, value):
    r.hset(project_key, field, value)

# get name, start date, or end date;
def get_project_info(project_key, field):
    return r.hget(project_key, field)



# add a skill that is associated with a project; the project is identified with project_key
def add_project_skill(project_key, skill):
    r.sadd(project_key+'_skills', skill)

# get all skills associated with the project with the entered project_key
def get_project_skills(project_key):
    return r.smembers(project_key+'_skills')

# add a line of description for a project; the project is identified with project_key
def add_project_description(project_key, description):
    r.sadd(project_key+'_description', description)

# get all lines of description written for the project with the entered project_key
def get_project_description(project_key):
    return r.smembers(project_key+'_description')

#example
# create_user("jack133003")

# set_info("jack133003", "name", "Lebron James")
# set_info("jack133003", "phone", "6471234455")
# set_info("jack133003", "email", "lebron.james@gmail.com")
# set_info("jack133003", "linkedin", "linkedin.com/in/lebron-james")

# print(get_info("jack133003","name"))

# add_summary("jack133003","I am in 3rd year")
# add_summary("jack133003", "I am in Electrical Engineering")

# add_job("jack133003", "jack133003_job1")

# set_job_info("jack133003_job1", "company", "Intel")
# set_job_info("jack133003_job1", "position", "Electrical Engineer Co-op")
# set_job_info("jack133003_job1", "start date", "May 2022")
# set_job_info("jack133003_job1", "end date", "September 2023")
# set_job_info("jack133003_job1", "location", "Toronto, ON")

# print(get_job_info("jack133003_job1", "position"))

# add_education("jack133003", "jack133003_education1")

# set_education_info("jack133003_education1", "major", "Electrical Engineering")
# set_education_info("jack133003_education1", "degree", "Bachelor of Engineering (Co-op)")
# set_education_info("jack133003_education1", "school", "McMaster University")
# set_education_info("jack133003_education1", "level", "3")
# set_education_info("jack133003_education1", "location", "Hamilton, ON")
# set_education_info("jack133003_education1", "GPA", "3.0")
# set_education_info("jack133003_education1", "start date", "September 2021")
# set_education_info("jack133003_education1", "end date", "June 2026")

# print(get_education_info("jack133003_education1", "degree"))

# add_skill("jack133003", "C++")
# add_skill("jack133003", "Python")
# add_skill("jack133003", "PSpice")
# add_skill("jack133003", "Altium Designer")

# print(get_skills("jack133003"))

# add_job_skill("jack133003_job1", "Python")
# add_job_skill("jack133003_job1", "C")
# add_job_skill("jack133003_job1", "Verilog")

# print(get_job_skills("jack133003_job1"))

# add_job_description("jack133003_job1", "Increased revenue by 15 percent using a C++ application")

# print(get_job_description("jack133003_job1"))

# add_education_description("jack133003_education1", "I have joined boxing and robotics club.")

# print(get_education_description("jack133003_education1"))

# add_project("jack133003", "jack133003_project1")

# set_project_info("jack133003_project1", "name", "DC Power Supply")
# set_project_info("jack133003_project1", "start date", "September 2023")
# set_project_info("jack133003_project1", "end date", "January 2024")

# print(get_project_info("jack133003_project1", "name"))

# add_project_skill("jack133003_project1", "Circuit Design")

# add_project_description("jack133003_project1", "Built a DC power supply using a centre tapped rectifier and transformer")

# print(get_project_skills("jack133003_project1"))
# print(get_education_description("jack133003_project1"))
