# Import the document object to interact with HTML
from pyscript import document

def compute_average(e):
    s1 = document.getElementById("score1").value
    s2 = document.getElementById("score2").value

    # Check if inputs are empty to prevent errors
    if not s1 or not s2:
        return

    avg = (float(s1) + float(s2)) / 2
    output = document.getElementById("output")

    if avg == 100:
        output.innerText = f"Average: {avg:.2f} You got a Perfect Score!!! 🏆"
        output.className = "perfect"
    elif avg >= 75:
        output.innerText = f"Average: {avg:.2f} You Passed! ✅"
        output.className = "passed"
    else:
        output.innerText = f"Average: {avg:.2f} You Failed... ❌"
        output.className = "failed"