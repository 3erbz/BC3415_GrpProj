from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

profile_page = Blueprint ('profile_page', __name__, template_folder='/templates')

@profile_page.route ('/profile', methods = ['GET'])
@login_required
def profile ():
    return render_template ("profile.html", user=current_user)

@profile_page.route ('/process', methods = ['POST'])
@login_required
def process ():
    # import packages
    from diffusers import StableDiffusionPipeline
    import torch
    import json
    from PIL import Image

    firstName = request.get_json ()
    if torch.cuda.is_available():
        print("Using GPU")
        pipe = StableDiffusionPipeline.from_pretrained(
            "nota-ai/bk-sdm-small", 
            torch_dtype=torch.float16, 
            use_safetensors=True,
        ).to("cuda")
        pipe.safety_checker = None  
    else:
        print("Using CPU")
        pipe = StableDiffusionPipeline.from_pretrained(
            "nota-ai/bk-sdm-small", 
            torch_dtype=torch.float32,
            use_safetensors=True,
    )
        pipe.safety_checker = None

    prompt = f"generate a picture suited for {firstName}."
    h = 200
    w = 200

    generated_img = pipe (prompt, height=h, width=w).images [0]
    image = Image.open (generated_img)
    print (image)

    return "success"