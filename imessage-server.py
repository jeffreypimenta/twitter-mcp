from pathlib import Path
import os
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP
from datetime import datetime, timedelta
import imessagedb
import phonenumbers
import contextlib
import io

mcp = FastMCP("iMessager")

