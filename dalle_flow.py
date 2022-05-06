# -*- coding: utf-8 -*-
import configparser
from docarray import Document
from utils import return_image_sprites


config = configparser.ConfigParser()
config.read(".env")
SERVER_URL = config.get(
    "SERVER",
    "url",
    # defaults to dalle-flow test server
    fallback="grpc://dalle-flow.jina.ai:51005",
)
# print(SERVER_URL)


def request_diffusion_sprite(fav, num_images):
    diffused = fav.post(
        f"{SERVER_URL}",
        parameters={"skip_rate": 0.5, "num_images": num_images},
        target_executor="diffusion",
    ).matches
    return diffused, return_image_sprites(diffused)


def request_sprites(prompt, num_images=9):

    da = (
        Document(text=prompt)
        .post(SERVER_URL, parameters={"num_images": num_images})
        .matches
    )
    return da, return_image_sprites(da)


def request_resolution(fav):
    da = fav.post(f"{SERVER_URL}/upscale", target_executor="upscaler")
    return da
