import google.generativeai as genai

from django.shortcuts import render
from django.conf import settings


genai.configure(api_key=settings.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')


def get_ai_page(request):
    if request.method == "POST":
        prompt = request.POST.get("message")
        if prompt:
            try:
                response = model.generate_content(prompt)
                message = response.text
            except Exception as e:
                message = f"Xatolik yuz berdi"
        else:
            message = "Savolni kiriting"
        return render(request, 'ai_assistent/ai_page.html', {'message': message})
    return render(
        request,
        "ai_assistent/ai_page.html",
    )
