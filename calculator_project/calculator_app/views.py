from django.shortcuts import render
from django.http import JsonResponse
from .models import Expression

def calculate_exp(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        expression = expression.replace('^', '**')
        try:
            result = eval(expression)
            Expression.objects.create(expression_text=expression)
            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return render(request, 'calculator.html')

def get_history(request):
    expressions = Expression.objects.all().values_list('expression_text', flat=True)
    return JsonResponse({'history': list(expressions)})



