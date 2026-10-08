# YouTube Content Copilot

AI-powered YouTube content creation assistant that helps creators research topics and generate structured video content using multi-agent AI.

## Overview

YouTube Content Copilot simplifies the YouTube content creation workflow by using specialized AI agents for research, script generation, and SEO content.

The application focuses on content drafting and creator assistance. Final editing and publishing remain under the creator's control.

## Features

* AI-powered topic research
* Structured YouTube script generation
* SEO title and description generation
* Keyword suggestions
* Multi-agent AI workflow
* Human review before publishing
* Streamlit frontend
* FastAPI backend

## Architecture

### Research Agent

Researches the given topic and provides information for content creation.

### Script Agent

Uses the research to create a structured YouTube video script.

### SEO Agent

Generates SEO-focused titles, descriptions, keywords, and content suggestions.

### Crew

Coordinates the different AI agents and manages the content-generation workflow.

## Project Structure

```text
youtube_content_copilot/
│
├── app/
│   ├── agents/
│   │   ├── crew.py
│   │   ├── research_agent.py
│   │   ├── script_agent.py
│   │   └── seo_agent.py
│   │
│   ├── backend/
│   │   └── main.py
│   │
│   └── frontend/
│       └── streamlit_app.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Tech Stack

* Python
* Streamlit
* FastAPI
* CrewAI
* OpenAI
* Multi-Agent AI
* REST API

## Workflow

```text
User Topic
    ↓
Research Agent
    ↓
Script Agent
    ↓
SEO Agent
    ↓
Content Draft
    ↓
Human Review & Editing
    ↓
Manual Publishing
```

## Example Use Case

A creator enters a topic such as:

**"Why do people change when they get money?"**

The system can assist with:

1. Researching the topic
2. Creating a structured video script
3. Generating a suitable title
4. Creating a video description
5. Suggesting SEO keywords
6. Preparing a content draft

The creator reviews and edits the generated content before publishing.

## Important

This project is designed as a content creation assistant, not an autonomous publishing system.

AI-generated content should be reviewed, fact-checked, and edited before publication.

## Future Improvements

* Tamil content generation
* YouTube trend research
* YouTube API integration
* Content history and versioning
* Thumbnail prompt generation
* Voice-over generation
* Automatic fact-checking
* RAG-based research
* Creator analytics

## Author

**Patham Priyal**

AI Automation & Generative AI Learner

GitHub: https://github.com/spriyaldiary-ship-it
