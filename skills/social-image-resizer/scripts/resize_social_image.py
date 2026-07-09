#!/usr/bin/env python3
"""Resize an image to 1080x1440 without modifying the original."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageEnhance, ImageFilter, ImageOps
except ModuleNotFoundError:
    print("缺少 Python 图片处理库 Pillow。请先安装：pip install Pillow", file=sys.stderr)
    raise SystemExit(2)


TARGET_SIZE = (1080, 1440)


def parse_color(value: str) -> tuple[int, int, int]:
    value = value.strip()
    if value.startswith("#") and len(value) == 7:
        return tuple(int(value[i : i + 2], 16) for i in (1, 3, 5))
    named = {"white": (255, 255, 255), "black": (0, 0, 0)}
    if value.lower() in named:
        return named[value.lower()]
    raise argparse.ArgumentTypeError("背景色请使用 #RRGGBB，例如 #FFFFFF")


def output_path_for(input_path: Path, output_dir: Path | None) -> Path:
    folder = output_dir if output_dir else input_path.parent / "output"
    folder.mkdir(parents=True, exist_ok=True)
    return folder / f"{input_path.stem}_1080x1440.jpg"


def open_image(path: Path) -> Image.Image:
    image = Image.open(path)
    image = ImageOps.exif_transpose(image)
    return image.convert("RGB")


def resize_center_crop(image: Image.Image) -> Image.Image:
    return ImageOps.fit(image, TARGET_SIZE, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))


def resize_pad(image: Image.Image, background: tuple[int, int, int]) -> Image.Image:
    fitted = ImageOps.contain(image, TARGET_SIZE, method=Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", TARGET_SIZE, background)
    offset = ((TARGET_SIZE[0] - fitted.width) // 2, (TARGET_SIZE[1] - fitted.height) // 2)
    canvas.paste(fitted, offset)
    return canvas


def resize_blur(image: Image.Image) -> Image.Image:
    background = ImageOps.fit(image, TARGET_SIZE, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
    background = background.filter(ImageFilter.GaussianBlur(radius=32))
    background = ImageEnhance.Brightness(background).enhance(0.82)

    foreground = ImageOps.contain(image, TARGET_SIZE, method=Image.Resampling.LANCZOS)
    offset = ((TARGET_SIZE[0] - foreground.width) // 2, (TARGET_SIZE[1] - foreground.height) // 2)
    background.paste(foreground, offset)
    return background


def resize_image(input_path: Path, mode: str, output_dir: Path | None, background: tuple[int, int, int], quality: int) -> Path:
    image = open_image(input_path)
    output_path = output_path_for(input_path, output_dir)

    if mode == "crop":
        result = resize_center_crop(image)
    elif mode == "pad":
        result = resize_pad(image, background)
    elif mode == "blur":
        result = resize_blur(image)
    else:
        raise ValueError(f"未知模式：{mode}")

    result.save(output_path, "JPEG", quality=quality, optimize=True)
    return output_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Resize social image to 1080x1440.")
    parser.add_argument("image", type=Path, help="Input image path")
    parser.add_argument("--mode", choices=["crop", "pad", "blur"], required=True, help="Resize mode")
    parser.add_argument("--output-dir", type=Path, default=None, help="Output folder, defaults to ./output next to image")
    parser.add_argument("--background", type=parse_color, default=(255, 255, 255), help="Pad background color, e.g. #FFFFFF")
    parser.add_argument("--quality", type=int, default=95, help="JPEG quality 1-100")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not args.image.exists():
        print(f"找不到图片：{args.image}", file=sys.stderr)
        return 1
    if not args.image.is_file():
        print(f"不是文件：{args.image}", file=sys.stderr)
        return 1
    if not 1 <= args.quality <= 100:
        print("quality 必须在 1 到 100 之间", file=sys.stderr)
        return 1

    output_path = resize_image(args.image, args.mode, args.output_dir, args.background, args.quality)
    print(f"处理完成：{output_path}")
    print("原图未修改。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())