#!/usr/bin/env python3
"""Nexus Agent v3.0 — 启动入口"""
import sys, os
if getattr(sys, 'frozen', False):
    BASE = os.path.dirname(sys.executable)
else:
    BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
os.environ.setdefault("NEXUS_BASE", os.path.join(BASE, "data"))

from nexus.server import start_server

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9800
    start_server(port=port, open_browser=True)
