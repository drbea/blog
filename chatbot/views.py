from django.shortcuts import render

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# # from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer


# # Create your views here.
# # Charger le modèle et le tokenizer
# model_name = "gpt2"  # Vous pouvez choisir un autre modèle approprié
# model = AutoModelForCausalLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)


# # Créer un pipeline de génération de texte
# text_generator = pipeline('text-generation', model=model, tokenizer=tokenizer)


# # @csrf_exempt
# # def chat(request):
# #     if request.method == 'POST':
# #         data = json.loads(request.body)
# #         user_message = data.get('message')

# #         # Générer une réponse à l'aide du modèle de langage
# #         generated_responses = text_generator(user_message, max_length=50, num_return_sequences=1)
# #         bot_response = generated_responses[0]['generated_text']

# #         return JsonResponse({'response': bot_response})
# #     return JsonResponse({'error': 'Only POST method allowed'})



# def chat(request):
#     if request.method == 'POST':
#         user_message = request.POST['message']
#         bot_response = text_generator(user_message)[0]['generated_text']
#         return JsonResponse({'bot_response': bot_response})
    
    