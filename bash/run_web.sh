#!/bin/bash

uvicorn --factory asgi:build_app --host 0.0.0.0 --port 8000
