import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print("result:")
print(completion.choices[0].message)