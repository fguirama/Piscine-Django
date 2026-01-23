#!/bin/bash

LIB_DIR='local_lib'
LOG_FILE='path_install.log'
PYTHON_SCRIPT='my_program.py'

echo -n '- pip version: '
pip --version

rm -rf "$LIB_DIR"

pip install \
    --target "$LIB_DIR" \
    --upgrade \
    git+https://github.com/jaraco/path.py.git \
    > "$LOG_FILE" 2>&1

if [ -d "$LIB_DIR/path" ]; then
    echo "✅ Library successfully installed "
    python3 "$PYTHON_SCRIPT"
else
    echo "❌ Installation failed"
    exit 1
fi