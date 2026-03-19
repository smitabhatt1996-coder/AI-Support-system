from flask import Flask, render_template, request

app = Flask(__name__)

def get_solution(query):
    query = query.lower()

    if "transcript" in query:
        return "Category: Transcript Issue\n\nSolution:\n1. Ensure full conversation is recorded\n2. Check microphone/audio clarity\n3. Retry transcript"

    elif "cpt code" in query or "icd-10 code" in query:
        return "Category: Coding Issue\n\nSolution:\n1. Add diagnosis\n2. Add procedure details\n3. Reprocess transcript"

    elif "screen" in query:
        return "Category: Technical Issue\n\nSolution:\n1. Select entire screen\n2. Enable system audio\n3. Keep permissions active"

    elif "treatment" in query:
        return "Category: Workflow Issue\n\nSolution:\n1. Enter patient details\n2. Update treatment plan\n3. Save changes"

    elif "save" in query:
        return "Category: Data Issue\n\nSolution:\n1. Fill required fields\n2. Check internet connection"

    elif "slow" in query:
        return "Category: Performance Issue\n\nSolution:\n1. Refresh system\n2. Check network"

    elif "summary" in query:
        return "Category: System Issue\n\nSolution:\nUse short structured notes"

    elif "mic" in query or "audio" in query:
        return "Category: Audio Issue\n\nSolution:\nCheck microphone permissions"

    else:
        return "Category: General Issue\n\nSolution:\nFollow help guide or contact support"


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        query = request.form["query"]
        result = get_solution(query)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    import os
    port=int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
