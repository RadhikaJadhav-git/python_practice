def read_file(request, file_id):
    from .models import Document

    doc = Document.objects.get(id=file_id)

    with open(doc.file.path, 'r') as f:
        content = f.read()

    return HttpResponse(content)