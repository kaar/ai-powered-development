# AI Powered Development

It saves typing not thinking!

* [Slack Channel](https://tibber.slack.com/archives/C05V3L5U8MQ)

## GitHub Copilot

* [Copilot](https://github.com/features/copilot)
* [GitHub.copilot VS Code Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
* [How to write better prompts for copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
* [GitHub Team - Copilot License](https://github.com/orgs/tibber/teams/copilot-license)

* [Example](./copilot/example.py)

### GitHub Next (GitHub Copilot X)

* [GitHub Next](https://githubnext.com/)
* [GitHub Copilot CLI](https://www.npmjs.com/package/@githubnext/github-copilot-cli)
* [GitHub Copilot Labs](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-labs)

```bash
npm install -g @githubnext/github-copilot-cli
github-copilot-cli auth
eval "$(github-copilot-cli alias -- "$0")"
```

```bash
git? delete current branch
gh? list open pull requests
?? find all files ending with .py
```

## ChatGPT

* [ChatGPT](https://chat.openai.com/)

### Plugins
* Diagrams: Show Me
* [Code Interpreter](https://openai.com/blog/chatgpt-plugins#code-interpreter)
    * [Price Example](https://chat.openai.com/share/43482b88-9035-4a65-8098-52d43378bd9e)


## OpenAI API

* [OpenAI API](https://platform.openai.com/docs/introduction)

* [CI](https://github.com/kaar/ci/)
Example of how to write your own tool against OpenAI API.

## Resources

* [StarCoder](https://arxiv.org/abs/2305.06161)
    StarCoder and StarCoderBase: 15.5B parameter models with 8K context length (arxiv.org)

* [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/pdf/2302.11382.pdf)

## Prompts

```
From now on, I would like you to ask me questions to deploy a Python
application to AWS. When you have enough information to deploy the
application, create a Python script to automate the deployment.
```
