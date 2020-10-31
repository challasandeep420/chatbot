#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "cf492019-9519-40c7-9286-07f9f39693ab")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "kJtAGo_x9GfN-rxT~-35F145~K5dL2ONf0")
