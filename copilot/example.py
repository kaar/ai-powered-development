from dataclasses import dataclass

# {
#   "id": "chatcmpl-85qsaukyeTAfMSfllp6li5E69QlMQ",
#   "object": "chat.completion",
#   "created": 1696405600,
#   "model": "gpt-3.5-turbo-0613",
#   "choices": [
#     {
#       "index": 0,
#       "message": {
#         "role": "assistant",
#         "content": "CI: Update README with installation instructions\n\nAdd installation instructions to the README file, explaining how to install the CI tool using pipx.\n\n```bash\npipx install kaar/ci\n```\n"
#       },
#       "finish_reason": "stop"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 191,
#     "completion_tokens": 40,
#     "total_tokens": 231
#   }
# }


@dataclass
class Message:
    role: str
    content: str


@dataclass
class Choice:
    index: int
    message: Message
    finish_reason: str


@dataclass
class Usage:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


@dataclass
class ChatCompletion:
    id: str
    object: str
    created: int
    model: str
    choices: list[Choice]
    usage: Usage


example = {
    "id": "chatcmpl-85qsaukyeTAfMSfllp6li5E69QlMQ",
    "object": "chat.completion",
    "created": 1696405600,
    "model": "gpt-3.5-turbo-0613",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "CI: Update README with installation instructions\n\nAdd installation instructions to the README file, explaining how to install the CI tool using pipx.\n\n```bash\npipx install kaar/ci\n```\n",
            },
            "finish_reason": "stop",
        }
    ],
    "usage": {"prompt_tokens": 191, "completion_tokens": 40, "total_tokens": 231},
}

chat_completion = ChatCompletion(
    id=example["id"],
    object=example["object"],
    created=example["created"],
    model=example["model"],
    choices=[
        Choice(
            index=choice["index"],
            message=Message(
                role=choice["message"]["role"],
                content=choice["message"]["content"],
            ),
            finish_reason=choice["finish_reason"],
        )
        for choice in example["choices"]
    ],
    usage=Usage(
        prompt_tokens=example["usage"]["prompt_tokens"],
        completion_tokens=example["usage"]["completion_tokens"],
        total_tokens=example["usage"]["total_tokens"],
    ),
)

print(chat_completion)
print(chat_completion.choices[0].message.content)
