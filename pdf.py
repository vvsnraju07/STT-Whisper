from PyPDF2 import PdfReader

reader = PdfReader("ex.pdf")
data=""
for i in reader.pages:
    data += i.extract_text()+"\n"
print(data)


with open("new.txt","w", encoding="utf-8") as f:
    f.write(data)
