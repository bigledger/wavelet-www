# Image Management Guidelines
**BigLedger Documentation Website**

## Overview

This document provides guidelines for managing images, screenshots, diagrams, and other media assets in the BigLedger documentation website. Follow these standards to ensure consistent, accessible, and maintainable visual content.

## Directory Structure

```
static/
├── screenshots/     # User interface screenshots
├── diagrams/        # Workflow and process diagrams
├── images/          # General images, logos, photos
├── icons/           # Custom icons and symbols
├── placeholders/    # Temporary content placeholders
├── api/            # API documentation assets
└── [other files]   # Favicons, manifests, etc.
```

## File Naming Conventions

### Screenshots
- **Format**: `screenshot-[module]-[feature].svg`
- **Examples**:
  - `screenshot-applet-store.svg`
  - `screenshot-order-details.svg`
  - `screenshot-pricing-config.svg`

### Diagrams
- **Format**: `[process-name]-[type].svg`
- **Examples**:
  - `organization-setup-workflow.svg`
  - `ecomsync-integration-flow.svg`
  - `payment-process-diagram.svg`

### General Images
- **Format**: `[descriptive-name].[ext]`
- **Examples**:
  - `bigledger-logo.png`
  - `product-hero-image.webp`
  - `team-photo.jpg`

### Icons
- **Format**: `[purpose]-icon.svg`
- **Examples**:
  - `applet-icon.svg`
  - `success-icon.svg`
  - `warning-icon.svg`

## Image Formats

### Preferred Formats

1. **SVG** - For diagrams, illustrations, icons
   - Scalable to any size
   - Small file sizes
   - Crisp at all resolutions
   - Editable with code

2. **WebP** - For photographs and complex images
   - Better compression than PNG/JPG
   - Modern browser support
   - Fallback to PNG if needed

3. **PNG** - For images requiring transparency
   - Good quality
   - Wide browser support
   - Larger file sizes

4. **JPG** - For photographs (when WebP not available)
   - Good compression for photos
   - No transparency support

### Format Guidelines
- Use **SVG** for all interface mockups and diagrams
- Use **WebP/PNG** for actual screenshots
- Use **PNG** when transparency is needed
- Avoid **GIF** except for simple animations

## Image Specifications

### Screenshots
- **Maximum width**: 800px
- **Format**: SVG (for mockups) or WebP/PNG (for real screenshots)
- **DPI**: 72-96 DPI for web
- **Color space**: sRGB

### Diagrams
- **Format**: SVG
- **Viewbox**: Set appropriate viewBox for scaling
- **Colors**: Use consistent brand colors
- **Text**: Readable at small sizes

### Icons
- **Size**: 64x64px standard (SVG scalable)
- **Format**: SVG
- **Style**: Consistent with brand guidelines

## Adding Images to Documentation

### 1. Place Image in Correct Directory
```bash
# Screenshots
/static/screenshots/new-feature-screen.svg

# Diagrams  
/static/diagrams/user-workflow.svg

# General images
/static/images/product-photo.webp
```

### 2. Reference in Markdown
```markdown
![Alt Text](/screenshots/new-feature-screen.svg)
*Figure 1: Caption describing the image*
```

### 3. Hugo Path Format
- Always use absolute paths starting with `/`
- No need to include `/static/` in the path
- Hugo automatically serves files from `/static/` directory

## Accessibility Requirements

### Alt Text
- **Required** for all images
- **Descriptive** - explain what the image shows
- **Concise** - avoid redundant phrases like "image of"

```markdown
# Good
![Order details interface showing tabbed layout](/screenshots/order-details.svg)

# Bad
![](/screenshots/order-details.svg)
![Image of order details](/screenshots/order-details.svg)
```

### Captions
- **Recommended** for complex images
- **Format**: *Figure N: Description*
- **Placement**: Immediately after image

```markdown
![Order Management Interface](/screenshots/order-details.svg)
*Figure 1: Order Details Interface showing the tabbed layout for comprehensive order information*
```

### Color Contrast
- Ensure sufficient contrast for readability
- Test with accessibility tools
- Provide alternative text descriptions for complex diagrams

## Malaysian Localization

### Currency and Formatting
- Use **RM** (Malaysian Ringgit) in all financial screenshots
- Format numbers according to Malaysian standards: `RM 1,250.00`
- Include Malaysian date formats: `DD/MM/YYYY`

### Tax and Compliance
- Show **SST** (Sales and Service Tax) in pricing examples
- Include **LHDN** (Inland Revenue Board) references in tax screenshots
- Display **e-invoice** compliance features

### Language Considerations
- Primary language: **English**
- Include Malay terms where relevant
- Consider Chinese and Arabic layouts for future expansion

### Local Context
- Use Malaysian business examples
- Show local payment methods (FPX, etc.)
- Include Malaysian marketplace integrations (Shopee, Lazada)

## Creating Screenshots

### Tools Recommended
- **Browser Developer Tools** - For web interface screenshots
- **Figma/Adobe XD** - For mockups and diagrams
- **Snagit/LightShot** - For quick captures
- **SVG editors** - Inkscape, Adobe Illustrator

### Screenshot Standards
1. **Clean interface** - Remove personal data
2. **Consistent browser** - Use same browser/OS for consistency
3. **Standard zoom** - 100% zoom level
4. **Full interface** - Include relevant context
5. **Malaysian data** - Use local examples

### Mockup Creation
- Use placeholder data that reflects Malaysian business context
- Include realistic but anonymized information
- Show proper Malaysian formatting for dates, currency, addresses
- Maintain brand consistency in colors and fonts

## Workflow Diagrams

### Design Principles
- **Left-to-right flow** for English documentation
- **Clear decision points** with diamond shapes
- **Consistent colors** for different types of actions
- **Readable text** at all zoom levels

### Malaysian Business Context
- Include compliance checkpoints (LHDN, SST)
- Show local business registration processes
- Include Malaysian-specific workflow steps
- Reference local regulations and requirements

### Creating Effective Diagrams
1. **Start with user goals** - What is the user trying to achieve?
2. **Show decision points** - Where do users make choices?
3. **Include error handling** - What happens when things go wrong?
4. **Malaysian compliance** - Where do local requirements apply?

## Performance Optimization

### File Size Guidelines
- **Screenshots**: < 100KB when possible
- **Diagrams**: < 50KB (SVG compression)
- **Photos**: < 200KB (use WebP compression)
- **Icons**: < 10KB (optimize SVG)

### Optimization Techniques
1. **SVG optimization** - Remove unnecessary code
2. **Image compression** - Use appropriate quality settings
3. **Lazy loading** - Hugo handles this automatically
4. **Responsive images** - SVG scales automatically

### Tools for Optimization
- **SVGO** - SVG optimization
- **TinyPNG** - PNG/JPG compression  
- **Squoosh** - Modern image compression
- **ImageOptim** - Mac image optimization

## Version Control

### Git Management
- **Commit images separately** from text changes when possible
- **Use descriptive commit messages**: "Add pricing interface screenshot"
- **Avoid large binary files** - compress before committing
- **Use Git LFS** for large assets if needed

### File Organization
- Keep related images together in appropriate directories
- Use consistent naming to group related assets
- Remove unused images regularly
- Document image sources and creation dates

## Quality Assurance

### Before Publishing Checklist
- [ ] Image displays correctly in all browsers
- [ ] Alt text is descriptive and accurate
- [ ] Caption provides additional context
- [ ] File size is optimized
- [ ] Malaysian context is accurate
- [ ] Accessibility requirements met
- [ ] Consistent with brand guidelines
- [ ] No sensitive information exposed

### Testing Process
1. **Visual check** - Does the image display correctly?
2. **Accessibility test** - Screen reader compatibility
3. **Performance test** - Loading speed acceptable?
4. **Mobile test** - Responsive on all devices?
5. **Cross-browser test** - Works in major browsers?

## Maintenance

### Regular Tasks
- **Monthly**: Review and optimize large images
- **Quarterly**: Update screenshots to match latest UI
- **Yearly**: Audit unused images and remove them
- **As needed**: Replace placeholders with actual screenshots

### Updating Images
1. **Replace files** with same filename to maintain links
2. **Update alt text** if image content changes significantly  
3. **Test all references** after replacing images
4. **Update captions** if context changes

### Troubleshooting Common Issues

**Image not displaying:**
- Check file path (should start with `/`)
- Verify file exists in `/static/` directory
- Ensure correct file extension
- Check for typos in filename

**Poor image quality:**
- Use higher resolution source
- Optimize compression settings
- Consider SVG for diagrams/illustrations
- Check image format is appropriate

**Slow loading:**
- Compress images further
- Consider using WebP format
- Optimize SVG code
- Check file sizes

## Integration with Hugo

### Static File Handling
- Files in `/static/` are copied to site root
- Reference without `/static/` prefix
- Hugo handles cache busting automatically
- Multi-language sites share static assets

### Build Process
- Images are processed during `hugo build`
- SVG files are served as-is
- Other formats may be optimized
- Check build logs for any issues

### Development vs Production
- Local development: Files served directly
- Production: Files may be CDN-cached
- Test both environments before deploying
- Ensure paths work in both contexts

---

## Quick Reference

### Adding a New Screenshot
1. Create/capture image
2. Optimize and save to `/static/screenshots/`
3. Add to documentation: `![Alt text](/screenshots/filename.svg)`
4. Include caption: `*Figure N: Description*`
5. Test display and accessibility

### Creating a Diagram
1. Design in SVG editor or code
2. Include Malaysian business context
3. Save to `/static/diagrams/`
4. Reference in documentation
5. Validate accessibility and mobile display

### Image Checklist
- [ ] Correct directory placement
- [ ] Descriptive filename
- [ ] Optimized file size
- [ ] Accessibility compliance
- [ ] Malaysian localization
- [ ] Brand consistency
- [ ] Cross-platform testing

---

**Last Updated**: August 17, 2025  
**Version**: 1.0  
**Maintainer**: BigLedger Documentation Team