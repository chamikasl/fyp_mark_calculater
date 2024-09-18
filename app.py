from flask import Flask, request, render_template

app = Flask(__name__)

def calculate_required_project_marks(sum_of_highest_two):
    required_marks = {}
    
    classifications = {
        "1st Class": 70,
        "1st Class Borderline": 68,
        "2nd Upper": 60,
        "2nd Upper Borderline": 58,
        "2nd Lower": 50,
        "2nd Lower Borderline": 48,
        "3rd Class": 40
    }

    for class_name, target in classifications.items():
        required_project_mark = (target * 3) - sum_of_highest_two
        required_marks[class_name] = required_project_mark

    return required_marks

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            marks = [
                float(request.form['rmit']),
                float(request.form['cis']),
                float(request.form['sppm'])
            ]
            if any(mark < 0 or mark > 100 for mark in marks):
                raise ValueError

            selected_marks = sorted(marks, reverse=True)[:2]
            sum_of_highest_two = sum(selected_marks)

            required_marks = calculate_required_project_marks(sum_of_highest_two)

            result = {class_name: (mark if 0 <= mark <= 100 else 'Not possible') for class_name, mark in required_marks.items()}
        except ValueError:
            result = 'Invalid input.'

        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

