# Capybara+

**Capybara** is a versatile Discord chatbot powered by Generative AI. It provides support for text, image, videos and other multimedia inputs, centered around help with code. To steer away from monotone chat assistants, bot embodies a playful capybara persona, asking for virtual treats (lush green grass emojis and images) for writing code. 
This was originally an update to my old discord-py bot from 2019 that worked on if-else checks with a long list of word matching input-output pairs, several parts of which had become obsolete with newer versions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Customization](#customization)
- [Contributing](#contributing)
- [Discord.py](#discordpy)

## Features

- **Supports text, image, video, and multimedia inputs.**
- **Embodied in a Capybara**
- **Multi-Platform Compatibility:** Seamless integration with Discord.
- **Customized on Google's 2B Gemini 1.5 Flash** 

## Installation

To get started with Capybara+, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/CapybaraPlus.git
   cd CapybaraPlus

   
2. **Install the Google AI Python:**
  ```bash
  $ pip install google-generativeai 
  ```
See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python

 ## Usage
Subject to Google's **free tier** limits

**Rate Limits****

**15 RPM (requests per minute)**

**1 million TPM (tokens per minute)**

**1,500 RPD (requests per day)**

## Commands

I have designed it to run in a seperate text channel of its own and therefore no prefix is added and capy responds to each and every message.

However prefix functionality can be easily achieved by removing from comment and fixing indentation.

  ```python
    # message.content.startswith('!')
  ```
## Customization

While testing I notice a small number of incorrect flags by Gemini. It by default blocks possible harm based on prediction threshold \
<code> BLOCK_MEDIUM_AND_ABOVE </code> are blocked. You can change this on your own:

The following table describes the harm block thresholds used by VertexAI:

| Threshold                          | Description                                |
|------------------------------------|--------------------------------------------|
| HARM_BLOCK_THRESHOLD_UNSPECIFIED   | Unspecified harm block threshold.          |
| BLOCK_LOW_AND_ABOVE                | Block low threshold and above (i.e. block more). |
| BLOCK_MEDIUM_AND_ABOVE             | Block medium threshold and above.          |
| BLOCK_ONLY_HIGH                    | Block only high threshold (i.e. block less). |
| BLOCK_NONE                         | Block none.                                |

`BLOCK_NONE` might expose you to undesirable content. However it is clearly stated that even then the use of Gemini is subject to ToS and Privacy Policy and violation may lead to action. `BLOCK_HIGH` seems to work just right for me without any wrong flags raised. These flags wont't break the code though, just don't expect a reply!

It can be customised here
```
...
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  safety_settings="BLOCK_NONE"
...
```

`model_name` can be changed to use 1.0 pro or 1.5 pro models of Gemini however there won't be any apparent change that is, **unless you plan to take into your hands adding image generation functionality** 

## Contributing
Any contribution or suggestion is welcome. I plan to add dictionary or class based different `history[]` list for each users and making it persistent upto some time for more contextual immersive conversions.

## Discord.py

Check out the Discord.py API Wrapper that made this possible in python
https://discordpy.readthedocs.io/en/stable/

