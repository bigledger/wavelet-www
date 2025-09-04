#!/bin/bash

# BigLedger Wiki Deployment Script
# This script handles the complete deployment process for the BigLedger documentation site

set -e  # Exit on error

echo "🚀 Starting BigLedger Wiki deployment process..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Check prerequisites
check_prerequisites() {
    echo "Checking prerequisites..."
    
    # Check Hugo
    if ! command -v hugo &> /dev/null; then
        print_error "Hugo is not installed. Please install Hugo first."
        exit 1
    fi
    print_status "Hugo is installed ($(hugo version | head -n1))"
    
    # Check Git
    if ! command -v git &> /dev/null; then
        print_error "Git is not installed. Please install Git first."
        exit 1
    fi
    print_status "Git is installed"
    
    # Check if we're in the right directory
    if [ ! -f "hugo.yaml" ]; then
        print_error "Not in the BigLedger Wiki directory. Please run from the project root."
        exit 1
    fi
    print_status "In correct directory"
}

# Build the site
build_site() {
    echo ""
    echo "Building site with Hugo..."
    
    # Clean old build
    rm -rf public/
    print_status "Cleaned old build files"
    
    # Build with Hugo
    hugo --gc --minify
    
    if [ $? -eq 0 ]; then
        print_status "Site built successfully"
    else
        print_error "Hugo build failed"
        exit 1
    fi
}

# Test the build locally
test_locally() {
    echo ""
    echo "Would you like to test the site locally first? (y/n)"
    read -r response
    
    if [[ "$response" == "y" ]]; then
        print_status "Starting local server on http://localhost:1313"
        print_warning "Press Ctrl+C to stop the server and continue deployment"
        hugo server
    fi
}

# Commit changes
commit_changes() {
    echo ""
    echo "Checking for uncommitted changes..."
    
    if [[ -n $(git status -s) ]]; then
        print_warning "You have uncommitted changes:"
        git status -s
        echo ""
        echo "Would you like to commit them now? (y/n)"
        read -r response
        
        if [[ "$response" == "y" ]]; then
            git add -A
            echo "Enter commit message:"
            read -r commit_message
            git commit -m "$commit_message"
            print_status "Changes committed"
        else
            print_warning "Continuing without committing local changes"
        fi
    else
        print_status "No uncommitted changes"
    fi
}

# Push to GitHub
push_to_github() {
    echo ""
    echo "Pushing to GitHub..."
    
    # Get current branch
    branch=$(git branch --show-current)
    
    # Push changes
    if git push origin "$branch"; then
        print_status "Pushed to GitHub successfully"
        return 0
    else
        print_error "Failed to push to GitHub"
        return 1
    fi
}

# Trigger GitHub Actions
trigger_deployment() {
    echo ""
    echo "GitHub Actions will automatically deploy the site..."
    
    # Check if gh CLI is installed
    if command -v gh &> /dev/null; then
        echo "Checking deployment status..."
        
        # Wait a moment for the action to start
        sleep 5
        
        # Get the latest run
        run_id=$(gh run list --workflow=deploy.yml --limit=1 --json databaseId --jq '.[0].databaseId')
        
        if [ -n "$run_id" ]; then
            echo "Deployment run started: #$run_id"
            echo "You can monitor it at: https://github.com/bigledger/blg-wiki/actions/runs/$run_id"
            
            # Option to watch the deployment
            echo ""
            echo "Would you like to watch the deployment progress? (y/n)"
            read -r response
            
            if [[ "$response" == "y" ]]; then
                gh run watch "$run_id"
                
                # Check if successful
                conclusion=$(gh run view "$run_id" --json conclusion --jq '.conclusion')
                if [[ "$conclusion" == "success" ]]; then
                    print_status "Deployment completed successfully!"
                else
                    print_error "Deployment failed. Check the logs for details."
                    exit 1
                fi
            fi
        fi
    else
        print_warning "GitHub CLI not installed. Cannot monitor deployment status."
        echo "Check deployment at: https://github.com/bigledger/blg-wiki/actions"
    fi
}

# Verify deployment
verify_deployment() {
    echo ""
    echo "Verifying deployment..."
    
    # Test main site
    if curl -s -o /dev/null -w "%{http_code}" https://wiki.bigledger.com | grep -q "200\|301\|302"; then
        print_status "Main site is accessible: https://wiki.bigledger.com"
    else
        print_error "Main site is not accessible"
    fi
    
    # Test a few key pages
    for path in "modules" "user-guide/getting-started" "zh/modules" "ms/modules" "ar/modules"; do
        if curl -s -o /dev/null -w "%{http_code}" "https://wiki.bigledger.com/$path/" | grep -q "200\|301\|302"; then
            print_status "Page accessible: /$path/"
        else
            print_warning "Page may have issues: /$path/"
        fi
    done
    
    echo ""
    print_status "Deployment verification complete!"
    echo "Site is live at: https://wiki.bigledger.com"
}

# Main deployment flow
main() {
    echo "======================================"
    echo "  BigLedger Wiki Deployment Script"
    echo "======================================"
    echo ""
    
    check_prerequisites
    build_site
    test_locally
    commit_changes
    
    if push_to_github; then
        trigger_deployment
        verify_deployment
    else
        print_error "Deployment cancelled due to GitHub push failure"
        exit 1
    fi
    
    echo ""
    echo "======================================"
    print_status "Deployment process complete!"
    echo "======================================"
}

# Run main function
main "$@"