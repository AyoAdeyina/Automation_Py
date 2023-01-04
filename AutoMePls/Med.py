import pyttsx3,PyPDF2

pdfreader = PyPDF2.PdfFileReader(open("ACL_Pro.pdf", "rb"))
speaker = pyttsx3.init()

for pg_num in range(pdfreader.numPages):
    text = pdfreader.getPage(pg_num).extract_text()
    clean_txt = text.strip().replace('\n', ' ')
    print(clean_txt)

speaker.save_to_file(clean_txt, 'medic.mp3')
speaker.runAndWait()

speaker.stop()