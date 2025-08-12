# BigLedger Documentation - Development Guidelines

## Language Strategy

### Primary Language: English (en)
- **All new content should be authored in English first**
- English content is located in `content/en/`
- This is the authoritative version of all documentation
- Keep English content up-to-date and comprehensive

### Supported Languages
1. **Chinese (zh)** - `content/zh/`
2. **Malay (ms)** - `content/ms/`  
3. **Arabic (ar)** - `content/ar/` (RTL support enabled)

### Translation Policy
- Translations are updated periodically, not in real-time
- English content takes priority for new features and updates
- Translation folders may not always have complete parity with English
- When creating new content, focus only on the English version

### Content Creation Guidelines for Claude

When creating or updating documentation:

1. **Always work in the English (`content/en/`) directory**
2. **Do not create translations automatically**
3. **Structure all new content in English first**
4. **Use clear, simple English that is easy to translate**
5. **Avoid idioms and culturally-specific references**

### File Structure Example
```
content/
├── en/           # PRIMARY - Always update this first
│   ├── _index.md
│   ├── user-guide/
│   ├── developer-docs/
│   ├── api-reference/
│   └── tutorials/
├── zh/           # Chinese translations (updated periodically)
├── ms/           # Malay translations (updated periodically)
└── ar/           # Arabic translations (updated periodically, RTL)
```

### Important Commands

Test the site locally:
```bash
hugo server -D
```

Build the site:
```bash
hugo --gc --minify
```

Deploy to production:
```bash
hugo deploy --target=production
```

### Language URLs
- English: https://wiki.bigledger.com/ (default)
- Chinese: https://wiki.bigledger.com/zh/
- Malay: https://wiki.bigledger.com/ms/
- Arabic: https://wiki.bigledger.com/ar/

## Remember
**When authoring content, focus exclusively on the English version in `content/en/`. Translations will be handled separately.**