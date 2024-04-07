import requests
# import pyttsx3
import random
from gradio_client import Client
import os
import shutil

def txt_to_img(prompt):
    client = Client("ByteDance/SDXL-Lightning")
    result = client.predict(
        prompt,  # str in 'Enter your prompt (English)' Textbox component
        "8-Step",  # Literal['1-Step', '2-Step', '4-Step', '8-Step'] in 'Select inference steps' Dropdown component
        api_name="/generate_image"
    )
    return result

def move_image_to_current_directory(source_path):
    # Extract the filename from the source path
    filename = os.path.basename(source_path)
    
    # Define the destination path as the current working directory with the filename
    destination_path = os.path.join(os.getcwd(), filename)
    
    # Move the file
    shutil.move(source_path, destination_path)
    print(f"Image moved to {destination_path}")
    return destination_path

# Constants
API_URL = "https://api-inference.huggingface.co/models/aspis/gpt2-genre-story-generation"
HEADERS = {"Authorization": "Bearer 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"}

def generate_story_via_api(prompt, length=250, num_sequences=1, api_url=API_URL, headers=HEADERS):
    payload = {
        "inputs": prompt,
        "parameters": {
            "num_return_sequences": num_sequences,
            "max_new_tokens": length
        }
    }
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        generated_stories = response.json()
        return [story["generated_text"][len(prompt):].strip() for story in generated_stories]
    else:
        return [f"Error: {response.status_code} - {response.text}"]


API_URL_OPT = "https://api-inference.huggingface.co/models/gpt2-xl"
def generate_option_via_api(prompt, length=20, num_sequences=2, api_url=API_URL_OPT, headers=HEADERS):
    payload = {
        "inputs": prompt,
        "parameters": {
            "num_return_sequences": num_sequences,
            "max_new_tokens": 25
        }
    }
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        generated_stories = response.json()
        return [story["generated_text"][len(prompt):].strip() for story in generated_stories]
    else:
        return [f"Error: {response.status_code} - {response.text}"]

# Initialize text-to-speech engine
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 125)


# Main story generation loop
story_starters = {
    "1. Ancient Ruins":"Beneath the ancient ruins of a forgotten civilization, a pair of explorers uncover a map leading to the fabled City of Echoes.",
    "2. Legend Island":"As the storm raged on, Captain Marlowe navigated her ship towards the eye, where legend told of an island appearing only once every hundred years.",
    "3. Guardian Spirits":"In the dense jungles of the Amazon, a wildlife photographer stumbles upon a hidden path that locals say is guarded by spirits of the forest.",
    "4. Alien Cavern":"High in the snow-capped mountains, a lone hiker discovers a cave with walls lined with strange, glowing symbols that hint at an alien presence long ago.",
    "5. Time-Travelling Artifact":"Deep in the Sahara, an archaeologist finds an artifact that is the key to unlocking the secrets of a time-traveling civilization.",
    "6. Mythical Alter-Dimension":"On the night of the blue moon, a young sorcerer opens a portal to a parallel world filled with mythical creatures and untold dangers.",
    "7. The Detective Comeback":"A retired detective receives an anonymous letter hinting at the location of a lost treasure that has eluded fortune hunters for centuries.",
    "8. Sacred Sanctuary":"In a post-apocalyptic world, a band of survivors embarks on a quest to find a sanctuary said to be untouched by the devastation.",
    "9. The Underwater City":"During a dive in the Bermuda Triangle, a marine biologist encounters an underwater city that is still inhabited by descendants of its original dwellers.",
    "10. Trip to the Stone Age":"A group of friends camping in the Rockies find themselves transported to an ancient era where they must navigate a land of dinosaurs and primitive tribes.",
    "11. The Whispering Depths":"Knight Elore, armored and resolute, faces the mysterious cave's entrance. Legends lure him onward, his destiny concealed within its depths."
}
story_nums = {
    1: "1. Ancient Ruins",
    2: "2. Legend Island",
    3: "3. Guardian Spirits",
    4: "4. Alien Cavern",
    5: "5. Time-Travelling Artifact",
    6: "6. Mythical Alter-Dimension",
    7: "7. The Detective Comeback",
    8: "8. Sacred Sanctuary",
    9: "9. The Underwater City",
    10: "10. Trip to the Stone Age",
    11: "11. The Whispering Depths"
}

selectbox_items = [
    "1. Ancient Ruins",
    "2. Legend Island",
    "3. Guardian Spirits",
    "4. Alien Cavern",
    "5. Time-Travelling Artifact",
    "6. Mythical Alter-Dimension",
    "7. The Detective Comeback",
    "8. Sacred Sanctuary",
    "9. The Underwater City",
    "10. Trip to the Stone Age",
    "11. The Whispering Depths"
]

# imagePaths = []
# for keys in story_starters:
#     print(keys)
# prompt_num = int(input("Choose one of the stories from above: "))
# initial_prompt = story_starters[story_nums[prompt_num]]
# print(initial_prompt)
final_chap = '''Out of nowhere-there came a wizard taking you to what you desire .You stood before the ancient temple. Your goal: the fabled Emerald Heart, said to hold unimaginable power-the real treasure.

The colossal stone statue, the Guardian of the Emerald, came alive. Its emerald eyes glowed, ready to strike down anyone who dared approach.

Take him down and inifinite powers awaits you. He is powerful and relentless in his pursuit but lacks stamina. For every second of his attack he must rest the same. Here's something you don't know about about yourself, the symphony between the thumb and palm, the first will attack and the latter will defend'''

# for _ in range(4):
#     # Generate the main part of the story
#     gen_story = generate_story_via_api(initial_prompt, length=250, num_sequences=1)
#     to_print_story = gen_story[0]
#     last_full_stop_index = to_print_story.rfind(".")
#     last_qmark_index = to_print_story.rfind("?")
#     last_emark_index = to_print_story.rfind("!")
#     last_quote_index = to_print_story.rfind('"')
#     last_story_index = max(last_full_stop_index, last_qmark_index, last_emark_index, last_quote_index)
#     if last_story_index != -1:
#         to_print_story = to_print_story[:last_story_index + 1]  # Remove the part before the last full stop
#     else:
#         to_print_story = to_print_story
#     print (to_print_story)
#     # print(gen_story[0])
#     imageGen = txt_to_img(to_print_story)
#     newWorkDir = move_image_to_current_directory(imageGen)
#     # print("new working dir=", newWorkDir)

    
#     # Create options for the next part of the story
#     options_prompt = gen_story[0] + " At this critical juncture, they face a dilemma:"
#     story_options = generate_option_via_api(options_prompt, length=20, num_sequences=2)
    
#     # Present options to the user
#     for i, story in enumerate(story_options):
#         option_text = story.split(".")[0]  # Take the first sentence as an option
#         to_print_opt = option_text
#         last_full_stop_index_opt = to_print_opt.rfind(".")
#         last_qmark_index_opt = to_print_opt.rfind("?")
#         last_emark_index_opt = to_print_opt.rfind("!")
#         last_quote_index_opt = to_print_opt.rfind('"')
#         last_opt_index = max(last_full_stop_index_opt,last_qmark_index_opt,last_emark_index_opt,last_quote_index_opt)
#         if last_opt_index != -1:
#             to_print_opt = to_print_opt[:last_opt_index + 1]  # Remove the part before the last full stop
#         else:
#             to_print_opt = to_print_opt
#         print(f"Option {i+1}: {to_print_opt}\n")
    
#     # User makes a choice
#     user_choice = input("What choice do you make? (1/2): ")
#     chosen_option = story_options[int(user_choice) - 1].split(".")[0]
#     initial_prompt += chosen_option

# print(final_chap)
# imageGen = txt_to_img(final_chap)
# newWorkDir = move_image_to_current_directory(imageGen)


# # # Generate the conclusion of the story
# # final_story = generate_story_via_api(initial_prompt, length=250, num_sequences=1)
# # print(final_story[0])