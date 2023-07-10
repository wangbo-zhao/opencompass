# dataloader settings
val_pipeline = [
    dict(type='mmpretrain.torchvision/Resize',
         size=(224, 224),
         interpolation=3),
    dict(type='mmpretrain.torchvision/ToTensor'),
    dict(type='mmpretrain.torchvision/Normalize',
         mean=(0.48145466, 0.4578275, 0.40821073),
         std=(0.26862954, 0.26130258, 0.27577711)),
    dict(type='mmpretrain.PackInputs',
         algorithm_keys=[
             'question', 'answer', 'category', 'l2-category', 'context',
             'index', 'options_dict', 'options', 'split'
         ])
]

dataset = dict(type='opencompass.OmniMMBench',
               data_file='data/mm_benchmark/mmagi_v030_full_inferin.tsv',
               pipeline=val_pipeline)

dataloader = dict(batch_size=1,
                  num_workers=4,
                  dataset=dataset,
                  collate_fn=dict(type='pseudo_collate'),
                  sampler=dict(type='DefaultSampler', shuffle=False))

# model settings
model = dict(
    type='blip2-vicuna-instruct-omnimmbench',
    freeze_vit=True,
    low_resource=False,
    llm_model='/mnt/petrelfs/share_data/ouyanglinke/vicuna-7b/',
    sys_prompt=  # noqa: E251
    '###Human: What is the capital of China? There are several options:\nA. Beijing\nB. Shanghai\nC. Guangzhou\nD. Shenzhen\n###Assistant: A\n'
)

# evaluation settings
evaluator = [
    dict(
        type='opencompass.DumpResults',
        save_path=  # noqa: E251
        'work_dirs/instructblip_vicuna7b/instructblipvicuna_mmagibench.xlsx')
]

load_from = '/mnt/petrelfs/share_data/liuyuan/llm_weights/instructblip_vicuna_7b/instruct_blip_vicuna7b_trimmed.pth'  # noqa