from flask import Flask, render_template, request, redirect, url_for
import gemini

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_jd', methods=['POST'])
def generate_jd():
    company_name = request.form['company_name']
    job_title = request.form['job_title']
    mandatory_skills = request.form.getlist('mandatory_skills')
    overall_experience = request.form['overall_experience']
    primary_skill = request.form['primary_skill']
    min_experience_primary = request.form['min_experience_primary']

    jd = gemini.generate_job_description(
        company_name, job_title, mandatory_skills,
        overall_experience, primary_skill, min_experience_primary,
        app.config['GEMINI_API_KEY']
    )
    return render_template('job_description.html', jd=jd)


@app.route('/finalize_jd', methods=['POST'])
def finalize_jd():
    edited_jd = request.form['edited_jd']
    print("Finalized Job Description:")
    print(edited_jd)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
