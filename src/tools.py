import cohere as c


co = c.Client("")
strings = '''Insert string of Job description here'''
prompt = f"Can you identify skills from this job description: {strings}"


response = co.generate(  
    model='command-nightly', 
    prompt = prompt,  
    max_tokens=50, # This parameter is optional. 
    temperature=0.750)

intro_paragraph = response.generations[0].text




