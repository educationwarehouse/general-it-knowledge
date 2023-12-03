import json
import os
import pathlib

from slugify import slugify
import xml.etree.ElementTree as ET

# Input data (replace this with your data)
input_data = {
  "IDE: Your Digital Workbench": {
    "Basic": [
      "IDEs",
      "Plugins",
      "Smart code navigation",
      "Shortcuts/keybindings",
      "Code snippets",
      "Code formatting",
      "Code completion",
      "Code formatting",
      "Code completion",
      "Integrating external tools",
      "Database management",
      "Data manipulation",
      "Importing and exporting data",
      "Version control",
      "Regular expressions",
      "Multi-cursor edits",
      "Resolving merge conflicts"
    ],
    "Novice": [
      "PyCharm (get the student license for the PRO version, highly recommended)",
      "VS Code (free, construct your own flavor)",
      "Vim (free. For the tough folks)",
      "JupyterLab (free, web-based data science-oriented)",
      "Quick selections",
      "Artificial intelligence",
      "Refactoring tools",
      "Debugging tools",
      "Testing tools",
      "Code snippets",
      "Code formatting",
      "Integrating external tools",
      "Database management",
      "Data manipulation",
      "Importing and exporting data",
      "Version control",
      "Regular expressions",
      "Multi-cursor edits",
      "Resolving merge conflicts"
    ],
    "Intermediate": [
      "Remote development",
      "Remote debugging",
      "Live edit",
      "Code with me",
      "REPLs",
      "Jupyter notebook integration",
      "Scientific Stack Support",
      "Web development support",
      "Code formatting",
      "Code completion",
      "Instant access to documentation",
      "Documentation generation",
      "Duplicate code detector",
      "Quick-fixes using alt-enter",
      "Search-everywhere",
      "Regex support",
      "Goto file/class/symbol",
      "Goto declaration",
      "Find usages"
    ]
  }
}





# Load the XML file
tree = ET.parse("Writerside/hi.tree")
root = tree.getroot()

# Output directory
output_dir = "./Writerside/topics"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through the input data and generate Markdown files
for topic, levels in input_data.items():
    # Slugify the topic for the file name
    topic_slug = slugify(topic, lowercase=False)

    # Loop through the XPs for the topic
    for level, subtopics in levels.items():
        # Slugify the for the file name
        level_slug = slugify(level, lowercase=False)
        level_element = root.find(f".//toc-element[@topic='{level}.md']")

        # Create the Markdown file
        base_filename = f"{level_slug}-{topic_slug}.md"
        mdfile_filename = os.path.join(output_dir, base_filename)
        mdfile = pathlib.Path(mdfile_filename)
        if mdfile.exists():
            print(f"File {mdfile_filename} already exists")
            continue
        with mdfile.open("w") as file:
            if level_element is not None:
                toc_element = ET.Element("toc-element", topic=base_filename)
                level_element.append(toc_element)
            # Write the title
            file.write(f"# {level} {topic}\n\n")

            # Write the Markdown list
            for subtopic in subtopics:
                file.write(f"* {subtopic}\n")

        print(f"Created {level_slug}-{topic_slug}.md in {output_dir}")

tree.write("Writerside/hi.tree")
print("XML file updated successfully.")
