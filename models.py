from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch # type: ignore
import random

# Load pre-trained GPT-2 model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_text(prompt, max_length=100):
    """Generates text using the GPT-2 model."""
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids=input_ids, max_length=max_length, num_return_sequences=1)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

def generate_personalized_carol(user_name, user_interest):
    """Generates a personalized Christmas carol."""

    template = f"""
    On this {random.choice(['bright', 'jolly', 'festive'])} Christmas morn, 
    {user_name} with {random.choice(['joy', 'glee', 'delight'])} will {random.choice(['sing', 'dance', 'rejoice'])},
    For {user_interest} and the spirit so {random.choice(['grand', 'bright', 'warm'])},
    A Christmas carol, a joyful refrain. 
    """

    prompt = f"Write a Christmas carol verse about {user_interest} for {user_name}."
    generated_verse = generate_text(prompt)

    personalized_carol = template + "\n" + generated_verse 

    return personalized_carol