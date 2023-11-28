import json
import os
import shutil
dat = json.load(open('/openseg_blob/PD/lcx/make_cate/new_resource/picked_url.json'))
prefix = '/openseg_blob/'
index = 0
# "PD/Crello_v2/benchmark_init_text2typo/Advertising/6543b57e1406cdffcd4096c2_pred.png
for item in dat:
    if 'supp' in item:
        continue
    d_name = item.split('/')[-2]
    shutil.copy(prefix+item,f"/openseg_blob/PD/lcx/make_cate/new_resource/init_pngs/{d_name}_{index}.png")
    
    template_name = item.split('/')[-1].split('_')[0]
    shutil.copy(f'/openseg_blob/PD/Crello_v2/benchmark_init_text2typo/{d_name}/{template_name}.json',f"/openseg_blob/PD/lcx/make_cate/new_resource/jsons/{d_name}_{index}.json")
    
    obj_url = f"/openseg_blob/PD/Crello_v2/benchmark_init_if/{d_name}/{template_name}_obj.png"
    bg_url = f"/openseg_blob/PD/Crello_v2/benchmark_init_if/{d_name}/{template_name}_bg.png"
    shutil.copy(obj_url,f'/openseg_blob/PD/lcx/make_cate/new_resource/pngs/{d_name}_{index}_obj.png')
    shutil.copy(bg_url,f'/openseg_blob/PD/lcx/make_cate/new_resource/pngs/{d_name}_{index}_bg.png')
    index+=1
    