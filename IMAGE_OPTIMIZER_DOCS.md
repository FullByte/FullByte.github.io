# Image Optimizer Documentation

## Overview

The `image_optimizer.py` script is a comprehensive tool for optimizing images in MkDocs projects. It combines the functionality of the previous `convert_to_webp.py` and `cleanup_images.py` scripts into a single, powerful image optimization solution.

## Features

### 🔄 Image Conversion

- Converts PNG, JPEG, and JPG images to WebP format
- Configurable quality settings (1-100)
- Lossless compression option
- Automatic RGBA to RGB conversion for lossy WebP
- Smart handling of existing WebP files (skip if newer)

### 📝 Markdown Reference Updates

- **Clean References**: Simple `![alt](image.webp)` format (recommended)
- **Fallback References**: HTML `<picture>` elements with WebP and fallback support
- Automatic detection and replacement of image references
- Safe processing with error handling

### 🧹 Cleanup Operations

- Removes original images when WebP equivalents exist
- Preserves animated GIFs (8 files in current project)
- Safe deletion with existence verification

### 📊 Analytics & Reporting

- Real-time conversion statistics
- Size reduction calculations
- Image inventory reporting
- Comprehensive operation summaries

## Usage Examples

### Show Current Image Inventory

```bash
python image_optimizer.py --inventory
```

### Convert All Images to WebP

```bash
python image_optimizer.py --mode convert
```

### Update Markdown with Clean WebP References

```bash
python image_optimizer.py --mode update --clean-references
```

### Clean Up Original Images

```bash
python image_optimizer.py --mode cleanup
```

### Complete Optimization (Recommended)

```bash
python image_optimizer.py --mode all --clean-references
```

### High Quality Conversion

```bash
python image_optimizer.py --quality 95 --mode all
```

### Lossless Conversion

```bash
python image_optimizer.py --lossless --mode all
```

### Quiet Operation

```bash
python image_optimizer.py --quiet --mode all
```

## Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--docs-path` | Path to docs directory | `docs` |
| `--quality` | WebP quality (1-100) | `85` |
| `--lossless` | Use lossless WebP compression | `False` |
| `--extensions` | Image extensions to convert | `jpg jpeg png` |
| `--mode` | Operation mode | `all` |
| `--clean-references` | Use clean WebP references | `False` |
| `--quiet` | Suppress verbose output | `False` |
| `--inventory` | Show image inventory and exit | `False` |

## Operation Modes

### `convert`

- Only converts images to WebP format
- Does not modify markdown files
- Does not delete original images

### `update`

- Only updates markdown file references
- Requires existing WebP files
- Choice between clean or fallback reference format

### `cleanup`

- Only deletes original images with WebP equivalents
- Preserves images without WebP versions
- Safe deletion with verification

### `all` (Default)

- Performs all operations in sequence:
  1. Convert images to WebP
  2. Update markdown references
  3. Clean up original images

## Reference Formats

### Clean References (Recommended)

```markdown
![Alt text](image.webp)
```

- Simple, clean markdown syntax
- Works with modern browsers (95%+ support)
- Recommended for new projects

### Fallback References

```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Alt text">
</picture>
```

- HTML picture element with fallback
- Supports older browsers
- Larger file size due to keeping originals

## Current Project Status

Based on the last inventory check:

- **WebP Images**: 544 files ✅
- **Original Images**: 0 files (JPG/JPEG/PNG) ✅
- **Animated GIFs**: 8 files (preserved) ✅
- **Markdown Files**: 161 files updated ✅
- **Size Reduction**: 55.2% (76MB → 34MB) ✅

## Error Handling

The script includes comprehensive error handling:

- Graceful handling of corrupted images
- Safe file operations with existence checks
- Detailed error reporting
- Continuation of processing despite individual failures

## Best Practices

1. **Always backup** your project before running optimization
2. **Test locally** before deploying optimized images
3. **Use clean references** for better maintainability
4. **Check inventory** before and after optimization
5. **Preserve animated GIFs** as they don't convert well to WebP
6. **Monitor build process** to ensure all references work correctly

## Integration with MkDocs

The optimizer is designed specifically for MkDocs projects:

- Respects MkDocs file structure
- Updates relative image paths correctly
- Compatible with Material theme
- Works with static site generation
- Optimizes for web delivery

## Performance Impact

Expected improvements after optimization:

- **Load Time**: 40-60% faster image loading
- **Bandwidth**: 55%+ reduction in data transfer
- **Storage**: Significant space savings
- **SEO**: Better Core Web Vitals scores
- **UX**: Faster page rendering

## Troubleshooting

### Common Issues

**WebP not displaying**: Check browser compatibility and use fallback format
**Build errors**: Verify all image references are correct after cleanup
**Large GIFs**: Consider alternative formats for animated content
**Quality issues**: Adjust quality settings or use lossless mode

### Recovery

If you need to recover original images:

1. Use git to restore files: `git checkout HEAD -- docs/`
2. Re-run conversion without cleanup: `--mode convert`
3. Update references as needed: `--mode update`
