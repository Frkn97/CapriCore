#!/usr/bin/env bash
cd "$(dirname "$0")"
export CAPRI_NODE_PATH="$PWD/.runtime/node/bin/node"
export PATH="$PWD/.runtime/node/bin:$PATH"
exec ./node_modules/electron/dist/electron apps/desktop/main.mjs \
  --ozone-platform=x11 \
  --disable-gpu-vsync \
  --log-level=3
