import textwrap
import google.generativeai as genai
from IPython.display import Markdown


def post_process_text(text):
    cleaned_text = text.replace("**", "")
    return cleaned_text


def generate_job_description(company_name, job_title, mandatory_skills, overall_experience, primary_skill,
                             min_experience_primary, key):
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-pro')
    jd = (f"Job Description for {job_title} at {company_name}\nSkills: {', '.join(mandatory_skills)}\nOverall "
          f"Experience: {overall_experience} years\nPrimary Skill: {primary_skill}\nMinimum Experience on Primary "
          f"Skill: {min_experience_primary} years")
    response = model.generate_content(jd)
    return post_process_text(response.text)
