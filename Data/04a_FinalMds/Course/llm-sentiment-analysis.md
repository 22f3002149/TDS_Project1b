## LLM Sentiment Analysis

[OpenAI's API](https://platform.openai.com/) provides access to language models like GPT 4o, GPT 4o mini, etc.

For more details, read OpenAI's guide for:

- [Text Generation](https://platform.openai.com/docs/guides/text-generation)
- [Vision](https://platform.openai.com/docs/guides/vision)
- [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Start with this quick tutorial:

[![OpenAI API Quickstart: Send your First API Request](https://i.ytimg.com/vi_webp/Xz4ORA0cOwQ/sddefault.webp)

This image shows a macOS terminal displaying a snippet of a `.zshrc` configuration file, which customizes the Z shell environment.

The file exports several key variables:
*   `PATH`: Defines directories for executable files, including Ruby gems and Android SDK tools.
*   `LANGUAGE` and `LC_ALL`: Set to `en_US.UTF-8`.
*   `ANDROID_HOME`: Points to the Android SDK directory.
*   `OPENAI_API_KEY`: Reveals configuration for OpenAI integration.

The editor view indicates it's part of an IDE with syntax highlighting, showing how developers personalize their command-line setups.
](https://youtu.be/Xz4ORA0cOwQ)

Here's a minimal example using `curl` to generate text:

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{ "role": "user", "content": "Write a haiku about programming." }]
  }'
```

Let's break down the request:

- `curl https://api.openai.com/v1/chat/completions`: The API endpoint for text generation.
- `-H "Content-Type: application/json"`: The content type of the request.
- `-H "Authorization: Bearer $OPENAI_API_KEY"`: The API key for authentication.
- `-d`: The request body.
  - `"model": "gpt-4o-mini"`: The model to use for text generation.
  - `"messages":`: The messages to send to the model.
    - `"role": "user"`: The role of the message.
    - `"content": "Write a haiku about programming."`: The content of the message.

[![LLM Sentiment Analysis](https://i.ytimg.com/vi_webp/_D46QrX-2iU/sddefault.webp)

This screenshot captures a video call interface showing participants discussing prison demographics and internal conflicts from the TV show "Oz." The shared screen displays key terms like 'Security State Penitentiary,' listing groups such as Aryans, Muslims, gangs, Italians, and Irish. Participants are identified by initials AG and P, highlighting clandestine deals and ongoing strife within the fictional facility.
](https://youtu.be/_D46QrX-2iU)

This video explains how to use large language models (LLMs) for sentiment analysis and classification, covering:

- **Sentiment Analysis**: Use OpenAI API to identify the sentiment of movie reviews as positive or negative.
- **Prompt Engineering**: Learn how to craft effective prompts to get desired results from LLMs.
- **LLM Training**: Understand how to train LLMs by providing examples and feedback.
- **OpenAI API Integration**: Integrate OpenAI API into Python code to perform sentiment analysis.
- **Tokenization**: Learn about tokenization and its impact on LLM input and cost.
- **Zero-Shot, One-Shot, and Multi-Shot Learning**: Understand different approaches to using LLMs for learning.

Here are the links used in the video:

- [Jupyter Notebook](https://colab.research.google.com/drive/1tVZBD9PKto1kPmVJFNUt0tdzT5EmLLWs)
- [Movie reviews dataset](https://drive.google.com/file/d/1X33ao8_PE17c3htkQ-1p2dmW2xKmOq8Q/view)
- [OpenAI Playground](https://platform.openai.com/playground/chat)
- [OpenAI Pricing](https://openai.com/api/pricing/)
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/)
- [OpenAI Docs](https://platform.openai.com/docs/overview)
