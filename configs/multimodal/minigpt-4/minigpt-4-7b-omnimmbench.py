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

dataset = dict(type='opencompass.OmniMMBenchDataset',
               data_file='data/mm_benchmark/mmagi_v030_full_inferin.tsv',
               pipeline=val_pipeline)

dataloader = dict(batch_size=1,
                  num_workers=4,
                  dataset=dataset,
                  collate_fn=dict(type='pseudo_collate'),
                  sampler=dict(type='DefaultSampler', shuffle=False))

# model settings
model = dict(
    type='minigpt-4-omnimmbench',
    freeze_vit=True,
    freeze_qformer=True,
    max_txt_len=160,
    end_sym='###',
    low_resource=False,
    llama_model='/mnt/petrelfs/share_data/ouyanglinke/vicuna-7b/',
    sys_prompt=  # noqa: E251
    '###Human: What is the capital of China? There are several options:\nA. Beijing\nB. Shanghai\nC. Guangzhou\nD. Shenzhen\n###Assistant: A\n'
)

# evaluation settings
evaluator = [
    dict(type='opencompass.DumpResults',
         save_path='work_dirs/minigpt-4-7b-omnimmbench.xlsx')
]

load_from = '/mnt/petrelfs/share_data/liuyuan/llm_weights/minigpt4-7b/prerained_minigpt4_7b.pth'  # noqa