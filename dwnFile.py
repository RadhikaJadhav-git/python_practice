from django.http import FileResponse
from .models import Document

def download_file(request, file_id):
    doc = Document.objects.get(id=file_id)
    return FileResponse(open(doc.file.path, 'rb'),
                        as_attachment=True,
                        filename=doc.file.name)