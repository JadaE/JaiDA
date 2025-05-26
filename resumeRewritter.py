import subprocess


def readResume():
   resumeFile = "062025Resume.tex"
   with open(resumeFile, "r") as f:
      resume_text = f.read()
   #print(resume_text[:1000])
   return resume_text

   # Compile LaTeX to PDF
   subprocess.run(["pdflatex", "resume.tex"])
   # need pdflatex installed locally to do this

#with open(resumeFile, "w") as f:
#      f.write(latex_code)
'''
Store your LaTeX resume in a structured .tex template.

Parse or rewrite individual sections (experience, summary, etc.) with LangChain output.

Save updated .tex, compile to .pdf with pdflatex, and serve/download.

We can scaffold this with modular {{ jinja-like }} tags or string replacement to make edits easy.
'''

### or ###

'''
Use pylatex:

Lets you write LaTeX code in a Pythonic way.

More flexible than fpdf if you're integrating LLM output into a .tex file.
'''