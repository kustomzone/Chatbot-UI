from transformers import GenerationConfig

def get_output(
    model, tokenizer, prompts, 
    temperature=0.90, top_p=0.75
):
    # GenerationConfig ref: https://huggingface.co/docs/transformers/main_classes/text_generation#transformers.GenerationConfig
    generation_config = GenerationConfig(
        temperature=temperature,
        top_p=top_p,
        num_beams=4,
        # use_cache=False,
        #min_length,
        #max_length
        #early_stopping=True, 

        #top_k,
        #num_beams,
        #do_sample
    )

    if len(prompts) == 1:
        print("there is only a prompt")
        encoding = tokenizer(prompts, return_tensors="pt")
        input_ids = encoding["input_ids"].cuda()
        generated_id = model.generate(
            input_ids=input_ids,
            generation_config=generation_config,
            max_new_tokens=256
        )

        print("generated_id")
        print(generated_id)
        print(tokenizer.batch_decode(generated_id))

        return tokenizer.batch_decode(generated_id)
    else:
        print("there are multiple prompts")
        encodings = tokenizer(prompts, padding=True, return_tensors="pt").to('cuda')
        generated_ids = model.generate(
            **encodings,
            generation_config=generation_config,
            max_new_tokens=256
        )

        print("generated_ids")
        print(generated_ids)
        print(tokenizer.batch_decode(generated_ids))

        return tokenizer.batch_decode(generated_ids)