---
name: social-image-resizer
description: Resize a user-provided image into a 1080x1440 vertical 3:4 image for 小红书, 抖音, or social posting when the user says "小红书图片", "抖音图片", "3:4图片", "1080x1440", or asks to make a vertical social image. Use Python + Pillow script support, preserve the original image, output to an output folder, and avoid stretching or distortion.
---

# Social Image Resizer

Use this skill when the user gives an image and asks for a 小红书 / 抖音 / 3:4 / 1080x1440 vertical version.

## Goal

- Target size: `1080 x 1440`
- Target ratio: `3:4`
- Output format: `.jpg`
- Output filename: `<original_filename>_1080x1440.jpg`
- Output folder: `output` next to the original image unless the user specifies another output folder.

## Rules

1. Do not modify the original image.
2. Keep the original image unchanged.
3. Put the resized image in an `output` folder.
4. Use output filename format: `原文件名_1080x1440.jpg`.
5. Do not stretch or distort the image.
6. If the original ratio does not match, prefer center crop when it is safe.
7. If a person, face, product, or important subject may be cropped, use blurred background fill instead.
8. If the user does not specify the method, ask them to choose one:
   - 居中裁剪
   - 留白填充
   - 模糊背景填充
9. After processing, tell the user the output file path.
10. If Pillow is missing, tell the user to install it with:
    - `pip install Pillow`

## Method Choice

- `crop` / 居中裁剪: Fill 1080x1440 by cropping extra edges from the center. Best for scenery, objects with safe margins, and images where edge loss is acceptable.
- `pad` / 留白填充: Fit the full image inside 1080x1440 and fill the remaining area with white. Best when nothing can be cropped.
- `blur` / 模糊背景填充: Create a blurred full-frame background, then place the full original image centered on top. Best for portraits, people, products, screenshots, or any important subject.

When unsure whether a subject may be cut off, choose `blur` or ask the user.

## Script

Use the bundled script:

```powershell
python "C:\Users\Administrator\.codex\skills\social-image-resizer\scripts\resize_social_image.py" "C:\path\to\image.png" --mode blur
```

Supported modes:

- `crop`
- `pad`
- `blur`

Optional arguments:

- `--output-dir <folder>` to choose a different output folder.
- `--background "#FFFFFF"` for pad mode background color.
- `--quality 95` for JPG quality.

## Response

After processing, respond in Chinese with:

- The chosen method.
- The output image path.
- A reminder that the original image was not modified.