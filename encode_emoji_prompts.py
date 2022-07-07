import codecs
from encode_emoji import replace_emoji_characters


# Read excel file

import pandas as pd
import glob

PATH = "./"
DATA_FILE = "common_law_model_responses_mastersheet.xlsx"
# DATA_FILE = "prompts_modified.csv"
NO_ROWS = 50 # Number of rows

prompts_df = pd.read_excel(PATH + DATA_FILE, engine="openpyxl")[:1000]

idx = 0
modified_prompts = []
modified_responses = []
for prompt_no, row in prompts_df.iterrows():
    print(f'de-emojfiying row {prompt_no}')
    print(f'prompt {row["prompt"]}')
    print(f'response {row["response"]}')
    print(row.isna().sum())

    if not row['prompt'] or not row['response'] or row.isna().sum() > 4:
        print(f"skipping row {prompt_no}")
        continue
    modified_prompts.append(replace_emoji_characters(row['prompt']))
    modified_responses.append(replace_emoji_characters(row['response']))    


prompt_response_df = pd.DataFrame({"prompt": modified_prompts, "response": modified_responses})
prompt_response_df.to_excel(PATH + "prompts_de_emojified.xlsx", index=False)

