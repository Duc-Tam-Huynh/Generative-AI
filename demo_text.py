import google.generativeai as palm

API_KEY = "AIzaSyA3FrYTkTE7QpPjSwRsTkUdzstgEMHkP1A"

palm.configure(api_key=API_KEY)

model_list = [_ for _ in palm.list_models()]
for model in model_list:
    print(model.name)

#Example 1. Text Generation
model_id = 'models/text-bison-001'
prompt = '''
write a maketing proposal to sell a ice cream product. limit the proposal to 50 words
'''
completion = palm.generate_text(
    model = model_id,
    prompt = prompt,
    temperature=0.99, # Controls the randomness of the output. Must be positive, A temperature of zero will be deterministic
    # The maximum length of response
    max_output_tokens = 800,
    candidate_count = 2
)

#completion.result
#print(completion.candidates[0]['output'])

outputs = [output['output'] for output in completion.candidates]

for ouput in outputs:
    print(ouput)
    print('*'*50)