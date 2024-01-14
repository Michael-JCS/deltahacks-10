from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from typing import List
from docx2pdf import convert
import cohere as c

def rerank():
    co = c.Client("")
    relevant_descriptions = []
    ranked_jobs = {}
    strings = f'''Which string is the closest to this job title: {x}'''
    job_title_query = {} #takes has the desc and find the ones that are best for the job title
    #{key = job : value = [array of descriptions]}
    for jobs, description in job_title_query:
        response = co.rerank(query=strings, documents=description, top_n=3, model='rerank-english-v2.0')

        for r in enumerate(response):
            # relevant_jobs.append(r.relevance_score)
            relevant_descriptions.append(r.documents['text'])
        ranked_jobs[jobs] = relevant_descriptions
        relevant_descriptions = []
    return ranked_jobs #{Job : [3/4 Best Bullet Points Per Job]}


def create_resume(name: str, email: str, phone: str, job_info, ranked_jobs, education, word_filename='resume.docx', pdf_filename='resume.pdf'):
    # Create a new Word document
    doc = Document()
    # Add contact information
    heading = doc.add_heading(name, level=1)
    heading.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    run = heading.runs[0]
    font = run.font
    font.size = Pt(14)  # You can adjust the size as needed
    font.name = 'Times New Roman'

    # Add contact information
    doc.add_paragraph(f"Email: {email} | Phone: {phone}")

    # Add a line under the contact information
    count = 0
    # Add skills section
    doc.add_heading('Skills', level=2)
    string = ''
    for job in ranked_jobs:
    # Check if the job title exists in job_info before accessing it
        print(job_info[0]['title'])
        if job_info[count]['title'] in job:
            skills = job_info[count]['skills']
            for skill in skills:
                string += f", {skill}"
            doc.add_paragraph(string[2:])    
        count += 1

    # Add experience section
    doc.add_heading('Experience', level=2)
    for job in job_info:
        doc.add_heading(f"{job['title']}, {job['company']} ({job['start_date']} - {job['end_date']})", level=3)
        doc.add_paragraph(ranked_jobs[job['title']])
                       

    # Add education section
    doc.add_heading('Education', level=2)
    for school in education:
        doc.add_paragraph(f"{school['degree']} in {school['major']}, {school['school']} ({school['graduation_date']})")
        

    # Save the Word document
    doc.save(word_filename)
    print(f"Resume generated successfully: {word_filename}")

    # Convert Word to PDF
    convert(word_filename, pdf_filename)
    print(f"PDF generated successfully: {pdf_filename}")



# # if __name__ == "__main__":
# #     # Example data
# #     name = "John Doe"
# #     email = "john.doe@example.com"
# #     phone = "123-456-7890"
# #     skills = ["Python", "Data Analysis", "Problem Solving"]
# #     experience = [
# #         {
# #             "title": "Software Engineer",
# #             "company": "Tech Company",
# #             "start_date": "Jan 2020",
# #             "end_date": "Present",
# #             "description": "Worked on developing and maintaining software applications.",
# #         },
# #     ]
# #     education = [
# #         {
# #             "degree": "Bachelor of Science",
# #             "major": "Computer Science",
# #             "school": "University XYZ",
# #             "graduation_date": "May 2019",
# #         },
# #     ]

# #     create_resume(name, email, phone, skills, experience, education)
