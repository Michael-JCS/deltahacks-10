from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import cohere as c

def rerank():
    co = c.Client("")
    relevant_jobs = []
    strings = '''Which string is the closest to this job title: Insert string of Job description here'''
    job_title_query = [] #takes has the desc and find the ones that are best for the job title


    response = co.rerank(query=strings, documents=job_title_query, top_n=3, model='rerank-english-v2.0')

    for idx, r in enumerate(response):
        relevant_jobs.append(r.relevance_score)
    
    return relevant_jobs


def create_resume(name, email, phone, skills, experience, education, filename='resume.docx'):
    # Create a new Word document
    doc = Document()

    # Add a heading with the name
    heading = doc.add_heading(name, level=1)
    heading.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    # Add contact information
    doc.add_paragraph(f"Email: {email}")
    doc.add_paragraph(f"Phone: {phone}")
    doc.add_paragraph()  # Add an empty line

    # Add skills section
    doc.add_heading('Skills', level=2)
    for skill in skills:
        doc.add_paragraph(skill)

    # Add experience section
    doc.add_heading('Experience', level=2)
    for job in experience:
        doc.add_paragraph(f"{job['title']}, {job['company']} ({job['start_date']} - {job['end_date']})")
        doc.add_paragraph(job['description'])
        doc.add_paragraph()  # Add an empty line

    # Add education section
    doc.add_heading('Education', level=2)
    for school in education:
        doc.add_paragraph(f"{school['degree']} in {school['major']}, {school['school']} ({school['graduation_date']})")
        doc.add_paragraph()  # Add an empty line

    # Save the document
    doc.save(filename)
    print(f"Resume generated successfully: {filename}")



# if __name__ == "__main__":
#     # Example data
#     name = "John Doe"
#     email = "john.doe@example.com"
#     phone = "123-456-7890"
#     skills = ["Python", "Data Analysis", "Problem Solving"]
#     experience = [
#         {
#             "title": "Software Engineer",
#             "company": "Tech Company",
#             "start_date": "Jan 2020",
#             "end_date": "Present",
#             "description": "Worked on developing and maintaining software applications.",
#         },
#     ]
#     education = [
#         {
#             "degree": "Bachelor of Science",
#             "major": "Computer Science",
#             "school": "University XYZ",
#             "graduation_date": "May 2019",
#         },
#     ]

#     create_resume(name, email, phone, skills, experience, education)
