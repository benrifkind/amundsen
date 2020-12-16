# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from flask import Flask
from metadata_service.config import LocalConfig


def get_user_details(app: Flask, user_id: str):
    from flask import g
    # user_info = app.oidc.user_getinfo(["name", "email"])
    token_info = g.oidc_token_info
    user_info = dict(
        user_id=user_id,
        email=token_info["sub"],
        first_name=user_id.split(".")[0],
        last_name=user_id.split(".")[1].split("@")[0],
    )

    return user_info


class OidcConfig(LocalConfig):
    USER_DETAIL_METHOD = get_user_details
