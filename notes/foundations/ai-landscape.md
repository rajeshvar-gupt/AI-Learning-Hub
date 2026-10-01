# AI-001 · Understanding the AI landscape

Level: beginner. Prerequisites: none. Outcomes: distinguish learning methods from application designs; choose a simple approach; explain why output needs evaluation.

## What is it?

AI is a broad field of systems performing tasks associated with intelligent behavior. Machine learning learns patterns from data; deep learning uses multilayer neural networks. Generative AI produces content. These describe different aspects of a system, so labels can overlap.

## Why do we need these distinctions?

Imagine a college help desk. Sending a fixed deadline reminder, predicting a ticket category, drafting a reply and deciding which tool to use are different tasks. Naming them precisely helps you select data, tests and permissions instead of using the most complex tool for every job.

## How the pieces differ

| Term | Working meaning | College example |
|---|---|---|
| AI | Broad field including learned and rule-based approaches | A system that reasons over course requirements |
| ML | Learns a predictive pattern from examples | Classify a help-desk ticket |
| DL | ML using multilayer neural networks | Recognize a photographed handwritten digit |
| GenAI | Produces new content based on learned patterns | Draft an explanation of a concept |
| LLM | A language model trained at large scale | Generate a textual answer |
| RAG | Retrieve relevant evidence and supply it to generation | Answer from an approved course handbook |
| AI assistant | User-facing helper; may use models and tools | Course question-answering interface |
| AI agent | System that selects actions/tools toward a goal using feedback | Decide whether to search a syllabus or inspect a timetable |
| Agentic AI | Systems/designs with agent-like autonomy and goal-directed control | Replan a bounded task after an unavailable tool |
| Automation | Execute a process automatically; AI is optional | Send a reminder based on a stored deadline |

Agent terminology varies across practitioners. Here, the key distinction is who controls the next step: predefined workflow logic or dynamic agent decisions. An assistant can include an agent. A workflow can call an LLM. Neither name guarantees correctness or general intelligence.

## An intuitive example: answering a course question

Question: “What do I need before taking the advanced module?”

A fixed FAQ lookup may answer if the exact question is known. A retrieval system can find the prerequisite section. RAG can use that section to compose an answer. An agent may choose between syllabus search and a course-catalog tool, inspect the result and stop when it has evidence. Extra autonomy is useful only if it improves the task enough to justify additional failure paths.

## A small rule-based example

This Python example demonstrates deterministic logic, not a trained ML model:

```python
question = "When is the assignment deadline?"
if "deadline" in question.lower():
    response = "Check the published assignment page."
else:
    response = "Please contact the course help desk."
print(response)
```

Expected output: `Check the published assignment page.` The condition checks whether a word occurs in normalized text. No training data or learned parameters are used. It will also react to “I am not asking about the deadline”, showing why a keyword rule has limitations.

## Where is it used?

Predictive models can support demand estimation or document categorization. Generative systems can help draft text or code. Retrieval can make a document collection easier to search. Tool-based systems can coordinate steps in an application. Each needs task-specific checks; a convincing demonstration on one input is not sufficient evaluation.

## Key concepts

A dataset is a collection of examples. A feature is an input representation used by a model. A target is the value/category to be predicted in supervised learning. Training adjusts a model from data; inference applies it. Evaluation measures behavior on suitable cases, preferably including data and scenarios not used to tune the solution.

## Common mistakes

- Treating every automated script as ML: inspect whether a pattern was learned.
- Assuming a chatbot is an agent: inspect control flow and available actions.
- Treating RAG as a factual guarantee: retrieval can miss relevant evidence and generation can misuse it.
- Reporting training performance as proof of generalization: test on appropriate held-out cases.
- Equating agentic behavior with AGI: bounded tool use does not establish general intelligence.
- Adding multiple agents before a single workflow is evaluated: complexity introduces more failure paths.

## Interview and practice

1. When would a fixed rule be preferable to a model?
2. Can an assistant be powered by a fixed workflow? Explain.
3. What two things can fail in a RAG application?
4. How would you decide whether dynamic tool selection helps?
5. What would you test before letting a system send a message?

Discuss one example for each, then complete the [diagnostic](../../assignments/AI-001/questions.md). For a mini project, sketch the help-desk system with allowed inputs, outputs and an explicit stopping condition.

## References and next step

Working definitions are informed by [Google's ML glossary](https://developers.google.com/machine-learning/glossary). For the workflow/agent distinction, see [Anthropic's engineering discussion](https://www.anthropic.com/engineering/building-effective-agents). Both checked 1 October 2026. Examples and study guidance here are original.

Next: choose your starting stage in the [AI engineer roadmap](../../roadmaps/ai-engineer.md). Detailed Python lessons are planned. [Notes home](../README.md)
