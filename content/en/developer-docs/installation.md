---
title: Installation
weight: 10
---

Guide for installing and configuring BigLedger SDK.

## System Requirements

- Node.js 16+ or Python 3.8+
- 4GB RAM minimum
- 10GB free disk space

## Installation Methods

### NPM (Node.js)

```bash
npm install @bigledger/sdk
```

### Pip (Python)

```bash
pip install bigledger-sdk
```

### Docker

```bash
docker pull bigledger/sdk:latest
```

## Configuration

Create a configuration file:

```javascript
// config.js
module.exports = {
  apiKey: 'YOUR_API_KEY',
  network: 'mainnet', // or 'testnet'
  timeout: 30000
};
```

## Verification

Verify your installation:

```javascript
const BigLedger = require('@bigledger/sdk');

const client = new BigLedger({
  apiKey: 'YOUR_API_KEY'
});

client.getStatus().then(console.log);
```

## Troubleshooting

Common issues and solutions:

- **Connection errors**: Check your API key and network settings
- **Version conflicts**: Ensure you're using compatible versions
- **Permission issues**: Verify your account has the necessary permissions