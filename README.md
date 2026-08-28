# MCP Screenshot Server 📸

A powerful [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server for capturing screenshots and annotating images with boxes, lines, arrows, circles, text, and highlights.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![MCP](https://img.shields.io/badge/MCP-compatible-purple.svg)

## Features

### 🎯 Smart Annotation (NEW!)

- 🧠 **Unified `annotate` Tool** - One tool for all annotation types
- 📍 **Flexible Positioning** - Named positions ("top-left", "center"), percentages ("50%,30%"), or pixels
- ⚓ **Anchor & Offset** - Control which part of annotation aligns to position, with pixel-level fine-tuning
- 🔄 **Auto-Adjust** - Annotations automatically stay within image bounds
- ⚡ **Batch Annotations** - Apply multiple annotations in a single call
- 🏷️ **Quick Labeling** - Label multiple regions with one command
- 🎯 **Pixel-Perfect Mode** - `precise_annotate` for exact coordinate control
- 🔍 **Tesseract OCR Integration** - `detect_text` to extract on-screen text coordinates and `target_text` for automatic element alignment

### 🤖 AI Vision & OCR Integration

- Works great with **Gemini**, **Claude**, and other vision models for intelligent annotation placement
- Local **Tesseract OCR** extraction returns exact `[x, y, width, height]` bounding boxes without hallucinated coordinates
- Use `target_text` in `precise_annotate` or `annotate` to automatically target buttons, labels, and UI elements

### Capture & Load

- 📷 **Screenshot Capture** - Full screen, region, or window-specific captures
- 📂 **Load Images** - Load existing image files for annotation

### Annotations

- 📦 **Box Annotation** - Draw rectangles with customizable colors and fill
- ➡️ **Arrow Annotation** - Draw directional arrows with adjustable head sizes
- 📏 **Line Drawing** - Simple line annotations
- ⭕ **Circle/Ellipse** - Draw circles and ellipses
- 📝 **Text Overlay** - Add text with custom fonts and backgrounds
- 🔦 **Highlight Regions** - Semi-transparent highlight overlays
- 🔢 **Numbered Callouts** - Auto-numbered callouts for step-by-step guides
- 🖼️ **Border Tool** - Add borders around images

### Editing

- 🔲 **Blur/Pixelate** - Hide sensitive information (passwords, emails)
- ✂️ **Crop** - Crop images to specific regions
- 📐 **Resize** - Resize with scale or exact dimensions
- 🔄 **Rotate/Flip** - Rotate 90/180/270 degrees, flip horizontal/vertical
- 🌓 **Brightness/Contrast** - Adjust image appearance
- 💧 **Watermark** - Add text watermarks
- ↩️ **Undo** - Undo annotations (up to 10 levels)

### Export

- 💾 **Save Images** - Export to PNG, JPG, WebP, and more
- ⚡ **Quick Save** - One-click save to Desktop/Downloads
- 📋 **Clipboard Support** - Copy images directly to system clipboard
- 👁️ **Preview Integration** - Open in macOS Preview.app for native editing
- 🐳 **Docker Ready** - Run as a containerized service

## Examples

Screenshots captured from the browser and annotated using the MCP Screenshot Server tools:

### Basic Annotations

Box, arrow, text, highlight, and circle annotations:

![Basic Annotations](docs/example-basic.png)

### Numbered Callouts

Step-by-step guides with numbered markers:

![Numbered Callouts](docs/example-callouts.png)

### Highlights & Regions

Highlight important sections and mark areas for blur:

![Highlights](docs/example-highlight.png)

### Pixel-Perfect Annotations

Using `precise_annotate` with exact coordinates:

![Pixel Perfect](docs/pixel_perfect_v2.png)

### PII Redaction

Blur or redact sensitive information:

![PII Redacted](docs/mcp_tools_demo.png)

## Quick Start

### Installation

```bash
# Using pip
pip install mcp-screenshot-server

# Using uv (recommended)
uv add mcp-screenshot-server

# From source
git clone https://github.com/aamar-shahzad/mcp-screenshot-server.git
cd mcp-screenshot-server
pip install -e .
```

### Running the Server

```bash
# stdio transport (default - for Cursor AI, Claude Desktop, etc.)
mcp-screenshot-server

# HTTP transport (for web clients)
mcp-screenshot-server --transport streamable-http --port 8000

# SSE transport
mcp-screenshot-server --transport sse --port 8000
```

## Integration with Cursor AI

### Method 1: Local Installation (Recommended)

1. **Install the package**:

   ```bash
   pip install mcp-screenshot-server
   # or
   uv tool install mcp-screenshot-server
   ```

2. **Add to Cursor settings** (`~/.cursor/mcp.json` or workspace `.cursor/mcp.json`):

   ```json
   {
     "mcpServers": {
       "screenshot": {
         "command": "mcp-screenshot-server",
         "args": []
       }
     }
   }
   ```

3. **Restart Cursor** to load the MCP server.

### Method 2: Using uvx (No Installation)

```json
{
  "mcpServers": {
    "screenshot": {
      "command": "uvx",
      "args": ["mcp-screenshot-server"]
    }
  }
}
```

### Method 3: Using Docker

1. **Build the Docker image**:

   ```bash
   docker build -t mcp-screenshot-server .
   ```

2. **Add to Cursor settings**:
   ```json
   {
     "mcpServers": {
       "screenshot": {
         "command": "docker",
         "args": ["run", "-i", "--rm", "mcp-screenshot-server"]
       }
     }
   }
   ```

### Method 4: HTTP Transport

1. **Start the server**:

   ```bash
   mcp-screenshot-server --transport streamable-http --port 8000
   ```

2. **Add to Cursor settings**:
   ```json
   {
     "mcpServers": {
       "screenshot": {
         "url": "http://localhost:8000/mcp"
       }
     }
   }
   ```

## Available Tools

### 🎯 Smart Annotation Tools (Recommended!)

These tools use flexible positioning and auto-adjustment for easier annotation:

| Tool               | Description                                   |
| ------------------ | --------------------------------------------- |
| `annotate`         | Unified annotation with smart positioning     |
| `precise_annotate` | **Pixel-perfect** annotations at exact coords |
| `batch_annotate`   | Apply multiple annotations in ONE call        |
| `label_regions`    | Quickly label multiple areas with one command |

**Position Formats:**

- **Named**: `"top-left"`, `"center"`, `"bottom-right"`, `"top-right-quarter"`, etc.
- **Percentage**: `"50%, 30%"` (from top-left)
- **Pixels**: `"100px, 200px"` (absolute coordinates)

**Anchor Options** (controls which part of annotation aligns to position):

- `"top-left"`, `"top-center"`, `"top-right"`
- `"center-left"`, `"center"`, `"center-right"`
- `"bottom-left"`, `"bottom-center"`, `"bottom-right"`

**Examples:**

```python
# Smart annotation with anchor and offset
annotate(img, "box", "830px, 195px", width=140, height=55,
         anchor="top-left", offset_x=0, offset_y=0)

# Pixel-perfect annotation (no transformations)
precise_annotate(img, "box", x=830, y=195, width=140, height=55, color="blue")
precise_annotate(img, "text", x=830, y=168, text="Code Button", font_size=24)
precise_annotate(img, "arrow", x=100, y=200, x2=300, y2=200, color="red")

# Multiple annotations in one call
batch_annotate(img, '[{"type":"box","position":"top-left"},{"type":"text","position":"center","text":"Hello"}]')

# Label multiple regions at once
label_regions(img, '{"Header":"top-center","Sidebar":"center-left","Main":"center"}')
```

### 🤖 Using with AI Vision Models

For the most accurate annotations, combine with vision-capable AI models:

```
1. Take screenshot with browser/capture tool
2. AI (Gemini/Claude) analyzes image and identifies element coordinates
3. Use precise_annotate with exact coordinates from AI
4. Result: pixel-perfect annotations every time
```

### Screenshot Capture & Multi-Monitor

| Tool                 | Description                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| `list_monitors`      | **NEW!** List connected displays with IDs, names, resolutions, and offsets   |
| `capture_screenshot` | Capture full screen, specific monitor (`monitor=1` or `name`), region, window |
| `load_image`         | Load an existing image file for annotation                                   |

### Basic Annotation Tools (for pixel-precise control)

| Tool                   | Description                             |
| ---------------------- | --------------------------------------- |
| `precise_annotate`     | **NEW!** Pixel-perfect multi-type tool  |
| `add_box`              | Draw rectangles/boxes on images         |
| `add_line`             | Draw lines on images                    |
| `add_arrow`            | Draw arrows on images                   |
| `add_text`             | Add text annotations                    |
| `add_circle`           | Draw circles/ellipses                   |
| `add_highlight`        | Add semi-transparent highlight regions  |
| `add_numbered_callout` | Add auto-numbered callouts (1, 2, 3...) |
| `add_border`           | Add border around entire image          |

### Editing Tools

| Tool                    | Description                            |
| ----------------------- | -------------------------------------- |
| `blur_region`           | Blur/pixelate sensitive areas          |
| `crop_image`            | Crop image to specific region          |
| `resize_image`          | Resize with scale or dimensions        |
| `rotate_image`          | Rotate 90, 180, or 270 degrees         |
| `flip_image`            | Flip horizontal or vertical            |
| `adjust_brightness`     | Adjust image brightness                |
| `adjust_contrast`       | Adjust image contrast                  |
| `add_watermark`         | Add text watermark                     |
| `undo`                  | Undo last annotation (up to 10 levels) |
| `get_undo_count`        | Check available undo operations        |
| `reset_callout_counter` | Reset auto-numbering to 0              |

### Image Management

| Tool              | Description                            |
| ----------------- | -------------------------------------- |
| `list_images`     | List all images in the current session |
| `get_image`       | Get a specific image by ID             |
| `duplicate_image` | Create a copy of an existing image     |
| `delete_image`    | Remove an image from the session       |

### Export Tools

| Tool                   | Description                                   |
| ---------------------- | --------------------------------------------- |
| `save_image`           | Save image to disk (PNG, JPG, WebP, etc.)     |
| `quick_save`           | Quick save to Desktop/Downloads/Documents     |
| `copy_to_clipboard`    | Copy image to system clipboard                |
| `get_image_base64`     | Get image as base64-encoded string            |
| `open_in_preview`      | Open image in macOS Preview or default viewer |
| `open_file_in_preview` | Open any image file in Preview/default viewer |

## macOS Preview Integration

On macOS, you can use the `open_in_preview` tool to open images in the native **Preview.app**, which provides additional markup tools.

### Preview's Native Tools:

- ✏️ **Sketch** - Freehand drawing
- ⬜ **Shapes** - Rectangles, circles, arrows, speech bubbles
- 📝 **Text** - Add text boxes with custom fonts
- ✍️ **Signature** - Add your saved signature
- 🎨 **Colors** - Full color picker
- 📏 **Border** - Adjust line thickness

This allows you to combine MCP annotations with Preview's native tools for more complex edits.

## Usage Examples

### Basic Screenshot and Annotation

```python
# In Cursor AI, you can ask:
# "Take a screenshot and add a red box around the error message"

# The AI will use these tools:
# 1. capture_screenshot() -> returns image_id
# 2. add_box(image_id, x=100, y=200, width=300, height=50, color="red")
# 3. save_image(image_id, path="~/Desktop/annotated.png")
```

### Creating a Bug Report Screenshot

```
User: Take a screenshot of my screen and highlight the button at coordinates
      (500, 300) with a red circle, add an arrow pointing to it, and save it.

AI uses:
1. capture_screenshot(mode="fullscreen")
2. add_circle(image_id, x=500, y=300, radius=40, color="red", line_width=3)
3. add_arrow(image_id, x1=400, y1=200, x2=480, y2=280, color="red")
4. add_text(image_id, x=350, y=180, text="Click here!", color="red")
5. save_image(image_id, path="~/Desktop/bug-report.png")
```

### Annotating an Existing Image

```
User: Load the image at ~/Downloads/mockup.png and add numbered callouts

AI uses:
1. load_image(path="~/Downloads/mockup.png")
2. add_circle(image_id, x=100, y=100, radius=20, color="blue", fill="blue")
3. add_text(image_id, x=92, y=88, text="1", color="white")
4. add_circle(image_id, x=300, y=200, radius=20, color="blue", fill="blue")
5. add_text(image_id, x=292, y=188, text="2", color="white")
6. save_image(image_id, path="~/Downloads/mockup-annotated.png")
```

## Docker Usage

### Build and Run

```bash
# Build the image
docker build -t mcp-screenshot-server .

# Run with stdio transport
docker run -i --rm mcp-screenshot-server

# Run with HTTP transport
docker run -p 8000:8000 mcp-screenshot-server \
    --transport streamable-http --port 8000

# Run with volume for saving screenshots
docker run -p 8000:8000 -v $(pwd)/screenshots:/app/screenshots \
    mcp-screenshot-server --transport streamable-http
```

### Docker Compose

```bash
# Start HTTP server
docker-compose up -d mcp-screenshot-server

# Start stdio server
docker-compose --profile stdio up -d mcp-screenshot-server-stdio
```

## Configuration

### Environment Variables

| Variable   | Description             | Default   |
| ---------- | ----------------------- | --------- |
| `MCP_HOST` | Host for HTTP transport | `0.0.0.0` |
| `MCP_PORT` | Port for HTTP transport | `8000`    |

### Command Line Arguments

```
mcp-screenshot-server [OPTIONS]

Options:
  --transport {stdio,streamable-http,sse}
                        Transport to use (default: stdio)
  --host HOST           Host for HTTP transports (default: 0.0.0.0)
  --port PORT           Port for HTTP transports (default: 8000)
```

## Platform Support

| Platform | Screenshot                | Clipboard        | Notes                |
| -------- | ------------------------- | ---------------- | -------------------- |
| macOS    | ✅ Native `screencapture` | ✅ AppleScript   | Full support         |
| Windows  | ✅ PIL ImageGrab          | ✅ PowerShell    | Full support         |
| Linux    | ✅ PIL/scrot              | ✅ xclip/wl-copy | Requires X11/Wayland |
| Docker   | ✅ With Xvfb              | ⚠️ Limited       | Headless mode        |

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/aamar-shahzad/mcp-screenshot-server.git
cd mcp-screenshot-server

# Install with development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linting
ruff check src/
```

### Project Structure

```
mcp-screenshot-server/
├── src/
│   └── mcp_screenshot_server/
│       ├── __init__.py
│       └── server.py          # Main MCP server implementation
├── tests/
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── LICENSE
```

## Troubleshooting

### macOS: "screencapture" requires screen recording permission

Go to **System Preferences > Privacy & Security > Screen Recording** and enable the terminal or IDE you're using.

### Linux: Clipboard not working

Install clipboard tools:

```bash
# For X11
sudo apt install xclip

# For Wayland
sudo apt install wl-clipboard
```

### Docker: Screenshots are blank

The Docker container runs in headless mode. For actual screen capture, you need to run the server natively on the host system.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- Image processing powered by [Pillow](https://pillow.readthedocs.io/)
