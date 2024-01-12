from django.shortcuts import render
from django.shortcuts import redirect
from .models import Register

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        resume = request.FILES.get('resume')
        portfolio = request.POST.get('portfolio')
        linkedin = request.POST.get('linkedin')

        applicant = Register.objects.create(
            name = name,
            email = email,
            city = city,
             resume = resume,
             portfolio = portfolio,
            linkedin = linkedin,
        )
        applicant.save()
        return redirect('https://flutterwave.com/pay/dw99wyqendr5')
    return render(request, 'index.html')