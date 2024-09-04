import os
import re
import unicodedata

# Function to convert a string to ASCII-safe kebab case
def to_kebab_case(text):
    # Normalize the text to decompose special characters into ASCII equivalents
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    # Remove any remaining special characters except spaces and hyphens
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    # Replace spaces with hyphens and convert to lowercase
    return re.sub(r'\s+', '-', text).lower()

# Read the YAML content from the file
with open('source.yaml', 'r', encoding='utf-8') as file:
    content = file.read()

# Split the content based on the '---' delimiter surrounded by newlines
sections = re.split(r'\n---\n', content.strip())

# Ensure the output directory exists
output_dir = "output_files"
os.makedirs(output_dir, exist_ok=True)

# Iterate through the sections and write each to a separate file
for i in range(0, len(sections), 2):
    if i + 1 < len(sections):
        front_matter = sections[i].strip()
        body_content = sections[i + 1].strip()

        # Extract title from the front matter
        lines = front_matter.splitlines()
        title_line = next((line for line in lines if line.startswith("title:")), None)
        
        if title_line:
            title = title_line.split(":", 1)[1].strip().strip('"')
            filename = f"{to_kebab_case(title)}.md"
            filepath = os.path.join(output_dir, filename)
            
            # Write the front matter and content to the file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('---\n')
                f.write(front_matter + '\n')
                f.write('---\n')
                f.write(body_content + '\n')
            
            print(f"Created {filepath}")
        else:
            print(f"Warning: No title found in section {i//2 + 1}. Skipping section.")
