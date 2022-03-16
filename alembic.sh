#!/bin/bash
PYTHONPATH=$PYTHONPATH:`pwd` alembic "$@"
