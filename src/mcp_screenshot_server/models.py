"""Pydantic models for MCP Screenshot Server tool results."""

from pydantic import BaseModel, Field


class TextElement(BaseModel):
    """Text element detected via OCR with bounding box coordinates."""
    text: str = Field(description="Detected text content")
    x: int = Field(description="X coordinate (left)")
    y: int = Field(description="Y coordinate (top)")
    width: int = Field(description="Width in pixels")
    height: int = Field(description="Height in pixels")
    confidence: float = Field(default=100.0, description="OCR confidence score (0-100)")


class MonitorInfo(BaseModel):
    """Information about a display monitor."""
    id: int = Field(description="Monitor index (1-based: 1, 2, ...)")
    name: str = Field(description="Monitor name or connector (e.g. eDP-1, HDMI-A-1, Display 1)")
    width: int = Field(description="Width in pixels")
    height: int = Field(description="Height in pixels")
    x: int = Field(default=0, description="X offset on virtual screen")
    y: int = Field(default=0, description="Y offset on virtual screen")
    is_primary: bool = Field(default=False, description="Whether this is the primary monitor")
    scale: float | None = Field(default=1.0, description="Display scale factor if available")


class MonitorListResult(BaseModel):
    """List of available monitors."""
    monitors: list[MonitorInfo] = Field(description="List of detected monitors")
    count: int = Field(description="Total number of active monitors")
    virtual_width: int = Field(description="Total virtual screen width across all monitors")
    virtual_height: int = Field(description="Total virtual screen height across all monitors")
    message: str = Field(description="Status message")


class ScreenshotResult(BaseModel):
    """Result of a screenshot capture or load operation."""
    image_id: str = Field(description="Unique identifier for the captured image")
    width: int = Field(description="Image width in pixels")
    height: int = Field(description="Image height in pixels")
    message: str = Field(description="Status message")
    detected_text: list[TextElement] = Field(
        default_factory=list,
        description="Text elements with bounding boxes detected via OCR"
    )


class OCRResult(BaseModel):
    """Result of an OCR text detection operation."""
    image_id: str = Field(description="Image ID that was analyzed")
    count: int = Field(description="Number of detected text elements")
    elements: list[TextElement] = Field(default_factory=list, description="List of detected text elements")
    message: str = Field(description="Status message")


class AnnotationResult(BaseModel):
    """Result of an annotation operation."""
    image_id: str = Field(description="Image ID that was annotated")
    message: str = Field(description="Status message")


class SaveResult(BaseModel):
    """Result of saving an image."""
    path: str = Field(description="Full path where the image was saved")
    message: str = Field(description="Status message")


class ImageInfo(BaseModel):
    """Information about a stored image."""
    image_id: str
    width: int
    height: int
    size_bytes: int


class ImageListResult(BaseModel):
    """List of available images."""
    images: list[ImageInfo]
    count: int


class DeleteResult(BaseModel):
    """Result of deleting an image."""
    message: str = Field(description="Status message")


class UndoCountResult(BaseModel):
    """Result of getting undo count."""
    image_id: str = Field(description="Image ID")
    undo_count: int = Field(description="Number of available undo operations")


class ClipboardResult(BaseModel):
    """Result of clipboard operation."""
    message: str = Field(description="Status message")


class Base64Result(BaseModel):
    """Result of base64 encoding."""
    image_id: str = Field(description="Image ID")
    data: str = Field(description="Base64-encoded image data with data URI prefix")
    message: str = Field(description="Status message")


class PreviewResult(BaseModel):
    """Result of opening image in preview."""
    message: str = Field(description="Status message")
    path: str = Field(description="Path to the image file")


class MemoryStatsResult(BaseModel):
    """Memory usage statistics for the image store."""
    image_count: int = Field(description="Number of images in store")
    max_images: int = Field(description="Maximum allowed images")
    memory_mb: float = Field(description="Current memory usage in MB")
    max_memory_mb: int = Field(description="Maximum allowed memory in MB")
    undo_levels: int = Field(description="Maximum undo history per image")


class ConfigureLimitsResult(BaseModel):
    """Result of configuring memory limits."""
    max_images: int = Field(description="New maximum image count")
    max_memory_mb: int = Field(description="New maximum memory in MB")
    undo_levels: int = Field(description="New undo history limit")
    evicted_count: int = Field(description="Number of images evicted after applying new limits")
    message: str = Field(description="Status message")


class StepAnnotationResult(BaseModel):
    """Result of adding a step annotation (callout + arrow + optional text)."""
    image_id: str = Field(description="Image ID that was annotated")
    step_number: int = Field(description="The step number used")
    callout_position: tuple[int, int] = Field(description="Position of the callout circle")
    target_position: tuple[int, int] = Field(description="Position the arrow points to")
    message: str = Field(description="Status message")


class ComparisonResult(BaseModel):
    """Result of comparing two images."""
    image_id: str = Field(description="ID of the diff image created")
    difference_percentage: float = Field(description="Percentage of pixels that differ")
    identical: bool = Field(description="True if images are identical")
    message: str = Field(description="Status message")


class SessionExportResult(BaseModel):
    """Result of exporting a session."""
    path: str = Field(description="Path to the exported session file")
    image_count: int = Field(description="Number of images exported")
    total_size_mb: float = Field(description="Total size of exported data in MB")
    message: str = Field(description="Status message")


class SessionImportResult(BaseModel):
    """Result of importing a session."""
    image_count: int = Field(description="Number of images imported")
    image_ids: list[str] = Field(description="List of imported image IDs")
    message: str = Field(description="Status message")
