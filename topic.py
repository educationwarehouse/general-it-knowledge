import json
import os
import pathlib

from slugify import slugify
import xml.etree.ElementTree as ET

# Input data (replace this with your data)
input_data = {
    "Version Control": {
        "Basic": [
            "Git, Mercurial, and SVN",
            "GitHub",
            "GitLab",
            "Bitbucket",
            "Semantic versioning (SEMVER)",
            "Branching strategies",
        ],
        "Novice": [
            "Conventional commits",
            "Best practise: Commit messages",
            "Best practise: Branching",
            "Best practise: Merging"
        ],
        "Intermediate": [
            "Git hooks",
            "Change logs and release notes",
            "Automating versioning and changelogs using Semantic release",
            "Naming conventions",
            "Trunk-based development",
            "Feature branching",
            "Release branching",
            "Hotfix branching",
            "Best practise: Rebasing",
            "Best practise: Cherry-picking",
            "Best practise: Resetting",
            "Best practise: Stashing"
        ],
        "Advanced": [
            "Best practise: Amending",
            "Best practise: Reflogs",
            "Best practise: Bisecting",
            "Best practise: Squashing",
            "Best practise: Tagging",
            "Best practise: Submodules",
            "Best practise: Subtrees",
            "Best practise: Worktrees",
            "Best practise: GPG signing",
            "Best practise: Git aliases",
            "Best practise: Git configuration"
        ]
    }
}

# Load the XML file
tree = ET.parse("Writerside/per_level.tree")
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
        if level_element is not None:
            toc_element = ET.Element("toc-element", topic=base_filename)
            level_element.append(toc_element)
        else:
            raise Exception('ERROR: Could not find element for ' + level)
        if mdfile.exists():
            print(f"File {mdfile_filename} already exists")
            continue
        with mdfile.open("w") as file:

            # Write the title
            file.write(f"# {level} {topic}\n\n")

            # Write the Markdown list
            for subtopic in subtopics:
                file.write(f"* {subtopic}\n")

        print(f"Created {level_slug}-{topic_slug}.md in {output_dir}")

tree.write("Writerside/hi.tree")
print("XML file updated successfully.")
