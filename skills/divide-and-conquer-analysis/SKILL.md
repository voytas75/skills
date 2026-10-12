---
name: divide-and-conquer-analysis
description: Use when analyzing a specific element by divide and conquer.
version: 1.0.0
author: Wojciech Napierała + Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [analysis, decomposition, reasoning, risk, verification]
---

# Divide and Conquer Analysis

## Purpose
Apply this skill when the user wants to analyze a **specific element** (e.g. problem, decision, system, document, process, offer, or plan) using the method:
> Break down → analyze parts → check dependencies → synthesize results → verify → draw conclusion.

Priority is correctness and usefulness, not length. Do not overcomplicate a simple problem and do not create artificial decomposition.

## Entry Condition
1. Determine whether the user has specified the element to analyze.
2. If not, do not start the analysis and reply only with:
> Specify the element you want me to analyze.
3. Do not guess missing data, goal, or context. If the information can be safely obtained from available sources or tools, check it first. Otherwise mark it as missing or ask for it when it prevents a reliable analysis.

## Procedure

### 1. Define the scope
Establish and clearly separate:
- **element under analysis**;
- **goal of the analysis** and the decision question;
- **available context and evidence**;
- **constraints** (time, scope, data access, risk);
- **missing information** that could change the outcome.

If the goal was not explicitly stated, analyze only what is needed to answer the most direct question arising from the request. Do not attribute goals the user did not provide.

### 2. Break down the problem
Decompose the element only into logical and relevant parts appropriate to its type, for example:
- components or stages;
- assumptions and variants;
- dependencies;
- risks and constraints;
- decision criteria.

Match the depth of decomposition to complexity:
- for a simple problem: a few parts or analysis without further breakdown;
- for a complex problem: as many levels as needed to avoid hiding critical dependencies.

Do not break down the problem for its own sake. Every part must help achieve the analysis goal.

### 3. Analyze the parts
For each relevant part, present as appropriate to available data:
- **facts** — confirmed by source, observation, or data;
- **conclusions** — derived from facts;
- **assumptions** — accepted but unconfirmed conditions;
- **hypotheses** — possible explanations that require checking;
- **problems and consequences**;
- **confidence level**: high / medium / low and briefly why.

Never present assumptions or hypotheses as facts. Do not draw conclusions that go beyond the evidence.

### 4. Check dependencies
Examine relevant interactions between parts:
- causal and conditional dependencies;
- conflicts and trade-offs;
- shared constraints;
- problem propagation from component to whole;
- elements whose outcome changes the assessment of other parts.

If there are no significant dependencies, state this explicitly instead of inventing apparent links.

### 5. Synthesize the result
Combine findings into a coherent picture. Answer the main goal and indicate:
- key findings;
- problems, risks, and consequences;
- realistic options and trade-offs if needed for a decision;
- implications for the whole;
- practical conclusion or conditional decision.

When recommending a non-trivial decision, also provide the strongest reasonable alternative and one observable signal that would change the recommendation.

### 6. Verify before responding
Perform a final check:
- does the analysis cover elements relevant to the goal;
- are facts correct and clearly distinguished from assumptions and hypotheses;
- do conclusions follow logically from the evidence;
- were significant dependencies and alternative interpretations considered;
- is the confidence level appropriate;
- was unnecessary complexity introduced.

Correct any detected error before presenting the result. If it cannot be resolved, mark it as **to be verified**.

## Response Contract
Adapt structure and level of detail to the problem while keeping clear sections:
1. **Scope**
2. **Part Analysis**
3. **Dependencies**
4. **Problems and Risks**
5. **Conclusions**
6. **Uncertainty / To Be Verified**
7. **Final Assessment**

For simple matters, sections may be short or combined. For complex matters, use concise subsections or a list of parts.

## Quality Rules
- Do not guess missing data.
- Do not hide uncertainty.
- Do not overcomplicate simple problems.
- Increase decomposition only with complexity.
- Verify facts with tools when available and when they can significantly affect the outcome.
- Provide source or basis for important facts when the analysis uses external data.
- End with a useful assessment, not just a description.