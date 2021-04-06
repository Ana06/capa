---
name: "Ana"
title: "Ana"
description: I am trying something
labels: ana

body:
- type: markdown
  attributes:
    value: |
      Explain things here

- type: input
  attributes:
    label: Project name
    description: |
      Provide the name 
    value: |
      `PROJECT_NAME`: https://pypi.org/project/PROJECT_NAME
  validations:
    required: true
...
