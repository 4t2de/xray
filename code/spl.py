import os
import random
import shutil
from tqdm import tqdm

source_root = r"D:\projects\xray\data"
test_root = r"D:\projects\xray\test"
test_split = 0.05

for dataset_name in os.listdir(source_root):
    dataset_path = os.path.join(source_root, dataset_name)
    if not os.path.isdir(dataset_path):
        continue

    all_images = []
    for root, _, files in os.walk(dataset_path):
        for f in files:
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                all_images.append(os.path.join(root, f))

    random.shuffle(all_images)
    num_test = int(len(all_images) * test_split)
    test_images = all_images[:num_test]

    for img_path in tqdm(test_images, desc=f"Splitting {dataset_name}"):
        rel_path = os.path.relpath(img_path, dataset_path)
        dest_path = os.path.join(test_root, dataset_name, rel_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.move(img_path, dest_path)

    print(f"Moved {num_test} images ({test_split*100:.1f}%) from {dataset_name}")
