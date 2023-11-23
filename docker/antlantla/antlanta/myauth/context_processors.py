def show_me(request):
    context = {}
    context['company'] = "Antlanta Projects"    
    context['email'] = "info@antlantaprojects.co.za"    
    context['tel'] = "067 869 5716 | 072 540 1400"    
    return context