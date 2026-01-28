from huggingface_hub import HfApi
#import os
from google.colab import userdata

api = HfApi(token=userdata.get("HF_TOKEN"))
api.upload_folder(
    folder_path="self_paced_courses_1_mlops/deployment",
    repo_id="sarojk8325/PIMA-Diabetes-Prediction"                                         # enter the Hugging Face username here
    repo_type="space",
    path_in_repo="",                          # optional: subfolder path inside the repo
)
