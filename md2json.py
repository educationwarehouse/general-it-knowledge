import os
import re
import json
import xml.etree.ElementTree as ET

levels = ['Basic', 'Novice', 'Intermediate', 'Advanced', 'Expert']
pattern = re.compile(r'(Basic|Novice|Intermediate|Advanced|Expert)-.*?.md')

tree = ET.parse("Writerside/per_level.tree")
root = tree.getroot()

md_files = [e.attrib['topic'] for e in root.findall(".//toc-element[@topic]")]
md_files = [e for e in md_files if pattern.match(e)]

parsed_data = {}
compact = True

folder = 'Writerside/topics'
for file_name in md_files:
    match = pattern.match(file_name)
    with open(os.path.join(folder, file_name), 'r') as file:
        file_contents = file.read()
        # Extract required information from file_contents
        level = match[1]
        # find the H1 heading using '#' and extract the text
        subject = re.search(
            r'# (Basic|Novice|Intermediate|Advanced|Expert) (.*)',
            file_contents,
        )[2]
        # save the rest of the file contents as the info
        info = re.sub(
            fr'# .*? {subject}',
            '',
            file_contents,
        ).strip()
        # Update the dictionary
        if level not in parsed_data:
            parsed_data[level] = {}
        parsed_data[level][subject] = info.split('\n')

if compact:
    json_output = json.dumps(parsed_data)
else:
    json_output = json.dumps(parsed_data, indent=4)

print('Given this json document: ')
print('```')
print(json_output)
print('```')
print()
print('Given that i want this will be written as a syllabus. I don\'t want students to have to jump jump around to '
      'higher-level subjects before being able to do lower level subjects. '
      'please check the current setup is valid, and present any Errors and Warnings you encounter. '
      )
