# AGENTS.md

This file provides instructions for AI coding agents working on the 0xfab1 MkDocs website project.

## Project Overview

This is a personal website built with MkDocs Material theme, containing 449+ markdown files across tech documentation, making guides, and personal content. The site features:

- **Static Site Generator**: MkDocs with Material theme
- **Content**: Tech documentation, tutorials, personal projects, and making guides
- **Optimization**: Automated image conversion to WebP, build optimization, statistics generation
- **Deployment**: GitHub Pages with automated CI/CD

## Dev Environment Setup

- **Python Environment**: Use the virtual environment in `.venv/`
- **Dependencies**: Install with `pip install -r requirements.txt`
- **Activate venv**:
  - Windows: `.venv\Scripts\Activate.ps1`
  - Unix: `source .venv/bin/activate`

## Build Commands

- **Development Server**: `python serve.py` (recommended) or `mkdocs serve`
- **Build Site**: `python build.py` or `mkdocs build`
- **Build with Options**:
  - `python build.py --serve` - Build and serve
  - `python build.py --clean` - Clean build
  - `python build.py --no-optimize` - Skip image optimization
- **Generate Statistics**: `python generate_stats.py`
- **Optimize Images**: `python image_optimizer.py`

## Testing

- **Site Testing**: `python site_tester.py` - Tests built site for issues
- **Media Path Check**: `python check_media_paths.py` - Validates media file references
- **Build Validation**: Always test locally before deploying

## File Structure

```bash
docs/                 # Markdown content
├── about/           # Personal content
├── tech/            # Technical documentation  
├── make/            # Making/building guides
└── index.md         # Homepage

site/                # Built output (auto-generated)
overrides/           # Theme customizations
scripts/             # Build automation scripts
```

## Content Guidelines

- **Images**:
  - Place images in same directory as referencing markdown
  - Use `_filename.ext` naming convention
  - Prefer WebP format (auto-converted during build)
- **Audio/Video**: Place media files in same directory as markdown
- **Links**: Use relative paths for internal content

## Build Process Details

1. **Image Optimization**: Converts JPG/PNG to WebP, maintains originals
2. **Statistics Generation**: Updates `docs/about/0xfab1/stats.md` with site metrics
3. **Site Building**: MkDocs processes markdown to HTML
4. **Minification**: HTML/CSS/JS minified in production

## Performance Configuration

- **Disabled Plugins** (for speed):
  - RSS plugin (was processing all 449+ files)
  - Git revision date plugin (was running git commands on every file)
  - HTML proofer (for development)
- **Navigation**:
  - `use_directory_urls: false` for flat URL structure
  - Collapsed navigation by default

## MkDocs Configuration

- **Config File**: `mkdocs.yml`
- **Theme**: Material with dark/light mode toggle
- **Features**: Instant navigation, search, code highlighting
- **Plugins**: Search, minify, selective RSS (when enabled)

## Deployment

- **Platform**: GitHub Pages
- **Automation**: GitHub Actions workflow
- **Process**: Push to main → Auto build → Deploy to `https://0xfab1.net`

## Code Style

- **Python Scripts**: Follow PEP 8, use type hints where helpful
- **Markdown**: Standard markdown with consistent heading structure
- **YAML**: Consistent indentation (2 spaces)
- **File Naming**: Use descriptive names, `_` prefix for assets

## Common Tasks

### Adding New Content

1. Create markdown file in appropriate `docs/` subdirectory
2. Add images/media in same directory
3. Test locally with `python serve.py`
4. Verify media paths work correctly

### Optimizing Images

- Run `python image_optimizer.py` to convert new images to WebP
- Script automatically updates markdown references
- Original files are removed after conversion

### Updating Statistics

- Run `python generate_stats.py` to update site metrics
- Automatically adds timestamped entries to stats.md
- Tracks word counts, file changes, reading time estimates

### Troubleshooting Build Issues

- Check `python site_tester.py` output for broken links/issues
- Verify image paths with `python check_media_paths.py`
- For slow builds, ensure heavy plugins are disabled
- Clean build with `python build.py --clean`

## Security Considerations

- **Media Files**: Ensure uploaded media doesn't contain sensitive metadata
- **External Links**: Validate external references regularly
- **Dependencies**: Keep MkDocs and plugins updated

## Performance Notes

- Site has 449+ markdown files - expect initial builds to take 1-2 minutes
- Image optimization processes ~544 images
- Use `--no-optimize` flag for faster development iterations
- Development server supports hot reloading for content changes

## Commit Guidelines

- **Format**: `<type>: <description>`
- **Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`
- **Examples**:
  - `docs: add new ansible guide`
  - `feat: improve image optimization script`
  - `fix: resolve broken audio file paths`

## Before Committing

1. Run `python site_tester.py` to check for issues
2. Verify build with `python build.py`
3. Test key pages in browser
4. Check that new media files are accessible

## Agent-Specific Notes

- **Large Codebase**: 449+ content files, focus on specific sections when editing
- **Image Handling**: Always run image optimizer after adding new images
- **Path References**: Use relative paths, maintain flat directory structure
- **Build Testing**: Always test builds locally - broken builds break deployment
- **Statistics**: Re-generate stats after significant content changes
