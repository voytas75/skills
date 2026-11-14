---
name: evidence-driven-debugging
description: Diagnose bugs, test failures, integration or UI unexpected state, or verify a repair; not routine reads or cosmetic edits.
metadata:
  authorship-label: "Autorska synteza i adaptacja do OpenClaw, oparta na istniejących wzorcach diagnostyki, przeglądu kodu i weryfikacji. Sprawdzona w ograniczonych testach; bez potwierdzonej ogólnej przewagi."
  concept-and-requirements: "Wojciech Napierała"
  development-integration-and-testing: "Wiedźmin / OpenClaw, z wykorzystaniem AI"
  inspirations: "obra/superpowers; anthropics/knowledge-work-plugins; galiprandi/skills"
  attribution-scope: "Autorstwo opracowania konkretnego skilla, nie metod, na których się opiera."
---

Establish expected/observed behavior and actual running code/config/session identity; preserve minimal redacted evidence.
Reproduce the smallest failure or compare intermittent successful/failing traces; make bounded claims if there is no deterministic reproduction.
Trace data/control/config across component boundaries; confirm the probe and edited build actually took effect.
Use one explicit hypothesis with a predicted differentiating result, and one minimal experiment/change at a time.
Repeated failures mean reconsider measurements, assumptions, and architecture, not automatic architecture blame.
Apply the smallest complete authorized fix, without unrelated refactors; review relevant correctness, security, performance, and consumers, distinguishing confirmed findings from suspicions.
Verify the original symptom, neighboring behavior, and appropriate broader checks; where practical a regression test must fail without the fix and pass with it using isolated state.
For UI work, a click, toast, or URL is not persistence proof: check the actual outcome and current account, focus, and refs via native tools.
Intermittent success is bounded evidence, not proof of elimination.
During an active incident prioritize authorized containment; separate mitigation, workaround, and permanent fix.
Do not install/update extra tools, create tunnels, extract tokens, or widen authorization.
Finish with a concise Polish diagnosis, change, evidence, and limitations, with proportional steps.

A symptom does not establish its mechanism: duplicate outcomes alone do not confirm a concurrency root cause. Label an unmeasured mechanism as a hypothesis, state which observation would weaken it, and compare successful/failing traces before assuming a specific internal boundary.

Before changing active code or configuration, first inspect its effective runtime identity/value; a prediction about that value is not an executed or proposed pre-change check.
After comparing intermittent successful/failing traces, if concurrency remains a supported hypothesis, explicitly test the synchronization or ownership invariant with a controlled interleaving; if the mechanism is still unknown, state the discriminating trace observation needed before choosing such a test. Do not replace this step with more stress runs alone.
