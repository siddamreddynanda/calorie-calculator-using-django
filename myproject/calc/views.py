from django.shortcuts import render

def calculator(request):
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operation = request.POST.get('operation')
            
            if operation == 'Add':
                result = num1 + num2
            elif operation == 'Subtract':
                result = num1 - num2
            elif operation == 'Multiply':
                result = num1 * num2
            elif operation == 'Divide':
                result = num1 / num2 if num2 != 0 else "Error (Zero Division)"
        except ValueError:
            result = "Invalid Input"
            
    return render(request, 'calculator.html', {'result': result})