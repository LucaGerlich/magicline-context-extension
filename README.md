# Magicline API Context Extension

A context extension for [gemini-cli](https://github.com/google-gemini/gemini-cli) designed to assist developers when working with the Magicline API.

## Project Description

This project provides a structured context for AI models to ensure accurate and reliable assistance during Magicline API integrations. It includes:
- **Rules of Engagement**: Strict operating rules in `GEMINI.md` to prevent hallucinations and ensure adherence to official documentation.
- **Local Documentation**: A `docs/` folder containing relevant API documentation excerpts for quick reference by the AI.
- **Output Standards**: Defined structures for endpoint plans, data contracts, and implementation examples.

## Purpose

The main goal of this extension is to streamline development tasks such as:
- Generating TypeScript interfaces for Magicline API responses.
- Drafting `curl` or Node.js requests based on local documentation.
- Understanding pagination, authentication, and error handling specific to Magicline.

## Disclaimer

**Please note:** The documentation contained in the `docs/` folder has been copied from the official **Magicline** documentation. All rights and ownership of that content belong solely to Magicline. This extension was created as a personal tool to facilitate development with their API and is not an official Magicline product.

## Installation

To install this context extension, run the following command:

```bash
gemini extensions install https://github.com/LucaGerlich/magicline-context-extension.git --auto-update --consent
```

## Usage

To use this context extension with `gemini-cli`, you can point the tool to the `GEMINI.md` file or include the repository's content in your prompt context to provide the AI with the necessary domain knowledge.
