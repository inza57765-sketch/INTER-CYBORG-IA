Changelog — INTER-CYBORG.IA

All notable changes to this project will be documented in this file.

The format is inspired by "Keep a Changelog" (https://keepachangelog.com/en/1.1.0/).

[Unreleased]

Planned

- Develop the central Core orchestrator.
- Separate model selection from API communication.
- Improve conversational memory management.
- Implement robust HTTP and network error handling.
- Expand automated tests.

[0.1.0] - 2026-10-16

Added

- Initial Python prototype for AI model interaction.
- "choice_models()" function for selecting a model and submitting user messages.
- API communication using the "requests" library.
- Authentication integration through the "auth" package.
- Basic conversational history using user and assistant messages.
- Extraction and display of the AI model's response.
- Initial authentication tests.
- Initial project structure with "auth/", "core/", and "tests/".

Notes

- The current prototype uses in-memory conversation history.
- The Core orchestrator architecture is still under development.
- Error handling and multi-conversation support require further improvements.
