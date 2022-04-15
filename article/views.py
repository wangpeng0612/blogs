from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def article_column(request):
    if request.method == 'GET':
        # columns = ArticleColumn.objects.filter(user_id=request.user.id)
        columns = ArticleColumn.objects.all()
        column_form = ArticleColumnForm()
        return render(request, 'article/column/article_column.html', {'columns': columns, 'column_form': column_form})

    if request.method == 'POST':
        column_name = request.POST.get('column', '')
        columns = ArticleColumn.objects.filter(column=column_name)
        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse('1')