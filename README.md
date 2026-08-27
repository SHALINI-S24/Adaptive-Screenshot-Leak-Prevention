# Adaptive AI-Based Screenshot Leak Prevention System

## Overview

A Windows-based screenshot leak prevention system that analyzes screen content using OCR and dynamically determines whether a screenshot should be allowed, watermarked, or blocked based on the sensitivity of the detected information.

## Current Status

### Implemented
- Python development environment
- Background screenshot monitoring
- Print Screen detection
- Dynamic screen capture
- OCR-based text extraction
- OCR confidence extraction

### Technologies
- Python
- EasyOCR
- OpenCV
- Pillow
- SQLite
- PyQt6
- Streamlit

## Planned Features

- Sensitive information detection
- Dynamic risk scoring
- Adaptive security policies
- Allow / watermark / block decisions
- Screenshot activity logging
- Monitoring dashboard
- Windows background agent
- Standalone Windows executable