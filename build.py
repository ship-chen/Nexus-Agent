#!/usr/bin/env python3
"""Nexus Agent v3.0 完整版打包脚本 — 本地GUI专用"""
import subprocess
import sys
import os
def build(mode="dir"):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--name=NexusAgentV3",
        "--windowed",
        "--clean",
        "--add-data=nexus;nexus",

        # ======================
        # 我只加这 2 行！别的全不动！
        "--add-data=gui_config.yaml;.",
        "--hidden-import=watchdog",
        # ======================

        "--hidden-import=nexus.ui.theme",
        "--hidden-import=nexus.ui.widgets",
        "--hidden-import=nexus.mcp",
        "--hidden-import=nexus.skills",
        "--hidden-import=nexus.engine",
        "--hidden-import=nexus.memory",
        "--hidden-import=nexus.tools",
        "--hidden-import=nexus.providers",
        "--hidden-import=nexus.gateway",
        "--hidden-import=nexus.voice",
        "--hidden-import=nexus.evolution",
        "main_gui.py"
    ]
    if mode == "single":
        cmd.insert(5, "--onefile")
    else:
        cmd.insert(5, "--onedir")
    subprocess.check_call(cmd)
    print("\n✅ Nexus Agent v3.0 打包完成！")
    print(f"📦 输出位置：dist/NexusAgentV3{'/' if mode == 'dir' else '.exe'}")
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Nexus Agent v3.0 打包脚本")
    args = parser.parse_args()
    build("single" if args.single else "dir")
