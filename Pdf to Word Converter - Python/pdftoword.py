#pip install aspose.words
import aspose.words as aw
doc = aw.Document("meupdf.pdf")
doc.save("doc.docx")