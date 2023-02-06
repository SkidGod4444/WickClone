# -*- coding: utf-8 -*-

"""
jishaku.features.filesystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The jishaku filesystem-related commands.

:copyright: (c) 2021 Devon (Gorialis) R
:license: MIT, see LICENSE for more details.

"""

import io
import os
import pathlib
import re

import aiohttp
import discord

from jishaku.exception_handling import ReplResponseReactor
from jishaku.features.baseclass import Feature
from jishaku.hljs import get_language, guess_file_traits
from jishaku.paginators import PaginatorInterface, WrappedFilePaginator, use_file_check
from jishaku.types import ContextA


class FilesystemFeature(Feature):
    """
    Feature containing the filesystem-related commands
    """

    __cat_line_regex = re.compile(r"(?:\.\/+)?(.+?)(?:#L?(\d+)(?:\-L?(\d+))?)?$")



    @Feature.Command(parent="jsk", name="curl")
    async def jsk_curl(self, ctx: ContextA, url: str):
        """
        Download and display a text file from the internet.

        This command is similar to jsk cat, but accepts a URL.
        """

        # remove embed maskers if present
        url = url.lstrip("<").rstrip(">")

        async with ReplResponseReactor(ctx.message):
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.read()
                    hints = (
                        response.content_type,
                        url
                    )
                    code = response.status

            if not data:
                return await ctx.send(f"HTTP response was empty (status code {code}).")

            if use_file_check(ctx, len(data)):  # File "full content" preview limit
                # Shallow language detection
                language = None

                for hint in hints:
                    language = get_language(hint)

                    if language:
                        break

                await ctx.send(file=discord.File(
                    filename=f"response.{language or 'txt'}",
                    fp=io.BytesIO(data)
                ))
            else:
                try:
                    paginator = WrappedFilePaginator(io.BytesIO(data), language_hints=hints, max_size=1980)
                except UnicodeDecodeError:
                    return await ctx.send(f"Couldn't determine the encoding of the response. (status code {code})")
                except ValueError as exc:
                    return await ctx.send(f"Couldn't read response (status code {code}), {exc}")

                interface = PaginatorInterface(ctx.bot, paginator, owner=ctx.author)
                await interface.send_to(ctx)
