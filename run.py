import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse, unquote

def download_website(url, output_dir="website"):
    try:
        # Set headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124'
        }
        os.makedirs(os.path.join(output_dir, 'ticket-master'), exist_ok=True)
        # Only download color.css from the asset root and save to ticket-master folder
        color_css_url = urljoin(url, 'color.css')
        color_css_path = os.path.join(output_dir, 'ticket-master', 'color.css')
        try:
            response = requests.get(color_css_url, headers=headers, timeout=10)
            response.raise_for_status()
            with open(color_css_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {color_css_url} to {color_css_path}")
        except Exception as e:
            print(f"Failed to download {color_css_url}: {e}")
        # Commented out: Downloading other assets and HTML
        """
        # Fetch the main page
        print(f"Downloading {url}...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML to find assets
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # List of known assets from error logs
        known_assets = [
            'your-qr-code-image.png',
            'bottom.png',
            'style.css',
            'color.css'
        ]
        
        # Collect assets from HTML
        assets = []
        for img in soup.find_all('img', src=True):
            assets.append(('img', img['src']))
        for link in soup.find_all('link', href=True):
            assets.append(('link', link['href']))
        for script in soup.find_all('script', src=True):
            assets.append(('script', script['src']))
        
        # Add known assets to ensure they're downloaded
        for asset in known_assets:
            assets.append(('manual', asset))
        
        # Save the original HTML
        html_path = os.path.join(output_dir, "index.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        
        # Download each asset
        for tag_type, asset_url in assets:
            try:
                # Remove query parameters (e.g., ?t=1753661922383)
                clean_asset_url = unquote(asset_url.split('?')[0])
                # Convert relative URLs to absolute
                full_url = urljoin(url, clean_asset_url)
                # Get the path for saving
                parsed_url = urlparse(full_url)
                asset_path = os.path.join(output_dir, parsed_url.path.lstrip('/'))
                
                # Create directories if needed
                os.makedirs(os.path.dirname(asset_path), exist_ok=True)
                
                # Download the asset
                asset_response = requests.get(full_url, headers=headers, timeout=10)
                asset_response.raise_for_status()
                
                # Save the asset
                with open(asset_path, "wb") as f:
                    f.write(asset_response.content)
                print(f"Downloaded {full_url} to {asset_path}")
            except Exception as e:
                print(f"Failed to download {full_url}: {e}")
        
        # Patch index.html to use relative paths
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Replace absolute or root-relative paths with relative paths
        replacements = {
            '/your-qr-code-image.png': './your-qr-code-image.png',
            '/bottom.png': './bottom.png',
            '/style.css': './style.css',
            '/color.css': './color.css',
            '/color.css?t=1753661922383': './color.css'
        }
        for old, new in replacements.items():
            html_content = html_content.replace(old, new)
        
        # Save the patched HTML
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Patched {html_path} with relative paths")
        """
        print(f"Website downloaded to '{output_dir}'")
        return True
    
    except Exception as e:
        print(f"Error downloading website: {e}")
        return False

if __name__ == "__main__":
    # Target website
    target_url = "https://amar-louis.github.io/ticket-master/"
    
    # Ethical reminder
    print(f"Downloading {target_url}")
    print("Ensure you have permission to download and use this website locally.")
    
    # Download the website
    if download_website(target_url):
        print("\nTo run the website locally:")
        print(f"1. Navigate to the downloaded folder: cd website")
        print("2. Start a local server: python -m http.server 8000")
        print("3. Open your browser and go to http://localhost:8000")