#!/usr/bin/env python3
"""
Automatically fix broken links by mapping them to existing pages
"""

import os
import re
from pathlib import Path

# Mapping of broken links to their correct destinations
LINK_MAPPINGS = {
    # Core pages that exist
    '/ai-intelligence/': '/ai-intelligence/',
    '/applets-workflows/': '/applets-workflows/', 
    '/e-invoice-peppol/': '/e-invoice-peppol/',
    '/demos-resources/': '/demos-resources/',
    
    # Map all applets links to applets section
    '/applets/': '/applets/',
    '/applet-store/': '/applets/applet-store/',
    '/applets/applet-directory/': '/applets/applet-directory/',
    '/applets/organization-applet/': '/applets/organization-applet/',
    '/applets/stock-take-applet/': '/applets/stock-take-applet/',
    '/applets/selection-guide/': '/applets/',
    '/applets/finance/': '/applets/',
    '/applets/hr/': '/applets/',
    '/applets/sales/': '/applets/',
    '/applets/supply-chain/': '/applets/',
    
    # Map modules to existing module pages
    '/modules/': '/modules/',
    '/modules/crm/': '/modules/crm/',
    '/modules/financial-accounting/': '/modules/financial-accounting/',
    '/modules/hr/': '/modules/hr/',
    '/modules/inventory/': '/modules/inventory/',
    '/modules/manufacturing/': '/modules/manufacturing/',
    '/modules/pos/': '/modules/pos/',
    '/modules/procurement/': '/modules/procurement/',
    '/modules/projects/': '/modules/projects/',
    
    # Map business operations
    '/business-operations/': '/business-operations/',
    '/business-operations/account-receivable/': '/business-operations/account-receivable/',
    '/business-operations/accounting/': '/business-operations/accounting/',
    '/business-operations/dashboard/': '/business-operations/dashboard/',
    '/business-operations/main-dashboard/': '/business-operations/dashboard/',
    '/business-operations/order/': '/business-operations/order/',
    '/business-operations/sales-dashboard/': '/business-operations/sales-dashboard/',
    
    # Map e-commerce
    '/ecommerce/': '/ecommerce/',
    '/ecommerce/b2b/': '/ecommerce/b2b/',
    '/ecommerce/cp-commerce/': '/ecommerce/cp-commerce/',
    '/ecommerce/integration-with-shopify/': '/ecommerce/integration-with-shopify/',
    '/ecommerce/introduction-to-ecomsync/': '/ecommerce/introduction-to-ecomsync/',
    '/ecommerce/marketplace-tab/': '/ecommerce/marketplace-tab/',
    
    # Map industry solutions
    '/industry-solutions/': '/industry-solutions/',
    '/industry-solutions/automotive-and-workshop-industry/': '/industry-solutions/automotive-and-workshop-industry/',
    '/industry-solutions/food-and-beverage-fb-industry/': '/industry-solutions/food-and-beverage-fb-industry/',
    '/industry-solutions/industry-guide/': '/industry-solutions/industry-guide/',
    
    # Map user guide
    '/user-guide/': '/user-guide/',
    '/user-guide/creating-an-item/': '/user-guide/creating-an-item/',
    '/user-guide/document-item-types/': '/user-guide/document-item-types/',
    '/user-guide/editing-an-item/': '/user-guide/editing-an-item/',
    '/user-guide/introduction/': '/user-guide/introduction/',
    '/user-guide/item-maintenance/': '/user-guide/item-maintenance/',
    '/user-guide/member-listing/': '/user-guide/member-listing/',
    '/user-guide/platform-overview/': '/user-guide/introduction/',
    '/user-guide/price-book/': '/user-guide/price-book/',
    '/user-guide/pricing-scheme/': '/user-guide/pricing-scheme/',
    '/user-guide/team/': '/user-guide/team/',
    
    # Map developers
    '/developers/': '/developers/',
    '/developer-docs/': '/developers/',
    '/developer-docs/installation/': '/developers/getting-started/',
    '/developer/applets/': '/developers/',
    '/developer/architecture/': '/developers/',
    '/developer/integrations/': '/developers/',
    
    # Map API links
    '/api/': '/developers/api-reference/',
    '/api/e-invoice/': '/developers/api-reference/einvoice/',
    
    # Map guides to appropriate sections
    '/guides/accounting-guides/': '/guides/accounting-guides/',
    '/guides/best-practices/': '/guides/',
    '/guides/e-invoice-best-practices/': '/e-invoice-peppol/',
    '/guides/e-invoice-integration/': '/e-invoice-peppol/',
    '/guides/einvoice-guides/': '/guides/einvoice-guides/',
    '/guides/inventory-guides/': '/guides/inventory-guides/',
    '/guides/integration/': '/developers/',
    '/guides/module-config/': '/modules/',
    '/guides/platform-setup/': '/user-guide/',
    
    # Map non-existing sections to closest match
    '/implementation/': '/user-guide/',
    '/implementation/deployment/': '/user-guide/',
    '/implementation/requirements/': '/user-guide/',
    '/implementation/setup/': '/user-guide/',
    '/integrations/': '/developers/',
    '/operations/daily/': '/business-operations/',
    '/operations/first-transaction/': '/business-operations/',
    '/platform/fundamentals/': '/user-guide/',
    '/platform/navigation/': '/user-guide/navigation/',
    
    # Map resource links
    '/resources/applet-guide/': '/applets/',
    '/resources/e-invoice-guide/': '/e-invoice-peppol/',
    '/resources/modules-brochure/': '/modules/',
    
    # Map support links
    '/support': '/user-guide/',
    '/support/e-invoice-faq/': '/e-invoice-peppol/',
    '/support/troubleshooting/': '/user-guide/',
    
    # Map technical links
    '/technical/data-dictionary/': '/developers/',
    '/technical/performance/': '/developers/',
    '/technical/security/': '/developers/',
    
    # Map templates
    '/templates/crm/': '/modules/crm/',
    '/templates/financial/': '/modules/financial-accounting/',
    '/templates/inventory/': '/modules/inventory/',
    
    # Map tutorials
    '/tutorials/': '/user-guide/',
    '/tutorials/crm/': '/modules/crm/',
    '/tutorials/financial-accounting/': '/modules/financial-accounting/',
    '/tutorials/first-invoice/': '/modules/financial-accounting/',
    '/tutorials/inventory/': '/modules/inventory/',
    '/tutorials/pos/': '/modules/pos/',
    
    # Map docs
    '/docs/best-practices/accounting/': '/modules/financial-accounting/',
    '/docs/best-practices/crm/': '/modules/crm/',
    '/docs/best-practices/inventory/': '/modules/inventory/',
    '/docs/hr/': '/modules/hr/',
    '/docs/manufacturing/': '/modules/manufacturing/',
    '/docs/modules/': '/modules/',
    '/docs/procurement/': '/modules/procurement/',
    '/docs/projects/': '/modules/projects/',
    
    # Map misc
    '/demo-request/': '/demos-resources/',
    '/demo/': '/demos-resources/',
    '/demo/e-invoice/': '/e-invoice-peppol/',
    '/consultation/': '/demos-resources/',
    '/subscribe/': '/demos-resources/',
    '/best-practices/': '/user-guide/',
    
    # Map AI links
    '/ai/getting-started/': '/ai-intelligence/',
    '/ai/pricing/': '/ai-intelligence/',
    
    # Language links
    '/zh/': '/',
    '/ms/': '/',
    '/ar/': '/',
    
    # Remove image/asset references - these should be handled separately
    '/screenshots/': '',
    '/diagrams/': '',
}

def fix_link(match):
    """Replace broken link with mapped link"""
    text = match.group(1)
    link = match.group(2)
    
    # Check if we have a mapping
    clean_link = link.split('#')[0].split('?')[0]
    if clean_link in LINK_MAPPINGS:
        new_link = LINK_MAPPINGS[clean_link]
        if new_link:  # Only replace if we have a valid mapping
            return f'[{text}]({new_link})'
    
    # Return original if no mapping
    return match.group(0)

def fix_file(filepath):
    """Fix all broken links in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match markdown links
        link_pattern = re.compile(r'\[([^\]]+)\]\((/[^)]+)\)')
        
        # Replace broken links
        original_content = content
        content = link_pattern.sub(fix_link, content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    content_dir = "content/en"
    
    if not os.path.exists(content_dir):
        print(f"Error: {content_dir} directory not found")
        return 1
    
    print("Fixing broken links in all markdown files...")
    
    fixed_count = 0
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                if fix_file(filepath):
                    fixed_count += 1
                    print(f"  Fixed: {filepath.replace('content/en/', '')}")
    
    print(f"\n✅ Fixed broken links in {fixed_count} files")
    return 0

if __name__ == "__main__":
    exit(main())