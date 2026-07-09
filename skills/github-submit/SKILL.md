---
name: github-submit
description: Beginner-friendly GitHub submit workflow for Python learning code, especially code written in PyCharm projects. Use when the user says things like "帮我提交代码", "我要把 day03 上传 GitHub", "帮我 push 到 GitHub", "今天的代码怎么提交", or asks to submit recently changed PyCharm code. Always inspect the PyCharm project repository first, show changed files, ask the user for a commit message, and ask for confirmation before pushing.
---

# GitHub Submit

Use this instruction-only workflow to help a beginner submit Python learning code to GitHub safely.

## Workflow

1. Inspect the PyCharm project repository first.
   - Prefer the most recently used or clearly named PyCharm project when the user does not specify a path.
   - Common location: `C:\Users\Administrator\PycharmProjects\...`.
   - If multiple PyCharm projects look possible, ask the user which one to use.
2. Run `git status` in that project repository before making changes.
3. Explain the changed files in simple language:
   - New files
   - Modified files
   - Deleted files
   - Untracked files
4. Do not run `git add .`.
5. Ask which specific files or folders to include when the user has not already specified them.
6. Add only the files or folders the user explicitly approves.
7. Ask the user to enter the commit message.
   - Do not invent the final commit message when the user has not provided one.
   - If the user asks for help choosing one, suggest a short Chinese message and ask them to confirm it.
8. Before committing, summarize:
   - Files that will be committed
   - Commit message
   - Current branch
9. Ask for confirmation before running `git commit`.
10. Commit only after the user confirms.
11. Before pushing, show the planned push target:
   - Current branch
   - Remote name and URL if available
   - Commit message
   - Files committed
12. Ask for confirmation before running `git push`.
13. Push only after the user confirms.
14. After pushing, remind the user to open or refresh the GitHub repository page and check that the code appears.

## Guardrails

- Keep explanations beginner-friendly and concise.
- Do not skip the PyCharm project check when the user says the code was written in PyCharm.
- Avoid destructive Git commands such as `git reset --hard`, `git clean`, or checkout/revert operations unless the user explicitly asks and understands the effect.
- If the working tree contains unrelated files, point them out and leave them unstaged unless the user explicitly includes them.
- If there is no Git repository, explain that the folder is not initialized and ask whether to initialize Git or switch to the correct project folder.
- If no remote is configured, explain that GitHub is not connected yet and ask for the repository URL before pushing.
- If authentication fails, explain that GitHub login/token setup is needed; do not invent credentials or continue retrying blindly.
